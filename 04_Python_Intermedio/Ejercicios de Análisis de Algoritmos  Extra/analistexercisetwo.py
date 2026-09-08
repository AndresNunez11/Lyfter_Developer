class ExerciseTwo:

    def print_answer(self):
        print(f'Complejidad: \n linear_search-> O(n) \n binary_search-> O(log n)')
        print(f'Linear Search conviene cuando:\n Cuando es una lista pequeña y cuando la lista no esta ordenada \nBinary Search conviene cuando: \n La lista esta ordenada, y hay muchos elementos dentro de la lista ')
        print(f'Si la lista no esta ordenada debemos de usar Linear Search para llegar al resultado esperado')

    def linear_search(my_list, target): #O(n)
        for item in my_list: #O(n)
            if item == target: #O(1)
                return True #O(1)
        return False #O(1)

    def binary_search(my_list, target):
        low = 0 #O(1)
        high = len(my_list,) - 1 #O(1)
        while low <= high: # O(log n)
            mid = (low + high) // 2
            if my_list[mid] == target: #O(1)
                return True #O(1)
            elif my_list[mid] < target: #O(1)
                low = mid + 1 #O(1)
            else: #O(1)
                high = mid - 1 #O(1)
        return False #O(1)