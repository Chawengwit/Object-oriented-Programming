# SuperClass
class Employee:
    _minsalary = 12000
    __maxsalary = 1000000
    company = "WithU Development"

    def __init__(self, name, salary, department):
        self.__name = name
        self.__salary = salary
        self._department = department

    # Method 
    def _showDatabyGetter(self):
        print("normal Method by Getter : {}".format(self.__name))
        print("normal Method by Getter : {}".format(self.__salary))

#############################################################


#SubClass (child)
class Accounting(Employee):
    def __init__(self):
        pass

class Programmer(Employee):
    def __init__(self):
        pass

class Sale(Employee):
    def __init__(self):
        pass


#############################################################

# Object
accounting = Accounting()
print("Global Variable",accounting.company)

programmer = Programmer()
print("Protect Variable",programmer._minsalary)

sale = Sale()
print("Private Variable",sale._Employee__maxsalary)
