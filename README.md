# Título de la Actividad

## Identificación de la Actividad
- **ID de la Actividad:** Práctica 2.2: Sentencias iterativas y saltos
- **Módulo:** PROG
- **Unidad de Trabajo:** U2: Sentencias condicionales y repetitivas
- **Fecha de Creación:** 19-10-2024
- **Fecha de Entrega:** 23-10-2024
- **Alumno(s):** 
  - **Nombre y Apellidos:** Antonio José Monge Monge
  - **Correo electrónico:** amonmon0206@g.educaand.es
  - **Iniciales del Alumno/Grupo:** AMM

## Descripción de la Actividad
Distintos ejercicios para aplicar lo visto en sentencias iterativas.

## Instrucciones de Compilación y Ejecución
1. **Requisitos Previos:**
   - Python ver. 3.11.9
   - Visual Studio Code

2. **Pasos para Compilar el Código:**
   Al ser Python no es necesario compilar.

3. **Pasos para Ejecutar el Código:**
   Desde el propio IDE.

4. **Ejecución de Pruebas:**
   pytest [nombre del test]

## Desarrollo de la Actividad
### Descripción del Desarrollo
 - Ejercicios con su documentación señalando que hace cada qué
 - Se señalan: la entrada, procesamiento y salida en el main() del ejercicio.

### Código Fuente
Ej del ejercicio 2.2.1:

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


### Ejemplos de Ejecución
- ***Entrada y salida incorrecta*** con el valor de edad: 0

¿Cuántos años tienes? 0
Error: Tienes que tener más de 0 años.
¿Cuántos años tienes? 

- ***Entrada y salida correcta***

¿Cuántos años tienes? 26
AÑOS CUMPLIDOS => 1..2..3..4..5..6..7..8..9..10..11..12..13..14..15..16..17..18..19..20..21..22..23..24..25..26

### Resultados de Pruebas
test del ejercicio 1:

# tests/test_ejercicio221.py

from src.ej221 import serie_palabra

def test_serie_palabra():
    # Prueba para verificar que la serie vaya bien con 10 repeticiones
    resultado = serie_palabra("Hola")
    esperado = "Hola\n" * 10
    assert resultado == esperado

    # Prueba para verificar que genera la serie con un número personalizado
    resultado = serie_palabra("Hola", 5)
    esperado = "Hola\n" * 5
    assert resultado == esperado

# La función imprime_serie no se puede probar directamente sin capturar salida.
# Pero puedes probar la función lee_datos manualmente.



## Conclusiones
Bastante insatisfecho por haber hecho tan pocos, culpa mía al haberse echado el tiempo encima. De todas formas, creo ver las cosas más claras y entenderlas algo mejor. Espero en el futuro organizarme mejor.

## Referencias y Fuentes
Referencia el ejercicio que posteó el profesor por el chat de gmail para hacer la estructura, los apuntes del modúlo y chatgpt para la corrección del código en algunos casos (la mayoría)


