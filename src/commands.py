from colors import Colors
from models import Book, BookManager

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