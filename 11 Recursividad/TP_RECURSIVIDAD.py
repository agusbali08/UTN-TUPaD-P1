"""
1) Crea una función recursiva que calcule el factorial de un número. Luego, utiliza esa
función para calcular y mostrar en pantalla el factorial de todos los números enteros
entre 1 y el número que indique el usuario.
"""

# Función recursiva para calcular el factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Pedimos al usuario el número hasta donde calcular
numero = int(input("Ingrese un número: "))

# Mostramos el factorial de todos los números entre 1 y el ingresado
for i in range(1, numero + 1):
    print(f"Factorial de {i} es: {factorial(i)}")

"""
2) Crea una función recursiva que calcule el valor de la serie de Fibonacci en la posición
indicada. Posteriormente, muestra la serie completa hasta la posición que el usuario
especifique.
"""

# Función recursiva para calcular el n-ésimo número de Fibonacci
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Pedimos al usuario la posición hasta donde calcular
posicion = int(input("Ingrese hasta qué posición de Fibonacci quiere calcular: "))

# Mostramos toda la serie hasta la posición indicada
print("Serie de Fibonacci:")
for i in range(posicion + 1):
    print(fibonacci(i), end=" ")

"""
3) Crea una función recursiva que calcule la potencia de un número base elevado a un
exponente, utilizando la fórmula 𝑛
𝑚 = 𝑛 ∗ 𝑛
(𝑚−1)
. Prueba esta función en un algoritmo general.
"""

# Función recursiva para calcular la potencia
def potencia(base, exponente):
    if exponente == 0:
        return 1
    else:
        return base * potencia(base, exponente - 1)

# Pedimos los datos al usuario
base = int(input("Ingrese la base: "))
exponente = int(input("Ingrese el exponente: "))

# Calculamos y mostramos el resultado
resultado = potencia(base, exponente)
print(f"{base} elevado a la {exponente} es: {resultado}")

"""
4) Crear una función recursiva en Python que reciba un número entero positivo en base
decimal y devuelva su representación en binario como una cadena de texto.

Cuando representamos un número en binario, lo expresamos usando solamente ceros (0) y
unos (1), en base 2. Para convertir un número decimal a binario, se puede seguir este
procedimiento:
1. Dividir el número por 2.
2. Guardar el resto (0 o 1).
3. Repetir el proceso con el cociente hasta que llegue a 0.
4. Los restos obtenidos, leídos de abajo hacia arriba, forman el número binario.

🧠Ejemplo:
Convertir el número 10 a binario:
10 ÷ 2 = 5 resto: 0
5 ÷ 2 = 2 resto: 1
2 ÷ 2 = 1 resto: 0
1 ÷ 2 = 0 resto: 1
Leyendo los restos de abajo hacia arriba: 1 0 1 0 → El resultado binario es "1010".
"""

# Función recursiva para convertir decimal a binario
def decimal_a_binario(n):
    if n == 0:
        return ""
    else:
        return decimal_a_binario(n // 2) + str(n % 2)

# Pedimos el número al usuario
numero = int(input("Ingrese un número entero positivo: "))

# Caso especial si el número es 0 (para que no devuelva cadena vacía)
if numero == 0:
    print("El número en binario es: 0")
else:
    binario = decimal_a_binario(numero)
    print(f"El número en binario es: {binario}")

"""
5) Implementá una función recursiva llamada es_palindromo(palabra) que reciba una
cadena de texto sin espacios ni tildes, y devuelva True si es un palíndromo o False si no
lo es.
 Requisitos:
La solución debe ser recursiva.
No se debe usar [::-1] ni la función reversed().
"""

# Función recursiva para verificar si una palabra es palíndromo
def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    elif palabra[0] != palabra[-1]:
        return False
    else:
        return es_palindromo(palabra[1:-1])

# Pedimos la palabra al usuario
palabra = input("Ingrese una palabra: ").lower()

# Llamamos a la función y mostramos el resultado
if es_palindromo(palabra):
    print("La palabra es un palíndromo.")
else:
    print("La palabra NO es un palíndromo.")

"""
6) Escribí una función recursiva en Python llamada suma_digitos(n) que reciba un
número entero positivo y devuelva la suma de todos sus dígitos.
 Restricciones:
No se puede convertir el número a string.
Usá operaciones matemáticas (%, //) y recursión.
Ejemplos:
suma_digitos(1234) → 10 (1 + 2 + 3 + 4)
suma_digitos(9) → 9
suma_digitos(305) → 8 (3 + 0 + 5)
"""

# Función recursiva para sumar los dígitos de un número
def suma_digitos(n):
    if n < 10:
        return n
    else:
        return (n % 10) + suma_digitos(n // 10)

# Pedimos el número al usuario
numero = int(input("Ingrese un número entero positivo: "))

# Llamamos a la función y mostramos el resultado
print(f"La suma de los dígitos es: {suma_digitos(numero)}")

"""
7) Un niño está construyendo una pirámide con bloques. En el nivel más bajo coloca n
bloques, en el siguiente nivel uno menos (n - 1), y así sucesivamente hasta llegar al
último nivel con un solo bloque.
Escribí una función recursiva contar_bloques(n) que reciba el número de bloques en el
nivel más bajo y devuelva el total de bloques que necesita para construir toda la
pirámide.
 Ejemplos:
contar_bloques(1) → 1 (1)
contar_bloques(2) → 3 (2 + 1)
contar_bloques(4) → 10 (4 + 3 + 2 + 1)
"""

# Función recursiva para contar los bloques de la pirámide
def contar_bloques(n):
    if n == 1:
        return 1
    else:
        return n + contar_bloques(n - 1)

# Pedimos el número de bloques en el nivel inferior
n = int(input("Ingrese la cantidad de bloques en el nivel más bajo: "))

# Llamamos a la función y mostramos el resultado
print(f"El total de bloques necesarios es: {contar_bloques(n)}")

"""
8) Escribí una función recursiva llamada contar_digito(numero, digito) que reciba un
número entero positivo (numero) y un dígito (entre 0 y 9), y devuelva cuántas veces
aparece ese dígito dentro del número.
 Ejemplos:
contar_digito(12233421, 2) → 3
contar_digito(5555, 5) → 4 
contar_digito(123456, 7) → 0 
"""

# Función recursiva para contar cuántas veces aparece un dígito en un número
def contar_digito(numero, digito):
    if numero == 0:
        return 0
    else:
        if numero % 10 == digito:
            return 1 + contar_digito(numero // 10, digito)
        else:
            return contar_digito(numero // 10, digito)

# Pedimos los datos al usuario
numero = int(input("Ingrese un número entero positivo: "))
digito = int(input("Ingrese el dígito a buscar (0-9): "))

# Validación opcional del dígito
if 0 <= digito <= 9:
    resultado = contar_digito(numero, digito)
    print(f"El dígito {digito} aparece {resultado} veces en el número.")
else:
    print("Debe ingresar un dígito entre 0 y 9.")
