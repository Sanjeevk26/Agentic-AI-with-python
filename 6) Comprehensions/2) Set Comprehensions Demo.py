# Python Set Comprehension Demo
# Topics:
# 1. Set comprehension syntax
# 2. Finding unique values
# 3. Using conditions
# 4. Nested set comprehension
# ---------------------------------------


# -----------------------------
# 1. Basic Set Comprehension
# -----------------------------

# A set stores only unique values.
# Duplicate values are automatically removed.

favorite_chais = [
    "masala chai",
    "green tea",
    "masala chai",
    "lemon tea",
    "green tea",
    "elaichi chai"
]

unique_chais = {chai for chai in favorite_chais}

print("Unique chai types:")
print(unique_chais)

print("-" * 40)


# -----------------------------
# 2. Set Comprehension with Condition
# -----------------------------

# Keep only chai names whose length is greater than 8.

unique_long_chais = {
    chai for chai in favorite_chais if len(chai) > 8
}

print("Unique chai names longer than 8 characters:")
print(unique_long_chais)

print("-" * 40)


# -----------------------------
# 3. Normal Loop Version
# -----------------------------

# The same logic can also be written using a normal loop.

unique_chais_loop = set()

for chai in favorite_chais:
    unique_chais_loop.add(chai)

print("Unique chai types using normal loop:")
print(unique_chais_loop)

print("-" * 40)


# -----------------------------
# 4. Nested Data Example
# -----------------------------

# We have a dictionary of chai recipes.
# Each recipe has a list of ingredients.

recipes = {
    "masala chai": ["ginger", "cardamom", "clove"],
    "elaichi chai": ["cardamom", "milk"],
    "spicy chai": ["ginger", "black pepper", "clove"]
}


# -----------------------------
# 5. Nested Set Comprehension
# -----------------------------

# Goal:
# Find all unique ingredients from all recipes.

unique_spices = {
    spice
    for ingredients in recipes.values()
    for spice in ingredients
}

print("Unique spices from all recipes:")
print(unique_spices)

print("-" * 40)


# -----------------------------
# 6. Same Nested Logic with Normal Loops
# -----------------------------

unique_spices_loop = set()

for ingredients in recipes.values():
    for spice in ingredients:
        unique_spices_loop.add(spice)

print("Unique spices using normal nested loops:")
print(unique_spices_loop)

print("-" * 40)


# -----------------------------
# Notes
# -----------------------------

# Set comprehension syntax:
# {expression for item in iterable if condition}

# Example:
# {chai for chai in favorite_chais}

# In nested comprehension:
# {
#     spice
#     for ingredients in recipes.values()
#     for spice in ingredients
# }

# ingredients:
# One full list of ingredients at a time.

# spice:
# One individual item from that ingredients list.

# The final expression is spice because
# that is the value we want to collect.

# Sets are unordered.
# Output order may change each time.
