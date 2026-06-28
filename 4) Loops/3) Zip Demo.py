# order_summary.py

# ---------------------------------------
# Python zip() Demo
# Topic:
# Preparing an order summary using two lists
# ---------------------------------------

# -----------------------------
# 1. Create Customer Names List
# -----------------------------

names = ["Hitesh", "Meera", "Sam", "Ali"]

# -----------------------------
# 2. Create Bills List
# -----------------------------

bills = [50, 70, 100, 55]

# -----------------------------
# 3. Use zip() to Combine Lists
# -----------------------------

# zip(names, bills) combines both lists position-wise.
# Example:
# Hitesh -> 50
# Meera  -> 70
# Sam    -> 100
# Ali    -> 55

print("Order Summary:")

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")

print("-" * 40)

# -----------------------------
# 4. Showing How zip() Creates Pairs
# -----------------------------

# zip() creates tuple pairs internally.
# We can convert it into a list to see the pairs clearly.

order_pairs = list(zip(names, bills))

print("Order pairs created by zip:")
print(order_pairs)

print("-" * 40)

# -----------------------------
# 5. Important Note
# -----------------------------

# zip() stops when the shortest list ends.

short_names = ["Ravi", "Priya", "Neha"]
short_bills = [40, 80]

print("Example with unequal list lengths:")

for name, amount in zip(short_names, short_bills):
    print(f"{name} paid {amount} rupees")

# Neha is ignored because there is no matching bill.

print("-" * 40)

# -----------------------------
# Notes
# -----------------------------

# Syntax:
# for variable1, variable2 in zip(list1, list2):
#     print(variable1, variable2)

# zip() is useful when two or more lists are related
# and need to be processed together.
