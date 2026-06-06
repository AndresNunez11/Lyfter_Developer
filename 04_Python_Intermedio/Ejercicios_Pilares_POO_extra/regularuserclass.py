from userclass import User

class Regularuser(User):
    def __init__(self):
        self._permissions = ['Read']
    
    def get_role(self):
        return 'Regular'
    
    def has_permission(self, permission):
        if permission in self._permissions:
            return True
        else: 
            return False
        
