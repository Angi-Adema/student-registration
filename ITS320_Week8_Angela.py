# Create a Student Course Registration system where students and admin can log in to 
# complete tasks such as registering for a course or for the admin, print a report or add a new course.

# Create a class to represent a user with attributes for username, password, and role (student or admin).
class User:
    # constructor to initialize the user object with username, password, and role
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class Student(User):
    # student-specific info
    pass

class Admin(User):
    # admin-specific info
    pass

# Create a list of established user objects.
users = [
    Admin("admin", "password", "admin"),
    Student("student1", "password1", "student"),
    Student("student2", "password2", "student")
]