# book.py

class Book:
    all = []

    def __init__(self, title, author):
        self.title = title
        self.author = author
        Book.all.append(self)

    def __repr__(self):
        return f"<Book: '{self.title}' by {self.author}>"
