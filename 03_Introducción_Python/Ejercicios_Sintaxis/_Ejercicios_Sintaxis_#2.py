"""
Cree un programa que le pida al usuario su nombre, apellido, y edad, 
y muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, 
adulto, o adulto mayor.
"""

name = input("Please indicate your name:: ")
last_name = input("Please indicate your last name:: ")
age = int(input("Please indicate your age:: "))

if(age <= 5 ):
    print(f"Your name is {name} {last_name} and your age is {age}. You are a baby.")
elif(age <= 10):
    print(f"Your name is {name} {last_name} and your age is {age}. You are a child.")
elif(age<13):
    print(f"Your name is {name} {last_name} and your age is {age}. You are a preadolescent.")
elif(age<18):
    print(f"Your name is {name} {last_name} and your age is {age}. You are an adolescent.")
elif(age<25):
    print(f"Your name is {name} {last_name} and your age is {age}. You are a young adult.")
elif(age<60):
    print(f"Your name is {name} {last_name} and your age is {age}. You are an adult.")
else:
    print(f"Your name is {name} {last_name} and your age is {age}. You are an elderly adult.")
