"""
Ejercicio 2.2.2¶

Escribir un programa que pregunte al usuario su edad y
 muestre por pantalla todos los años que ha cumplido
   (desde 1 hasta su edad).
   """

def lee_edad():

    """
    Lee la edad del usuario. Tiene que ser mayor que cero.
    Si no es así, el programa seguirá pidiendo un valor correcto
    retorna la edad del usuario como un numero entero.
    """

    edad_valida = False #Se controla la validez de la entrada
    edad = None #Se inicia la variable edad

    while not edad_valida: #Se empieza el bucle hasta que la edad es válida
        edad = input("¿Cuántos años tienes? ")

# Verificamos que la entrada sea un número entero y mayor que 0

        if edad.isdigit() and int(edad) > 0:
            edad_valida = True 
        else:
            print("Error: Tienes que tener más de 0 años.")

    return int(edad) #Se devuelve la edad válida

def muestra_años(edad: int) -> str:
    
    """
    Genera una cadena con los años cumplidos desde 1 hasta los 
    años proporcionados
    edad: la edad del usuario
    return: la cadena de años cumplidos.
    """

    return "1" + "".join(f"..{año}" for año in range(2, edad + 1))

def imprime_años(años: str):
    """
    Imprime los años cumplidos.
    años: La cadena de años cumplidos.
    """

    print (f"AÑOS CUMPLIDOS => {años}")

def main():
    
    # Entrada

    edad = lee_edad()

    # Procesamiento

    años = muestra_años(edad)

    # Salida

    imprime_años(años)


if __name__ == '__main__':
    main()