# conditionals_demo.py

# ---------------------------------------
# Python Conditionals Demo
# Topics:
# 1. if statement
# 2. input()
# 3. lower()
# 4. if-else
# 5. or operator
# 6. if-elif-else
# 7. Mini projects
# ---------------------------------------

# -----------------------------
# Mini Project 1:
# Smart Kettle Notification
# -----------------------------

# Problem:
# Show a notification only when the kettle has finished boiling.

kettle_boiled = True

if kettle_boiled:
    print("Kettle done! Time to make chai.")

print("-" * 40)

# -----------------------------
# Mini Project 2:
# Snack Suggestion System
# -----------------------------

# Problem:
# A cafe serves only cookies or samosa.
# If the user asks for either of them, confirm the order.
# Otherwise, show an unavailable message.

snack = input("Enter your preferred snack: ").lower()

if snack == "cookies" or snack == "samosa":
    print(f"Great choice! We will serve you {snack}.")
else:
    print("Sorry, we only serve cookies or samosa with tea.")

print("-" * 40)

# -----------------------------
# Mini Project 3:
# Chai Price Calculator
# -----------------------------

# Problem:
# Calculate chai price based on cup size.
# small  -> 10 rupees
# medium -> 15 rupees
# large  -> 20 rupees

cup = input("Choose your cup size - small, medium, large: ").lower()

if cup == "small":
    print("Price is 10 rupees.")
elif cup == "medium":
    print("Price is 15 rupees.")
elif cup == "large":
    print("Price is 20 rupees.")
else:
    print("Unknown cup size.")

print("-" * 40)

# -----------------------------
# Extra Notes
# -----------------------------

# = is used for assignment
# Example:
# snack = "samosa"

# == is used for comparison
# Example:
# snack == "samosa"

# lower() converts user input to lowercase
# This helps handle inputs like:
# Samosa, SAMOSA, samosa
