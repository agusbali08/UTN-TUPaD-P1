"""1) Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función
range."""

# Lista de múltiplos de 4 del 1 al 100
lista_multiplos_4 = list(range(4, 101, 4))

print(lista_multiplos_4)

"""2) Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el
penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el
indexing con números negativos!"""

# Lista con 5 elementos
mi_lista = ["boca", "riber", "independiente", "racing", "estudiantes"]

# Mostrar el penúltimo elemento
print("El penúltimo elemento es:", mi_lista[-2])

"""3) Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por
pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior. Por
ejemplo:
lista_vacia = []"""

# Crear lista vacía
lista_vacia = []

# Agregar tres palabras
lista_vacia.append("boca")
lista_vacia.append("riber")
lista_vacia.append("independiente")

# Imprimir la lista
print(lista_vacia)

"""4) Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”,
respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra
en los videos o bien investigar cómo funciona el indexing con números negativos!
animales = ["perro", "gato", "conejo", "pez"]"""

# Lista de animales
animales = ["perro", "gato", "conejo", "pez"]

# Reemplazar el segundo (índice 1)
animales[1] = "loro"

# Reemplazar el último (índice -1)
animales[-1] = "oso"

# Mostrar la lista modificada
print(animales)

"""5) Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza."""

# Se crea una lista de 5 numeros
numeros = [8, 15, 3, 22, 7]
# Se busca el numero mas grande(max(numeros)) y se lo elimina (numeros.remove())
numeros.remove(max(numeros))
# Imprimo las lista con el numero mas grande eliminado
print(numeros) # [8, 15, 3, 7]

"""6) Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por
pantalla los dos primeros."""

# Creamos la lista
lista = list(range(10, 31, 5))

# Mostrar los dos primeros elementos
print("Los dos primeros elementos son:", lista[0], "y", lista[1])

"""7) Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores
cualesquiera.
autos = ["sedan", "polo", "suran", "gol"]"""

# Lista de autos
autos = ["sedan", "polo", "suran", "gol"]

# Reemplazar los índices 1 y 2
autos[1] = "partner"
autos[2] = "corza"

# Mostrar la lista modificada
print(autos)

"""8) Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append
directamente. Imprimir la lista resultante por pantalla."""

# Crear lista vacía
dobles = []

# Agregar los dobles usando append
dobles.append(5 * 2)
dobles.append(10 * 2)
dobles.append(15 * 2)

# Mostrar la lista resultante
print(dobles)

"""9) Dada la lista “compras”, cuyos elementos representan los productos comprados por
diferentes clientes:
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],
["agua"]]
a) Agregar "jugo" a la lista del tercer cliente usando append.
b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
c) Eliminar "pan" de la lista del primer cliente.
d) Imprimir la lista resultante por pantalla"""

# Lista de compras
compras = [["pan", "leche"], ["arroz", "fideos", "salsa"], ["agua"]]

# a) Agregar "jugo" al tercer cliente
compras[2].append("jugo")

# b) Reemplazar "fideos" por "tallarines" en el segundo cliente
compras[1][1] = "tallarines"

# c) Eliminar "pan" de la lista del primer cliente
compras[0].remove("pan")

# Imprimir la lista resultante
print(compras)

"""10) Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
● Posición lista_anidada[0]: 15
● Posición lista_anidada[1]: True
● Posición lista_anidada[2][0]: 25.5
● Posición lista_anidada[2][1]: 57.9
● Posición lista_anidada[2][2]: 30.6
● Posición lista_anidada[3]: False
Imprimir la lista resultante por pantalla."""

lista_anidada = [[15, True], [25.5, 57.9, 30.6], [False]]

print(lista_anidada)