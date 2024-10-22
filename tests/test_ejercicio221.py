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
