
import pytest
from factorial import factorial

def test_factorial_1_falla():
    assert factorial(1) == 1

def test_factorial_1_pasa():
    assert factorial(1) == 1

def test_tipo_falla():
    with pytest.raises(TypeError):
        factorial("a")

def test_tipo_pasa():
    assert factorial(5) == 120

def test_negativo_falla():
    with pytest.raises(ValueError):
        factorial(-5)

def test_negativo_pasa():
    assert factorial(5) == 120

def test_positivo_falla():
    assert factorial(5) == 125  # Intentando hacer que falle

def test_positivo_pasa():
    assert factorial(5) == 120
