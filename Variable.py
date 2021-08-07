# Class
class Employee:
    #Class Variable
    _minsalary = 12000
    _maxsalary = 1000000

    #Instance Variable
    def __init__(self, name, salary, department):
        self.department = department
        self._salary = salary
        self.__name = name
        
    # Method 
    # used getter method call attribute
    def _showDatabyGetter(self):
        print("normal Method by Getter : {}".format(self.__name))
        print("normal Method by Getter : {}".format(self._salary))

# Object
obj1 = Employee("Witt", 100000, "Technical")

# ShowData
obj1._showDatabyGetter()
print("Global Variable > Min Salary :",Employee._minsalary)
print("Instance Variable > Salary :",obj1._salary)