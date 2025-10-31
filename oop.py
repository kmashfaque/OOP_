class Employee:
    def __init__(self, name, id, dept, salary, designation):
        self.name = name 
        self.id = id
        self.dept = dept
        self.salary = salary
        self.designation = designation

sam = Employee("Sam", 12, "IT", 35000, "Executive")

print(f"{sam.name} is our new employee. His id is {sam.id}. His department is {sam.dept} and salary is negotiated at {sam.salary}. His designation will be {sam.designation} ")
# print(sam.id)
# print(sam.dept)
# print(sam.salary)
# print(sam.designation)