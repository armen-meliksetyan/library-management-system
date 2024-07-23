import sqlite3
import os

class Database:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Database, cls).__new__(cls)
            cls._instance.db_path = os.getenv('DATABASE_PATH', 'default_library.db')
            cls._instance.connection = cls._instance.connect()
        return cls._instance
    
    def connect(self):
        try:
            conn = sqlite3.connect(self.db_path)
            print("Database connection established.")
            return conn
        except sqlite3.Error as e:
            print(f"Error connecting to database: {e}")

    def execute_query(self, query, params=None):
        cursor = self.connection.cursor()
        try:
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            self.connection.commit()
            # print("Query executed successfully.")
        except sqlite3.Error as e:
            print(f"Failed to execute query: {e}")
        return cursor

    def close(self):
        if self.connection:
            self.connection.close()
            print("Database connection closed.")

    def initialize(self):
        self.execute_query("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                isbn TEXT UNIQUE NOT NULL,
                borrowed BOOLEAN NOT NULL DEFAULT 0,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP           
            );
        """)
        self.execute_query("CREATE INDEX IF NOT EXISTS idx_title ON books(title);")
        self.execute_query("CREATE INDEX IF NOT EXISTS idx_author ON books(author);")
        self.execute_query("CREATE INDEX IF NOT EXISTS idx_isbn ON books(isbn);")
        self.execute_query("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );
        """)
        self.execute_query("""
            CREATE TABLE IF NOT EXISTS admins (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password_hash TEXT NOT NULL,
                created_at DATETIME DEFAULT CURRENT_TIMESTAMP
            );
        """)
        self.execute_query("""
            CREATE TABLE IF NOT EXISTS loans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT NOT NULL,
                isbn TEXT NOT NULL,
                borrowed_on DATE NOT NULL,
                returned_on DATE,
                FOREIGN KEY (email) REFERENCES users(email),
                FOREIGN KEY (isbn) REFERENCES books(isbn),
            );
        """)
        
        

