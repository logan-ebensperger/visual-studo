print("Welcome! Choose two numbers and I will tell you if one is a multiple of the other")

a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

if b == 0:
    print("Error: The second number cannot be zero.")
else:
    if a % b == 0:
        print(f"{a} is a multiple of {b}.")
        print(f"The number {a} is {a / b} times the number {b}.")
    elif b % a == 0:
        print(f"{b} is a multiple of {a}.")
        print(f"The number {b} is {b / a} times the number {a}.")
    else:
        print(f"Neither number is a multiple of the other.")