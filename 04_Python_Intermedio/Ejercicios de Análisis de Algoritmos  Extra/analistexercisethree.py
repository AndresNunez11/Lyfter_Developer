class ExerciseThree:

    def print_answer(self):
        print(f'La complejidad es: \n print_all_pairs -> #O(n^2)')
        print(f'Si cada clave tarda un segundo, en total serian 1 billon de segundos. (1,000,000 * 1,000,000 = 1,000,000,000,000)')

    def print_all_pairs(my_dict): #O(n^2)
        for key1 in my_dict: #O(n)
            for key2 in my_dict: #O(n^2)
                print(f"{key1}-{key2}") #O(1)