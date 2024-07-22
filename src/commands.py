from colors import Colors
from models import Book, BookManager, UserFactory

def add_book():
    print("Adding a new book...")
    title = input("Enter book title: ")
    author = input("Enter book author: ")
    isbn = input("Enter book ISBN: ")
    quantity = input("Enter quantity: ")
    try:
        quantity = int(quantity)
    except ValueError:
        print(f"{Colors.Red}Invalid quantity. Must be a number.{Colors.ENDC}")
        return

    book = Book(title, author, isbn, quantity)
    print(f"{Colors.Green}Book added successfully.\n{book}{Colors.ENDC}")

def add_copies():
    print("Adding copies to an existing book...")
    isbn = input("Enter the ISBN of the book to which you want to add copies: ")
    additional_quantity = input("Enter the number of copies to add: ")

    try:
        additional_quantity = int(additional_quantity)
    except ValueError:
        print(f"{Colors.Red}Invalid quantity. Must be a number.{Colors.ENDC}")
        return

    if BookManager.add_copies(isbn, additional_quantity):
        print(f"{Colors.Green}Successfully added {additional_quantity} copies to the book.{Colors.ENDC}")
    else:
        print(f"{Colors.Red}Failed to add copies. Book might not exist or other error occurred.{Colors.ENDC}")

def search_books():
    print("Search Books")
    search_type = input("Search by 'isbn', 'title', or 'author': ").strip().lower()
    if search_type not in ['isbn', 'title', 'author']:
        print("Invalid search type selected.")
        return

    search_query = input(f"Enter the {search_type}: ")
    results = BookManager.search_books(search_type, search_query)
    print(Colors.Green + results + Colors.ENDC)

def remove_book():
    print("Remove a Book from the Library")
    isbn = input("Enter the ISBN of the book to remove: ")
    result = BookManager.remove_book(isbn)
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
