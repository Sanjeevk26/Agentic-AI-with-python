# Python Object-Oriented Programming
# Topics:
# 1. The __init__ method
# 2. Object initialization
# 3. Instance attributes
# 4. Multiple objects
# 5. Default values
# 6. Keyword arguments
# 7. Validation
# -------------------------------------------------


# =================================================
# 1. Basic __init__ Example
# =================================================

class ChaiOrder:
    """
    Represent one chai order.
    """

    def __init__(self, chai_type, size):
        # These values are stored on the current object.
        self.chai_type = chai_type
        self.size = size

    def summary(self):
        return f"{self.size} ml of {self.chai_type}"


order_one = ChaiOrder("Masala Chai", 200)
order_two = ChaiOrder("Ginger Chai", 220)

print("Order one:")
print(order_one.summary())

print("Order two:")
print(order_two.summary())

print("-" * 50)


# =================================================
# 2. Independent Object Data
# =================================================

# Each object has its own namespace and values.

print("Order one attributes:")
print(order_one.__dict__)

print("Order two attributes:")
print(order_two.__dict__)

print("-" * 50)


# =================================================
# 3. Changing One Object
# =================================================

# Changing one object's size does not affect the other.

order_one.size = 250

print("After changing order one's size:")
print("Order one:", order_one.summary())
print("Order two:", order_two.summary())

print("-" * 50)


# =================================================
# 4. Default Parameter Values
# =================================================

class TeaOrder:
    def __init__(self, tea_type, size=150):
        self.tea_type = tea_type
        self.size = size

    def summary(self):
        return f"{self.size} ml of {self.tea_type}"


default_order = TeaOrder("Green Tea")
custom_order = TeaOrder("Lemon Tea", 300)

print("Default-size order:")
print(default_order.summary())

print("Custom-size order:")
print(custom_order.summary())

print("-" * 50)


# =================================================
# 5. Keyword Arguments
# =================================================

keyword_order = TeaOrder(
    tea_type="Oolong Tea",
    size=180,
)

print("Keyword argument order:")
print(keyword_order.summary())

print("-" * 50)


# =================================================
# 6. Avoiding Built-in Names
# =================================================

class SafeChaiOrder:
    def __init__(self, type_, size):
        # type_ avoids conflicting with Python's built-in type().
        self.type = type_
        self.size = size

    def summary(self):
        return f"{self.size} ml of {self.type}"


safe_order = SafeChaiOrder("Elaichi Chai", 190)

print("Safe parameter naming:")
print(safe_order.summary())

print("-" * 50)


# =================================================
# 7. Validation Inside __init__
# =================================================

class ValidatedChaiOrder:
    def __init__(self, chai_type, size):
        if not isinstance(chai_type, str):
            raise TypeError("chai_type must be a string")

        if not isinstance(size, (int, float)):
            raise TypeError("size must be a number")

        if size <= 0:
            raise ValueError("size must be greater than zero")

        self.chai_type = chai_type
        self.size = size

    def summary(self):
        return f"{self.size} ml of {self.chai_type}"


validated_order = ValidatedChaiOrder("Kesar Chai", 210)

print("Validated order:")
print(validated_order.summary())

print("-" * 50)


# =================================================
# 8. Handling Invalid Initialization
# =================================================

try:
    invalid_order = ValidatedChaiOrder("Masala Chai", -100)
except ValueError as error:
    print("Could not create order:", error)

print("-" * 50)


# =================================================
# 9. Adding an Optional Attribute Later
# =================================================

# Python allows attributes to be added later,
# although required attributes should normally
# be initialized inside __init__.

order_one.sugar = "Low"

print("Order one sugar preference:")
print(order_one.sugar)

print("Updated order one namespace:")
print(order_one.__dict__)

print("-" * 50)


# =================================================
# 10. Creating an Attribute Inside Another Method
# =================================================

class CustomOrder:
    def __init__(self, chai_type):
        self.chai_type = chai_type

    def add_note(self, note):
        self.note = note

    def summary(self):
        description = self.chai_type

        if hasattr(self, "note"):
            description += f" - Note: {self.note}"

        return description


custom_chai = CustomOrder("Masala Chai")

print("Before adding note:")
print(custom_chai.summary())

custom_chai.add_note("Less sugar")

print("After adding note:")
print(custom_chai.summary())

print("-" * 50)


# =================================================
# 11. Manual __init__ Call Demonstration
# =================================================

# Normal and recommended object creation:
manual_demo = ChaiOrder("Lemon Tea", 175)

# Conceptually, Python automatically calls:
# ChaiOrder.__init__(manual_demo, "Lemon Tea", 175)

print("Automatically initialized object:")
print(manual_demo.summary())

print("-" * 50)


# =================================================
# Notes
# =================================================

# __init__:
# Initializes an object after it is created.
#
#
# Basic syntax:
#
# class ChaiOrder:
#     def __init__(self, chai_type, size):
#         self.chai_type = chai_type
#         self.size = size
#
#
# Object creation:
#
# order = ChaiOrder("Masala Chai", 200)
#
#
# self:
# Refers to the current object.
#
#
# self.chai_type:
# Instance attribute stored on the object.
#
#
# chai_type:
# Parameter received during object creation.
#
#
# Important technical detail:
# __new__ creates the object.
# __init__ initializes the object.
#
#
# Best practices:
# - Initialize required attributes in __init__
# - Use clear parameter names
# - Avoid shadowing Python built-ins
# - Validate important input values
# - Use default values only when appropriate
