# define a function that perform arithmetic operations
def perform_operation(num1, num2, operation):
# perform basic arithmetic operations
# num1 (float): first number.
# num2 (float): second number.
# operations(str): operations to perform ('add', 'aubtract', 'multiply', 'divide').

# Returns:the result of the arithmetic operation, or an error message for invalid inputs


    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            return "Error Division by zero is not allowed."
        return num1/num2
    else:
        return "Error: Invalid operation."