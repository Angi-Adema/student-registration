# Create a Student Course Registration system where students and admin can log in to 
# complete tasks such as registering for a course or for the admin, print a report or add a new course.

# Create a class to represent a user with attributes for username, password, and role (student or admin).
class User:
    # Define a constructor to initialize the user object with username, password, and role
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

# Create a class to represent a student that inherits from the User class.
class Student(User):
    # Define a constructor with username, password, role
    def __init__(self, username, password, role):
        # Call the constructor of the parent class (User) to initialize the username, password, and role attributes
        super().__init__(username, password, role)
        self.courses = []  # list to store registered courses

# Create a class to represent an admin that inherits from the User class.
class Admin(User):
    pass

# Create a list of established user objects.
users = [
    Admin("admin", "password", "admin"),
    Student("student1", "password1", "student"),
    Student("student2", "password2", "student")
]

# Create a method to handle authentication for users based on their username and password.
def login():
    # Create a while True loop allowing the user to retry their credentials until they are correct.
    while True:

        # Prompt the user to enter their username.
        username = input("Please enter your username: ")

        # Prompt the user to enter their password.
        password = input("Please enter your password: ")

        # Loop through the list of users to see if a match exists for the provided username and password.
        for user in users:

            # Conditional to check if both the username and password match the stored user credentials.
            if user.username == username and user.password == password:
                return user  # Return the user object if credentials match
            
        # Print an error message if credentials do not match
        print("Invalid username or password. Please try again.")


