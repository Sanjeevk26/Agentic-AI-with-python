# Python Object-Oriented Programming
# Topics:
# 1. Class attributes
# 2. Instance attributes
# 3. Attribute shadowing
# 4. Deleting attributes
# 5. AttributeError
# 6. Instance methods
# 7. The self parameter
# 8. Calling methods through objects and classes
# -------------------------------------------------


# =================================================
# 1. Class Attributes
# =================================================

class Chai:
    temperature = "Hot"
    strength = "Strong"


cutting_chai = Chai()

print("Initial values:")
print("Class temperature:", Chai.temperature)
print("Object temperature:", cutting_chai.temperature)
print("Object strength:", cutting_chai.strength)

print("-" * 50)


# =================================================
# 2. Attribute Shadowing
# =================================================

# This creates an instance attribute named temperature.
# It shadows the class attribute with the same name.

cutting_chai.temperature = "Mild"

print("After attribute shadowing:")
print("Class temperature:", Chai.temperature)
print("Object temperature:", cutting_chai.temperature)

print("-" * 50)


# =================================================
# 3. Inspect the Object Namespace
# =================================================

# The shadowing value is stored directly
# inside the object's namespace.

print("cutting_chai namespace:")
print(cutting_chai.__dict__)

print("-" * 50)


# =================================================
# 4. Delete the Shadowing Attribute
# =================================================

# Delete the instance-specific temperature.
del cutting_chai.temperature

# The class attribute becomes visible again.
print("After deleting the instance temperature:")
print("Object temperature:", cutting_chai.temperature)
print("Class temperature:", Chai.temperature)

print("Object namespace:", cutting_chai.__dict__)

print("-" * 50)


# =================================================
# 5. Instance-Only Attribute
# =================================================

# cup_size exists only on this object.
cutting_chai.cup_size = "Small"

print("Cup size:", cutting_chai.cup_size)
print("Object namespace:", cutting_chai.__dict__)

print("-" * 50)


# =================================================
# 6. Delete an Instance-Only Attribute
# =================================================

del cutting_chai.cup_size

# There is no cup_size attribute on the class,
# so accessing it would raise AttributeError.

try:
    print(cutting_chai.cup_size)
except AttributeError as error:
    print("AttributeError:", error)

print("-" * 50)


# =================================================
# 7. Check an Attribute Safely
# =================================================

if hasattr(cutting_chai, "cup_size"):
    print("Cup size:", cutting_chai.cup_size)
else:
    print("cup_size does not exist")

print("-" * 50)


# =================================================
# 8. Basic Instance Method
# =================================================

class ChaiCup:
    size = 150

    def describe(self):
        """
        Describe the cup represented by the current object.
        """

        return f"A {self.size} ml chai cup"


cup_one = ChaiCup()

print("Calling method through the object:")
print(cup_one.describe())

print("-" * 50)


# =================================================
# 9. Multiple Objects and self
# =================================================

cup_two = ChaiCup()

# Shadow the class attribute only on cup_two.
cup_two.size = 100

print("Different objects using the same method:")
print("Cup one:", cup_one.describe())
print("Cup two:", cup_two.describe())

print("-" * 50)


# =================================================
# 10. Method Call Behind the Scenes
# =================================================

# These two calls are effectively equivalent.

print("Called through object:")
print(cup_one.describe())

print("Called through class:")
print(ChaiCup.describe(cup_one))

print("-" * 50)


# =================================================
# 11. Missing self Argument
# =================================================

# Calling an instance method through the class
# without passing an object causes TypeError.

try:
    ChaiCup.describe()
except TypeError as error:
    print("TypeError:", error)

print("-" * 50)


# =================================================
# 12. Another Class Method Example
# =================================================

class TeaOrder:
    default_price = 40

    def calculate_total(self, cups):
        return cups * self.default_price


regular_order = TeaOrder()
premium_order = TeaOrder()

# Only premium_order gets a different price.
premium_order.default_price = 60

print("Regular order total:")
print(regular_order.calculate_total(3))

print("Premium order total:")
print(premium_order.calculate_total(3))

print("-" * 50)


# =================================================
# 13. self Is a Convention
# =================================================

# This works technically, but using self is preferred.

class UnusualCup:
    size = 200

    def describe(current_object):
        return f"A {current_object.size} ml cup"


unusual_cup = UnusualCup()

print(unusual_cup.describe())

print("-" * 50)


# =================================================
# Notes
# =================================================

# Attribute:
# A value associated with a class or object.
#
#
# Class attribute:
# Defined on the class and shared as a fallback.
#
#
# Instance attribute:
# Stored directly on an individual object.
#
#
# Attribute shadowing:
# An instance attribute uses the same name as
# a class attribute and takes priority during lookup.
#
#
# del object.attribute:
# Deletes the attribute from the object's namespace.
#
#
# Attribute lookup:
# 1. Check the object
# 2. Check the class
# 3. Check parent classes
#
#
# Method:
# A function defined inside a class.
#
#
# self:
# Refers to the object calling an instance method.
#
#
# Object method call:
#
# cup.describe()
#
# Python effectively treats it like:
#
# ChaiCup.describe(cup)
#
#
# Important:
# self is not a reserved keyword, but it is the
# standard and recommended name.
