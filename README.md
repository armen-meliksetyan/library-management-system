## Getting Started

These instructions will get your copy of the project up and running on your local machine for development and testing purposes. Follow these simple steps to set up your development environment.

### Prerequisites

Ensure you have Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/downloads/).

### Setting Up a Virtual Environment

To isolate the project dependencies, use Python's built-in module `venv` to create a virtual environment. Here's how you can set it up:

1. **Navigate to Your Project Directory**:
   Open a terminal and navigate to the directory where your project is stored.

2. **Create the Virtual Environment**:
   Run the following command to create a virtual environment named `venv`. You can name it anything you prefer; `venv` is a common standard:
   ```bash
   python -m venv venv
   ```

3. **Activate the Virtual Environment**:
   Before installing dependencies and running the project, you need to activate the virtual environment. Activation varies by operating system:

   - **On Windows**:
     ```bash
     .\venv\Scripts\activate
     ```

   - **On macOS and Linux**:
     ```bash
     source venv/bin/activate
     ```
   When the virtual environment is activated, you'll see the environment name `(venv)` appear at the beginning of your terminal's command line.

### Installing Dependencies

With your virtual environment activated, install the project dependencies using `pip`, which is Python’s package installer:

```bash
pip install -r requirements.txt
```

## Configuration

### Environment Setup

The project uses environment variables to manage configuration options such as database connections and default user settings. Follow these steps to set up your environment file:

1. **Locate the `.env.example` File**:
   In the project root directory, you will find a file named `.env.example`. This file contains a template for the environment variables needed by the project.

2. **Create a `.env` File**:
   Copy the `.env.example` file and rename the copy to `.env`. This file will be used by the application to load configuration settings.

   ```bash
   cp .env.example .env
   ```

3. **Edit the `.env` File**:
   Open your newly created `.env` file in a text editor. You'll see several configuration options, such as:

   ```plaintext
   DATABASE_PATH=my_library.db

   DEFAULT_ADMIN_NAME=admin
   DEFAULT_ADMIN_EMAIL=admin@example.com
   DEFAULT_ADMIN_PASSWORD=pass123!
   ```

   You can change these values to suit your environment. For instance, you might want to change the `DATABASE_PATH` to specify a different location for your database file, or update the default admin credentials.

### Running the Application

Now that your environment is set up and dependencies are installed, you can run the application locally:

```bash
python src/main.py
```

## Project Architecture and Design

This library management system is designed with a focus on robust architecture and efficient data handling. Key aspects of the project's design and implementation include the manual construction of data structures, the use of object-oriented programming principles, and the integration of design patterns such as Singleton and Factory. Here’s an overview of how these components are utilized to enhance the system:

### Custom Data Structures

- **Efficient Lookups and Operations**: Custom data structures are implemented from scratch to ensure optimal performance tailored to the specific needs of the library system. These structures are designed to provide efficient lookups, inserts, and deletions, which are crucial for the dynamic handling of books and loans within the library.
  
- **Manual Implementation**: By manually implementing these data structures, the project avoids reliance on standard library structures that may not be best suited for specific use cases. This approach allows for fine-tuning and optimization specific to the application's requirements.

### Database Integration

- **Persistent Storage**: The system integrates a relational database (SQLite) to provide persistent storage of user data, book records, and loan information. This ensures that data remains intact and is consistently available across sessions and system restarts.

- **Database Operations**: CRUD (Create, Read, Update, Delete) operations are extensively implemented within the system to interact with the database, ensuring data integrity and providing a seamless user experience.

### Object-Oriented Programming (OOP)

- **Modularity and Scalability**: The application's architecture is built using OOP principles, promoting modularity and scalability. This structure makes the system easier to maintain and extend. Classes and objects encapsulate and modularize functionalities, making the codebase more organized and manageable.

- **Enhanced Code Reusability**: Through OOP, the system enhances code reusability with classes that can be extended and reused without significant modifications. This approach not only speeds up the development process but also reduces the likelihood of bugs.

### Design Patterns

- **Singleton Pattern**: The Singleton pattern is utilized for database connections and certain manager classes, ensuring that a single instance of a class is created and shared across the application. This pattern is particularly useful for managing connections and state, such as the current user session or database access.

- **Factory Pattern**: The Factory pattern is employed to create objects without specifying the exact class of the object that will be created. This is used extensively in user creation where the system needs to differentiate between different types of users (e.g., administrators and regular users) without hard-coding object creation throughout the application.

## Commands
The command structure in the `ArmLib Library Management System` provides a comprehensive and user-friendly interface for interacting with the library's functionalities. Each command corresponds to a specific operation within the system, allowing users to perform a variety of tasks related to book management, user management, and loan management. Below is an overview of each command and its purpose within the system:

### Command Overview

#### `addBook`
- **Functionality**: Adds a new book to the library's inventory.
- **How It Works**: Prompts the user to enter details about the book (title, author, and ISBN) and then adds this information to the database.

#### `searchBooks`
- **Functionality**: Allows searching for books in the library by ISBN, title, or author.
- **How It Works**: Users specify the search criteria and query, and the system retrieves and displays matching book records from the database.

#### `removeBook`
- **Functionality**: Removes a book from the library's inventory.
- **How It Works**: Users provide the ISBN of the book to be removed. The system checks if the book is not currently borrowed and, if so, removes it from the database.

#### `registerUser`
- **Functionality**: Registers a new user in the system.
- **How It Works**: Collects user information (type, name, email, and optionally password for admins) and registers them in the database, allowing them access to borrow books.

#### `borrowBook`
- **Functionality**: Allows a registered user to borrow a book.
- **How It Works**: Users enter their email and the ISBN of the book they wish to borrow. The system checks the availability of the book and, if available, marks it as borrowed.

#### `returnBook`
- **Functionality**: Manages the return process of a borrowed book.
- **How It Works**: Users enter their email, and the system updates the book's status to available, making it ready for the next borrower.

#### `searchLoan`
- **Functionality**: Provides the ability to search for active loans by user email or book ISBN.
- **How It Works**: Depending on the chosen method, the system will display either all books borrowed by a specific user or the user who has borrowed a specific book.

#### `loanReport`
- **Functionality**: Generates a report of all active loans.
- **How It Works**: The system compiles and displays a list of all books currently borrowed, including borrower details and the date of borrowing.

#### `exit`
- **Functionality**: Exits the system.
- **How It Works**: Closes the application, providing a graceful shutdown procedure.

### Exception Handling

- **Keyboard Interrupt (Ctrl+C)**: The system catches keyboard interrupts, ensuring that the application closes gracefully even when a user decides to exit using a keyboard shortcut like Ctrl+C.



