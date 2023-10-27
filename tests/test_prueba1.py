from .src.Unidad1.PruebasUnitarias.prueba1 import obtener

def test_obtener_mayor_o_cero():
    # Pruebas con números diferentes
    assert obtener(3, 5) == 5
    assert obtener(10, 7) == 10

    # Prueba con números iguales
    assert obtener(4, 4) == 0

    # Pruebas con números negativos
    assert obtener(-2, -5) == -2
    assert obtener(-10, -7) == -7

    # Pruebas con un número negativo y uno positivo
    assert obtener(-3, 3) == 3
    assert obtener(5, -5) == 5
