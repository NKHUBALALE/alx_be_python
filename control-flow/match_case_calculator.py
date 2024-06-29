num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ")

match operation:
    case "+":
        result = num1 + num2
    case "-":
        result = num1 - num2
    case "*":
        result = num1 * num2
    case "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero is not allowed."
    case _:
        result = "Error! Invalid operation."

# Output the result
if isinstance(result, str):  # If result is an error message
    print(result)
else:  # If result is a numerical calculation
    print(f"The result is {result}")
