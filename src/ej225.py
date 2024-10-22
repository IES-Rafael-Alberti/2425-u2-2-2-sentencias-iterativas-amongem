"""
EJERCICIO 2.2.5:
Escribir un programa que pregunte al usuario una cantidad 
a invertir, el interés anual y el número de años, y muestre 
por pantalla el capital obtenido en la inversión cada año que 
dura la inversión.

# Formula para calcular El capital tras un año.
amount *= 1 + interest / 100
# En donde:
# - amount: Cantidad a invertir
# - interest: Interes porcentual anual """


def lee_datos():
    """
    Se pide una cantidad a ingresar para invertir, interés anual
    y numero de años.
    Todos los valores deben de ser correctos (números mayores que cero)
    Si los datos son válidos, los devuelve y si hubiera algún error,
    None.
    """

    try:

        # Leer cantidad a invertir

        cantidad = float(input("¿Cuánto quieres invertir? "))
        if cantidad <= 0:
            print("Error: La cantidad debería ser mayor que 0.")
            return None, None, None

        interes = float(input("¿Qué interés anual? (en porcentaje) "))
        if interes <= 0:
            print("Error: El interés debe de ser mayor que cero.")
            return None, None, None
        
        años = int(input("¿Por cuántos años vas a invertir? "))
        if años <= 0:
            print("Error: El número de años debería ser mayor que cero.")
            return None, None, None
        
        return cantidad, interes, años
    
    except ValueError:
        print("Error: Por favor, ingresa valores númericos válidos.")
        return None, None, None
    

def calculo_capital(cantidad: float, interes: float, años:int) -> str:
    """
    Se calcula y devuelve una cadena con el capital obtenido cada año
    """

    resultado = ""
    for i in range (1, años +1):
        cantidad *= 1 + interes / 100
        resultado += f"Año {i}: {cantidad:.2f} euros\n"

    return resultado

def imprimir_resultado(resultado: str):
    """
    Se muestra el capital obtenido de año tras año.
    """

    print("Aquí tienes tu inversión:")
    print(resultado)


def main():

    # Entrada

    cantidad, interes, años = lee_datos()

    if cantidad is None or interes is None or años is None:
        return #Se para si los datos no son válidos

    # Procesamiento

    resultado = calculo_capital(cantidad, interes, años)

    # Salida

    imprimir_resultado(resultado)


if __name__ == '__main__':
    main()