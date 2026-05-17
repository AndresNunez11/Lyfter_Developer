from inidataclass import Datos
import bankaccountclass
import savingaccountclass
import circleclass, squareclass, rectangleclass
import smartphoneclass

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
    
    #ejercicio #1
    @staticmethod # Para no enviar ningun dato
    def bankacount(self): # (self, data) Se esta enviando el self y opction al llamar al objeto
        my_acount = bankaccountclass.BankAcount()
        print(f'Ingresa 1000 a la cuenta')
        my_acount._add_money(1000)
        print(f'Balance = {my_acount.balance}')
        print(f'Retira 500 de la cuenta')
        my_acount._substract_balance(500)
        print(f'Nuevo Balance = {my_acount.balance}')
        return my_acount.balance
    
    #ejercicio #1
    def saving_account(self, min_amount, amount, balance):
        my_account = savingaccountclass.SavingAccount(min_amount, amount, balance)
        return my_account.validate_balance()
        
    
    #ejercicio #3
    def calculate_shapes(self):
        my_rectangule = rectangleclass.Rectangule(large=(int(input(f'Digite el largo del rectangulo\n'))),width=(int(input(f'Digite el ancho del rectangulo\n'))))
        print(f'El area del rectangulo es:\n {my_rectangule.calculate_area()}\n El perimetro del rectangulo es:\n {my_rectangule.calculate_perimeter()}')
        my_square = squareclass.Square(side=(int(input(f'Digite el largo de lado del cuadrado\n'))))
        print(f'El area del cuadrado es:\n {my_square.calculate_area()}\n El perimetro del cuadrado es:\n {my_square.calculate_perimeter()}')
        my_circle = circleclass.Circle(radius=(int(input(f'Digite el largo del radio del circulo\n'))))
        print(f'El area del circulo es:\n {my_circle.calculate_area()}\n El perimetro del circulo es:\n {my_circle.calculate_perimeter()}')
        
    
    #ejercicio #3
    def Inheritance(self):
        my_iphone = smartphoneclass.Smartphone()
        print('Encender telefono: ')
        my_iphone.turn_on()
        print('Tomar una fotografia: ')
        my_iphone.take_photo()
        print('Realizar una llamada: ')
        my_iphone.Call()
        

        

        


