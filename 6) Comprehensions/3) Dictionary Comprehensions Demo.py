# Python Dictionary Comprehension Demo
# Topics:
# 1. Dictionary comprehension syntax
# 2. Looping through dictionary items
# 3. Converting INR prices to USD
# 4. Comparing normal loop vs comprehension
# 5. Adding conditions
# ---------------------------------------


# -----------------------------
# 1. Original Dictionary
# -----------------------------

# Tea prices are currently in INR.

tea_prices_inr = {
    "masala chai": 40,
    "green tea": 50,
    "lemon tea": 200
}


# -----------------------------
# 2. Normal Loop Approach
# -----------------------------

# Goal:
# Convert all tea prices from INR to USD.
# Assume 1 USD = 80 INR.

tea_prices_usd_loop = {}

for tea, price in tea_prices_inr.items():
    tea_prices_usd_loop[tea] = price / 80

print("Using normal loop:")
print(tea_prices_usd_loop)

print("-" * 40)


# -----------------------------
# 3. Dictionary Comprehension Approach
# -----------------------------

# Syntax:
# {key: value for item in iterable}

tea_prices_usd = {
    tea: price / 80
    for tea, price in tea_prices_inr.items()
}

print("Using dictionary comprehension:")
print(tea_prices_usd)

print("-" * 40)


# -----------------------------
# 4. Breaking Down the Syntax
# -----------------------------

# tea_prices_usd = {
#     tea: price / 80
#     for tea, price in tea_prices_inr.items()
# }
#
# tea:
# Key in the new dictionary.
#
# price / 80:
# Value in the new dictionary after converting INR to USD.
#
# tea_prices_inr.items():
# Gives both key and value from the original dictionary.


# -----------------------------
# 5. Dictionary Comprehension with Condition
# -----------------------------

# Convert only teas whose INR price is greater than 45.

expensive_teas_usd = {
    tea: price / 80
    for tea, price in tea_prices_inr.items()
    if price > 45
}

print("Expensive teas converted to USD:")
print(expensive_teas_usd)

print("-" * 40)


# -----------------------------
# 6. Formatting Prices
# -----------------------------

# round() can be used to make the result cleaner.

rounded_tea_prices_usd = {
    tea: round(price / 80, 2)
    for tea, price in tea_prices_inr.items()
}

print("Rounded USD prices:")
print(rounded_tea_prices_usd)

print("-" * 40)


# -----------------------------
# Notes
# -----------------------------

# Dictionary comprehension syntax:
# {key: value for item in iterable if condition}

# For dictionaries, use .items()
# when you need both key and value.

# Example:
# for tea, price in tea_prices_inr.items():

# Set comprehension:
# {expression for item in iterable}

# Dictionary comprehension:
# {key: value for item in iterable}

# The key:value pair is what makes it a dictionary.
