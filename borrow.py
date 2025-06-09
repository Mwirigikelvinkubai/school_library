# borrow.py

from datetime import date

class Borrow:
    all = []

    def __init__(self, student, book):
        from student import Student
        from book import Book

        if isinstance(student, Student) and isinstance(book, Book):
            self.student = student
            self.book = book
            self.date_borrowed = date.today()
            self.returned = False
            Borrow.all.append(self)
        else:
            raise ValueError("Invalid types for student or book")

    def __repr__(self):
        return f"<Borrow: {self.student.name} borrowed '{self.book.title}'>"

    def mark_returned(self):
        self.returned = True
