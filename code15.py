# 4. Create a User class that hides password and verifies it using a method.
class User:
    def __init__(self, username, password):
        self.username = username
        self.__password = password  

    def verify_password(self, password):
        return self.__password == password
user = User("john_doe", "securepassword123")
print(f"Username: {user.username}")
print(f"Password Verified: {user.verify_password('securepassword123')}")
print(f"Password Verified: {user.verify_password('wrongpassword')}")