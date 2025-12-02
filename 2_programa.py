"""Solicitar al usuario un número entero y mostrar si es par o impar."""
def pedir_numero():
    while True:
        try:
            numero = int(input("Ingrese un número entero: "))
            return numero
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")
def par_o_impar(numero):
    if numero % 2 == 0:
        print(f"El número {numero} es par.")
    else:
        print(f"El número {numero} es impar.")

if __name__ == "__main__":
    num = pedir_numero()
    par_o_impar(num)