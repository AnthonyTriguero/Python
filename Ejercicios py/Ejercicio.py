def palindromo(cadena):
    inicio = 0
    fin = len(cadena) - 1
    while cadena[inicio] == cadena[fin]:
        if inicio >= fin:
            return True
        inicio += 1
        fin -= 1
    return False


def palindromo_recursivo(cadena, inicio, fin):
    if inicio >= fin:
        return True
    if cadena[inicio] == cadena[fin]:
        return palindromo_recursivo(cadena, inicio+1, fin-1)
    else:
        return False


def remover_caracteres_especiales(cadena):
    cadena = cadena.lower()
    cadena = cadena.replace(" ", "")
    cadena = cadena.replace("á", "a")
    cadena = cadena.replace("é", "e")
    cadena = cadena.replace("í", "i")
    cadena = cadena.replace("ó", "o")
    cadena = cadena.replace("ú", "u")
    return cadena


cadena = "Isaac no ronca así"
cadena_limpia = remover_caracteres_especiales(cadena)
es_palindromo = palindromo(cadena_limpia)
if es_palindromo:
    print("Es palíndromo")
else:
    print("No es palíndromo")
es_palindromo = palindromo_recursivo(cadena_limpia, 0, len(cadena_limpia) - 1)
if es_palindromo:
    print("Con recursividad: es palíndromo")
else:
    print("Con recursividad: no es palíndromo")

palabras = [
    "oso",
    "parzibyte",
    "oro",
    "python",
    "Ada",  
    "Ana lava lana",
    "La tele letal",
    "Isaac no ronca así",
]
for palabra in palabras:
    # Esto es opcional. Yo limpio la palabra para quitar espacios y acentos
    palabra_limpia = remover_caracteres_especiales(palabra)
    es_palindromo = palindromo(palabra_limpia)
    es_palindromo_recursivo = palindromo_recursivo(
        palabra_limpia, 0, len(palabra_limpia)-1)
    print(
        f"'{palabra}' es palíndromo con ciclos? {es_palindromo}. Y con recursividad? {es_palindromo_recursivo}")