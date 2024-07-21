from database import Database

class BookManager:
    @staticmethod
    def add_copies(isbn, additional_quantity):
        if additional_quantity < 1:
            print("Invalid quantity to add. Quantity must be at least 1.")
            return False

        db = Database()
        cursor = db.execute_query("SELECT quantity FROM books WHERE isbn = ?", (isbn,))
        current_quantity = cursor.fetchone()[0]
        if current_quantity:
            new_quantity = current_quantity + additional_quantity
            db.execute_query("UPDATE books SET quantity = ? WHERE isbn = ?", (new_quantity, isbn))
            print(f"{additional_quantity} copies added successfully.")
            return True
        else:
            return False

    @staticmethod
    def check_out(isbn):
        db = Database()
        cursor = db.execute_query("SELECT quantity FROM books WHERE isbn = ?", (isbn,))
        if cursor.fetchone() and cursor.fetchone()[0] > 0:
            current_quantity = cursor.fetchone()[0]
            new_quantity = current_quantity - 1
            db.execute_query("UPDATE books SET quantity = ? WHERE isbn = ?", (new_quantity, isbn))
            print("Book checked out successfully.")
            return True
        else:
            print("Book not available for checkout.")
            return False

    @staticmethod
    def check_in(isbn):
        db = Database()
        cursor = db.execute_query("SELECT quantity FROM books WHERE isbn = ?", (isbn,))
        if cursor.fetchone():
            current_quantity = cursor.fetchone()[0]
            new_quantity = current_quantity + 1
            db.execute_query("UPDATE books SET quantity = ? WHERE isbn = ?", (new_quantity, isbn))
            print("Book checked in successfully.")
        else:
            print("Book not found.")
