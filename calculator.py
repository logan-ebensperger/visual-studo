num1 = float(input("Enter the first number: "))
operation = input("Enter an operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform calculation based on operation
if operation == "+":
    result = num1 + num2
    print("Result:", result)
elif operation == "-":
    result = num1 - num2
    print("Result:", result)
elif operation == "*":
    result = num1 * num2
    print("Result:", result)
elif operation == "/":
    if num2 == 0:
        print("Error: Division by 0 is not allowed.")
    else:
        result = num1 / num2
        print("Result:", result)
else:
    print("Invalid operation. Please use +, -, *, or /.")