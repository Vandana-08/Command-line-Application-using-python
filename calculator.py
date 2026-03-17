def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def div(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y

def mod(x, y):
    return x % y

def mul(x, y):
    return x * y


print("Calculator Using Python")

while True:
    print("\nSelect an operation")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Division (/)")
    print("4. Modulo (%)")
    print("5. Multiplication (*)")
    print("6. Exit")

    select = input("Enter your choice: ")

    if select == '6':
        print("Exiting calculator.....")
        break

    if select not in ['1', '2', '3', '4', '5']:
        print("Invalid Choice! Please select between 1 to 6")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input! Please enter numbers only.")
        continue

    if select == '1':
        print("Result is:", add(num1, num2))

    elif select == '2':
        print("Result is:", sub(num1, num2))

    elif select == '3':
        print("Result is:", div(num1, num2))

    elif select == '4':
        print("Result is:", mod(num1, num2))

    elif select == '5':
        print("Result is:", mul(num1, num2))
