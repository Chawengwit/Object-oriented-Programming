# Class
class Employee:
    # Constructor
    def __init__(self, name, salary, department):
        # public attribute
        self.department = department

        # protected attribute
        self._salary = salary

        # private attribute
        self.__name = name
        

    # Method 
    def printData(self):
        print("Employee name : {} Department : {} and Salary is : {}".format(self.__name, self.department, self._salary))

    # normal method call attribute
    def _showData(self):
        print("normal Method : {}".format(self.__name))
        print("normal Method : {}".format(self._salary))

    # used getter method call attribute
    def _showDatabyGetter(self):
        print("normal Method by Getter : {}".format(self.getName()))
        print("normal Method by Getter : {}".format(self.getSalary()))
        
    # setter Method
    def setName(self, name):
        self.__name = name

    def setSalary(self, salary):
        self._salary = salary

    # getter Method
    def getName(self):
        return self.__name
    def getSalary(self):
        return self._salary
    
    # Destructor
    def __del__(self):
        print("del destructor method")


# Object (public object)
obj1 = Employee("Witt", 100000, "Technical")

# Showdata before change
obj1.printData()

# Change Private & Protected attribute
obj1.setSalary(250000)
obj1.setName("Wittupuu")


# Showdata after change 
obj1._showData()

# get Object by getter method
print("Getter Name : ",obj1.getName())
print("Getter Salary : ",obj1.getSalary())

# get Object by normal method used getter method
obj1._showDatabyGetter()