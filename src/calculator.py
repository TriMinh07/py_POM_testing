def add(a: float, b: float) -> float:
    return a + b

def div(a: float, b: float) -> float:
    if b == 0:
        raise ZeroDivisionError("b must not be 0")
    return a / b