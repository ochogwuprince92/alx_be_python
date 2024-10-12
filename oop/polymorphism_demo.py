# polymorphism_demo.py
# This script demonstrates polymorphism through method overriding in a base class (Shape) and its derived classes (Rectangle, Circle).

import math

# Base Class: Shape
class Shape:
    def area(self):
        """Base area method to be overridden in derived classes."""
        raise NotImplementedError("Subclasses must override the area() method")

# Derived Class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize the rectangle with length and width attributes."""
        self.length = length
        self.width = width

    def area(self):
        """Override the area method to calculate the area of the rectangle."""
        return self.length * self.width

# Derived Class: Circle
class Circle(Shape):
    def __init__(self, radius):
        """Initialize the circle with a radius attribute."""
        self.radius = radius

    def area(self):
        """Override the area method to calculate the area of the circle."""
        return math.pi * self.radius ** 2
