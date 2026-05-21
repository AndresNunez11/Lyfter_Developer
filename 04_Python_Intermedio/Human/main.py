import humanclass

def main():
    try:
        person = humanclass.Human()
        print(person)
    except Exception as e:
        print(f'Error al correr la funcion principal. Error: {e}')

#Inicio del Sistema
if __name__ == "__main__":
    main()