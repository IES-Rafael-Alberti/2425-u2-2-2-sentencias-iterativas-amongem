"""
EJERCICIO 2.2.1 | Escribir un programa que pida al usuario 
una palabra y la muestre por pantalla 10 veces.
"""
def lee_datos():
    """
    Lee la palabra introducida por el usuario.
    :return: La palabra ingresada por el usuario o None si no es válida.
    """
    palabra = input("Dime una palabra: ")
    return palabra.strip() if palabra.strip() else None

def serie_palabra(palabra: str, veces: int = 10) -> str:
    """
    Genera una cadena con la palabra repetida 'veces' veces.
    :param palabra: La palabra que se repite.
    :param veces: El número de veces que se repite la palabra.
    :return: La cadena generada.
    """
    return (palabra + "\n") * veces

def imprime_serie(serie: str):
    """
    Imprime la serie generada de palabras.
    :param serie: La serie de palabras generada.
    """
    print(serie)

def main():
    # Entrada
    palabra = lee_datos()
    if palabra is None:
        print("Error: No ingresaste una palabra válida.")
        return
    
    # Procesamiento
    serie = serie_palabra(palabra)

    # Salida
    imprime_serie(serie)

# Se llama al programa principal
if __name__ == '__main__':
    main()
