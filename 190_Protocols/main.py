from typing import Protocol

# functions from typing module are mostly useful if you're working with Code Editors like VSCode or PyCharm


class Printable(Protocol):
    pages: int

    def print_item(self):
        pass

    def recycle(self):
        pass

class Book:
    pages: int

    def __init__(self, title: str):
        self.title = title

    def print_item(self):
        print(f"Printing Book: {self.title}")

    def recycle(self):
        print(f"Recycling: {self.title}")

class Magazine:
    pages: int

    def __init__(self, title: str):
        self.title = title

    def print_item(self):
        print(f"Printing Magazine: {self.title}")

    def recycle(self):
        print(f"Recycling: {self.title}")

    def hello(self):
        print(self.title, 'says hello')



def print_printable(printable: Printable):
    printable.print_item()

# create an instance of book
book: Printable = Book("Python")
print_printable(book)

# create an instance of magazine
magazine: Printable = Magazine("Pythonista")
print_printable(magazine)