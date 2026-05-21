class BankAcount:

    def __init__(self):
        self.balance  = 0

    def _add_money(self, amount):
        try:
            self.balance+=amount
            return self.balance
        except Exception as e:
            print(f'Error al ingresar dinero al balance. Error: {e}')    

    def _substract_balance(self, amount):  
        try:
            self.balance-=amount
            return self.balance
        except Exception as e:
            print(f'Error al retirar dinero al balance. Error: {e}')
    


