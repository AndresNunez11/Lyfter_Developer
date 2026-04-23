import circleclass
import busclass

#Funcion principal del sistema 
def main():
    try:
        # my_circle = circleclass.Circle(3)
        # my_circle.circle_area()
        # my_circle2 = circleclass.Circle(9)
        # my_circle2.circle_area()
        my_bus = busclass.Bus(3)
        my_bus.add_passengers()

    except Exception as e:
        print(f'Existe un error al iniciar la aplicacion {e}')


#Inicio del Sistema
if __name__ == "__main__":
    main()