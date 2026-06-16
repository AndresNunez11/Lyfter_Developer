from userclass import User

class AdminUser(User):
    def __init__(self):
        self._permissions = ['Modify','Read', 'Delete']

    def get_role(self):
        return 'Administrador'
    
    def has_permission(self, permission):
        if permission in self._permissions:
            return True
        else: 
            return False
    


