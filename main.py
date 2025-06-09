# main.py

from library import Library
from book import Book
from student import Student
from borrow import Borrow

# Setup
lib = Library("Greenfield School Library")

# Create Books
b1 = Book("1984", "George Orwell")
b2 = Book("To Kill a Mockingbird", "Harper Lee")
b3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

# Create Students
s1 = Student("Alice")
s2 = Student("Bob")

# Borrow Books
s1.borrow_book(b1)
s2.borrow_book(b2)
s1.borrow_book(b3)

# Return Book
s1.return_book(b1)

# Display Data
print("\nAll Books:", lib.all_books())
print("Borrowed Books:", lib.borrowed_books())
print("Available Books:", lib.available_books())
print("Student with Most Books:", lib.student_with_most_books())
