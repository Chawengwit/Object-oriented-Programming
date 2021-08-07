# Class
class Employee:
    # Constructor (private method)
    def __init__(self, name, salary, department):
        # public attribute
        self.name = name

        # protected attribute
        self._salary = salary

        # private attribute
        self.__department = department

    # Method : public method
    def printData(self):
        print("Employee name : {} Department : {} and Salary is : {}".format(self.name, self.__department, self._salary))

    # Method : protected method
    def _showData(self):
        print("Salary is : {}".format(self._salary))
        print("Department is : {}".format(self.__department))

    # Destructor (private method)
    def __del__(self):
        print("del destructor method")


# Object (public object)
obj1 = Employee("Witt", 100000, "Technical")

# Showdata before change
obj1.printData()

# Can change protected attribute
obj1._salary = 255000

# Canont change private attribute
obj1.__department = "Engineer"

# Showdata after change 
obj1._showData()