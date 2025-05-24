num1= float (input(" Enter First Number: "))
operator = input("Enter Operator(+,-,*,/):")
num2 = float(input("Enter Second Number:"))
if operator== "+":
    print("Result:", num1+num2)
elif operator== "-":
    print("Result:", num1-num2)
elif operator== "*":
    print("Result:", num1*num2)
elif operator== "/":
    print("Result:", num1/num2)
else:
    print("Invalid operation")
