# Create a Student Course Registration system where students and admin can log in to 
# complete tasks such as registering for a course or for the admin, print a report or add a new course.

# Create a list of established user objects.
users = [
    {"username": "admin", "password": "password", "role": "admin"},
    {"username": "student1", "password": "password1", "role": "student"},
    {"username": "student2", "password": "password2", "role": "student"}
]

class User:
    # username
    # password
    pass

class Student(User):
    # student-specific info
    pass

class Admin(User):
    # admin-specific info
    pass

