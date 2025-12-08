# mymath.py (a module)
PI = 3.14159

def area_circle(r):
    return PI * r * r

print("mymath imported")  # runs at import-time!


# main.py
import mymath         # executes mymath.py exactly once
from mymath import PI # pulls a name into current namespace

print(mymath.area_circle(2))
print(PI)


if __name__ == "__main__":
    # runs only when python mymath.py is executed directly
    print(area_circle(3))
