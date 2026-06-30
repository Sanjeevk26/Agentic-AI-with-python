# function_parameters_demo.py

# ---------------------------------------
# Python Function Parameters Demo
# Topics:
# 1. Parameters and arguments
# 2. Mutable and immutable values
# 3. Positional arguments
# 4. Keyword arguments
# 5. *args
# 6. **kwargs
# 7. Default parameter values
# 8. Default mutable argument trap
# ---------------------------------------


# -----------------------------
# 1. Basic Function Parameter
# -----------------------------

chai = "Ginger Chai"


def prepare_chai(order):
    print(f"Preparing {order}")


prepare_chai(chai)

# Original string does not change
print("Original chai:", chai)

print("-" * 40)


# -----------------------------
# 2. Mutable Value Example
# -----------------------------

# Lists are mutable.
# If a list is passed into a function and changed,
# the original list also changes.

chai_numbers = [1, 2, 3]


def edit_chai(cups):
    cups[1] = 42


edit_chai(chai_numbers)

print("Updated chai numbers:", chai_numbers)

print("-" * 40)


# -----------------------------
# 3. Positional Arguments
# -----------------------------

# Positional arguments depend on order.

def make_chai(tea, milk, sugar):
    print("Tea:", tea)
    print("Milk:", milk)
    print("Sugar:", sugar)


make_chai("Darjeeling", "yes", "low")

print("-" * 40)


# -----------------------------
# 4. Keyword Arguments
# -----------------------------

# Keyword arguments use parameter names.
# Order does not matter when names are provided.

make_chai(tea="Green", sugar="medium", milk="no")

print("-" * 40)


# -----------------------------
# 5. *args Example
# -----------------------------

# *args collects multiple positional arguments into a tuple.

def special_chai(*ingredients):
    print("Ingredients:", ingredients)


special_chai("cinnamon", "cardamom", "ginger")

print("-" * 40)


# -----------------------------
# 6. **kwargs Example
# -----------------------------

# **kwargs collects multiple keyword arguments into a dictionary.

def chai_extras(**extras):
    print("Extras:", extras)


chai_extras(sweetener="honey", foam="yes")

print("-" * 40)


# -----------------------------
# 7. *args and **kwargs Together
# -----------------------------

# Values without names go into ingredients.
# Values with names go into extras.

def special_order(*ingredients, **extras):
    print("Ingredients:", ingredients)
    print("Extras:", extras)


special_order(
    "cinnamon",
    "cardamom",
    sweetener="honey",
    foam="yes"
)

print("-" * 40)


# -----------------------------
# 8. Default Parameter Value
# -----------------------------

# If no value is passed, the default value is used.

def simple_chai_order(order="Masala Chai"):
    print("Order:", order)


simple_chai_order()
simple_chai_order("Ginger Chai")

print("-" * 40)


# -----------------------------
# 9. Default Mutable Argument Trap
# -----------------------------

# Avoid using a list as a default parameter.
# The same list is reused across function calls.

def bad_chai_order(order=[]):
    order.append("Masala Chai")
    print(order)


bad_chai_order()
bad_chai_order()

print("-" * 40)


# -----------------------------
# 10. Safe Default Value Using None
# -----------------------------

# Use None as the default value.
# Then create a new list inside the function.

def safe_chai_order(order=None):
    if order is None:
        order = []

    order.append("Masala Chai")
    print(order)


safe_chai_order()
safe_chai_order()

print("-" * 40)


# -----------------------------
# Notes
# -----------------------------

# Parameter:
# Placeholder written inside function definition.

# Argument:
# Actual value passed while calling the function.

# Positional argument:
# Matched based on position.

# Keyword argument:
# Matched based on parameter name.

# *args:
# Collects multiple positional arguments into a tuple.

# **kwargs:
# Collects multiple keyword arguments into a dictionary.

# Mutable values:
# Lists and dictionaries can be changed.

# Immutable values:
# Strings, numbers, and tuples cannot be changed directly.

# Best practice:
# Do not use mutable values like [] or {} as default parameters.
# Use None instead.
