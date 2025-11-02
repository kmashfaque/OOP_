class Employee:

    def __init__(self):
        self.name = "" 
        self.id = ""
        self.dept = ""
        self.salary = ""
        self.designation = ""
        self.password = ""
        self.loggedin = False
        # self.user()

    # getter
    def get_user_name(self):
        return self.name
    
    #setter
    def set_user_name(self, value):
        self.name = value

    def user(self):
        user_input = input("""Welcome to chatbook. How would you like to proceed!!
                           1. Enter 1 to sign Up
                           2. Enter 2 to sign In ==> """)

        if user_input == "1":
            self.signUp()

        if user_input == "2":
            self.signIn()

        
    def signUp(self):
        name = input("Enter your name: ")
        password = input("Enter password: ")
        dept = input("Enter your department: ")
        self.name = name 
        self.password = password
        self.dept = dept

        print("Signup successfully")
        self.user()

    def signIn(self):
        if not self.name and not self.password:
            print("You need to signup first")

        else:
            name = input("Enter you name: ")
            password = input("Enter you password: ")
            if self.name == name and self.password == password:
                self.loggedin = True
                print("Sign in successfully.")
                exit()
            else:
                print("Your creddential is incorrect!! Try Again")
                exit()
            
    
    
sam = Employee()

