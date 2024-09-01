import os
os.system("cls")

def suma(a, b):
    suma=a + b
    return suma

def resta(a,b):
    resta=a - b
    return resta

def division(a,b):
    division=a / b
    return division
def multiplicacion(a,b):
    multiplicacion=a * b
    return multiplicacion


num1=int(input("poner un numero: "))
num2=int(input("poner otro numero: "))
operacion = input("poner simbolo     +       -       /      *     : ")

if operacion == "+":
    print (suma(num1, num2))
elif operacion == "-":
    print(resta(num1, num2))
elif operacion == "*":
    print(multiplicacion(num1, num2))
elif operacion == "/":
    print(division(num1, num2))
else:
    print("error")

os.system("pause")
