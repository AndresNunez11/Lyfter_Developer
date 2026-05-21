from bankaccountclass import BankAcount


class SavingAccount(BankAcount):
    
    def __init__(self, min_balance, amount, balance):
        self.min_balance = min_balance 
        self.transaction_amount = amount
        self.balance = balance
    
    def validate_balance(self):
        try:
            print(f'Saldo: {self.balance}')
            self._substract_balance(self.transaction_amount)
            if self.balance < self.min_balance:
                self._add_money(self.transaction_amount)
                print(f'Fondos insuficientes. Saldo: {self.balance}')
                print(f'El monto minimo a mantener en la cuenta es {self.min_balance} ')
                return self.balance
            else:
                print(f'Se afecto el balance de la cuenta. Saldo: {self.balance}')
                return self.balance
        except Exception as e:
            print(f'Error al validar el balance de la cuenta. Error: {e}')
        
