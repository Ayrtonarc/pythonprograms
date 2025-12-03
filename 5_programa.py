"""Escribe un programa que solicite al usuario ingresar un numero entero positivo y determinar si
el numero es primo o no"""

def pedir_numero_positivo():
    while True:
        try:
            numero = int(input("Ingrese un número entero positivo: "))
            if numero > 0:
                return numero
            else:
                print("El número debe ser positivo. Intente de nuevo.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero positivo.")
def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

def mostrar_resultado(numero, es_primo):
    if es_primo:
        print(f"El número {numero} es primo.")
    else:
        print(f"El número {numero} no es primo.")

if __name__ == "__main__":
    numero = pedir_numero_positivo()
    resultado = es_primo(numero)
    mostrar_resultado(numero, resultado)