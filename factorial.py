"""
Módulo que contiene la función factorial para calcular el factorial de un número entero.
"""

def factorial(n):
    """
    Calcula el factorial de un número entero.

    Args:
        n (int): El número para calcular el factorial.

    Returns:
        int: El factorial de n.
    """
    if not isinstance(n, int):
        raise TypeError("El valor debe ser un número entero")
    if n < 0:
        raise ValueError("El número no puede ser negativo")
    if n in (0, 1):  # Usando 'in' para la comparación
        return 1
    return n * factorial(n - 1)
