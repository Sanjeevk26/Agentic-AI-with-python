```python
# tuples_demo.py

# ---------------------------------------
# Python Tuples Demo
# Topics:
# 1. Creating tuples
# 2. Tuple unpacking
# 3. Multiple variable assignment
# 4. Swapping variables
# 5. Membership testing
# 6. Case sensitivity
# ---------------------------------------

# -----------------------------
# 1. Creating a Tuple
# -----------------------------

# Tuples are created using parentheses ()
# Tuples are immutable, meaning their values cannot be changed directly

masala_spices = ("cardamom", "clove", "cinnamon")

print("Masala spices:", masala_spices)

# -----------------------------
# 2. Tuple Unpacking
# -----------------------------

# Tuple unpacking means extracting tuple values into separate variables

spice_one, spice_two, spice_three = masala_spices

print("Main masala spices:")
print("Spice 1:", spice_one)
print("Spice 2:", spice_two)
print("Spice 3:", spice_three)

# -----------------------------
# 3. Multiple Variable Assignment
# -----------------------------

# Python allows assigning multiple values in one line
# This behavior is powered by tuples behind the scenes

ginger_ratio, cardamom_ratio = 2, 1

print(f"Ginger to cardamom ratio: {ginger_ratio}:{cardamom_ratio}")

# -----------------------------
# 4. Swapping Variables
# -----------------------------

# Python can swap values without using a third variable

ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio

print(f"Ratio after swapping: {ginger_ratio}:{cardamom_ratio}")

# -----------------------------
# 5. Membership Testing
# -----------------------------

# The 'in' keyword checks whether a value exists inside a tuple

is_ginger_available = "ginger" in masala_spices
print("Is ginger in masala spices?", is_ginger_available)

is_cinnamon_available = "cinnamon" in masala_spices
print("Is cinnamon in masala spices?", is_cinnamon_available)

# -----------------------------
# 6. Case Sensitivity
# -----------------------------

# Membership testing is case-sensitive
# "Cinnamon" and "cinnamon" are treated as different values

is_capital_cinnamon_available = "Cinnamon" in masala_spices
print("Is Cinnamon with capital C in masala spices?", is_capital_cinnamon_available)
```
