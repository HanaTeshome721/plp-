class Book:
    def __init__(self, name, pages):
        self.name = name
        self.pages = pages

    def content_of_book(self):
        print(f"Name of the book is {self.name}, and it has {self.pages} pages.")

class ChildBook(Book):
    def content_of_book(self):
        print(f"This book '{self.name}' is for children. It has {self.pages} pages.")

class AdultBook(Book):
    def content_of_book(self):
        print(f"This book '{self.name}' is for adults. It has {self.pages} pages.")


class Vehicle:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} is moving")

class Car(Vehicle):
    def move(self):
        print(f"{self.name} is driving")

class Plane(Vehicle):
    def move(self):
        print(f"{self.name} is flying ")


