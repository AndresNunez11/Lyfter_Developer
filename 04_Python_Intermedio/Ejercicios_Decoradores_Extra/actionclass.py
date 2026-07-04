from inidataclass import Datos
from greetuser import GreetUser
from userlogin import UserLogin
from multiply import Multiply


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
    
    def new_user(self, name):
        user = GreetUser(name)
        user.repeat_info()
        print('Fin de ejercicio 1.')
    
    def show_user_profile(self, state):
        login = UserLogin()
        login.login(state)
        login.show_profile()
        print('Fin de ejercicio 2.')
    
    @Multiply.log_call
    @Multiply.validate_numbers
    def call_multiply(self, number1, number2):
        multiply = Multiply(number1, number2)
        return multiply
    


        
    