import circleclass
import busclass
import personclass

#Funcion principal del sistema 
def main():
    try:
        # my_circle = circleclass.Circle(3)
        # my_circle.circle_area()
        # my_circle2 = circleclass.Circle(9)
        # my_circle2.circle_area()
        person1 = personclass.Person()
        person2 = personclass.Person()
        person3 = personclass.Person()
        person4 = personclass.Person()
        person5 = personclass.Person()
        # person6 = personclass.Person()
        # person7 = personclass.Person()
        # person8 = personclass.Person()
        # person9 = personclass.Person()
        # person10 = personclass.Person()
        # person11 = personclass.Person()

        my_bus = busclass.Bus(3)
        my_bus.add_passengers(person1)
        my_bus.remote_passengers(person2)
        my_bus.add_passengers(person2)
        my_bus.add_passengers(person3)
        my_bus.remote_passengers(person1)
        my_bus.add_passengers(person4)
        my_bus.add_passengers(person5)


    except Exception as e:
        print(f'Existe un error al iniciar la aplicacion {e}')


#Inicio del Sistema
if __name__ == "__main__":
    main()