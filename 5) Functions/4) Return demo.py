# Python return Keyword Demo
# Topics:
# 1. Basic return
# 2. print vs return
# 3. Returning None
# 4. Returning one value
# 5. Early return
# 6. Returning multiple values
# 7. Ignoring returned values
# ---------------------------------------


# -----------------------------
# 1. Basic return Example
# -----------------------------

def make_chai():
    return "Here is your masala chai"


# Store returned value in a variable
return_value = make_chai()

print(return_value)

# We can also print the function call directly
print(make_chai())

print("-" * 40)


# -----------------------------
# 2. print vs return
# -----------------------------

def make_chai_with_print():
    print("Here is your masala chai")


# This function prints the message,
# but it does not return any value.
result = make_chai_with_print()

print("Returned value:", result)

print("-" * 40)


# -----------------------------
# 3. Function Returning Nothing
# -----------------------------

# If a function has no return,
# Python automatically returns None.

def idle_chaiwala():
    pass


print("Idle chaiwala returned:", idle_chaiwala())

print("-" * 40)


# -----------------------------
# 4. Returning One Value
# -----------------------------

def sold_cups():
    return 120


total = sold_cups()

print("Total cups sold:", total)

print("-" * 40)


# -----------------------------
# 5. Early Return
# -----------------------------

# Once return runs, the function stops.
# Any code after return in the same block will not run.

def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai is over"

    return "Chai is ready"


print(chai_status(0))
print(chai_status(5))

print("-" * 40)


# -----------------------------
# 6. Code After return Does Not Run
# -----------------------------

def test_return():
    return "Function ended here"

    # This line will never run
    print("This will never print")


print(test_return())

print("-" * 40)


# -----------------------------
# 7. Returning Multiple Values
# -----------------------------

def chai_report():
    sold = 100
    remaining = 20
    return sold, remaining


sold, remaining = chai_report()

print("Sold:", sold)
print("Remaining:", remaining)

print("-" * 40)


# -----------------------------
# 8. Returning Three Values
# -----------------------------

def detailed_chai_report():
    sold = 100
    remaining = 20
    not_paid = 10
    return sold, remaining, not_paid


sold, remaining, not_paid = detailed_chai_report()

print("Sold:", sold)
print("Remaining:", remaining)
print("Not paid:", not_paid)

print("-" * 40)


# -----------------------------
# 9. Ignoring a Returned Value
# -----------------------------

# Use underscore when a value is returned,
# but we do not want to use it.

sold, remaining, _ = detailed_chai_report()

print("Sold:", sold)
print("Remaining:", remaining)

print("-" * 40)


# -----------------------------
# Notes
# -----------------------------

# return:
# Sends a value back from a function.

# print:
# Displays output on the screen.

# None:
# Default return value when a function returns nothing.

# Early return:
# Used to exit a function before reaching the end.

# Multiple return values:
# Python can return multiple values separated by commas.

# Underscore:
# Commonly used to ignore a returned value.
