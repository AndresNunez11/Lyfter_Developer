class Salary:
    def __init__(self, salary):
        self.salary = salary
    
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        if float(salary) < 0:
            raise ValueError(f' El salario no puede ser negativo')
        self.__salary = float(salary)
        

    def promote(self, percentage):
        self.__salary = float(self.__salary)*(1+float(percentage)/100)
    
    
    
