from .user import User
from .admin import Admin
import bcrypt
from database import Database

class UserFactory:
    @staticmethod
    def create_user(user_type, name, email, password=None):
        if user_type == 'admin':
            return Admin(name, email, password)
        elif user_type == 'regular':
            return User(name, email)
        else:
            raise ValueError("Invalid user type provided")

    @staticmethod
    def admin_login(email, password):
        cursor = Database().execute_query("SELECT password_hash FROM admins WHERE email = ?", (email,))
        admin_data = cursor.fetchone()
        if admin_data:
            stored_password_hash = admin_data[0]
            if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash):
                return True, "Admin login successful."
            else:
                return False, "Invalid password."
        return False, "Admin not found."