"""
Cree un programa que elimine todos los números impares de una lista.

"""

'''
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list)
for index, data in enumerate(my_list):
    if(data%2 != 0):
        my_list.pop(index)
print(my_list) 
'''

'''
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,11,11,11]
my_list_even = []
print(my_list)
for index, data in enumerate(my_list):
    if(data%2 == 0):
        my_list_even.append(data)
print(my_list_even) 


my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,11,11,11]
my_list_even = []
print(my_list)
for index, data in enumerate(my_list):
    if(data%2 == 0):
        my_list_even.append(data)
print(my_list_even) 

'''
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,11,11,11]
my_list_temp = []
my_list_even = []
len_list = len(my_list)

while(len_list >0):
    data = my_list.pop(len_list-1)
    if(data%2 == 0):
        my_list_temp.append(data)
    len_list -=1
large = len(my_list_temp)
while(large >0):
    my_list_even.append(my_list_temp[large-1])
    large -=1
print(my_list_even)


