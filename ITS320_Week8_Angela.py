# Create a Student Course Registration system where students and admin can log in to 
# complete tasks such as registering for a course or for the admin, print a report or add a new course.

# Import the ABC and abstractmethod modules to create abstract base classes and enforce method implementation in derived classes
from abc import ABC, abstractmethod

# Create a class to represent a user with attributes for user_ID, password, and role (student or admin)
class User(ABC):
    # Define a constructor to initialize the user object with user_ID, password, and role
    def __init__(self, user_ID, password, role):
        self.__user_ID = user_ID
        self.__password = password
        self.__role = role

    # Use only getter methods to access the private user_ID, password, and role attributes.
    # Define getter method for retrieving the user_ID attribute
    def get_user_ID(self):
        return self.__user_ID

    # Define getter method for retrieving the password attribute
    def get_password(self):
        return self.__password

    # Define getter method for retrieving the role attribute
    def get_role(self):
        return self.__role

    # Define an abstract method to display the menu for the user based on their role
    @abstractmethod
    def display_menu(self):
        pass

# Create a class to represent a student that inherits from the User class
class Student(User):
    # Define a constructor with user_ID, password, role
    def __init__(self, user_ID, password, role):
        # Call the constructor of the parent class (User) to initialize the user_ID, password, and role attributes
        super().__init__(user_ID, password, role)
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

    # Create a method to display the student's menu options
    def display_menu(self):
        print("      Student Menu      ")
        print("------------------------------")
        print("1. Register for a Course")
        print("2. Drop a Course")
        print("3. View My Courses")
        print("4. View All Courses")
        print("5. Logout")

# Create a class to represent an admin that inherits from the User class
class Admin(User):
    # Define a method to display the admin's menu options
    def display_menu(self):
        print("      Admin Menu      ")
        print("-----------------------------------------")
        print("1. Add a Course")
        print("2. Remove a Course")
        print("3. Update a Course")
        print("4. Search for a Course")
        print("5. View Students Enrolled in a Course")
        print("6. View Courses a Student is Enrolled In")
        print("7. View Student IDs and Passwords")
        print("8. View All Courses")
        print("9. Logout")

# Create a list of established user objects
users = [
    Admin("admin", "password", "admin"),
    Student("student1", "password1", "student"),
    Student("student2", "password2", "student")
]

# Create a method to handle authentication for users based on their user_ID and password
def login():
    # Create a while True loop allowing the user to retry their credentials until they are correct
    while True:

        # Prompt the user to enter their user_ID
        user_ID = input("Please enter your user ID: ").strip()

        # Prompt the user to enter their password
        password = input("Please enter your password: ")

        # Loop through the list of users to see if a match exists for the provided user_ID and password
        for user in users:

            # Conditional to check if both the user_ID and password match the stored user credentials
            if user.get_user_ID() == user_ID and user.get_password() == password:
                return user  # Return the user object if credentials match
            
        # Print an error message if credentials do not match
        print("Invalid user ID or password. Please try again.")

# Create a class to represent a course with attributes for course_ID, title, description, credits, and capacity
class Course:
    # Define a constructor to initialize the course object with course_ID, title, description, credits, and capacity
    def __init__(self, course_ID, title, description, credits, capacity):
        self.__course_ID = course_ID
        self.__title = title
        self.__description = description
        self.__credits = credits
        self.__capacity = capacity
        self.__students = []  # list to store students registered for this course  

    # Define getter and setter methods to provide controlled access to the private course attributes
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
            # Remove the course from each enrolled student's course list
            for student in course.get_students():
                student.drop_course(course)  # Remove the course from the student's list of courses

            # Remove the course from the registration system's list of courses
            self.__courses.remove(course)

            return True  # Return True to indicate successful removal
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

    # Create a method to get all students registered in a course
    def get_students_in_course(self, course):
        # Check if the course exists in the registration system
        if course in self.__courses:
            return course.get_students()  # Return the list of students registered in the course
        return []  # Return an empty list if the course is not found

    # Create a method to get all courses a student is registered in
    def get_courses_for_student(self, student):
        return student.get_courses()  # Return the list of courses the student is registered in

    # Create a method to get all courses in the registration system
    def get_all_courses(self):
        return self.__courses  # Return the list of all courses in the registration system

    # Create a method to get all student IDs and passwords
    def get_student_credentials(self):
        # Create an empty list to store student credentials
        credentials = []

        # Loop through the list of users to collect student IDs and passwords
        for user in users:

            # Conditional to check if the role is a student
            if user.get_role().strip().lower() == "student":
                credentials.append((user.get_user_ID(), user.get_password()))  # Add the student's ID and password to the credentials list
        return credentials  # Return the list of student credentials

# Initialize the registration system
registration_system = RegistrationSystem()

# Create a list of courses to add to the registration system
course_list = [
    Course("ITS320", "Basic Programming", "Introduction to Python programming", 3, 25),
    Course("ITS321", "Advanced Programming", "Advanced topics in Python programming", 3, 25),
    Course("ITS322", "Data Structures", "Introduction to data structures in Python", 3, 25),
]

# Loop through the course list and add each course to the registration system
for course in course_list:
    registration_system.add_course(course)

# Create a function to handle the admin menu options
def admin_menu(admin):

    # Implement a while True loop to reprompt the user until they exit the system
    while True:
        # Call display_menu to display the admin menu options
        admin.display_menu()

        # Prompt the admin to enter their selection removing any leading or trailing whitespace
        selection = input("Please enter your selection: ").strip()

        # Implement the admin menu options based on the selection
        # Functionality to add a course
        if selection == "1":

            # Use a while True loop to reprompt for correct input
            while True:
                # Prompt the admin to enter the course ID ensuring it is not empty and removing any leading or trailing whitespace
                course_ID = input("Enter course ID: ").strip()

                # Check if the course ID is not empty
                if course_ID == "":
                    print("Course ID cannot be empty.")   # Notify the admin that the course ID cannot be empty
                    continue  # Reprompt the admin for the course ID if it is empty

                # Conditional to check if the course ID already exists
                if registration_system.search_course(course_ID) is not None:
                    print("Course ID already exists.")   # Notify the admin that the course ID already exists
                    continue  # Reprompt the admin for the course ID if it already exists

                break  # Exit the loop if the course ID is valid and does not already exist

            # Reprompt for course name until valid input is provided
            while True:
                # Prompt the admin to enter the course name ensuring it is not empty and removing any leading or trailing whitespace
                course_name = input("Enter course name: ").strip()

                # Check if the course name is not empty
                if course_name != "":
                    break   # Exit the loop if the course name is not empty
                print("Course name cannot be empty.")   # Notify the admin that the course name cannot be empty

            # Reprompt for course description until valid input is provided
            while True:
                # Prompt the admin to enter the course description ensuring it is not empty and removing any leading or trailing whitespace
                course_description = input("Enter course description: ").strip()

                # Check if the course description is not empty
                if course_description != "":
                    break   # Exit the loop if the course description is not empty
                print("Course description cannot be empty.")   # Notify the admin that the course description cannot be empty

            # Reprompt for course credits and capacity until valid input is provided
            while True:
                # Validate user input using a try/except statement
                try:
                    course_credits = int(input("Enter course credits: ").strip())
                    course_capacity = int(input("Enter course capacity: ").strip())

                    # Conditional to ensure values entered are positive
                    if course_credits > 0 and course_capacity > 0:
                        break   # Exit the loop if valid values are entered

                    # Print an error message if the values are not positive
                    print("Credits and capacity must be positive numbers.")
                
                # Handle the case where the user enters non-numeric values for credits or capacity
                except ValueError:
                    print("Invalid input. Please enter a whole, positive number for credits and capacity.")

            # Create a new Course object with the entered details
            new_course = Course(course_ID, course_name, course_description, course_credits, course_capacity)

            # Add the new course to the registration system
            registration_system.add_course(new_course)

            # Notify the admin that the course has been added successfully
            print(f"Course {course_name} added successfully.")

        # Functionality to remove a course
        elif selection == "2":
            # Reprompt for course ID or course name until valid input is provided
            while True:
                # Prompt the admin to enter the course ID or course name
                search_term = input("Enter the course ID or the course name: ").strip()

                # Validate that the input is not empty
                if search_term == "":
                    # Display an error message if the input is empty
                    print("Course ID or course name cannot be empty.")
                    continue   # Reprompt the admin for input if the input is empty

                # Search for the course using the entered search term
                course = registration_system.search_course(search_term)

                # Conditional to check to see if the course is found
                if course is None:
                    print("Course not found. Please try again.")  # Notify the admin that the course was not found
                    continue   # Reprompt the admin for input if the course was not found

                # Attempt to remove the course
                if registration_system.remove_course(course):
                    print(f"Course {course.get_title()} removed successfully.")  # Notify the admin that the course was removed successfully
                else:
                    print("Failed to remove the course.")  # Notify the admin that the course removal failed
                break   # Exit the loop after attempting to remove the course

        # Functionality to update a course
        elif selection == "3":
            # Reprompt for course ID or course name until valid input is provided
            while True:
                # Prompt the admin to enter the course ID or course name
                search_term = input("Enter the course ID or the course name to update: ").strip()

                # Validate that the input is not empty
                if search_term == "":
                    # Display an error message if the input is empty
                    print("Course ID or course name cannot be empty.")
                    continue   # Reprompt the admin for input if the input is empty

                # Search for the course using the entered search term
                course = registration_system.search_course(search_term)

                # Conditional to check to see if the course is found
                if course is None:
                    print("Course not found. Please try again.")  # Notify the admin that the course was not found
                    continue   # Reprompt the admin for input if the course was not found

                # Reprompt the admin to enter the new course details
                while True:
                    # Prompt the admin to enter the new course title
                    new_title = input("Enter the new title for the course: ").strip()

                    # Confirm the entry is not empty
                    if new_title == "":
                        print("Course title cannot be empty.")
                        continue   # Reprompt the admin for input if the title is empty
                    break   # Exit the loop if a valid title is entered

                # Reprompt the admin to enter the new course description
                while True:
                    # Prompt the admin to enter the new course description
                    new_description = input("Enter the new course description: ").strip()

                    # Confirm the entry is not empty
                    if new_description == "":
                        print("Course description cannot be empty.")
                        continue   # Reprompt the admin for input if the description is empty
                    break   # Exit the loop if a valid description is entered

                # Reprompt the admin to input new credits value
                while True:
                    # Use a try/except to validate input
                    try:
                        # Prompt the admin to enter the new credits and capacity values
                        new_credits = int(input("Enter the new credits for the course: ").strip())
                        new_capacity = int(input("Enter the new capacity for the course: ").strip())

                        # Conditional to validate user input 
                        if new_credits <= 0 or new_capacity <= 0:
                            # Notify the admin that the entered credits and capacity are not valid
                            print("Credits and capacity must be positive numbers.")  
                            continue   # Reprompt the admin for input if the credits or capacity are not valid

                        # Ensure the new capacity is not lower than the current number of enrolled students
                        if new_capacity < len(course.get_students()):
                            print(f"Capacity cannot be lower than the current enrollment of {len(course.get_students())} students.")
                            continue   # Reprompt the admin for input if the new capacity is too low

                        break   # Exit the loop if both credits and capacity are valid

                    # Notify admin of the error and reprompt for input
                    except ValueError:
                        print("Invalid input. Please enter valid whole numbers for credits and capacity.")

                # Update the course with the new values
                if registration_system.update_course(course, new_title, new_description, new_credits, new_capacity):
                    print(f"Course {course.get_title()} updated successfully.")
                else:
                    print("Failed to update the course.")
                break   # Exit the loop after updating the course

        # Search for a course
        elif selection == "4":
            # Reprompt the admin to enter the course ID or title to search for
            while True:
                # Search using user input term
                search_term = input("Enter the course ID or course title to search for: ").strip()

                # Conditional to ensure input is not empty
                if search_term == "":
                    print("Course ID or title cannot be empty.")
                    continue   # Reprompt the admin for input if the search term is empty

                # Search for the course using the provided search term
                course = registration_system.search_course(search_term)

                # Handle if the course is not found
                if course is None:
                    print("Course not found. Please try again.")
                    continue   # Reprompt the admin for input if the course is not found

                # Display the found course details
                print(f"Course ID: {course.get_course_ID()}")
                print(f"Course Title: {course.get_title()}")
                print(f"Course Description: {course.get_description()}")
                print(f"Course Credits: {course.get_credits()}")
                print(f"Course Capacity: {course.get_capacity()}")
                print(f"Enrolled Students: {len(course.get_students())}")

                # Logic to handle if the course is full
                if len(course.get_students()) >= course.get_capacity():
                    status = "Full"
                else:
                    status = "Not Full"
                print(f"Course Status: {status}")   # Display whether the course is full or not

                break   # Exit the loop after displaying the course details

        # Selection to handle viewing students who are enrolled in a course
        elif selection == "5":
            # Reprompt the admin to enter the course ID or title to search for students enrolled in that course
            while True:
                # Search using admin input to find the course
                search_term = input("Enter the course ID or course title to search for: ").strip()

                # Conditional to ensure input is not empty
                if search_term == "":
                    print("Course ID or title cannot be empty.")
                    continue   # Reprompt the admin for input if the search term is empty

                # Search for the course using the provided search term
                course = registration_system.search_course(search_term)

                # Handle if the course is not found
                if course is None:
                    print("Course not found. Please try again.")
                    continue   # Reprompt the admin for input if the course is not found

                # Display the list of students enrolled in the course
                students = registration_system.get_students_in_course(course)

                # Print formatted report showing the list of students enrolled in a course
                print("\n" + "=" * 55)
                print("           COURSE ENROLLMENT REPORT")
                print("=" * 55)
                print(f"Course ID: {course.get_course_ID()}")
                print(f"Course Title: {course.get_title()}")
                print(f"Description: {course.get_description()}")
                print(f"Credits: {course.get_credits()}")
                print(f"Capacity: {course.get_capacity()}")
                print(f"Current Enrollment: {len(students)}")
                print("-" * 55)

                # Check if there are any students enrolled in the course and display the result
                if len(students) == 0:
                    print("No students are currently enrolled in this course.")
                else:
                    print("Students enrolled in this course:")

                    # Loop through the list of students and print their user IDs
                    for student in students:
                        print(f"- Student ID: {student.get_user_ID()}")

                print("=" * 55)   # End of course enrollment report

                break   # Exit the loop after displaying the list of students

        # Selection to handle viewing a student's course report
        elif selection == "6":
            # Reprompt the admin for input if the student is not found
            while True:
                # Prompt the admin to enter the student ID
                student_ID = input("Enter the student ID: ").strip()

                # Validate that the input is not empty
                if student_ID == "":
                    print("Student ID cannot be empty.")   # Notify the admin that the input cannot be empty
                    continue   # Reprompt the admin for input if the student ID is empty

                # Search for the student
                student = None

                # Loop through the list of users to find the student with the matching ID
                for user in users:
                    # Check if the current user is a student and if their ID matches the input student ID using .strip() and .lower() making data consistent
                    if (
                        user.get_role().strip().lower() == "student"
                        and user.get_user_ID().strip().lower() == student_ID.lower()
                    ):
                        # Assign the found user to the student variable
                        student = user
                        # Exit the loop once the student is found
                        break

                # Handle if the student is not found
                if student is None:
                    print("Student not found. Please try again.")
                    continue  # Reprompt the admin for input if the student is not found

                # Get the courses the student is registered for
                courses = registration_system.get_courses_for_student(student)

                # Print formatted student course report
                print("\n" + "=" * 55)
                print("            STUDENT COURSE REPORT")
                print("=" * 55)
                print(f"Student ID: {student.get_user_ID()}")
                print("-" * 55)

                # Check if the student is registered for any courses and print the appropriate message
                if len(courses) == 0:
                    print("This student is not currently registered for any courses.")
                else:
                    print("Registered Courses:")

                    # Loop through each course the student is registered in and print its details
                    for course in courses:
                        print("-" * 55)
                        print(f"Course ID: {course.get_course_ID()}")
                        print(f"Course Title: {course.get_title()}")
                        print(f"Description: {course.get_description()}")
                        print(f"Credits: {course.get_credits()}")
                        print(f"Capacity: {course.get_capacity()}")

                # Print a closing line after listing all courses
                print("=" * 55)

                # Exit the loop after displaying the student's course report
                break

        # Option 7 logic to print all student IDs and passwords  
        elif selection == "7":

            # Retrieve all student credentials
            credentials = registration_system.get_student_credentials()

            # Print formatted student credential report
            print("\n" + "=" * 55)
            print("           STUDENT CREDENTIAL REPORT")
            print("=" * 55)

            # Check if there are no students credentials and display a message indicating this
            if len(credentials) == 0:
                print("No student credentials found.")
            else:
                # Loop through each student ID and password and print the information in a report
                for student_ID, password in credentials:
                    print(f"Student ID: {student_ID}")
                    print(f"Password: {password}")
                    print("-" * 55)

            # Print a closing line after displaying all student credentials
            print("=" * 55)

        # Print a report showing all university courses available   
        elif selection == "8":
            # Retrieve all courses from the registration system
            all_courses = registration_system.get_all_courses()

            # Print formatted all courses report
            print("\n" + "=" * 55)
            print("                ALL COURSES REPORT")
            print("=" * 55)

            # Check if there are no courses in the registration system and display a message to this effect
            if len(all_courses) == 0:
                print("No courses are currently available.")
            else:
                # Loop through each course and display its details
                for course in all_courses:

                    # Determine whether the course is full
                    if len(course.get_students()) >= course.get_capacity():
                        status = "Full"
                    else:
                        status = "Not Full"

                    # Print the course information
                    print(f"Course ID: {course.get_course_ID()}")
                    print(f"Course Title: {course.get_title()}")
                    print(f"Description: {course.get_description()}")
                    print(f"Credits: {course.get_credits()}")
                    print(f"Capacity: {course.get_capacity()}")
                    print(f"Current Enrollment: {len(course.get_students())}")
                    print(f"Status: {status}")
                    print("-" * 55)

            # Print a closing line after displaying all courses
            print("=" * 55)

        # Handle logging out if the admin selects 9
        elif selection == "9":
            # Display a logout message
            print("Logging out... Goodbye!")
            break  # Exit the admin menu loop
        else:
            # Handle invalid menu selection
            print("Invalid selection. Please try again.")
    
    
    
    
    
    


