from database import Database

class BookManager:
    @staticmethod
    def check_out(isbn):
        db = Database()
        cursor = db.execute_query("SELECT borrowed FROM books WHERE isbn = ?", (isbn,))
        result = cursor.fetchone()
        if result and not result[0]:
            db.execute_query("UPDATE books SET borrowed = 1 WHERE isbn = ?", (isbn,))
            print("Book checked out successfully.")
            return True
        else:
            print("Book not available for checkout.")
            return False

    @staticmethod
    def check_in(isbn):
        db = Database()
        cursor = db.execute_query("SELECT borrowed FROM books WHERE isbn = ?", (isbn,))
        result = cursor.fetchone()
        if result and result[0]:
            db.execute_query("UPDATE books SET borrowed = 0 WHERE isbn = ?", (isbn,))
            print("Book checked in successfully.")
            return True
        else:
            print("Book not found or not currently borrowed.")
            return False
        
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
            return False

        formatted = "Found Books:\n"
        for book in results:
            formatted += f"ISBN: {book[3]}, Title: {book[1]}, Author: {book[2]}\n"
        return formatted
    
    @staticmethod
    @staticmethod
    def remove_book(isbn):
        db = Database()
        cursor = db.execute_query("SELECT borrowed FROM books WHERE isbn = ?", (isbn,))
        book_info = cursor.fetchone()

        if not book_info:
            return "Book not found. No action taken."

        if book_info[0]:
            return "Cannot remove the book because it is currently borrowed."

        db.execute_query("DELETE FROM books WHERE isbn = ?", (isbn,))
        return "Book successfully removed."
       
    @staticmethod
    def get_latest_book():
        db = Database()
        query = "SELECT id, title, author, isbn, borrowed, created_at FROM books ORDER BY created_at DESC LIMIT 1"
        cursor = db.execute_query(query)
        latest_book = cursor.fetchone()

        if latest_book:
            return {
                'id': latest_book[0],
                'title': latest_book[1],
                'author': latest_book[2],
                'isbn': latest_book[3],
                'borrowed': latest_book[4],
                'created_at': latest_book[5]
            }
        else:
            return "No books found in the database."

