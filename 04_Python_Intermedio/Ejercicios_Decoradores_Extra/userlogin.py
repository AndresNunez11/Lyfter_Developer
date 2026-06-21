class UserLogin:

    def __init__(self):
        self.__user_logged_in = False
        

    # def validate_user_info(self, state):
    #     try:
    #         if(bool(state) == True):
    #             self.__user_logged_in = True
    #         else:
    #             self.__user_logged_in = False
    #         return (self.__user_logged_in)
    #     except Exception as e:
    
    def login(self, state):
        self.__user_logged_in = state
    
    @staticmethod
    def requires_login(func):
        def wrapper(self, *args):
            try:
                if (self.__user_logged_in):
                    print('Mostrando perfil del usuario')
                    return func(self, *args)
                else:
                    raise ValueError("Usuario no autenticado.")
            except Exception as e:
                print(f'Error de acceso. Error: {e}')
        return wrapper
    
    @requires_login
    def show_profile(self):
        print('Sesion de Usuario Activa.\nMenu Usuario: ')

