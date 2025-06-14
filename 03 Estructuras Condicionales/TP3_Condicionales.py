"""
1) Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años,
deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”.
"""

edad = int(input("Ingrese su edad: "))
if edad > 18:
    print("Es mayor de edad")

"""
2) Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá
mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el
mensaje “Desaprobado”.
"""

nota = float(input("Ingrese su nota: "))  # Usamos float para permitir decimales (ej: 7.5)

if nota >= 6:
    print("Aprobado")
else:
    print("Desaprobado")

"""
3) Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un
número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso
contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del
operador de módulo (%) en Python para evaluar si un número es par o impar.
"""

numero = int(input("Ingrese un número par: "))

while numero % 2 != 0:  # Mientras el número sea impar, repite
    print("Por favor, ingrese un número par")
    numero = int(input("Ingrese un número par: "))

print("Ha ingresado un número par")  # Sale del bucle cuando es par

"""
4) Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las
siguientes categorías pertenece:
● Niño/a: menor de 12 años.
● Adolescente: mayor o igual que 12 años y menor que 18 años.
● Adulto/a joven: mayor o igual que 18 años y menor que 30 años.
● Adulto/a: mayor o igual que 30 años.
"""

edad = int(input("Ingrese su edad: "))

if edad < 12:
    print("Niño/a")
elif 12 <= edad < 18:
    print("Adolescente")
elif 18 <= edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

"""
5) Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres
(incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en
pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por
pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso
de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal
como una lista o un string.
"""

contraseña = input("Ingrese una contraseña (8-14 caracteres): ")
longitud = len(contraseña)

if 8 <= longitud <= 14:
    print("Ha ingresado una contraseña correcta")
else:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

"""
6) Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si
hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.
"""

import random
from statistics import mode, median, mean

# Generar lista de 50 números aleatorios
numeros_aleatorios = [random.randint(1, 100) for _ in range(50)]

# Calcular moda, mediana y media
moda_valor = mode(numeros_aleatorios)
mediana_valor = median(numeros_aleatorios)
media_valor = mean(numeros_aleatorios)

# Determinar el sesgo
if media_valor > mediana_valor and mediana_valor > moda_valor:
    sesgo = "Sesgo positivo (a la derecha)"
elif media_valor < mediana_valor and mediana_valor < moda_valor:
    sesgo = "Sesgo negativo (a la izquierda)"
else:
    sesgo = "Sin sesgo aparente"

# Mostrar resultados
print(f"Lista generada: {numeros_aleatorios}")
print(f"Moda: {moda_valor}")
print(f"Mediana: {mediana_valor}")
print(f"Media: {media_valor}")
print(f"Resultado: {sesgo}")

"""
7) Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado
termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por
pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por
pantalla.
"""

texto = input("Ingrese una frase o palabra: ")

# Verificar si el texto no está vacío y si su último carácter es una vocal
if len(texto) > 0 and texto[-1] in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:
    print(texto + "!")
else:
    print(texto)

"""
8) Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3
dependiendo de la opción que desee:
1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO.
2. Si quiere su nombre en minúsculas. Por ejemplo: pedro.
3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro.
El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el
usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(),
lower() y title() de Python para convertir entre mayúsculas y minúsculas.
"""

nombre = input("Ingrese su nombre: ")
print("\nOpciones de formato:")
print("1. Nombre en MAYÚSCULAS (ejemplo: PEDRO)")
print("2. Nombre en minúsculas (ejemplo: pedro)")
print("3. Nombre con la primera letra mayúscula (ejemplo: Pedro)")
opcion = input("Seleccione una opción (1, 2 o 3): ")

if opcion == "1":
    print("\nResultado:", nombre.upper())
elif opcion == "2":
    print("\nResultado:", nombre.lower())
elif opcion == "3":
    print("\nResultado:", nombre.title())
else:
    print("\nError: Opción no válida. Debe ingresar 1, 2 o 3.")

"""
9) Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la
magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado
por pantalla:
● Menor que 3: "Muy leve" (imperceptible).
● Mayor o igual que 3 y menor que 4: "Leve" (ligeramente perceptible).
● Mayor o igual que 4 y menor que 5: "Moderado" (sentido por personas, pero
generalmente no causa daños).
● Mayor o igual que 5 y menor que 6: "Fuerte" (puede causar daños en estructuras
débiles).
● Mayor o igual que 6 y menor que 7: "Muy Fuerte" (puede causar daños significativos).
● Mayor o igual que 7: "Extremo" (puede causar graves daños a gran escala).
"""

magnitud = float(input("Ingrese la magnitud del terremoto: "))

if magnitud < 3.0:
    categoria = "Muy leve (imperceptible)"
elif 3.0 <= magnitud < 4.0:
    categoria = "Leve (ligeramente perceptible)"
elif 4.0 <= magnitud < 5.0:
    categoria = "Moderado (sentido por personas, generalmente sin daños)"
elif 5.0 <= magnitud < 6.0:
    categoria = "Fuerte (puede causar daños en estructuras débiles)"
elif 6.0 <= magnitud < 7.0:
    categoria = "Muy fuerte (puede causar daños significativos)"
else:
    categoria = "Extremo (puede causar graves daños a gran escala)"

print(f"\nClasificación: {categoria}")

"""
10) Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes
del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla
si el usuario se encuentra en otoño, invierno, primavera o verano.
"""

hemisferio = input("¿En qué hemisferio estás? (N para Norte / S para Sur): ")
mes = int(input("Ingresa el mes (1-12): "))
dia = int(input("Ingresa el día (1-31): "))

# Determinar el rango de fechas para cada estación
if (mes == 12 and dia >= 21) or (mes <= 3 and dia <= 20):
    estacion_norte = "Invierno"
    estacion_sur = "Verano"
elif (mes == 3 and dia >= 21) or (mes <= 6 and dia <= 20):
    estacion_norte = "Primavera"
    estacion_sur = "Otoño"
elif (mes == 6 and dia >= 21) or (mes <= 9 and dia <= 20):
    estacion_norte = "Verano"
    estacion_sur = "Invierno"
else:
    estacion_norte = "Otoño"
    estacion_sur = "Primavera"

# Asignar la estación según el hemisferio
if hemisferio == "N":
    print(f"\nEstación: {estacion_norte}")
elif hemisferio == "S":
    print(f"\nEstación: {estacion_sur}")
else:
    print("\nError: Hemisferio no válido. Ingresa 'N' o 'S'.")