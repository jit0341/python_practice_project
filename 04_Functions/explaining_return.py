def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

# temp_today now holds the actual Fahrenheit value (e.g., 77.0)
temp_today = celsius_to_fahrenheit(25)
print(f"Today's temperature is {temp_today}°F.")


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Calculate the average of two temperatures, one converted
temp_celsius1 = 10
temp_celsius2 = 30

avg_fahrenheit = (celsius_to_fahrenheit(temp_celsius1) + celsius_to_fahrenheit(temp_celsius2)) / 2
print(f"The average Fahrenheit temperature is: {avg_fahrenheit}°F")
# Output: The average Fahrenheit temperature is: 68.0°F


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def describe_temperature(temp_f):
    if temp_f > 85:
        return "It's hot!"
    elif temp_f < 40:
        return "It's cold!"
    else:
        return "The weather is pleasant."

celsius_value = 32 # This is ~90 F
# The return value of celsius_to_fahrenheit(celsius_value) is passed directly to describe_temperature
weather_description = describe_temperature(celsius_to_fahrenheit(celsius_value))
print(weather_description)
# Output: It's hot!


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

current_celsius = 40 # This is 104 F

if celsius_to_fahrenheit(current_celsius) > 100:
    print("Stay hydrated! It's over 100°F!")
else:
    print("Temperature is manageable.")
# Output: Stay hydrated! It's over 100°F!


def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

daily_celsius_readings = [0, 10, 20, 30, 40]
daily_fahrenheit_readings = []

for c in daily_celsius_readings:
    # The returned value is appended to the list
    daily_fahrenheit_readings.append(celsius_to_fahrenheit(c))

print(f"Fahrenheit readings: {daily_fahrenheit_readings}")
# Output: Fahrenheit readings: [32.0, 50.0, 68.0, 86.0, 104.0]


