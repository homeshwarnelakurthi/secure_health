import mysql.connector
import bcrypt

def initialize_users():
    """
    Initialize the users table with default users and hashed passwords.
    """
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Homesh@99",
            database="secure_health_db"
        )
        cursor = conn.cursor()
        
        users = [
            {"username": "root", "password": "Homesh@99", "user_group": "H"},
            {"username": "swaroop", "password": "password1", "user_group": "R"},
            {"username": "yamini", "password": "password2", "user_group": "R"}
        ]
        
        for user in users:
            hashed_password = bcrypt.hashpw(user["password"].encode(), bcrypt.gensalt())
            cursor.execute("""
                INSERT INTO users (username, password, user_group)
                VALUES (%s, %s, %s)
                ON DUPLICATE KEY UPDATE password = VALUES(password), user_group = VALUES(user_group)
            """, (user["username"], hashed_password, user["user_group"]))
        
        conn.commit()
        print("Users initialized successfully.")
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
    finally:
        cursor.close()
        conn.close()


def authenticate_user(username, password):
    """
    Authenticate the user and return their group if successful.
    """
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Homesh@99",
            database="secure_health_db"
        )
        cursor = conn.cursor()

        # Retrieve the stored password and user group for the provided username
        cursor.execute("SELECT password, user_group FROM users WHERE username = %s", (username,))
        result = cursor.fetchone()

        if result is None:
            print("User not found.")
            return None

        stored_password, user_group = result

        # Ensure stored_password is in bytes format
        if isinstance(stored_password, (bytearray, memoryview)):
            stored_password = bytes(stored_password)

        # Verify the password using bcrypt
        if bcrypt.checkpw(password.encode(), stored_password):
            return user_group
        else:
            print("Invalid password.")
            return None
    except mysql.connector.Error as err:
        print(f"Database error: {err}")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None
    finally:
        cursor.close()
        conn.close()

