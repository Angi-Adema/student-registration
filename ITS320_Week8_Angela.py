# Create a Student Course Registration system where students and admin can log in to 
# complete tasks such as registering for a course or for the admin, print a report or add a new course.

# Create a class to represent a user with attributes for username, password, and role (student or admin).
class User:
    # Define a constructor to initialize the user object with username, password, and role
    def __init__(self, username, password, role):
        self.__username = username
        self.__password = password
        self.__role = role

    # Use only getter methods to access the private username, password, and role attributes.
    # Define getter method for retrieving the username attribute
    def get_username(self):
        return self.__username

    # Define getter method for retrieving the password attribute
    def get_password(self):
        return self.__password

    # Define getter method for retrieving the role attribute
    def get_role(self):
        return self.__role

# Create a class to represent a student that inherits from the User class.
class Student(User):
    # Define a constructor with username, password, role
    def __init__(self, username, password, role):
        # Call the constructor of the parent class (User) to initialize the username, password, and role attributes
        super().__init__(username, password, role)
        self.__courses = []  # list to store registered courses

    # Define a getter method for retrieving the list of registered courses
    def get_courses(self):
        return self.__courses

    # Define a method to handle adding a course to the student's list of registered courses
    def add_course(self, course):
        self.__courses.append(course)

    # Define a method for dropping a course from the student's list of registered courses
    def drop_course(self, course):
        # Check if the course exists in the student's list of registered courses before attempting to remove it
        if course in self.__courses:
            self.__courses.remove(course)  # Remove the course from the student's list of registered courses
            return True  # Return True to indicate the course was successfully dropped
        return False  # Return False if the course was not found in the student's list of registered courses

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
        username = input("Please enter your username: ").strip()

        # Prompt the user to enter their password.
        password = input("Please enter your password: ").strip()

        # Loop through the list of users to see if a match exists for the provided username and password.
        for user in users:

            # Conditional to check if both the username and password match the stored user credentials.
            if user.get_username() == username and user.get_password() == password:
                return user  # Return the user object if credentials match
            
        # Print an error message if credentials do not match
        print("Invalid username or password. Please try again.")

# Create a class to represent a course with attributes for course_ID, title, description, credits, and capacity.
class Course:
    # Define a constructor to initialize the course object with course_ID, title, description, credits, and capacity
    def __init__(self, course_ID, title, description, credits, capacity):
        self.__course_ID = course_ID
        self.__title = title
        self.__description = description
        self.__credits = credits
        self.__capacity = capacity
        self.__students = []  # list to store students registered for this course  

    # Define getter and setter methods to provide controlled access to the private course attributes.
    # Define getter method for retrieving the course_ID attribute
    def get_course_ID(self):
        return self.__course_ID

    # Define getter method for retrieving the title attribute
    def get_title(self):
        return self.__title

    # Define setter method for updating the title attribute
    def set_title(self, title):
        self.__title = title

    # Define getter method for retrieving the description attribute
    def get_description(self):
        return self.__description

    # Define setter method for updating the description attribute
    def set_description(self, description):
        self.__description = description

    # Define getter method for retrieving the credits attribute
    def get_credits(self):
        return self.__credits

    # Define setter method for updating the credits attribute
    def set_credits(self, credits):
        self.__credits = credits

    # Define getter method for retrieving the capacity attribute
    def get_capacity(self):
        return self.__capacity

    # Define setter method for updating the capacity attribute
    def set_capacity(self, capacity):
        self.__capacity = capacity

    # Define getter method for retrieving the list of students registered for this course
    def get_students(self):
        return self.__students

    # Define a method receiving a student object and appending it to the list of students for this course
    def add_student(self, student):
        # Check if the student is already registered for the course and if the course has available capacity
        if student not in self.__students and len(self.__students) < self.__capacity:
            self.__students.append(student)     # Add the student to the course's student list
            return True   # Return True to indicate successful registration
        return False  # Return False to indicate registration failed due to either the student already being registered or the course being at capacity

    # Define a method for dropping a student from a course
    def remove_student(self, student):
        # Check if the student is registered for the course before attempting removal
        if student in self.__students:
            self.__students.remove(student)  # Remove the student from the course's student list
            return True  # Return True to indicate successful removal
        return False  # Return False to indicate removal failed because the student was not found

# Define a class that handles the registration system
class RegistrationSystem:
    # Define a constructor to initialize the registration system with an empty list of courses
    def __init__(self):
        self.__courses = []  # list to store all courses

    # Define getter method for retrieving the list of courses
    def get_courses(self):
        return self.__courses

    # Define method to add a course to the registration system
    def add_course(self, course):
        self.__courses.append(course)

    # Define method to register a student for a course
    def register_student(self, course, student):
        # Check if the course exists in the registration system
        if course in self.__courses:
            # Attempt to add the student to the course
            if course.add_student(student):
                student.add_course(course)   # Add the course to the student's list of courses
                return True   # Return True to indicate successful registration
        return False  # Return False to indicate registration failed

    # Define a method to drop a student from a course
    def drop_course(self, course, student):
        # Check if the course exists in the registration system
        if course in self.__courses:
            # Attempt to remove the student from the course
            if course.remove_student(student):
                student.drop_course(course)   # Remove the course from the student's list of courses
                return True   # Return True to indicate successful drop
        return False  # Return False to indicate drop failed

    # Define a method to remove a course from the registration system
    def remove_course(self, course):
        # Check if the course exists in the registration system before attempting removal
        if course in self.__courses:
            # Remove the course from the registration system's list of courses
            self.__courses.remove(course)
            return True   # Return True to indicate successful removal
        return False  # Return False to indicate removal failed because the course was not found
    
    # Define a method to search for a course by its name or ID
    def search_course(self, search_term):
        # Ensure the search_term removes leading/trailing whitespace and is lowercase
        search_term = search_term.strip().lower()
        # Iterate through the list of courses to find a match by removing leading/trailing whitespace from the title or ID and converting them to lowercase
        for course in self.__courses:
            if course.get_title().strip().lower() == search_term or course.get_course_ID().strip().lower() == search_term:
                return course   # Return the course if a match is found
        return None  # Return None if no matching course is found

    # Define a method to update a course
    def update_course(self, course, title, description, credits, capacity):
        # Check if the course exists in the registration system
        if course in self.__courses:
            # Update the course details
            course.set_title(title)
            course.set_description(description)
            course.set_credits(credits)
            course.set_capacity(capacity)
            return True   # Return True to indicate successful update
        return False  # Return False to indicate update failed because the course was not found
    
    


