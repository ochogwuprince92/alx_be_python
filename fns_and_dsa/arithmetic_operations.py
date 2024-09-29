def perform_operation(num1, num2, operation):
    # Check if the operation is addition
    if operation == "add":
        return num1 + num2
    # Check if the operation is subtraction
    elif operation == "subtract":
        return num1 - num2
    # Check if the operation is multiplication
    elif operation == "multiply":
        return num1 * num2
    # Check if the operation is division
    elif operation == "divide":
        # Handle division by zero
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        return num1 / num2
    # Handle invalid operations
    else:
        return "Error: Invalid operation."
