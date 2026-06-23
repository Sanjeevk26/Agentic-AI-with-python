```python
# strings_demo.py

# ---------------------------------------
# Python Strings Demo
# Topics:
# 1. String basics
# 2. Formatted strings
# 3. Indexing
# 4. Slicing
# 5. Reverse string
# 6. Encoding and decoding
# ---------------------------------------

# -----------------------------
# 1. String Basics
# -----------------------------

chai_type = "Ginger Chai"
customer_name = "Priya"

# Using formatted string
print(f"Order for {customer_name}: {chai_type} please!")

# -----------------------------
# 2. Strings Are Immutable
# -----------------------------

original_chai = "Masala Chai"

# This creates a new string, it does not change the original string directly
updated_chai = original_chai.replace("Masala", "Ginger")

print(f"Original chai: {original_chai}")
print(f"Updated chai: {updated_chai}")

# -----------------------------
# 3. Indexing
# -----------------------------

chai_description = "Aromatic and bold"

# Indexing starts from 0
first_character = chai_description[0]
second_character = chai_description[1]

print(f"First character: {first_character}")
print(f"Second character: {second_character}")

# -----------------------------
# 4. Slicing
# -----------------------------

# Syntax: string[start:end:step]
# End index is not included

first_word = chai_description[0:8]
print(f"First word: {first_word}")

# Same as above because missing start means start from beginning
first_word_shortcut = chai_description[:8]
print(f"First word using shortcut: {first_word_shortcut}")

# Missing end means go till the end
last_word = chai_description[13:]
print(f"Last word: {last_word}")

# -----------------------------
# 5. Step in Slicing
# -----------------------------

# Step 1 means every character
every_character = chai_description[0:8:1]
print(f"Every character: {every_character}")

# Step 2 means every second character
every_second_character = chai_description[0:8:2]
print(f"Every second character: {every_second_character}")

# -----------------------------
# 6. Reverse a String
# -----------------------------

# -1 step reverses the string
reversed_description = chai_description[::-1]
print(f"Reversed description: {reversed_description}")

# -----------------------------
# 7. Encoding and Decoding
# -----------------------------

label_text = "Chai Spécial"

# Encoding converts string into bytes
encoded_label = label_text.encode("utf-8")
print(f"Encoded label: {encoded_label}")

# Decoding converts bytes back into string
decoded_label = encoded_label.decode("utf-8")
print(f"Decoded label: {decoded_label}")

# -----------------------------
# 8. Multilingual String Example
# -----------------------------

hindi_chai = "अदरक चाय"

encoded_hindi_chai = hindi_chai.encode("utf-8")
decoded_hindi_chai = encoded_hindi_chai.decode("utf-8")

print(f"Original Hindi text: {hindi_chai}")
print(f"Encoded Hindi text: {encoded_hindi_chai}")
print(f"Decoded Hindi text: {decoded_hindi_chai}")
```
