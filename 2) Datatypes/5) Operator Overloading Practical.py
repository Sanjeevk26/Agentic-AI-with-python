```python
# lists_operator_overloading_demo.py

# ---------------------------------------
# Python Lists Demo
# Topics:
# 1. Operator overloading
# 2. Combining lists using +
# 3. Repeating lists using *
# 4. Introduction to itemgetter
# 5. Working with bytearray
# 6. Replacing bytearray values
# ---------------------------------------

# -----------------------------
# 1. Operator Overloading with +
# -----------------------------

# The + operator is normally used for addition.
# In lists, it combines two lists.
# This is called operator overloading.

base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor

print("Full liquid mix:", full_liquid_mix)

# -----------------------------
# 2. Repeating Lists with *
# -----------------------------

# The * operator repeats the items in a list.

strong_brew = ["black tea"] * 3

print("Strong brew:", strong_brew)

# If the list has multiple items, the full list is repeated.

strong_brew_with_water = ["black tea", "water"] * 3

print("Strong brew with water:", strong_brew_with_water)

# -----------------------------
# 3. Introduction to itemgetter
# -----------------------------

# itemgetter comes from the operator module.
# It is useful when extracting values or sorting complex data.

from operator import itemgetter

tea_options = [
    ("masala chai", 50),
    ("ginger chai", 40),
    ("green tea", 60)
]

# Get the price from the first tea option
get_price = itemgetter(1)

print("Price of first tea option:", get_price(tea_options[0]))

# -----------------------------
# 4. bytearray Basics
# -----------------------------

# bytearray is a mutable sequence of bytes.
# It is useful for raw data, binary data, and encoded text.

raw_spice_data = bytearray(b"cinnamon")

print("Raw spice data:", raw_spice_data)

# -----------------------------
# 5. Replacing Data in bytearray
# -----------------------------

# replace() returns a new value.
# So we must store the result back into the variable.

raw_spice_data = raw_spice_data.replace(b"cinnamon", b"cardamom")

print("Updated raw spice data:", raw_spice_data)

# -----------------------------
# 6. Decoding bytearray
# -----------------------------

# To print bytearray as normal text, decode it.

decoded_spice_data = raw_spice_data.decode("utf-8")

print("Decoded spice data:", decoded_spice_data)
```
