
# Lab Exercise 1: Building a Secure User Authentication System

# Key security concepts included:
# - Encapsulation
# - Password hashing
# - Input validation
# - Privilege-based access control

import hashlib


class User:
    """
    User class representing a system account.
    Sensitive attributes are private and protected.
    """

    def __init__(self, username, password, privilege_level="standard"):
        self.__username = None
        self.__password_hash = None
        self.__privilege_level = None
        self.__login_attempts = 0
        self.__account_status = "active"
        self.__activity_log = []

        # Use setters to enforce validation
        self.set_username(username)
        self.set_password(password)
        self.set_privilege_level(privilege_level)


# PRIVATE PASSWORD HASHING

    def __hash_password(self, password):
        """Hash password using SHA-256."""
        return hashlib.sha256(password.encode()).hexdigest()

   
# SETTERS WITH INPUT VALIDATION
    
    def set_username(self, username):
        if not username or not username.isalnum():
            raise ValueError("Username must be alphanumeric.")
        self.__username = username

    def set_password(self, password):
        if len(password) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        self.__password_hash = self.__hash_password(password)

    def set_privilege_level(self, level):
        if level not in ("guest", "standard", "admin"):
            raise ValueError("Invalid privilege level.")
        self.__privilege_level = level


# AUTHENTICATION LOGIC

    def authenticate(self, password):
        """Authenticate user and track failed attempts."""

        if self.__account_status == "locked":
            self.__log_activity("Login attempt on locked account")
            print("Account is locked.")
            return False

        if self.__hash_password(password) == self.__password_hash:
            self.reset_login_attempts()
            self.__log_activity("Successful login")
            print(f"Welcome, {self.__username}!")
            return True

        self.__login_attempts += 1
        self.__log_activity(f"Failed login attempt {self.__login_attempts}")
        print("Incorrect password.")

        if self.__login_attempts >= 3:
            self.__lock_account()

        return False

  
# LOGIN ATTEMPT MANAGEMENT

    def reset_login_attempts(self):
        """Reset failed login counter."""
        self.__login_attempts = 0

    def __lock_account(self):
        self.__account_status = "locked"
        self.__log_activity("Account locked")


# PRIVILEGE CONTROL

    def check_privilege(self, required_level):
        hierarchy = {"guest": 0, "standard": 1, "admin": 2}
        return hierarchy[self.__privilege_level] >= hierarchy[required_level]

    def unlock_account(self, admin_user):
        """Only admins can unlock accounts."""
        if admin_user.check_privilege("admin"):
            self.__account_status = "active"
            self.reset_login_attempts()
            self.__log_activity("Account unlocked by admin")
            return True
        return False

# LOGGING IS PRIVATE

    def __log_activity(self, message):
        self.__activity_log.append(message)


# SAFE GETTERS

    def get_safe_info(self):
        """Expose non-sensitive user data only."""
        return {
            "username": self.__username,
            "privilege_level": self.__privilege_level,
            "account_status": self.__account_status
        }

    def get_username(self):
        return self.__username



# DEMONSTRATION OF THE CODE

if __name__ == "__main__":

    admin = User("admin01", "AdminPass123", "admin")
    user = User("Rita", "UserPass123", "standard")

    # Failed login attempts
    user.authenticate("wrongpass")
    user.authenticate("wrongpass")
    user.authenticate("wrongpass")  # Account locks

    # Unauthorized unlock attempt
    print("User unlock attempt:", user.unlock_account(user))

    # Authorized unlock
    print("Admin unlock attempt:", user.unlock_account(admin))

    # Successful login
    user.authenticate("UserPass123")

    print(user.get_safe_info())
