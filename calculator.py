def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
    
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
op = input("Enter the operation you want to perform ('+' for 'addition', '-' for 'subtraction', 'x' for 'multiplication' and '/' for 'division'): ")

if op == "+":
    sum = add(a, b)
    print("The sum is", sum)
elif op == "-":
    diff = subtract(a, b)
    print("The difference is", diff)
elif op == "x":
    product = multiply(a, b)
    print("The product is", product)
elif op == "/":
    if b != 0:
        quotient = divide(a, b)
        print("The quotient is", quotient)
    else:
        print("Not defined!")
else:
    print("Please enter a valid operator!")