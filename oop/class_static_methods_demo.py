# class_static_methods_demo.py
# This script demonstrates the difference between static methods and class methods in Python.

class Calculator:
    # Class attribute
    calculation_type = "Arithmetic Operations"

    # Static method: Does not need access to class or instance attributes
    @staticmethod
    def add(a, b):
        """Returns the sum of two numbers."""
        return a + b

    # Class method: Can access class-level attributes
    @classmethod
    def multiply(cls, a, b):
        """Returns the product of two numbers and prints the class attribute."""
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
