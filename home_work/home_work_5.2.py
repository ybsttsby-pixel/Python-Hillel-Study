while True:
    num1 = float(input("Enter the first number: "))
    operation = input("Enter an operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error: division by zero!"
    else:
        result = "Unknown operation!"
    print("Result:", result)
    answer = input("Do you want to continue? (y/yes): ").lower()
    if answer not in ["y", "yes"]:
        print("Calculator has been closed.")
        break