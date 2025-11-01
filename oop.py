class Employee:

    def __init__(self):
        self.name = "" 
        self.id = ""
        self.dept = ""
        self.salary = ""
        self.designation = ""
        self.password = ""
        self.user()

    def user(self):
        user_input = input("""Welcome to chatbook. How would you like to proceed!!
                           1. Enter 1 to sign Up
                           2. Enter 2 to sign In ==> """)

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
        if not self.name and not self.password:
            print("You need to signup first")

        else:
            self.name = input("Enter you name: ")
            self.password = input("Enter you password: ")
            print("Sign in successfully.")
            
    
    
sam = Employee()

