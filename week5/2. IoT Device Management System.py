from datetime import datetime, timedelta



# USER CLASS

class User:
    def __init__(self, name, role="standard"):
        if role not in ("standard", "admin"):
            raise ValueError("Invalid role")
        self.__name = name
        self.__role = role

    def get_name(self):
        return self.__name

    def is_admin(self):
        return self.__role == "admin"



# DEVICE CLASS

class IoTDevice:
    def __init__(self, device_id, category, owner_name, version="1.0"):
        if not device_id or not category:
            raise ValueError("Invalid device data")

        self.__id = device_id
        self.__category = category
        self.__owner = owner_name
        self.__firmware = version

        self.__last_scan_time = None
        self.__compliant = False
        self.__active = True
        self.__logs = []


# INTERNAL LOGGING

    def __record(self, message):
        self.__logs.append(f"{datetime.now()} | {message}")


# SECURITY OPERATIONS

    def perform_scan(self):
        self.__last_scan_time = datetime.now()
        self.__compliant = True
        self.__record("Security scan successful")

    def verify_compliance(self):
        if self.__last_scan_time is None:
            self.__compliant = False
            return False

        if datetime.now() - self.__last_scan_time > timedelta(days=30):
            self.__compliant = False
            self.__record("Compliance expired")
            return False

        return self.__compliant

    def upgrade_firmware(self, new_version, user):
        if not user.is_admin():
            self.__record("Firmware update blocked (no admin rights)")
            return False

        self.__firmware = new_version
        self.perform_scan()
        self.__record(f"Firmware upgraded to {new_version}")
        return True


# ACCESS CONTROL

    def request_access(self, user):
        self.verify_compliance()

        if not self.__active:
            self.__record(f"Access denied to {user.get_name()} (inactive)")
            return False

        if user.is_admin():
            self.__record(f"Admin access granted to {user.get_name()}")
            return True

        if user.get_name() != self.__owner:
            self.__record(f"Access denied to {user.get_name()} (not owner)")
            return False

        if not self.__compliant:
            self.__record(f"Access denied to {user.get_name()} (non-compliant)")
            return False

        self.__record(f"Access granted to {user.get_name()}")
        return True


# QUARANTINE

    def isolate(self, user):
        if not user.is_admin():
            return False

        self.__active = False
        self.__record("Device isolated by admin")
        return True


# SAFE INFO

    def summary(self):
        self.verify_compliance()
        return {
            "device_id": self.__id,
            "category": self.__category,
            "owner": self.__owner,
            "firmware": self.__firmware,
            "compliant": self.__compliant,
            "active": self.__active
        }



# DEVICE MANAGER

class DeviceRegistry:
    def __init__(self):
        self.__inventory = []

    def register(self, device):
        self.__inventory.append(device)

    def unregister(self, device_id, user):
        if not user.is_admin():
            return False

        self.__inventory = [
            d for d in self.__inventory if d.summary()["device_id"] != device_id
        ]
        return True

    def security_overview(self, user):
        if not user.is_admin():
            return None

        report = []
        for device in self.__inventory:
            report.append(device.summary())
        return report



# PROGRAM EXECUTION (OUTPUT TRIGGER)

if __name__ == "__main__":

    admin = User("security_admin", "admin")
    user = User("Rita", "standard")

    manager = DeviceRegistry()

    sensor = IoTDevice("IOT-001", "Temperature Sensor", "Rita")
    manager.register(sensor)

    # Access before scan
    print(sensor.request_access(user))  # False

    # Run scan
    sensor.perform_scan()
    print(sensor.request_access(user))  # True

    # Expire scan manually
    sensor._IoTDevice__last_scan_time -= timedelta(days=31)
    print(sensor.request_access(user))  # False

    # Admin override
    print(sensor.request_access(admin))  # True

    # Quarantine
    sensor.isolate(admin)
    print(sensor.request_access(admin))  # False

    # Security report
    print(manager.security_overview(admin))
