def add(a: float, b: float) -> float:
    return a + b

def div(a: float, b: float) -> float:

    if b == 0:
        raise ZeroDivisionError("division by zero")
    return a / b

def minus(a: float, b: float) -> float:
    return a - b

def mul(a: float, b: float) -> float:
    return a * b

def do_Operation(a: float, b: float, o: str) -> float:
    if o == '+':
        return add(a, b)
    elif o == '-':
        return minus(a, b)
    elif o == '*':
        return mul(a, b)
    elif o == '/':
        return div(a, b)
    else:
        raise ValueError(f"Unsupported operation: {o}")
