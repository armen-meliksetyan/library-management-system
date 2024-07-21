from database import Database

class Book:
    def __init__(self, title, author, isbn, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.quantity = quantity
        self.db = Database()
        self.save()

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn}, Copies: {self.quantity})"
    
    def save(self):
        cursor = self.db.execute_query(
            "SELECT quantity FROM books WHERE isbn = ?", (self.isbn,)
        )
        result = cursor.fetchone()
        if result:
            new_quantity = result[0] + self.quantity
            self.db.execute_query(
                "UPDATE books SET title = ?, author = ?, quantity = ? WHERE isbn = ?",
                (self.title, self.author, new_quantity, self.isbn)
            )
        else:
            self.db.execute_query(
                "INSERT INTO books (isbn, title, author, quantity) VALUES (?, ?, ?, ?)",
                (self.isbn, self.title, self.author, self.quantity)
            )
        print(f"Database updated: {self.title} (ISBN: {self.isbn}) now has {self.quantity} copies available.")

    def add_copies(self, additional_quantity):
        if additional_quantity < 1:
            print("Invalid quantity to add. Quantity must be at least 1.")
            return False
        
        self.quantity += additional_quantity
        self.save()

    def check_out(self):
        if self.quantity > 0:
            self.quantity -= 1
            self.save()
            print(f"Book checked out successfully: {self.title}")
            return True
        else:
            print(f"Book not available for checkout: {self.title}")
            return False

    def check_in(self):
        self.quantity += 1
        self.save()
        print(f"Book checked in successfully: {self.title}")
