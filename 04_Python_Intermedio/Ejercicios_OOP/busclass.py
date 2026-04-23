import personclass

class Bus:
    

    def __init__(self, max_passengers, person):
        self.max_passengers = max_passengers
        self.bus_passengers = 0 
        self.person = person

    def add_passengers(self):
        person = personclass.Person(self.bus_passengers)
        self.bus_passengers+=1
    

