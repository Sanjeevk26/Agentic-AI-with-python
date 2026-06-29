# Python while Loop Demo
# Topic:
# Simulating tea heating until it reaches boiling temperature
# ---------------------------------------

# -----------------------------
# Problem:
# Tea starts heating at 40 degrees Celsius.
# It boils at 100 degrees Celsius.
# Increase temperature by 15 degrees each step.
# Print every temperature step.
# -----------------------------

# Starting temperature
temperature = 40

# Boiling point
boiling_point = 100

# Heating step
increase_by = 15

print("Tea Heating Simulation Started")

# -----------------------------
# while Loop
# -----------------------------

# The loop will continue as long as temperature is less than 100.
# Once temperature reaches or exceeds 100, the loop stops.

while temperature < boiling_point:
    print(f"Current temperature: {temperature}°C")

    # Increase temperature by 15
    # This is the short form of:
    # temperature = temperature + 15
    temperature += increase_by

# This line runs after the loop ends
print("Tea is ready to boil.")

print("-" * 40)

# -----------------------------
# Extra Example:
# Printing After Increasing Temperature
# -----------------------------

# In this version, the temperature is increased first
# and printed after that.

temperature = 40

print("Second Simulation: Increase first, then print")

while temperature < boiling_point:
    temperature += increase_by
    print(f"Current temperature: {temperature}°C")

print("Tea is ready to boil.")

# -----------------------------
# Notes:
# -----------------------------

# while loop syntax:
# while condition:
#     code_to_repeat

# The condition must eventually become false.
# Otherwise, the loop can run forever.

# temperature += 15
# means:
# temperature = temperature + 15
