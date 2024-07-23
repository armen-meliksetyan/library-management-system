import os
from dotenv import load_dotenv
from database import Database
# from models import UserFactory
# from colors import Colors
from commands import *

load_dotenv()

Database().initialize()

def create_default_admin():
    admin_name = os.getenv('DEFAULT_ADMIN_NAME')
    admin_email = os.getenv('DEFAULT_ADMIN_EMAIL')
    admin_password = os.getenv('DEFAULT_ADMIN_PASSWORD')

    if not all([admin_name, admin_email, admin_password]):
        print("Missing environment variables for default admin. Please check your .env file.")
        return 

    cursor = Database().execute_query('SELECT email FROM admins WHERE email = ?', (admin_email,))
    if cursor.fetchone():
        print("Default admin already exists.")
    else:
        UserFactory.create_user('admin', admin_name, admin_email, admin_password)
        print("Default admin created successfully.")

def login():
    create_default_admin()
    print("Please log in to continue:")
    attempt_count = 0
    while True:
        email = input("Enter admin's email: ")
        password = input("Enter password: ")
        success, message = UserFactory.admin_login(email, password)
        print(message)
        if success:
            return True
        attempt_count += 1
        if attempt_count >= 3:
            print(f"{Colors.Red}Too many failed login attempts. Exiting.{Colors.ENDC}")
            return False

def main():
    try:
        print(f"{Colors.Blue}Welcome to ArmLib Library Management System{Colors.ENDC}")
        print(Colors.Intro)
        if login():
            print(Colors.Welcome)
            while True:
                command = input("Enter command: ")
                if command == 'exit':
                    print("Goodbye!")
                    break
                elif command == 'addBook':
                    add_book()
                elif command == 'searchBooks':
                    search_books()
                elif command == 'removeBook':
                    remove_book()
                elif command == 'registerUser':
                    register_user()
                elif command == 'borrowBook':
                    borrow_book()
                elif command == 'returnBook':
                    return_book()
                elif command == 'searchLoan':
                    search_loan()
                elif command == 'loanReport':
                    generate_loan_report()
                elif command:
                    print(f"{Colors.Red}Unknown command. Try again.{Colors.ENDC}")
    except KeyboardInterrupt:
        print("\nGoodbye!")
        


if __name__ == "__main__":
    main()
