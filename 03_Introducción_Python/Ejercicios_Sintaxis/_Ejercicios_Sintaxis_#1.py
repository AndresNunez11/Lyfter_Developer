'''
Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.
Si le salen errores, no se asuste. Lealos e intente comprender qué significan.
Los errores son oportunidades de aprendizaje.
Por ejemplo:
string + string → ?
string + int → ?
int + string → ?
list + list → ?
string + list → ?
float + int → ?
bool + bool → ?
'''

string = 'test string'
string2= 'test string2'
number = 2
list1 =[1,2,3,4]
list2 = ['andres', 'jose', 'pablo', 'pedro']
list3 = [4,5,6,7]
decimal_number = 123.1234
bool1 = True
bool2 = False
bool3 = True
bool4 = False


"string + string → ?"
print(string+string2) 
"= prueba stringprueba string2"

"string + int → ?"
print(string+number)
"= TypeError: can only concatenate str (not "int") to str"

"int + string → ?"
print(number+string)
"= TypeError: unsupported operand type(s) for +: 'int' and 'str'"

"list + list → ?"
print(list1 + list3) 
"=[1, 2, 3, 4, 4, 5, 6, 7]"
print(list1+list2)
"[1, 2, 3, 4, 'andres', 'jose', 'pablo', 'pedro']"

"string + list → ?"
print(string + list3)
"= TypeError: can only concatenate str (not "list") to str"

"float + int → ?"
print(decimal_number+number)
"= 125.1234"

"bool + bool → ?"
print(bool1 + bool2)
print(bool1 + bool3)
print(bool2 + bool4)
"= 1 - 2 - 0"

