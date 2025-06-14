""" 1) Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100
(incluyendo ambos extremos), en orden creciente, mostrando un número por línea."""

for i in range(101):
    print(i)

"""2) Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de
dígitos que contiene."""

# Solicitar número al usuario
numero = int(input("Ingrese un número entero: "))

# Convertimos a string y contamos los dígitos
cantidad_digitos = len(str(numero))

print("La cantidad de dígitos es:", cantidad_digitos)

"""3) Escribe un programa que sume todos los números enteros comprendidos entre dos valores
dados por el usuario, excluyendo esos dos valores."""

# Solicitar los dos números al usuario
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Aseguramos que num1 sea el menor y num2 el mayor
if num1 > num2:
    num1, num2 = num2, num1

suma = 0

# Sumamos los números entre num1 y num2, excluyendo los extremos
for i in range(num1 + 1, num2):
    suma += i

print("La suma de los números entre", num1, "y", num2, "es:", suma)

"""4) Elabora un programa que permita al usuario ingresar números enteros y los sume en
secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese
un 0."""

suma = 0
numero = int(input("Ingrese un número (0 para finalizar): "))

while numero != 0:
    suma += numero
    numero = int(input("Ingrese un número (0 para finalizar): "))

print("La suma total es:", suma)


"""5) Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el
programa debe mostrar cuántos intentos fueron necesarios para acertar el número."""

import random

# Generar número aleatorio entre 0 y 9
numero_secreto = random.randint(0, 9)
intentos = 0

# Bucle hasta que el usuario adivine
adivinanza = -1

while adivinanza != numero_secreto:
    adivinanza = int(input("Adivina el número (entre 0 y 9): "))
    intentos += 1

print("¡Correcto! El número era", numero_secreto)
print("Cantidad de intentos:", intentos)

"""6) Desarrolla un programa que imprima en pantalla todos los números pares comprendidos
entre 0 y 100, en orden decreciente."""

# Desde 100 hasta 0, de 2 en 2
for i in range(100, -1, -2):
    print(i)

"""7) Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un
número entero positivo indicado por el usuario."""

# Pedir al usuario un número entero positivo
n = int(input("Ingrese un número entero positivo: "))

suma = 0

for i in range(n + 1):
    suma += i

print("La suma de los números de 0 a", n, "es:", suma)

"""8) Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el
programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son
negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad
menor, pero debe estar preparado para procesar 100 números con un solo cambio)."""

# Cantidad de números (podés cambiar este valor para probar)
cantidad = 100

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i+1}: "))

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("\nCantidad de pares:", pares)
print("Cantidad de impares:", impares)
print("Cantidad de positivos:", positivos)
print("Cantidad de negativos:", negativos)

"""9) Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la
media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe
poder procesar 100 números cambiando solo un valor)."""

cantidad = 5

suma = 0

for i in range(cantidad):
    numero = int(input(f"Ingrese el número {i+1}: "))
    suma += numero

media = suma / cantidad

print("\nLa media de los números ingresados es:", media)

"""10) Escribe un programa que invierta el orden de los dígitos de un número ingresado por el
usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745."""

# Pedir el número al usuario
numero = int(input("Ingrese un número: "))

# Convertimos a string, invertimos y volvemos a convertir a entero
numero_invertido = int(str(numero)[::-1])

print("El número invertido es:", numero_invertido)