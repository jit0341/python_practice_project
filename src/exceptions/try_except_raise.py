def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("You tried to divide by zero!")
    return a / b

try:
    x = divide(10, 0)
except ZeroDivisionError as e:
    print("Caught an error:", e)