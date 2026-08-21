from nodoclass import Node
from listmodelclas import ListModel

#Clase para que el nombre no puede estar vacio
class emptyTypeError(Exception):
    def __init__(self):
        super().__init__(f' La lista no puede estar vacia')

class BubbleSort():
    new_list: "ListModel"
    head: "Node"

    def __init__(self, newlist):
        self.new_list = newlist
        self.head = self.new_list.head

    #Validar que la nota ingresada este entre 0 y 100
    def validate_number(self, newnumber):
        try:
            newnumber = int(newnumber)
            return newnumber
        except ValueError:
            raise ValueError("Error: La lista contiene elementos no numéricos")  

    def validate_empty_list(self):
        # print('Obteniendo datos de la lista')
        if self.new_list.head is None:
            raise emptyTypeError()
    
        
    def bubble_sort_linkedlist(self):
        try:
            # print(f'Validando la lista ....')
            self.validate_empty_list()
            currentNode = self.head
            # print(f'Validando los numeros ....')
            while currentNode is not None:
                # print(f'Validando si {currentNode.data} es un numero')
                self.validate_number(currentNode.data)
                # print('OK')
                currentNode = currentNode.next
            # print(f'Ordenando los numeros ....')
            swapped = True
            i=1   
            c=1     
            # print(currentNode.data)
            # print(currentNode.next.data)
            while swapped:
                swapped = False
                previousNode = None
                currentNode = self.head
                # print(f'Numero de iteracion {i}')
                # print(f'Compara Nodo actual {currentNode.data} -> siguente Nodo {currentNode.next.data}') 
                while currentNode.next is not None:
                    # print(f'Ciclo interno {c}')
                    if int(currentNode.data) > int(currentNode.next.data):
                        # print(f'Validar si es mayor {currentNode.data} -> {currentNode.next.data}') 
                        auxNode = currentNode
                        currentNode = currentNode.next
                        auxNode.next = currentNode.next
                        currentNode.next = auxNode
                        if previousNode is None:
                            self.head = currentNode
                        else:
                            previousNode.next = currentNode
                        # print(f'Reemplazar valor {currentNode.data} -> {currentNode.next.data}') 
                        swapped = True
                        c+=1
                    previousNode = currentNode
                    currentNode = currentNode.next  
                i+=1
            self.new_list.head = self.head
            self.new_list.print_structre()
            print(f'Cantidad de Iteraciones:{i}')
            print(f'Cantidad de cambios realizados: {c}')
        except (emptyTypeError, ValueError) as error:
            print(f'Existe un error al ordenar la lista {error}') 



