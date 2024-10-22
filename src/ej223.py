
"""
EJERCICIO 2.2.3: Escribir un programa que pida al usuario un número entero positivo y muestre 
por pantalla todos los números impares desde 1 hasta ese número separados por comas."""


def lee_datos():
    
    numero = input("Dime un número (entero postivo): ")

    # Se verifica si la entrada es un número y mayor que cero

    if not numero.isdigit():
        return None
    numero_entero = int(numero)

    if numero_entero <= 0:
        return None
    
    return numero_entero

def sacar_impares(numero: int) -> str:

    """
    Generar una cadena con todos los números impares desde 1 hasta
    el número solicitado.
    numero: El número hasta donde salen los impares.
    return: la cadena de números impares.
    """

    impares = ""

    for i in range(1, numero + 1):
        if i % 2 != 0: #Con esto se ve si es par
            if impares == "":
                impares += str(i)
            else:
                impares += ", " +str(i)

    return impares

def imprimir_impares(numeros: str):
    """
    Imprime los números impares
    """

    print(f"NÚMEROS IMPARES => {numeros}")

def main():
    
    #Entrada
    numero = lee_datos()

    if numero is None:
        print("Error: Debe ser un número entero positivo.")
        return #se acaba si el numero no es válido
    
    #Procesamiento

    impares = sacar_impares(numero)

    #Salida

    imprimir_impares(impares)

if __name__=='__main__':
    main()

