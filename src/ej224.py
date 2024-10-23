"""
Escribir un programa que pida al usuario un número entero positivo y
 muestre por pantalla la cuenta atrás desde ese número hasta cero
 separados por comas.
 """
def lee_numero():

    """
    Lee el número solicitado por el usuario.
    return: el número entero positivo o None si no es válido.
    """

    numero = input("Dime un número(entero positivo): ")

    # Verificación si el tal, es un número y mayor que cero

    if not numero.isdigit():
        return None
    numero_entero = int(numero)

    if numero_entero <= 0:
        return None
    
    return numero_entero

def cuenta_atras(numero: int) -> str:
    """
    Se genera una cadena con la cuenta atrás del número solicitado
    hasta cero.
    
    numero: desde donde se hace la cuenta atrás.
    return: la cadena de la cuenta atrás.
    """

    cuentatras = ""

    for i in range (numero, -1, -1): 
        if cuentatras == "":
            cuentatras += str(i)
        else:
            cuentatras += ", " + str(i)

    return cuentatras

def imprimir_cuenta_atras(cuenta: str):
    """
    Se imprime la cuenta atrás.
    cuenta: La cadena de la cuenta atrás
    """

    print(f"CUENTA ATRÁS => {cuenta}")


def main():

    # Entrada

    numero = lee_numero()

    if numero is None:
        print("Error: Te dije un número entero positivo. ")
        return #si no hay numero válido, pues se termina.
    
    # Procesamiento

    cuenta = cuenta_atras(numero)


    # Salida

    imprimir_cuenta_atras(cuenta)


if __name__ == '__main__':
    main()