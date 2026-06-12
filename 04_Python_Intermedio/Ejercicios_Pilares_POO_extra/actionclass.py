from inidataclass import Datos
from employeeclass import Employee
from adminuserclass import AdminUser
from regularuserclass import Regularuser
from carclass import Car
from motorcycleclass import Motorcycle


# import inidataclass

class Menu_Actions(Datos):
    def __init__(self, path):
        # self.contador = 0
        self.path = path
        self.balance = 0
        
        
    def show_menu(self):
        for index, exercise in enumerate(self.list_exercise) :
            print(f'{index} - {exercise}')    
            # self.contador+=1        
    
    def employee_exercise( name, amount):
        employee = Employee(name, amount)
        print(f'Nombre: {employee.name}\nSalario: {employee.salary}')
        percentaje =  int(input(f'Digite el porcentaje de aumento\n'))
        employee.promote(percentaje)
        print(f'Nombre: {employee.name}\nNuevo Salario: {employee.salary}')
    
    def user_exercise():
        user1 = AdminUser()
        user2 = Regularuser()
        print(f'Usuario 1 Role: {user1.get_role()} ')
        print(f'Usuario 2 Role: {user2.get_role()} ')
        print(f'Usuario 1, acceso a Lectura: {user1.has_permission('Read')}')
        print(f'Usuario 1, acceso a Eliminar: {user1.has_permission('Delete')}')
        print(f'Usuario 1, acceso a Modificar: {user1.has_permission('Modify')}')
        print(f'Usuario 2, acceso a Lectura: {user2.has_permission('Read')}')
        print(f'Usuario 2, acceso a Eliminar: {user2.has_permission('Delete')}')
        print(f'Usuario 2, acceso a Modificar: {user2.has_permission('Modify')}')

    def vehicle_exercise():
        vehicle1 = Car('Toyota','2016','4','Yaris')
        vehicle2 = Motorcycle('Yamaha', '2015','Yamaha MT-03','2','321 cc, bicilíndrico')
        print(vehicle1.get_info())
        print(vehicle2.get_info())



        

        

        


