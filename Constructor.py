# Class
class Employee:
    # Constructor
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    # Method :
    def printData(self):
        print("Employee name : {} Department : {} and Salary is : {}".format(self.name, self.department, self.salary))

    # Destructor 
    def __del__(self):
        print("del destructor method")


# Object
obj1 = Employee("Witt", 500000, "Technical")
obj1.printData()
obj2 = Employee("Chawengwit", 100000, "Data Engineer")
obj3 = Employee("Hog", 200000, "Product Analyst")

# Showdata
obj1.salary = 150000
obj1.printData()
obj2.printData()
obj3.printData()

# isinstance
print("Obj1 is instance in Employee",isinstance(obj1,Employee))

# List method & attribute
print("Check Method & Attribute : ", dir(obj1))

# Check class
print("Check class Obj1 : ", obj1.__class__)