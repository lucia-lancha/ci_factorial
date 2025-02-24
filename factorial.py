def factorial(n):
    if type(n) != int:
        raise TypeError("El valor debe ser un número entero")
    if n < 0:
        raise ValueError("El número no puede ser negativo")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
