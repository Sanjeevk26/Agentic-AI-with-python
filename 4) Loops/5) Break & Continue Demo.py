# loop_control_demo.py

# ---------------------------------------
# Python Loop Control Demo
# Topics:
# 1. continue
# 2. break
# 3. indentation in loops
# 4. for-else
# ---------------------------------------

# -----------------------------
# Mini Project 1:
# Chai Flavor Availability
# -----------------------------

# Problem:
# Some chai flavors are out of stock.
# Skip out-of-stock flavors.
# Stop completely if a discontinued flavor is found.

flavors = ["ginger", "out of stock", "lemon", "discontinued", "tulsi"]

print("Checking chai flavors:")

for flavor in flavors:
    # continue skips the current iteration
    if flavor == "out of stock":
        continue

    # break stops the entire loop
    if flavor == "discontinued":
        print("Discontinued item found.")
        break

    # This runs only for normal available flavors
    print(f"{flavor} item found.")

# This is outside the loop
print("Outside of loop.")

print("-" * 40)

# -----------------------------
# Understanding continue
# -----------------------------

# In this example:
# ginger        -> printed
# out of stock  -> skipped
# lemon         -> printed
# discontinued  -> loop stops
# tulsi         -> never reached

# -----------------------------
# Mini Project 2:
# for-else Example
# -----------------------------

# Problem:
# Find the first staff member eligible to manage the store.
# If nobody is eligible, show fallback message.

staff = [
    ("Amit", 16),
    ("Zara", 17),
    ("Raj", 15)
]

print("Checking staff eligibility:")

for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible to manage the staff.")
        break
else:
    # This else belongs to the for loop, not the if statement.
    # It runs only if the loop did not hit break.
    print("No one is eligible to manage the staff.")

print("-" * 40)

# -----------------------------
# Mini Project 3:
# for-else When Someone Is Eligible
# -----------------------------

staff = [
    ("Amit", 16),
    ("Zara", 19),
    ("Raj", 15)
]

print("Checking staff eligibility again:")

for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible to manage the staff.")
        break
else:
    print("No one is eligible to manage the staff.")

print("-" * 40)

# -----------------------------
# Notes
# -----------------------------

# continue:
# Skips the current loop iteration and moves to the next item.

# break:
# Stops the loop completely.

# for-else:
# The else block runs only when the loop completes without break.

# Indentation is very important:
# - Code inside for runs during the loop.
# - Code inside if runs only when the condition is true.
# - Code outside the loop runs after the loop ends.
