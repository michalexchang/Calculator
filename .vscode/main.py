operators = ["+", "-", "x", "/"]

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

while True:
    num1 = int(input())
    operator = input("Choose + - x / ")

    if operator not in operators:
        print("Not a valid operator")
        operator = input("Choose + - x / ")

    match operator:
        case "+":
            num2 = int(input())
            print(add(num1, num2))
        case "-":
            num2 = input()
            print(subtract(num1, num2))
        case "*":
            num2 = input()
            print(multiply(num1, num2))
        case "/":
            num2 = input()
            print(divide(num1, num2))
