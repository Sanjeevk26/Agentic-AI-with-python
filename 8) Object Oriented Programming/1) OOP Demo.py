# Python Object-Oriented Programming
# Topics:
# 1. Creating classes
# 2. Creating objects
# 3. type()
# 4. isinstance()
# 5. Class attributes
# 6. Instance attributes
# 7. Namespaces
# 8. Attribute overriding
# -------------------------------------------------


# =================================================
# 1. Creating a Basic Class
# =================================================

class Chai:
    pass


print("Type of Chai class:")
print(type(Chai))

print("-" * 50)


# =================================================
# 2. Creating an Object
# =================================================

ginger_tea = Chai()

print("Type of ginger_tea:")
print(type(ginger_tea))

print("-" * 50)


# =================================================
# 3. Checking Class Membership
# =================================================

class ChaiTime:
    pass


print("Is ginger_tea a Chai object?")
print(isinstance(ginger_tea, Chai))

print("Is ginger_tea a ChaiTime object?")
print(isinstance(ginger_tea, ChaiTime))

print("-" * 50)


# =================================================
# 4. Class Attributes
# =================================================

class SimpleChai:
    origin = "India"
    is_hot = True


print("Accessing attributes through the class:")
print("Origin:", SimpleChai.origin)
print("Is hot:", SimpleChai.is_hot)

print("-" * 50)


# =================================================
# 5. Creating Multiple Objects
# =================================================

masala_chai = SimpleChai()
ginger_chai = SimpleChai()

print("Masala chai:")
print("Origin:", masala_chai.origin)
print("Is hot:", masala_chai.is_hot)

print()

print("Ginger chai:")
print("Origin:", ginger_chai.origin)
print("Is hot:", ginger_chai.is_hot)

print("-" * 50)


# =================================================
# 6. Override an Attribute on One Object
# =================================================

# This creates an instance attribute on masala_chai.
# It does not modify the class or ginger_chai.

masala_chai.is_hot = False

print("After changing masala_chai.is_hot:")

print("Class value:", SimpleChai.is_hot)
print("Masala chai value:", masala_chai.is_hot)
print("Ginger chai value:", ginger_chai.is_hot)

print("-" * 50)


# =================================================
# 7. Add Unique Instance Attributes
# =================================================

masala_chai.flavor = "Masala"
masala_chai.size = "Large"

ginger_chai.flavor = "Ginger"
ginger_chai.size = "Medium"

print("Masala chai properties:")
print("Flavor:", masala_chai.flavor)
print("Size:", masala_chai.size)

print()

print("Ginger chai properties:")
print("Flavor:", ginger_chai.flavor)
print("Size:", ginger_chai.size)

print("-" * 50)


# =================================================
# 8. Inspect Object Namespaces
# =================================================

# __dict__ shows attributes stored directly
# inside an object's namespace.

print("masala_chai namespace:")
print(masala_chai.__dict__)

print()

print("ginger_chai namespace:")
print(ginger_chai.__dict__)

print("-" * 50)


# =================================================
# 9. Inspect the Class Namespace
# =================================================

print("Selected values from the class namespace:")
print("Origin:", SimpleChai.__dict__["origin"])
print("Is hot:", SimpleChai.__dict__["is_hot"])

print("-" * 50)


# =================================================
# 10. New Objects Still Use Class Defaults
# =================================================

lemon_chai = SimpleChai()

print("New lemon chai object:")
print("Origin:", lemon_chai.origin)
print("Is hot:", lemon_chai.is_hot)

# masala_chai changed only its own value.
print("Masala chai is still overridden:", masala_chai.is_hot)

print("-" * 50)


# =================================================
# 11. Adding a Class Attribute Later
# =================================================

SimpleChai.category = "Beverage"

print("Class category:", SimpleChai.category)
print("Masala chai category:", masala_chai.category)
print("Ginger chai category:", ginger_chai.category)
print("Lemon chai category:", lemon_chai.category)

print("-" * 50)


# =================================================
# 12. Attribute Lookup Demonstration
# =================================================

class Tea:
    temperature = "Hot"


tea_one = Tea()
tea_two = Tea()

# Both objects initially read the class attribute.
print("Initial values:")
print("Tea class:", Tea.temperature)
print("Tea one:", tea_one.temperature)
print("Tea two:", tea_two.temperature)

# Create an instance-specific value.
tea_one.temperature = "Cold"

print()

print("After overriding tea_one.temperature:")
print("Tea class:", Tea.temperature)
print("Tea one:", tea_one.temperature)
print("Tea two:", tea_two.temperature)

print("-" * 50)


# =================================================
# Notes
# =================================================

# Class:
# A blueprint used to create objects.
#
#
# Object:
# An instance created from a class.
#
#
# Class creation:
#
# class Chai:
#     pass
#
#
# Object creation:
#
# ginger_tea = Chai()
#
#
# Class attribute:
# Defined inside a class and available through
# the class and its objects.
#
#
# Instance attribute:
# Stored directly on one object.
#
#
# Namespace:
# A mapping where Python stores names and values.
#
#
# Attribute lookup:
# Python checks the object's namespace first.
# If the attribute is not found, it checks the class.
#
#
# type():
# Shows the type of a class or object.
#
#
# isinstance():
# Checks whether an object belongs to a class.
#
#
# __dict__:
# Shows attributes stored directly in many
# classes and object namespaces.
