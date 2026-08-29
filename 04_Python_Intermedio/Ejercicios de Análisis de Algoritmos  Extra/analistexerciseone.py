class ExerciseOne:

    def print_answer(self):
        print(f'Complejidad \nmanual_add -> O(n) \nadd_formula -> O(1)')
        print(f'Si el numero es 1000000, utilizaria add_formula, ya que reduce el tiempo de ejecuion, no utiliza un ciclo si no que calcula sobre los datos que nos estan dando')

    def manual_add(n): #O(n)
        result = 0 #O(1)
        for i in range(1, n + 1): #O(n)
            result += i #O(1)
        return result #O(1)

    def add_formula(n): #O(1)
        return n * (n + 1) // 2 #O(1)
