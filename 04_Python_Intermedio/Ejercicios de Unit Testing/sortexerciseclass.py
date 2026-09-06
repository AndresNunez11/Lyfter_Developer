# numberslist= 'A'
# numberslist2= [5,6,7,8,4,3,9,2,1]


def bubble_sort(numberslist):
    large = len(numberslist)
    for i in range(large):
        for j in range(0,large-i-1):
            if numberslist[j] > numberslist[j + 1]:
                numberslist[j],numberslist[j + 1] = numberslist[j + 1], numberslist[j]
    # print(f'{numberslist}')
    return numberslist

def bubble_sort_steps(numberslist):
    iterations = 0
    comparisons = 0
    large = len(numberslist)
    for i in range(large):
        iterations += 1
        for j in range(0, large - i - 1):
            comparisons += 1
            if numberslist[j] > numberslist[j + 1]:
                numberslist[j], numberslist[j + 1] = numberslist[j + 1], numberslist[j]
    return numberslist, iterations, comparisons

def validated_bubble_sort(numberslist):
    if not isinstance(numberslist, list):
        raise TypeError("El dato no es una lista")
    if len(numberslist) == 0:
        raise ValueError("La lista no puede estar vacía")
    for number in numberslist:
        if not isinstance(number, (int, float)):
            raise ValueError("Error: La lista contiene elementos no numéricos")
    # print(f'{numberslist}')
    return bubble_sort(numberslist)
    

# def main():
#     validated_bubble_sort(numberslist)

# main()
            

