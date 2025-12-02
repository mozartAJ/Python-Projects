#This script performs basic arithmetic operations

def add(x: float, y: float) -> float:
    return x + y

def subtract(x: float, y: float) -> float:
    return x - y

def multiply(x: float, y: float) -> float:
    return x * y

def divide(x: float, y: float) -> float:
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y

print("Welcome to the Python Calculator!")
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
print('The result is:')

if choice == '1':
    print('You have chosen addition.')
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == '2':
    print('You have chosen subtraction.')
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == '3':
    print('You have chosen multiplication.')
    print(f"{num1} * {num2} = {multiply(num1, num2)}")
elif choice == '4':
    print('You have chosen division.')
    try:
        print(f"{num1} / {num2} = {divide(num1, num2)}")
    except ValueError as e:
        print(e)
else:
    print("Invalid input")

#End of calculator script