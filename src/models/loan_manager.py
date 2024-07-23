from data_structures import BiHashmap
from database import Database
from .book_manager import BookManager

class LoanManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(LoanManager, cls).__new__(cls)
            cls._instance.init_manager()
        return cls._instance
    
    def init_manager(self):
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
        user_exists = self.db.execute_query("SELECT email FROM users WHERE email = ?", (email,))
        if not user_exists.fetchone():
            return False, "No user found with the provided email. Please register first."

        existing_loan = self.loans.get_by_key(email)
        if existing_loan:
            return False, f"This user already has a borrowed book: ISBN {existing_loan}. Please return it before borrowing another."

        if not BookManager.check_out(isbn):
            return False, "This book is currently unavailable."

        self.loans.set(email, isbn)
        self.db.execute_query("INSERT INTO loans (email, isbn, borrowed_on) VALUES (?, ?, DATE('now'))", (email, isbn))
        return True, "Loan recorded successfully."


    def return_book(self, email):
        isbn = self.loans.get_by_key(email)
        if not isbn:
            return False, "No current loan record found for this user."
        
        BookManager.check_in(isbn)

        self.loans.remove_by_key(email)
        self.db.execute_query("UPDATE loans SET returned_on = DATE('now') WHERE email = ? AND isbn = ?", (email, isbn))
        return True, "Book returned successfully."