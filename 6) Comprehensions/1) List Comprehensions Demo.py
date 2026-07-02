# Python Comprehensions Demo
# Topics:
# 1. What is comprehension?
# 2. List comprehension
# 3. Filtering items
# 4. Comparing loop vs comprehension
# ---------------------------------------


# -----------------------------
# 1. Menu List
# -----------------------------

menu = [
    "masala chai",
    "iced lemon tea",
    "green tea",
    "iced peach tea",
    "ginger chai"
]


# -----------------------------
# 2. Normal Loop Approach
# -----------------------------

# Goal:
# Create a new list with only iced tea items.

iced_teas_loop = []

for tea in menu:
    if "iced" in tea:
        iced_teas_loop.append(tea)

print("Using normal loop:")
print(iced_teas_loop)

print("-" * 40)


# -----------------------------
# 3. List Comprehension Approach
# -----------------------------

# Syntax:
# [expression for item in iterable if condition]

iced_teas = [tea for tea in menu if "iced" in tea]

print("Using list comprehension:")
print(iced_teas)

print("-" * 40)


# -----------------------------
# 4. Breaking Down the Syntax
# -----------------------------

# iced_teas = [tea for tea in menu if "iced" in tea]
#
# tea before for:
# Value that will be added to the new list.
#
# for tea in menu:
# Loops through every item in the menu.
#
# if "iced" in tea:
# Adds only those items that contain the word "iced".


# -----------------------------
# 5. Using a Different Variable Name
# -----------------------------

# The variable name can be anything.
# But it must be used consistently.

iced_items = [my_tea for my_tea in menu if "iced" in my_tea]

print("Using different variable name:")
print(iced_items)

print("-" * 40)


# -----------------------------
# 6. Filtering by Length
# -----------------------------

# Get menu items whose length is greater than 12.

long_items = [tea for tea in menu if len(tea) > 12]

print("Menu items longer than 12 characters:")
print(long_items)

print("-" * 40)


# -----------------------------
# 7. Filtering Short Items
# -----------------------------

# Get menu items whose length is less than 12.

short_items = [tea for tea in menu if len(tea) < 12]

print("Menu items shorter than 12 characters:")
print(short_items)

print("-" * 40)


# -----------------------------
# Notes
# -----------------------------

# Comprehensions are a shorter way to create collections.
# Most comprehension logic can also be written using loops.
#
# List comprehension syntax:
# [expression for item in iterable if condition]
#
# expression:
# What should be added to the new list.
#
# item:
# Current value from the iterable.
#
# iterable:
# A collection like list, string, tuple, set, etc.
#
# condition:
# Optional filter condition.
