# conditionals_advanced_demo.py

# ---------------------------------------
# Python Conditionals Advanced Demo
# Topics:
# 1. Nested if statements
# 2. pass keyword
# 3. Ternary operator
# 4. int() conversion
# 5. match-case
# ---------------------------------------

# -----------------------------
# Mini Project 1:
# Smart Thermostat Alert System
# -----------------------------

# Problem:
# If device is active, check temperature.
# If temperature is above 35, show high temperature alert.
# Otherwise, show temperature is normal.
# If device is not active, show device is offline.

device_status = "active"
temperature = 38

if device_status == "active":
    if temperature > 35:
        print("High temperature alert!")
    else:
        print("Temperature is normal.")
else:
    print("Device is offline.")

print("-" * 40)

# -----------------------------
# pass Keyword Example
# -----------------------------

# pass is used as a temporary placeholder.
# It means "do nothing for now".

device_status = "offline"

if device_status == "active":
    pass
else:
    print("Device is offline.")

print("-" * 40)

# -----------------------------
# Mini Project 2:
# Delivery Fee Waiver
# -----------------------------

# Problem:
# If order amount is more than 300, delivery is free.
# Otherwise, delivery fee is 30 rupees.

# input() always returns a string.
# int() converts the string input into an integer.

order_amount = int(input("Enter the order amount: "))

# Ternary operator:
# value_if_true if condition else value_if_false

delivery_fee = 0 if order_amount > 300 else 30

print(f"Delivery fee is: {delivery_fee} rupees")

print("-" * 40)

# -----------------------------
# Mini Project 3:
# Railway Seat Info System
# -----------------------------

# Problem:
# Based on the seat type, show its features.
# Valid seat types:
# sleeper, ac, general, luxury

seat_type = input(
    "Enter seat type - sleeper, ac, general, luxury: "
).lower()

# match-case is useful when one variable has many possible values.
# Requires Python 3.10 or later.

match seat_type:
    case "sleeper":
        print("Sleeper: No AC, beds available.")

    case "ac":
        print("AC: Air conditioned, comfy ride.")

    case "general":
        print("General: Cheapest option, no reservation.")

    case "luxury":
        print("Luxury: Premium seats with meals.")

    case _:
        print("Invalid seat type.")

print("-" * 40)

# -----------------------------
# Extra Notes
# -----------------------------

# Nested if:
# Used when one condition should be checked inside another condition.

# Ternary operator:
# Used for short if-else logic in one line.

# match-case:
# Used when checking one value against many possible cases.

# .lower():
# Converts user input to lowercase.
# This helps match values like AC, ac, Ac, or aC.
