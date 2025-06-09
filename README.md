School Library System

A simple Python OOP project modeling a school library. It demonstrates class creation, object relationships, and aggregate/association methods — aligned with the Phase 3 Code Challenge rubric.

---

including 

- `Book` class with title and author
- `Student` class with borrowing/return behavior
- `Borrow` class tracks which student borrowed which book and whether it’s returned
- `Library` class provides a centralized way to see all books and available ones



File Structure

```bash
school_library/
├── book.py       # Book class
├── student.py    # Student class and their behavior
├── borrow.py     # Borrow relationship class
├── library.py    # Library aggregation methods
└── main.py       # Driver script to run and test the system
