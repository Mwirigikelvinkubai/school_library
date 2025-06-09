# student.py

from borrow import Borrow  # ✅ Add this import

class Student:
    all = []

    def __init__(self, name):
        self.name = name
        Student.all.append(self)

    def __repr__(self):
        return f"<Student: {self.name}>"

    def borrows(self):
        return [b for b in Borrow.all if b.student == self]

    def borrowed_books(self):
        return [b.book for b in self.borrows()]

    def has_borrowed(self, book):
        return book in self.borrowed_books()

    def borrow_book(self, book):
        if self.has_borrowed(book):
            print(f"{self.name} already borrowed '{book.title}'.")
        else:
            Borrow(self, book)
            print(f"{self.name} borrowed '{book.title}'.")

    def return_book(self, book):
        for b in self.borrows():
            if b.book == book and not b.returned:
                b.mark_returned()
                print(f"{self.name} returned '{book.title}'.")
                return
        print(f"{self.name} has not borrowed '{book.title}' or already returned it.")
