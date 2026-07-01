# Python Types of Functions Demo
# Topics:
# 1. Pure functions
# 2. Impure functions
# 3. Recursive functions
# 4. Lambda functions
# 5. filter()
# ---------------------------------------


# -----------------------------
# 1. Pure Function
# -----------------------------

# A pure function only depends on the input given to it.
# It does not change any outside/global value.

def pure_chai(cups):
    return cups * 10


pure_result = pure_chai(3)

print("Pure function result:", pure_result)

print("-" * 40)


# -----------------------------
# 2. Impure Function
# -----------------------------

# An impure function changes something outside itself.
# Here, the function changes a global variable.

total_chai = 0


def impure_chai(cups):
    global total_chai
    total_chai += cups
    return total_chai


print("Before impure function:", total_chai)

impure_chai(5)

print("After impure function:", total_chai)

print("-" * 40)


# -----------------------------
# 3. Recursive Function
# -----------------------------

# A recursive function calls itself.
# It must have a stopping condition.

def pour_chai(n):
    print("Cups left to pour:", n)

    if n == 0:
        return "All cups poured"

    return pour_chai(n - 1)


result = pour_chai(3)

print(result)

print("-" * 40)


# -----------------------------
# 4. Lambda Function
# -----------------------------

# Lambda functions are small anonymous functions.
# They are useful for short one-line logic.

add_tax = lambda price: price + 10

print("Price after tax:", add_tax(100))

print("-" * 40)


# -----------------------------
# 5. Lambda with filter()
# -----------------------------

# filter() keeps only the values where the condition is True.

chai_types = ["light", "kadak", "ginger", "kadak"]

strong_chai = list(filter(lambda chai: chai == "kadak", chai_types))

print("Strong chai:", strong_chai)

print("-" * 40)


# -----------------------------
# 6. Filtering Opposite Values
# -----------------------------

# This keeps all chai types that are not kadak.

not_kadak_chai = list(filter(lambda chai: chai != "kadak", chai_types))

print("Not kadak chai:", not_kadak_chai)

print("-" * 40)


# -----------------------------
# Notes
# -----------------------------

# Pure function:
# Does not change outside data.

# Impure function:
# Changes outside/global data.

# Recursive function:
# Calls itself and needs a stopping condition.

# Lambda function:
# Small anonymous function.

# filter():
# Filters values based on True or False condition.

# list():
# Converts the filter result into a list.

# Best practice:
# Prefer pure functions when possible.
# Avoid changing global variables unless really needed.
