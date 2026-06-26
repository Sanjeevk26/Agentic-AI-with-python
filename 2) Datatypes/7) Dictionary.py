
# dictionaries_demo.py

# ---------------------------------------
# Python Dictionaries Demo
# Topics:
# 1. Creating dictionaries
# 2. Adding data
# 3. Accessing data
# 4. Deleting data
# 5. Membership testing
# 6. keys(), values(), items()
# 7. popitem()
# 8. update()
# 9. Safe access using get()
# ---------------------------------------

# -----------------------------
# 1. Creating a Dictionary
# -----------------------------

# Dictionary stores data in key-value pairs.
# Here, type, size, and sugar are keys.

chai_order = dict(
    type="Masala Chai",
    size="Large",
    sugar=2
)

print("Chai order:", chai_order)

# -----------------------------
# 2. Creating an Empty Dictionary
# -----------------------------

chai_recipe = {}

# Adding values using keys
chai_recipe["base"] = "Black Tea"
chai_recipe["liquid"] = "Milk"

print("Chai recipe:", chai_recipe)

# -----------------------------
# 3. Accessing Data
# -----------------------------

# Values are accessed using their keys

recipe_base = chai_recipe["base"]

print("Recipe base:", recipe_base)

# -----------------------------
# 4. Deleting Data
# -----------------------------

# del removes a key-value pair from the dictionary

del chai_recipe["liquid"]

print("Recipe after deleting liquid:", chai_recipe)

# -----------------------------
# 5. Membership Testing
# -----------------------------

# The 'in' keyword checks whether a key exists in the dictionary

is_sugar_in_order = "sugar" in chai_order

print("Is sugar in the order?", is_sugar_in_order)

# -----------------------------
# 6. Redefining Dictionary
# -----------------------------

chai_order = {
    "type": "Ginger Chai",
    "size": "Medium",
    "sugar": 1
}

print("New chai order:", chai_order)

# -----------------------------
# 7. keys(), values(), and items()
# -----------------------------

# keys() gives all keys
print("Order keys:", chai_order.keys())

# values() gives all values
print("Order values:", chai_order.values())

# items() gives key-value pairs as tuples
print("Order items:", chai_order.items())

# -----------------------------
# 8. popitem()
# -----------------------------

# popitem() removes and returns the last inserted item

last_item = chai_order.popitem()

print("Removed last item:", last_item)
print("Order after popitem:", chai_order)

# -----------------------------
# 9. Updating a Dictionary
# -----------------------------

# update() adds new key-value pairs or updates existing ones

extra_spices = {
    "cardamom": "crushed",
    "ginger": "sliced"
}

chai_recipe.update(extra_spices)

print("Updated chai recipe:", chai_recipe)

# -----------------------------
# 10. Safe Access with get()
# -----------------------------

# Directly accessing a missing key can crash the program.
# get() safely returns a default value if the key does not exist.

customer_note = chai_order.get("customer_note", "No note given")

print("Customer note:", customer_note)

# If the key exists, get() returns the actual value.

chai_size = chai_order.get("size", "Size not available")

print("Chai size:", chai_size)
