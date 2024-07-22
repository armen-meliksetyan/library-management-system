from data_structures import BiHashmap
from database import Database
from .book_manager import BookManager

class LoanManager:
    def __init__(self):
        self.loans = BiHashmap()
        self.db = Database()
        self.load_loans()

    def load_loans(self):
        query = "SELECT email, isbn FROM loans WHERE returned_on IS NULL;"
        cursor = self.db.execute_query(query)
        ongoing_loans = cursor.fetchall()
        for email, isbn in ongoing_loans:
            self.loans.set(email, isbn)

    def borrow_book(self, email, isbn):
        if not BookManager.check_out(isbn):
            return "This book is currently unavailable."
        self.loans.set(email, isbn)
        self.db.execute_query("INSERT INTO loans (email, isbn, borrowed_on) VALUES (?, ?, DATE('now'))", (email, isbn))
        return "Loan recorded successfully."

    def return_book(self, email):
        isbn = self.loans.get_by_key(email)
        if not isbn:
            return "No current loan record found for this user."
        
        BookManager.check_in(isbn)

        self.loans.remove_by_key(email)
        self.db.execute_query("UPDATE loans SET returned_on = DATE('now') WHERE email = ? AND isbn = ?", (email, isbn))
        return "Book returned successfully."