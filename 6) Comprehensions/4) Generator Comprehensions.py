# Python Generator Expression Demo
# Topics:
# 1. Generator expression syntax
# 2. List comprehension vs generator expression
# 3. Memory-efficient processing
# 4. Using sum() with generator expressions
# 5. Consuming generators
# ---------------------------------------


# -----------------------------
# 1. Daily Sales Data
# -----------------------------

# Imagine this list has hundreds or millions of records.
# For demo purposes, we are using a small list.

daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]


# -----------------------------
# 2. List Comprehension
# -----------------------------

# This creates the full list in memory immediately.

above_five_sales_list = [sale for sale in daily_sales if sale > 5]

print("Using list comprehension:")
print(above_five_sales_list)

print("-" * 40)


# -----------------------------
# 3. Generator Expression
# -----------------------------

# This creates a generator object.
# It does not create the full list immediately.

above_five_sales_generator = (sale for sale in daily_sales if sale > 5)

print("Using generator expression:")
print(above_five_sales_generator)

print("-" * 40)


# -----------------------------
# 4. Consuming a Generator with for Loop
# -----------------------------

# A generator gives values one by one.

print("Generator values one by one:")

above_five_sales_generator = (sale for sale in daily_sales if sale > 5)

for sale in above_five_sales_generator:
    print(sale)

print("-" * 40)


# -----------------------------
# 5. Using sum() with Generator Expression
# -----------------------------

# sum() can consume the generator directly.
# This is memory efficient because no extra list is created.

total_sales = sum(sale for sale in daily_sales if sale > 5)

print("Total sales above 5:")
print(total_sales)

print("-" * 40)


# -----------------------------
# 6. Same Logic Using List
# -----------------------------

# This also works, but it creates a list first.

total_sales_list = sum([sale for sale in daily_sales if sale > 5])

print("Total sales above 5 using list comprehension:")
print(total_sales_list)

print("-" * 40)


# -----------------------------
# 7. Generator Can Be Consumed Once
# -----------------------------

sales_generator = (sale for sale in daily_sales if sale > 5)

print("First consumption:")
print(list(sales_generator))

print("Second consumption:")
print(list(sales_generator))

# The second output is empty because the generator
# was already consumed the first time.

print("-" * 40)


# -----------------------------
# Notes
# -----------------------------

# List comprehension syntax:
# [expression for item in iterable if condition]

# Generator expression syntax:
# (expression for item in iterable if condition)

# List comprehension:
# Creates the full list in memory.

# Generator expression:
# Produces one item at a time.

# Generator expressions are useful when:
# - Data is large
# - Memory efficiency matters
# - We only need to process items one by one

# Common ways to consume generators:
# - for loop
# - sum()
# - list()
# - next()
