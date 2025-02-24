"""
Módulo que contiene las pruebas unitarias para la función factorial.
"""

import pytest
from factorial import factorial

def test_factorial_1_pasa():
    """
    Test para verificar que el factorial de 1 es 1.
    """
    assert factorial(1) == 1

def test_tipo_pasa():
    """
    Test para verificar que el factorial de 5 es 120.
    """
    assert factorial(5) == 120

def test_tipo_falla():
    """
    Test para verificar que se lanza TypeError si no es un entero.
    """
    with pytest.raises(TypeError):
        factorial("a")

def test_negativo_pasa():
    """
    Test para verificar que el factorial de 5 es 120.
    """
    assert factorial(5) == 120

def test_negativo_falla():
    """
    Test para verificar que se lanza ValueError si el número es negativo.
    """
    with pytest.raises(ValueError):
        factorial(-5)

def test_positivo_falla():
    """
    Test para verificar que el factorial de 5 NO es 125.
    """
    assert factorial(5) == 120  # Intentando hacer que falle

def test_factorial_0_pasa():
    """
    Test para verificar que el factorial de 0 es 1.
    """
    assert factorial(0) == 1
