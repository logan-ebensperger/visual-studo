def print_multiplication_table():

    try:
        num = int(input("enter a number to print it's multiplication table: "))
        print(f"multiplication table for {num}:")
        for i in range(1 , 11):
            product = num * i
            print(f"{num} x {i} = {product}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

if __name__ == "__main__":
    print_multiplication_table()
