"""
1) Dado el diccionario precios_frutas
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva':
1450}
Añadir las siguientes frutas con sus respectivos precios:
● Naranja = 1200
● Manzana = 1500
● Pera = 2300
"""

precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

# Agregar nuevas frutas
precios_frutas['Naranja'] = 1200
precios_frutas['Manzana'] = 1500
precios_frutas['Pera'] = 2300

print(precios_frutas)

"""
2) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, actualizar los precios de las siguientes frutas:
● Banana = 1330
● Manzana = 1700
● Melón = 2800
"""

# Actualización de precios
precios_frutas['Banana'] = 1330
precios_frutas['Manzana'] = 1700
precios_frutas['Melón'] = 2800

print(precios_frutas)

"""
3) Siguiendo con el diccionario precios_frutas que resulta luego de ejecutar el código
desarrollado en el punto anterior, crear una lista que contenga únicamente las frutas sin los
precios.
"""

# Obtener solo los nombres de las frutas (las claves)
lista_frutas = list(precios_frutas.keys())

print(lista_frutas)

"""
4) Escribí un programa que permita almacenar y consultar números telefónicos.
• Permití al usuario cargar 5 contactos con su nombre como clave y número como valor.
• Luego, pedí un nombre y mostrale el número asociado, si existe
"""

# Crear el diccionario vacío
agenda = {}

# Cargar 5 contactos
for i in range(5):
    nombre = input(f"Ingresá el nombre del contacto {i + 1}: ")
    telefono = input(f"Ingresá el número de {nombre}: ")
    agenda[nombre] = telefono

# Consultar un contacto
consulta = input("Ingresá el nombre del contacto que querés consultar: ")

if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print(f"No se encontró el contacto {consulta}.")

"""
5) Solicita al usuario una frase e imprime:
• Las palabras únicas (usando un set).
• Un diccionario con la cantidad de veces que aparece cada palabra.
"""

# Pedir una frase al usuario
frase = input("Ingresá una frase: ")

# Separar la frase en palabras
palabras = frase.split()

# 1. Palabras únicas (conjunto)
palabras_unicas = set(palabras)
print("Palabras únicas:", palabras_unicas)

# 2. Cantidad de veces que aparece cada palabra (diccionario)
contador_palabras = {}
for palabra in palabras:
    if palabra in contador_palabras:
        contador_palabras[palabra] += 1
    else:
        contador_palabras[palabra] = 1

print("Repeticiones de palabras:", contador_palabras)

"""
6) Permití ingresar los nombres de 3 alumnos, y para cada uno una tupla de 3 notas.
Luego, mostrá el promedio de cada alumno.
"""

# Crear un diccionario para guardar los alumnos y sus notas
alumnos = {}

# Ingresar los datos de 3 alumnos
for i in range(3):
    nombre = input(f"Ingresá el nombre del alumno {i + 1}: ")
    notas = tuple(float(input(f"Ingresá la nota {j + 1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

# Mostrar el promedio de cada alumno
for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {alumno} es {promedio:.2f}")

"""
7) Dado dos sets de números, representando dos listas de estudiantes que aprobaron Parcial 1
y Parcial 2:
• Mostrá los que aprobaron ambos parciales.
• Mostrá los que aprobaron solo uno de los dos.
• Mostrá la lista total de estudiantes que aprobaron al menos un parcial (sin repetir)
"""

# Sets de ejemplo
parcial1 = {"Ana", "Juan", "Sofía", "Marcos"}
parcial2 = {"Sofía", "Lucas", "Juan", "Carla"}

# Aprobados en ambos parciales
ambos = parcial1 & parcial2  
print("Aprobaron ambos parciales:", ambos)

# Aprobados solo uno de los dos
solo_uno = parcial1 ^ parcial2  
print("Aprobaron solo uno de los dos:", solo_uno)

# Todos los aprobados
todos = parcial1 | parcial2  
print("Aprobaron al menos un parcial:", todos)

"""
8) Armá un diccionario donde las claves sean nombres de productos y los valores su stock.
Permití al usuario:
• Consultar el stock de un producto ingresado.
• Agregar unidades al stock si el producto ya existe.
• Agregar un nuevo producto si no existe.
"""

# Diccionario de productos y stock
stock = {
    "pan": 10,
    "leche": 5,
    "arroz": 20
}

producto = input("Ingresá el nombre de un producto: ").lower()

if producto in stock:
    print(f"Stock actual de {producto}: {stock[producto]}")
    agregar = int(input("¿Cuántas unidades querés agregar?: "))
    stock[producto] += agregar
    print(f"Nuevo stock de {producto}: {stock[producto]}")
else:
    nuevo_stock = int(input(f"{producto} no existe. Ingresá el stock inicial: "))
    stock[producto] = nuevo_stock
    print(f"{producto} agregado con stock: {stock[producto]}")

"""
9) Creá una agenda donde las claves sean tuplas de (día, hora) y los valores sean eventos.
"""

# Agenda con tuplas como clave
agenda = {
    ("lunes", "10:00"): "Reunión de equipo",
    ("martes", "15:00"): "Clase de Python",
    ("viernes", "09:00"): "Entrenamiento"
}

# Pedir día y hora al usuario
dia = input("Ingresá el día: ").lower()
hora = input("Ingresá la hora (formato HH:MM): ")

clave = (dia, hora)

# Consultar la agenda
if clave in agenda:
    print(f"Actividad programada: {agenda[clave]}")
else:
    print("No hay actividades programadas en ese horario.")

"""
10) Dado un diccionario que mapea nombres de países con sus capitales, construí un nuevo
diccionario donde:
• Las capitales sean las claves.
• Los países sean los valores.
"""

# Diccionario original: país -> capital
paises = {
    "Argentina": "Buenos Aires",
    "Francia": "París",
    "Japón": "Tokio",
    "Brasil": "Brasilia",
    "Italia": "Roma"
}

# Crear el diccionario invertido: capital -> país
capitales = {capital: pais for pais, capital in paises.items()}

print("Diccionario original (país -> capital):")
print(paises)

print("\nDiccionario invertido (capital -> país):")
print(capitales)
