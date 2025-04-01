# 1) Crear un programa que imprima por pantalla el mensaje: "Hola Mundo!".

print("Hola Mundo!")

# 2) Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo con su nombre.

nombre = input("Ingresa tu nombre: ")
print(f"Hola {nombre}!")

# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla los datos ingresados.

nombre = input("Nombre: ")
apellido = input("Apellido: ")
edad = input("Edad: ")
lugar = input("Lugar de residencia: ")
print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {lugar}.")

# 4) Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

import math
radio = float(input("Ingrese el radio del círculo: "))
area = math.pi * radio ** 2
perimetro = 2 * math.pi * radio
print(f"El área es {area:.2f} y el perímetro es {perimetro:.2f}.")

# 5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

segundos = int(input("Ingrese la cantidad de segundos: "))
horas = segundos / 3600
print(f"{segundos} segundos equivalen a {horas:.2f} horas.")

# 6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

numero = int(input("Ingrese un número: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

# 7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos.

a = float(input("Ingrese el primer número: "))
b = float(input("Ingrese el segundo número: "))
print(f"Suma: {a + b}, Resta: {a - b}, Multiplicación: {a * b}, División: {a / b:.2f}")

# 8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.

peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print(f"Su IMC es {imc:.2f}")

# 9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.

celsius = float(input("Ingrese la temperatura en Celsius: "))
fahrenheit = (9/5) * celsius + 32
print(f"{celsius}°C equivalen a {fahrenheit:.2f}°F")

# 10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números.

n1 = float(input("Ingrese el primer número: "))
n2 = float(input("Ingrese el segundo número: "))
n3 = float(input("Ingrese el tercer número: "))
promedio = (n1 + n2 + n3) / 3
print(f"El promedio es {promedio:.2f}")






