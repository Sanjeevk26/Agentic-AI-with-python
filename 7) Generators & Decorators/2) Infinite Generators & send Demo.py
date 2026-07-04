# Python Generators Demo
# Topics:
# 1. Infinite generators
# 2. Independent generator state
# 3. Sending values with send()
# 4. Priming a generator
# 5. Closing a generator
# -------------------------------------------------


# =================================================
# 1. Infinite Generator
# =================================================

def infinite_chai():
    """
    Generate an unlimited sequence of chai refill messages.

    The generator pauses at every yield and resumes
    when next() is called again.
    """

    count = 1

    while True:
        yield f"Refill #{count}"
        count += 1


# Create a generator object
refill_station = infinite_chai()

print("First customer's refills:")

# The generator is infinite, but this loop controls
# how many values are requested.
for _ in range(3):
    print(next(refill_station))

print("-" * 40)


# =================================================
# 2. Independent Generator Objects
# =================================================

# Every generator object stores its own state.

user_one = infinite_chai()
user_two = infinite_chai()

print("User one's refills:")

for _ in range(3):
    print(next(user_one))

print("User two's refills:")

for _ in range(6):
    print(next(user_two))

print("-" * 40)


# =================================================
# 3. Generator That Receives Data
# =================================================

def chai_customer():
    """
    Receive chai orders through send().

    The first yield pauses the generator and waits
    for the first order.

    Every later yield pauses the generator again
    and waits for another order.
    """

    print("Welcome! What chai would you like?")

    # The value sent using send() is stored in order.
    order = yield

    while True:
        print(f"Preparing {order}")

        # Pause and wait for the next order.
        order = yield


# Create the generator object
stall = chai_customer()

# Creating the object does not execute the body yet.
print("Generator created.")

# Prime the generator.
# This runs it until the first yield.
next(stall)

# Send orders into the paused generator.
stall.send("Masala Chai")
stall.send("Lemon Chai")
stall.send("Ginger Chai")

print("-" * 40)


# =================================================
# 4. Priming with send(None)
# =================================================

second_stall = chai_customer()

# send(None) can also prime a newly created generator.
second_stall.send(None)

second_stall.send("Elaichi Chai")
second_stall.send("Kesar Chai")

print("-" * 40)


# =================================================
# 5. Separate Customers Maintain Separate State
# =================================================

customer_one = chai_customer()
customer_two = chai_customer()

# Prime both generators separately.
next(customer_one)
next(customer_two)

customer_one.send("Masala Chai")
customer_two.send("Green Tea")
customer_one.send("Lemon Tea")
customer_two.send("Ginger Chai")

print("-" * 40)


# =================================================
# 6. Closing Generators
# =================================================

# Close generators when they are no longer required.

stall.close()
second_stall.close()
customer_one.close()
customer_two.close()

print("Customer generators closed.")

print("-" * 40)


# =================================================
# Notes
# =================================================

# Infinite generator:
#
# def generator():
#     while True:
#         yield value
#
#
# next(generator):
# Requests the next generated value.
#
#
# generator.send(value):
# Sends a value into a generator paused at yield.
#
#
# order = yield:
# The value provided through send() is stored in order.
#
#
# Priming:
# A generator must first reach its initial yield.
#
# Use:
# next(generator)
#
# Or:
# generator.send(None)
#
#
# generator.close():
# Stops the generator.
#
#
# Important:
# An infinite generator should always be consumed
# through controlled logic such as a limited loop,
# a condition, or an external cancellation mechanism.
