# Python Generators Demo
# Topics:
# 1. Normal functions
# 2. Generator functions
# 3. yield keyword
# 4. Generator objects
# 5. next()
# 6. StopIteration
# 7. Lazy evaluation
# ---------------------------------------


# -----------------------------
# 1. Basic Generator Function
# -----------------------------

# A generator function uses yield instead of return.
# Each yield produces one value and pauses the function.

def serve_chai():
    yield "Masala Chai"
    yield "Ginger Chai"
    yield "Elaichi Chai"


# Calling the function creates a generator object.
stall = serve_chai()

print("Generator object:")
print(stall)

print("-" * 40)


# -----------------------------
# 2. Using Generator with for Loop
# -----------------------------

# A for loop automatically gets values one by one.

stall = serve_chai()

print("Serving chai using a for loop:")

for cup in stall:
    print(cup)

print("-" * 40)


# -----------------------------
# 3. Normal Function vs Generator
# -----------------------------

# Normal function:
# Creates and returns the full list immediately.

def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]


# Generator function:
# Produces one cup at a time.

def get_chai_generator():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"


chai_list = get_chai_list()
chai_generator = get_chai_generator()

print("Normal function result:")
print(chai_list)

print("Generator function result:")
print(chai_generator)

print("-" * 40)


# -----------------------------
# 4. Using next()
# -----------------------------

# next() manually requests one value at a time.

chai = get_chai_generator()

print("First next call:")
print(next(chai))

print("Second next call:")
print(next(chai))

print("Third next call:")
print(next(chai))

print("-" * 40)


# -----------------------------
# 5. StopIteration
# -----------------------------

# Calling next() after all values are produced
# raises a StopIteration exception.

chai = get_chai_generator()

print(next(chai))
print(next(chai))
print(next(chai))

try:
    print(next(chai))
except StopIteration:
    print("Generator is exhausted. No more values are available.")

print("-" * 40)


# -----------------------------
# 6. Lazy Evaluation
# -----------------------------

# The function body does not fully run
# when the generator object is created.

def prepare_chai():
    print("Preparing first cup")
    yield "Masala Chai"

    print("Preparing second cup")
    yield "Ginger Chai"

    print("Preparing third cup")
    yield "Lemon Chai"


chai_service = prepare_chai()

print("Generator created.")
print("No chai has been prepared yet.")

print(next(chai_service))
print(next(chai_service))
print(next(chai_service))

print("-" * 40)


# -----------------------------
# 7. Generator Is Consumed Once
# -----------------------------

chai = serve_chai()

print("First loop:")

for cup in chai:
    print(cup)

print("Second loop:")

# Nothing will print because the generator
# has already been exhausted.

for cup in chai:
    print(cup)

print("-" * 40)


# -----------------------------
# 8. Create a New Generator to Reuse It
# -----------------------------

chai = serve_chai()

print("New generator object:")

for cup in chai:
    print(cup)

print("-" * 40)


# -----------------------------
# Notes
# -----------------------------

# return:
# Ends a normal function and sends back a result.

# yield:
# Produces one value and pauses the function.

# next():
# Requests the next value from a generator.

# StopIteration:
# Raised when the generator has no more values.

# Lazy evaluation:
# Values are generated only when requested.

# Generator:
# Useful when processing large data
# without loading everything into memory at once.
