# ---------------------------------------
# Python enumerate() Demo
# Topic:
# Creating a numbered tea menu board
# ---------------------------------------

# -----------------------------
# 1. Create a Tea Menu List
# -----------------------------

menu = ["green", "lemon", "spiced", "mint"]

# -----------------------------
# 2. Normal for Loop
# -----------------------------

# This prints the menu items,
# but it does not give item numbers.

print("Menu without numbering:")

for item in menu:
    print(f"Menu item is {item}")

print("-" * 40)

# -----------------------------
# 3. Using enumerate()
# -----------------------------

# enumerate() gives both:
# 1. index number
# 2. item value

print("Menu with default numbering:")

for index, item in enumerate(menu):
    print(f"{index}. {item} chai")

print("-" * 40)

# -----------------------------
# 4. Using enumerate() with start=1
# -----------------------------

# By default, enumerate() starts from 0.
# For a menu board, starting from 1 is better.

print("Tea Menu Board:")

for index, item in enumerate(menu, start=1):
    print(f"{index}. {item} chai")

print("-" * 40)

# -----------------------------
# Notes
# -----------------------------

# Syntax:
# for index, item in enumerate(sequence, start=1):
#     print(index, item)

# index stores the number.
# item stores the actual value from the list.

# enumerate() is useful when we need
# both position and value while looping.
