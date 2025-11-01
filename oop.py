class Employee:

    def __init__(self, name, id, dept, salary, designation):
        self.name = name 
        self.id = id
        self.dept = dept
        self.salary = salary
        self.designation = designation
        self.user()

    def user(self):
        user_input = input("""Welcome to chatbook. How would you like to proceed!!
                           1. Enter 1 to sign Up
                           2. Enter 2 to sign In""")

        if user_input == "1":
            self.signUp()

        if user_input == "2":
            self.signIn()

        
    def signUp(self):
        self.name = input("Enter your name: ")
        self.password = input("Enter password: ")
        self.dept = input("Enter your department: ")
        print("Signup successfully")

    def signIn(self):
        self.name = input("Enter you name: ")
        self.password = input("Enter you password")
        print("Sign in successfully.")
         
    
    
sam = Employee("Sam", 12, "IT", 35000, "Executive")

# print(f"{sam.name} is our new employee. His id is {sam.id}. His department is {sam.dept} and salary is negotiated at {sam.salary}. His designation will be {sam.designation} ")
# print(sam.id)
# print(sam.dept)
# print(sam.salary)
# print(sam.designation)