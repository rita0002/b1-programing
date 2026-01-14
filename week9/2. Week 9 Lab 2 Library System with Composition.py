# Library System - Alternative Implementation

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn

    def info(self):
        return f"{self.title} by {self.author} (ISBN {self.isbn})"

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add(self, book):
        self.books.append(book)
        return f"Book added: {book.info()}"

    def remove(self, title):
        for b in self.books:
            if b.title.lower() == title.lower():
                self.books.remove(b)
                return f"Book removed: {b.info()}"
        return f"No book titled '{title}' found."

    def list_all(self):
        if not self.books:
            return f"{self.name} has no books."
        result = f"Books in {self.name}:\n"
        for idx, book in enumerate(self.books, start=1):
            result += f"{idx}. {book.info()}\n"
        return result

    def search(self, term):
        found_books = [b for b in self.books if term.lower() in b.title.lower()]
        if found_books:
            result = f"Found {len(found_books)} book(s):\n"
            for b in found_books:
                result += f"- {b.info()}\n"
            return result
        return f"No books found with '{term}'"

# Test Library
lib = Library("City Library")
b1 = Book("Python Crash Course", "Eric Matthes", "978-1593279288")
b2 = Book("Clean Code", "Robert Martin", "978-0132350884")
b3 = Book("The Pragmatic Programmer", "Hunt & Thomas", "978-0201616224")

print(lib.add(b1))
print(lib.add(b2))
print(lib.add(b3))
print(lib.list_all())
print(lib.search("Python"))
print(lib.remove("Clean Code"))
print(lib.list_all())
