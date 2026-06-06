import salaryclass

class Employee:

    def __init__(self,name, salary):
        self.__name = name 
        self.__salary = salaryclass.Salary(salary) 
    
    @property
    def name(self):
        return self.__name
    
    @property
    def salary(self):
        return self.__salary
    

