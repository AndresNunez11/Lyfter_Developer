import personclass

class Bus:
    

    def __init__(self, max_passengers):
        self.max_passengers = max_passengers
        self.bus_passengers = 0 
        self.person_list=[]
        

    def add_passengers(self, person):
        try:
            if self.bus_passengers<self.max_passengers:
                self.bus_passengers+=1
                self.person_list.append(person)
                print(f"Ha subido la persona numero {person.number} al bus!")
                print(f'Cantidad de pasageros en el bus{len(self.person_list)},\nCapacidad: {self.max_passengers}\nDisponible {self.max_passengers-self.bus_passengers}')
            else:
                print(f"La persona numero {person.number} intenta subir al bus, pero:")
                print(f'No hay capacidad en el autobus para subir a otro pasajero')
        except Exception as e:
            print(f'Error al intentar subir un pasajero al autobus. Error:{e}')
    
    def remote_passengers(self, person):
        try:
            if person in self.person_list:
                self.bus_passengers-=1
                self.person_list.remove(person)
                print(f"El pasajero {person.number} se ha bajado del bus")
                print(f'Pasajeros actuales: {len(self.person_list)},\nCapacidad: {self.max_passengers}\nDisponible {self.max_passengers-self.bus_passengers}')
            else:
                print(f"El pasajero {person.number} no está en el bus")   
        except Exception as e:
            print(f'Error al intentar bajar un pasajero al autobus. Error:{e}') 
        
        


    


