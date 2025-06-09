# library.py

from book import Book
from student import Student
from borrow import Borrow

class Library:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<Library: {self.name}>"

    def all_books(self):
        return Book.all

    def all_students(self):
        return Student.all

    def all_borrows(self):
        return Borrow.all

    def borrowed_books(self):
        return [b.book for b in Borrow.all if not b.returned]

    def available_books(self):
        borrowed = self.borrowed_books()
        return [book for book in Book.all if book not in borrowed]

    def student_with_most_books(self):
        return max(Student.all, key=lambda s: len(s.borrowed_books()), default=None)
