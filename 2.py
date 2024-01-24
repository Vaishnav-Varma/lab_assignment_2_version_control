class Employee:
    def __init__(self, id, name, age, salary):
        self.id = id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeDatabase:
    def __init__(self):
        self.employees = []

    def add_employee(self, id, name, age, salary):
        self.employees.append(Employee(id, name, age, salary))

    def sort_by(self, parameter):
        if parameter == "Age":
            self.employees.sort(key=lambda x: x.age)
        elif parameter == "Name":
            self.employees.sort(key=lambda x: x.name)
        elif parameter == "Salary":
            self.employees.sort(key=lambda x: x.salary)
        else:
            print("Invalid parameter")

    def print_employees(self):
        for employee in self.employees:
            print(f"ID: {employee.id}, Name: {employee.name}, Age: {employee.age}, Salary: {employee.salary}")

db = EmployeeDatabase()
db.add_employee("161E90", "Ramu", 35, 59000)
db.add_employee("171E22", "Tejas", 30, 82100)
db.add_employee("171G55", "Abhi", 25, 100000)
db.add_employee("152K46", "Jaya", 32, 85000)

option = input("Enter the parameter to sort by: 1. Age 2. Name 3. Salary: ")
db.sort_by(option)
db.print_employees()
#