# Python Generators Demo
# Topics:
# 1. yield from
# 2. Combining generators
# 3. send()
# 4. close()
# 5. GeneratorExit
# 6. Cleanup with finally
# -------------------------------------------------


# =================================================
# 1. Local Chai Generator
# =================================================

def local_chai():
    """Yield locally available chai varieties."""

    yield "Masala Chai"
    yield "Ginger Chai"


# =================================================
# 2. Imported Chai Generator
# =================================================

def imported_chai():
    """Yield imported tea varieties."""

    yield "Matcha"
    yield "Oolong Chai"


# =================================================
# 3. Combine Generators with yield from
# =================================================

def full_menu():
    """
    Delegate value generation to two other generators.
    """

    yield from local_chai()
    yield from imported_chai()


print("Full chai menu:")

for chai in full_menu():
    print(chai)

print("-" * 40)


# =================================================
# 4. Manual Alternative to yield from
# =================================================

def full_menu_manual():
    """
    This produces the same result without yield from.
    """

    for chai in local_chai():
        yield chai

    for chai in imported_chai():
        yield chai


print("Full menu using manual loops:")

for chai in full_menu_manual():
    print(chai)

print("-" * 40)


# =================================================
# 5. Generator That Receives Orders
# =================================================

def chai_stall():
    """
    Receive chai orders until the generator is closed.

    The finally block runs when close() is called.
    """

    print("Chai stall opened.")

    try:
        while True:
            order = yield "Waiting for chai order"
            print(f"Preparing {order}")

    finally:
        print("Stall closed. Cleaning up resources.")


# Create the generator object
stall = chai_stall()

# Start the generator and pause at the first yield
status = next(stall)
print(status)

# Send values into the generator
status = stall.send("Masala Chai")
print(status)

status = stall.send("Ginger Chai")
print(status)

# Gracefully stop the generator
stall.close()

print("-" * 40)


# =================================================
# 6. Handling GeneratorExit Explicitly
# =================================================

def customer_service():
    """
    Demonstrate the GeneratorExit exception raised by close().
    """

    try:
        while True:
            customer = yield "Waiting for customer"
            print(f"Serving {customer}")

    except GeneratorExit:
        print("Customer service generator received GeneratorExit.")
        print("Customer service stopped.")


service = customer_service()

print(next(service))
print(service.send("Customer 1"))

service.close()

print("-" * 40)


# =================================================
# 7. Checking Generator State After close()
# =================================================

closed_stall = chai_stall()
print(next(closed_stall))

closed_stall.close()

try:
    next(closed_stall)
except StopIteration:
    print("The closed generator cannot produce more values.")

print("-" * 40)


# =================================================
# Notes
# =================================================

# yield:
# Produces a value and pauses the generator.
#
#
# yield from:
# Delegates value generation to another iterable.
#
# Example:
# yield from local_chai()
#
#
# next(generator):
# Starts or resumes the generator.
#
#
# generator.send(value):
# Sends a value into a generator paused at yield.
#
#
# generator.close():
# Stops the generator.
#
#
# GeneratorExit:
# Raised inside a generator when close() is called.
#
#
# finally:
# Recommended for resource cleanup because it runs
# when the generator is closed or otherwise terminated.
#
#
# Common cleanup use cases:
# - Closing database connections
# - Closing files
# - Releasing network resources
# - Stopping streams
# - Releasing locks
