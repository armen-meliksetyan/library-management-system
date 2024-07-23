from database import Database

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.db = Database()
        self.save()

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"
    
    def save(self):
        cursor = self.db.execute_query(
            "SELECT isbn FROM books WHERE isbn = ?", (self.isbn,)
        )
        result = cursor.fetchone()
        if result:
            self.db.execute_query(
                "UPDATE books SET title = ?, author = ? WHERE isbn = ?",
                (self.title, self.author, self.isbn)
            )
        else:
            self.db.execute_query(
                "INSERT INTO books (isbn, title, author, borrowed) VALUES (?, ?, ?, 0)",
                (self.isbn, self.title, self.author)
            )
        return f"Database updated: {self}"
