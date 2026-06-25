# sets_demo.py

# ---------------------------------------
# Python Sets Demo
# Topics:
# 1. Creating sets
# 2. Union
# 3. Intersection
# 4. Difference
# 5. Membership testing
# 6. Case sensitivity
# 7. Frozen set
# ---------------------------------------

# -----------------------------
# 1. Creating Sets
# -----------------------------

# Sets are created using curly braces {}
# Sets store only unique values

essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}

print("Essential spices:", essential_spices)
print("Optional spices:", optional_spices)

# -----------------------------
# 2. Union
# -----------------------------

# Union combines all unique values from both sets
# The | operator is used for union

all_spices = essential_spices | optional_spices

print("All spices:", all_spices)

# -----------------------------
# 3. Intersection
# -----------------------------

# Intersection gives only common values from both sets
# The & operator is used for intersection

common_spices = essential_spices & optional_spices

print("Common spices:", common_spices)

# -----------------------------
# 4. Difference
# -----------------------------

# Difference gives values present in the first set
# but not present in the second set

only_in_essential = essential_spices - optional_spices

print("Only in essential spices:", only_in_essential)

# -----------------------------
# 5. Membership Testing
# -----------------------------

# The 'in' keyword checks whether a value exists in a set

is_cloves_in_essential = "cloves" in essential_spices
print("Is cloves in essential spices?", is_cloves_in_essential)

is_cloves_in_optional = "cloves" in optional_spices
print("Is cloves in optional spices?", is_cloves_in_optional)

# -----------------------------
# 6. Case Sensitivity
# -----------------------------

# Membership testing is case-sensitive
# "Cloves" and "cloves" are different values

is_capital_cloves_available = "Cloves" in optional_spices

print("Is Cloves with capital C in optional spices?", is_capital_cloves_available)

# -----------------------------
# 7. Duplicate Values in Sets
# -----------------------------

# Sets automatically remove duplicate values

duplicate_spices = {"ginger", "ginger", "cardamom", "cardamom"}

print("Set with duplicates removed:", duplicate_spices)

# -----------------------------
# 8. Frozen Set
# -----------------------------

# frozenset is an immutable version of a set
# Once created, it cannot be changed

fixed_spices = frozenset({"cardamom", "ginger", "cinnamon"})

print("Frozen set:", fixed_spices)

# The below line would give an error because frozenset cannot be changed
# fixed_spices.add("cloves")
