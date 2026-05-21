
"""
Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
"""

first_list = ['Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list = ['casos', 'los', 'la', 'por', 'es', 'util']
index=0

if(len(first_list)==len(second_list)):  
    while (index < len(first_list)):
        dato1 = first_list[index]
        dato2 = second_list[index]    
        print(f"{dato1} {dato2}")
        index+=1
else:
    print("Las listas no son del mismo tamaño")


first_list2 = ['Primera lista','Hay', 'en', 'que', 'iteracion', 'indices', 'muy']
second_list2 = ['y Segunda segunda','casos', 'los', 'la', 'por', 'es', 'util']

if(len(first_list2)==len(second_list2)):  
    for index in range(0, len(first_list2)):
        dato1 = first_list2[index]
        dato2 = second_list2[index]    
        print(f"{dato1} {dato2}")
else:
    print("Las listas no son del mismo tamaño")
