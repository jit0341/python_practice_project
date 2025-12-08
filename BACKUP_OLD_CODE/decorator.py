import time

def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"⏱️ {func.__name__} took {end - start:.6f} seconds")
        return result
    return wrapper

@timing_decorator
def compute_square(n):
    return [i**2 for i in range(n)]

@timing_decorator
def compute_factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print(compute_square(1000000))
print(compute_factorial(5000))