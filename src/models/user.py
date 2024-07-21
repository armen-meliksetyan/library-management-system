from database import Database

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.save()

    def save(self):
        Database().execute_query(
            "INSERT INTO users (name, email) VALUES (?, ?) ON CONFLICT(email) DO NOTHING",
            (self.name, self.email)
        )

    def __str__(self):
        return f"User {self.name}, Email: {self.email}"