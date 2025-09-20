def from_cel():
    x = float(input("Enter temperature in Celsius: "))
    y = input("Convert into: \n 1. Fahrenheit \n 2. Kelvin \nEnter choice: ")

    if y == '1':
        final = (x * 9/5) + 32
        print(f"The temperature is: {final} °F")
    elif y == '2':
        final = x + 273.15
        print(f"The temperature is: {final} K")
    else:
        print("Invalid choice!")

def from_fah():
    x = float(input("Enter temperature in Fahrenheit: "))
    y = input("Convert into: \n 1. Celsius \n 2. Kelvin \nEnter choice: ")

    if y == '1':
        final = (x - 32) * 5/9
        print(f"The temperature is: {final} °C")
    elif y == '2':
        final = (x - 32) * 5/9 + 273.15
        print(f"The temperature is: {final} K")
    else:
        print("Invalid choice!")

def from_kel():
    x = float(input("Enter temperature in Kelvin: "))
    y = input("Convert into: \n 1. Celsius \n 2. Fahrenheit \nEnter choice: ")

    if y == '1':
        final = x - 273.15
        print(f"The temperature is: {final} °C")
    elif y == '2':
        final = (x - 273.15) * 9/5 + 32
        print(f"The temperature is: {final} °F")
    else:
        print("Invalid choice!")

def get_temp():
    t = input("Convert from: \n 1. Celsius \n 2. Fahrenheit \n 3. Kelvin \nEnter choice: ")
    if t == "1":
        from_cel()
    elif t == "2":
        from_fah()
    elif t == "3":
        from_kel()
    else:
        print("Please enter correct input")

get_temp()
