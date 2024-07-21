import bcrypt
from database import Database

class Admin:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password_hash = self.hash_password(password)
        self.save()

    def hash_password(self, password):
        password_bytes = password.encode('utf-8')
        hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt())
        return hashed

    def verify_password(self, provided_password):
        return bcrypt.checkpw(provided_password.encode('utf-8'), self.password_hash)

    def save(self):
        Database().execute_query(
            "INSERT INTO admins (name, email, password_hash) VALUES (?, ?, ?) ON CONFLICT(email) DO UPDATE SET password_hash = excluded.password_hash",
            (self.name, self.email, self.password_hash)
        )

    def __str__(self):
        return f"Admin {self.name}, Email: {self.email}"
    
