class Person():
	counter = 0 # variable de clase (se comparte entre todos)

	def __init__(self):
		Person.counter += 1  # ID único automático
		self.number = Person.counter 
		self.name = input('Digite el nombre de la persona: \n ')
		self.age = int(input('Digite edad de la persona: \n'))



	

