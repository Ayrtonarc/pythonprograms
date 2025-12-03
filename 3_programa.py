"""Escribir un programa que determine si lo que ingresa el usuario es palíndromo o no."""
def pedir_texto():
    texto = input("Ingrese un texto: ")
    return texto

def es_palindromo(texto):
    texto_limpio = ''.join(texto.split()).lower()
    return texto_limpio == texto_limpio[::-1]
def mostrar_resultado(texto, es_palindromo):
    if es_palindromo:
        print(f'El texto "{texto}" es un palíndromo.')
    else:
        print(f'El texto "{texto}" no es un palíndromo.')


if __name__ == "__main__":
    texto = pedir_texto()
    resultado = es_palindromo(texto)
    mostrar_resultado(texto, resultado)