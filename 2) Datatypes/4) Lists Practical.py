```python
# lists_demo.py

# ---------------------------------------
# Python Lists Demo
# Topics:
# 1. Creating lists
# 2. Adding items using append()
# 3. Removing items using remove()
# 4. Combining lists using extend()
# 5. Indexing
# 6. Inserting items using insert()
# 7. Removing last item using pop()
# 8. Reversing lists
# 9. Sorting lists
# 10. Using max() and min()
# ---------------------------------------

# -----------------------------
# 1. Creating a List
# -----------------------------

# Lists are created using square brackets []
# Lists are mutable, which means they can be changed after creation

ingredients = ["water", "milk", "black tea"]

print("Original ingredients:", ingredients)

# -----------------------------
# 2. Adding Items with append()
# -----------------------------

# append() adds an item at the end of the list

ingredients.append("sugar")

print("After adding sugar:", ingredients)

# -----------------------------
# 3. Removing Items with remove()
# -----------------------------

# remove() removes a specific item from the list

ingredients.remove("water")

print("After removing water:", ingredients)

# -----------------------------
# 4. Combining Lists with extend()
# -----------------------------

# extend() adds all items from another list

spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)

print("Chai ingredients after extend:", chai_ingredients)

# -----------------------------
# 5. List Indexing
# -----------------------------

# Indexing starts from 0
# water = index 0
# milk = index 1
# ginger = index 2
# cardamom = index 3

print("Item at index 0:", chai_ingredients[0])
print("Item at index 1:", chai_ingredients[1])

# -----------------------------
# 6. Inserting Items with insert()
# -----------------------------

# insert(index, value) adds an item at a specific position
# Existing items move to the right

chai_ingredients.insert(2, "black tea")

print("After inserting black tea at index 2:", chai_ingredients)

# -----------------------------
# 7. Removing Last Item with pop()
# -----------------------------

# pop() removes the last item and also returns it

last_added = chai_ingredients.pop()

print("Removed item using pop:", last_added)
print("After pop:", chai_ingredients)

# -----------------------------
# 8. Reversing a List
# -----------------------------

# reverse() changes the original list order

chai_ingredients.reverse()

print("After reversing:", chai_ingredients)

# -----------------------------
# 9. Sorting a List
# -----------------------------

# sort() sorts the list alphabetically

chai_ingredients.sort()

print("After sorting:", chai_ingredients)

# -----------------------------
# 10. max() and min()
# -----------------------------

# max() gives the highest value
# min() gives the lowest value

sugar_levels = [1, 2, 3, 4, 5]

maximum_sugar_level = max(sugar_levels)
minimum_sugar_level = min(sugar_levels)

print("Maximum sugar level:", maximum_sugar_level)
print("Minimum sugar level:", minimum_sugar_level)
```
