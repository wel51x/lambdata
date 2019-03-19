# Winstons's code
"""
Classes to represent Complex numbers.
"""

class Complex:
    r = 0.0
    i = 0.0
    
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

    def add(self, realpart=0.0, imagpart=0.0):
        """Add a complex number to current object's number."""
        return self.r + realpart, self.i + imagpart

    def subtract(self, realpart=0.0, imagpart=0.0):
        """Subtract a complex number from current object's number."""
        return self.r - realpart, self.i - imagpart

    def multiply(self, realpart=0.0, imagpart=0.0):
        """Multiply a complex number by current object's number."""
        return self.r * realpart, self.i * imagpart

    def divide(self, realpart=0.0, imagpart=0.0):
        """Divide current object's number by a complex number."""
        if realpart == 0.0 or imagpart == 0.0:
            return 0.0, 0.0, "zero-divide attempted, inputs =", realpart, imagpart
        else:
            return self.r / realpart, self.i / imagpart
