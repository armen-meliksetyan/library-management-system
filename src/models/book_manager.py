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
        result = cursor.fetchone()
        if result and result[0] > 0:
            current_quantity = result[0]
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
        result = cursor.fetchone()
        if result:
            current_quantity = result[0]
            new_quantity = current_quantity + 1
            db.execute_query("UPDATE books SET quantity = ? WHERE isbn = ?", (new_quantity, isbn))
            print("Book checked in successfully.")
        else:
            print("Book not found.")

    @staticmethod
    def search_books(search_type, search_query):
        db = Database()

        if search_type == 'isbn':
            cursor = db.execute_query("SELECT * FROM books WHERE isbn = ?", (search_query,))
        elif search_type == 'title':
            cursor = db.execute_query("SELECT * FROM books WHERE title LIKE ?", ('%' + search_query + '%',))
        elif search_type == 'author':
            cursor = db.execute_query("SELECT * FROM books WHERE author LIKE ?", ('%' + search_query + '%',))
        else:
            return "Invalid search type. Use 'isbn', 'title', or 'author'."

        results = cursor.fetchall()
        if not results:
            return "No books found."

        formatted = "Found Books:\n"
        for book in results:
            formatted += f"ISBN: {book[3]}, Title: {book[1]}, Author: {book[2]}, Quantity: {book[4]}\n"
        return formatted
    
    @staticmethod
    def remove_book(isbn):
        db = Database()
        cursor = db.execute_query("SELECT * FROM books WHERE isbn = ?", (isbn,))
        if not cursor.fetchone():
            return "Book not found. No action taken."

        db.execute_query("DELETE FROM books WHERE isbn = ?", (isbn,))
        return "Book successfully removed."
       
    @staticmethod
    def get_latest_book():
        db = Database()
        query = "SELECT id, title, author, isbn, quantity, created_at FROM books ORDER BY created_at DESC LIMIT 1"
        cursor = db.execute_query(query)
        latest_book = cursor.fetchone()

        if latest_book:
            return {
                'id': latest_book[0],
                'title': latest_book[1],
                'author': latest_book[2],
                'isbn': latest_book[3],
                'quantity': latest_book[4],
                'created_at': latest_book[5]
            }
        else:
            return "No books found in the database."

