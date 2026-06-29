# Python Walrus Operator Demo
# Topics:
# 1. Statement vs expression
# 2. Walrus operator :=
# 3. Using walrus in if statement
# 4. Using walrus with input()
# 5. Using walrus in while loop
# ---------------------------------------

# -----------------------------
# 1. Without Walrus Operator
# -----------------------------

# Normal approach:
# First calculate the remainder.
# Then check it in the if condition.

value = 13
remainder = value % 5

if remainder:
    print(f"Not divisible. Remainder is {remainder}")

print("-" * 40)

# -----------------------------
# 2. With Walrus Operator
# -----------------------------

# Walrus operator assigns and checks the value in the same line.
# remainder := value % 5 means:
# Calculate value % 5 and store it in remainder.

value = 13

if remainder := value % 5:
    print(f"Not divisible. Remainder is {remainder}")

print("-" * 40)

# -----------------------------
# 3. Cup Size Example
# -----------------------------

# Available cup sizes in the tea shop

available_sizes = ["small", "medium", "large"]

# The input value is stored in requested_size.
# Then it is checked against available_sizes.

if requested_size := input("Enter your chai cup size: ").lower():
    if requested_size in available_sizes:
        print(f"Serving {requested_size} chai")
    else:
        print(f"Size unavailable: {requested_size}")

print("-" * 40)

# -----------------------------
# 4. Walrus Operator in while Loop
# -----------------------------

# The user must choose one valid flavor.
# The loop keeps running until the flavor exists in the list.

flavors = ["masala", "ginger", "lemon", "mint"]

print(f"Available flavors: {flavors}")

while (flavor := input("Choose your flavor: ").lower()) not in flavors:
    print(f"Sorry, {flavor} is not available.")

print(f"You chose {flavor} chai.")

print("-" * 40)

# -----------------------------
# Notes
# -----------------------------

# = is used for normal assignment.
# Example:
# x = 5

# := is used for assignment inside an expression.
# Example:
# if remainder := value % 5:

# The walrus operator can make code shorter,
# but it should be used only when it improves readability.

# Requires Python 3.8 or later.
