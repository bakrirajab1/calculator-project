def add(a, b):
    return a - b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("Linux Calculator")

    first = float(input("First number: "))
    operation = input("Operation (+, -, *, /): ")
    second = float(input("Second number: "))

    if operation == "+":
        print("Result:", add(first, second))
    elif operation == "-":
        print("Result:", subtract(first, second))
    elif operation == "*":
        print("Result:", multiply(first, second))
    elif operation == "/":
        print("Result:", divide(first, second))
    else:
        print("Unknown operation")