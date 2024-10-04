# robust_division_calculator.py

def safe_divide(numerator, denominator):
    try:
        # Convert the inputs to floats for division
        numerator = float(numerator)
        denominator = float(denominator)

        # Perform the division and return the result
        result = numerator / denominator
        return f"The result of the division is {result}"

    except ZeroDivisionError:
        # Handle division by zero
        return "Error: Cannot divide by zero."
    
    except ValueError:
        # Handle non-numeric input
        return "Error: Please enter numeric values only."
