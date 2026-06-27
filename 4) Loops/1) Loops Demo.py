# loops_demo.py

# ---------------------------------------
# Python Loops Demo
# Topics:
# 1. for loop
# 2. range()
# 3. Looping through numbers
# 4. Looping through lists
# 5. Mini projects
# ---------------------------------------

# -----------------------------
# Mini Project 1:
# Token Dispenser
# -----------------------------

# Problem:
# A tea stall owner has a digital token display.
# For every customer in line, a token number is printed.

print("Mini Project 1: Token Dispenser")

# range(1, 11) generates numbers from 1 to 10.
# The ending value 11 is not included.

for token in range(1, 11):
    print(f"Serving chai to token #{token}")

print("-" * 40)

# -----------------------------
# Mini Project 2:
# Chai Batch Simulation
# -----------------------------

# Problem:
# A chai shop makes tea in batches.
# We want to simulate 4 batches.

print("Mini Project 2: Chai Batch Simulation")

# range(1, 5) generates numbers from 1 to 4.
# The ending value 5 is not included.

for batch in range(1, 5):
    print(f"Preparing chai for batch #{batch}")

print("-" * 40)

# -----------------------------
# Mini Project 3:
# Chai Order Queue
# -----------------------------

# Problem:
# We have a list of customer names.
# Print an order ready message for each customer.

print("Mini Project 3: Chai Order Queue")

orders = ["Hitesh", "Aman", "Becky", "Carlos"]

# A list is iterable, so we can loop through it directly.

for name in orders:
    print(f"Order ready for {name}")

print("-" * 40)

# -----------------------------
# Extra Example:
# Looping Through a String
# -----------------------------

# Strings are also iterable.
# This loop prints each character one by one.

print("Extra Example: Looping Through a String")

chai_name = "Chai"

for letter in chai_name:
    print(letter)

print("-" * 40)

# -----------------------------
# Notes
# -----------------------------

# for loop syntax:
# for variable in sequence:
#     task_to_repeat

# range(start, stop):
# Starts from start value.
# Stops before the stop value.

# Example:
# range(1, 5) gives 1, 2, 3, 4

# The variable name can be anything.
# But it is better to use meaningful names like:
# token, batch, name, item, order
