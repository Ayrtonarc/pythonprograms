"""Escribir un programa que determine si lo que ingresa el usuario es palíndromo o no."""
def pedir_texto():
    texto = input("Ingrese un texto: ")
    return texto

def es_palindromo(texto):
    texto_limpio = ''.join(texto.split()).lower()
    return texto_limpio == texto_limpio[::-1]

