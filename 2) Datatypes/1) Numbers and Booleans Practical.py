# Python Numbers, Booleans, and Operations Demo

import sys
from fractions import Fraction
from decimal import Decimal

# -----------------------------
# 1. Integers
# -----------------------------

black_tea_grams = 14
ginger_grams = 3

# Addition
total_grams = black_tea_grams + ginger_grams
print(f"Total grams of base tea: {total_grams}")

# Subtraction
remaining_tea = black_tea_grams - ginger_grams
print(f"Remaining tea grams: {remaining_tea}")

# Multiplication
flavor_strength = black_tea_grams * ginger_grams
print(f"Flavor strength: {flavor_strength}")

# -----------------------------
# 2. Division Types
# -----------------------------

milk_liters = 7
servings = 4

# Normal division gives decimal output
milk_per_serving = milk_liters / servings
print(f"Milk per serving: {milk_per_serving}")

# Floor division ignores decimal part
total_teabags = 7
pots = 4

bags_per_pot = total_teabags // pots
print(f"Whole tea bags per pot: {bags_per_pot}")

# Modulo gives remainder
total_cardamom_pods = 10
pods_per_cup = 3

leftover_pods = total_cardamom_pods % pods_per_cup
print(f"Leftover cardamom pods: {leftover_pods}")

# -----------------------------
# 3. Exponent / Power
# -----------------------------

base_flavor_strength = 2
scale_factor = 3

powerful_flavor = base_flavor_strength ** scale_factor
print(f"Scaled flavor strength: {powerful_flavor}")

# -----------------------------
# 4. Large Number Readability
# -----------------------------

tea_leaves_harvested = 1_000_000_000
print(f"Total tea leaves harvested: {tea_leaves_harvested}")

# -----------------------------
# 5. Booleans
# -----------------------------

is_boiling = True
stir_count = 5

# True behaves like 1
total_actions = stir_count + is_boiling
print(f"Total actions: {total_actions}")

# bool() conversion
milk_present = 0
print(f"Is milk present? {bool(milk_present)}")

milk_present = 11
print(f"Is milk present now? {bool(milk_present)}")

empty_value = None
print(f"Is empty value true? {bool(empty_value)}")

# -----------------------------
# 6. Logical Operators
# -----------------------------

water_hot = True
tea_added = True

# and: both conditions must be true
can_serve_chai = water_hot and tea_added
print(f"Can serve chai? {can_serve_chai}")

tea_available = True
coffee_available = False

# or: at least one condition must be true
can_drink = tea_available or coffee_available
print(f"Can drink something? {can_drink}")

# not: reverses the boolean value
is_cup_empty = False
print(f"Is cup not empty? {not is_cup_empty}")

# -----------------------------
# 7. Floating-Point Numbers
# -----------------------------

ideal_temp = 95.5
current_temp = 95.4

difference_temp = ideal_temp - current_temp
print(f"Ideal temperature: {ideal_temp}")
print(f"Current temperature: {current_temp}")
print(f"Temperature difference: {difference_temp}")

# Float system information
print(f"Float information: {sys.float_info}")

# -----------------------------
# 8. Fractions
# -----------------------------

half_cup = Fraction(1, 2)
quarter_cup = Fraction(1, 4)

total_fraction = half_cup + quarter_cup
print(f"Total fraction quantity: {total_fraction}")

# -----------------------------
# 9. Decimal
# -----------------------------

price = Decimal("19.99")
tax = Decimal("2.50")

total_price = price + tax
print(f"Total price using Decimal: {total_price}")

# -----------------------------
# 10. Complex Numbers
# -----------------------------

complex_number = 2 + 3j
print(f"Complex number: {complex_number}")
print(f"Real part: {complex_number.real}")
print(f"Imaginary part: {complex_number.imag}")
```
