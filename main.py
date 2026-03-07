operators = ["+", "-", "x", "/"]

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        quotient = a / b
    except ZeroDivisionError:
        return "You can't devide by 0"
    return quotient

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
            num2 = int(input())
            print(subtract(num1, num2))
        case "*":
            num2 = int(input())
            print(multiply(num1, num2))
        case "/":
            num2 = int(input())
            print(divide(num1, num2))
