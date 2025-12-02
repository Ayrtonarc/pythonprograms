""""""

def pedir_dos_numeros():
    while True:
        try:
            primer_numero = int(input("Ingrese el primer número: "))
            segundo_numero = int(input("Ingrese el segundo número: "))
            return primer_numero, segundo_numero
        except ValueError:
            print("Entrada inválida. Por favor, ingrese números enteros.")

def mostrar_invertido(primer_numero, segundo_numero):
    print(f"Números ingresados en orden invertido: {segundo_numero}, {primer_numero}")

if __name__ == "__main__":
    x, y = pedir_dos_numeros()
    mostrar_invertido(x, y)












