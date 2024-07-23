from colors import Colors
from models import Book, BookManager, UserFactory, LoanManager


def add_book():
    print("Adding a new book...")
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    isbn = input("Enter book ISBN: ")

    book = Book(title, author, isbn)
    print(f"{Colors.Green}Book added successfully.\n{book}{Colors.ENDC}")


def search_books():
    print("Search Books")
    search_type = input("Search by 'isbn', 'title', or 'author': ").strip().lower()
    if search_type not in ['isbn', 'title', 'author']:
        print(f"{Colors.Red}Invalid search type selected.{Colors.ENDC}")
        return

    search_query = input(f"Enter the {search_type}: ")
    results = BookManager.search_books(search_type, search_query)
    if not results:
        print(f"{Colors.Red}No books found.{Colors.ENDC}")
        return
    print(Colors.Green + results + Colors.ENDC)

def remove_book():
    print("Remove a Book from the Library")
    isbn = input("Enter the ISBN of the book to remove: ")
    result = BookManager.remove_book(isbn)
    if not result:
        print(f"{Colors.Yellow}Book not found. No action taken.{Colors.ENDC}")
        return
    print(Colors.Green + result + Colors.ENDC)

def register_user():
    print("Register New User")
    user_type = input("Enter user type (admin/regular): ")
    name = input("Enter name: ")
    email = input("Enter email: ")
    password = None
    if user_type == 'admin':
        password = input("Enter password: ")

    result = UserFactory.create_user(user_type, name, email, password)
    print(f"{Colors.Green}User added successfully.\n{result}{Colors.ENDC}")

def borrow_book():
    email = input("Enter your email: ")
    isbn = input("Enter the ISBN of the book you want to borrow: ")
    
    success, message = LoanManager().borrow_book(email, isbn)
    if success:
        print(Colors.Green + message + Colors.ENDC)
    else:
        print(Colors.Yellow + message + Colors.ENDC)
    
def return_book():
    email = input("Enter your email: ")
    
    success, message = LoanManager().return_book(email)
    if success:
        print(Colors.Green + message + Colors.ENDC)
    else:
        print(Colors.Yellow + message + Colors.ENDC)

def search_loan():
    print("Search for a loan:")
    print(f"{Colors.Yellow}[1]{Colors.ENDC} By User Email")
    print(f"{Colors.Yellow}[2]{Colors.ENDC} By Book ISBN")
    choice = input("Choose your search method (1 for user email, 2 for book ISBN): ")

    if choice == '1':
        email = input("Enter user's email: ")
        isbn = LoanManager().loans.get_by_key(email)
        if isbn:
            print(f"{Colors.Green}User {email} has borrowed book with ISBN {isbn}.{Colors.ENDC}")
        else:
            print(f"{Colors.Yellow}No loans found for this email.{Colors.ENDC}")
    elif choice == '2':
        isbn = input("Enter book's ISBN: ")
        email = LoanManager().loans.get_by_value(isbn)
        if email:
            print(f"{Colors.Green}Book with ISBN {isbn} is currently borrowed by {email}.{Colors.ENDC}")
        else:
            print(f"{Colors.Yellow}No loans found for this ISBN.{Colors.ENDC}")
    else:
        print(f"{Colors.Red}Invalid choice, please try again.{Colors.ENDC}")

def generate_loan_report():
    loans = LoanManager().generate_loan_report()
    report = LoanManager().format_loan_report(loans)
    print(report)