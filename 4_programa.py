"""Crear un programa que el usuario ingrese, una cadena de texto y que cuente el numero de palabras
y muestre el resultado una palabra se define como una secuencia de caracteres separados por espacios."""

def pedir_cadena():
    cadena = input("Ingrese una cadena de texto: ")
    return cadena

def contar_palabras(cadena):
    palabras = cadena.split()
    return len(palabras)

def mostrar_resultado(cadena, cantidad_palabras):
    print(f'La cadena ingresada tiene {cantidad_palabras} palabras.')

if __name__ == "__main__":
    cadena = pedir_cadena()
    cantidad_palabras = contar_palabras(cadena)
    mostrar_resultado(cadena, cantidad_palabras)