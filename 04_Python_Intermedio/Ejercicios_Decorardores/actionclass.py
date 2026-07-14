from inidataclass import Datos
from personalinfoclass import Personalinfo
from numbersclass import Numbers
from userclass import User



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



    # se llama al decorardor al crear el usuario, se utiliza el @ la clase y el metodo
    @Personalinfo.print_info
    def create_user_info(self, name,lastname,**kwargs):
        print(f'La informacion se esta agregando a la base de datos...')
        print(f'La informacion de: {name} {lastname}, fue agregada correctamente')
        return name
        # print(f'Informacion del usuario agregada')
        


    @Numbers.validate_numbers
    def numbers(*args):
        return(f'Fin de la validaciion')
        # while  True:
        #     pass
        
    def new_user(self, name, birthday):
        return User(name, birthday)
    
    @User.major_age        
    def show_user(self,user):
        pass

    
    

        

        

        


