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
        return self.__salary.salary # devuelve el valor numérico contenido dentro del objeto Salary. sin ese punto salary devuelve el objeto, puedo llamarlo porque salary es una propiedad en clase salary
    
    def promote(self, percentaje):
        self.__salary.promote(percentaje)

    

