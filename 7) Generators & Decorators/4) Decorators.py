# Python Decorators Demo
# Topics:
# 1. Basic decorators
# 2. Code before and after a function
# 3. functools.wraps
# 4. *args and **kwargs
# 5. Returning function results
# 6. Logging decorator
# -------------------------------------------------

from functools import wraps


# =================================================
# 1. Basic Decorator
# =================================================

def my_decorator(func):
    """
    Add behavior before and after another function.
    """

    @wraps(func)
    def wrapper():
        print("Before the function runs")

        func()

        print("After the function runs")

    return wrapper


@my_decorator
def greet():
    print("Hello from the decorators class")


greet()

print("-" * 50)


# =================================================
# 2. Preserving Function Metadata
# =================================================

# Because @wraps(func) is used,
# the original function name is preserved.

print("Function name:", greet.__name__)
print("Function documentation:", greet.__doc__)

print("-" * 50)


# =================================================
# 3. Decorator Without @ Syntax
# =================================================

def simple_decorator(func):
    @wraps(func)
    def wrapper():
        print("Starting the function")

        func()

        print("Function completed")

    return wrapper


def welcome():
    print("Welcome to Python decorators")


# This is equivalent to using @simple_decorator.
welcome = simple_decorator(welcome)

welcome()

print("-" * 50)


# =================================================
# 4. Reusable Logging Decorator
# =================================================

def log_activity(func):
    """
    Log when a function starts and finishes.

    *args receives positional arguments.
    **kwargs receives keyword arguments.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")

        result = func(*args, **kwargs)

        print(f"Finished calling {func.__name__}")

        return result

    return wrapper


# =================================================
# 5. Decorated Function with One Argument
# =================================================

@log_activity
def brew_chai(chai_type):
    print(f"Brewing {chai_type}")


brew_chai("Masala Chai")

print("-" * 50)


# =================================================
# 6. Positional and Keyword Arguments
# =================================================

@log_activity
def prepare_chai(chai_type, milk="No", sugar="Medium"):
    print(f"Chai type: {chai_type}")
    print(f"Milk: {milk}")
    print(f"Sugar: {sugar}")


prepare_chai("Ginger Chai")

print()

prepare_chai(
    "Green Tea",
    milk="No",
    sugar="Low"
)

print("-" * 50)


# =================================================
# 7. Returning a Result Through a Decorator
# =================================================

@log_activity
def calculate_order_total(quantity, price_per_cup):
    return quantity * price_per_cup


total = calculate_order_total(3, 40)

print("Order total:", total)

print("-" * 50)


# =================================================
# 8. Applying One Decorator to Many Functions
# =================================================

@log_activity
def serve_customer(customer_name):
    print(f"Serving {customer_name}")


@log_activity
def close_stall():
    print("Closing the chai stall")


serve_customer("Aarav")
close_stall()

print("-" * 50)


# =================================================
# 9. Logging Arguments
# =================================================

def detailed_log(func):
    """
    Log function name, arguments, and returned result.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Function: {func.__name__}")
        print(f"Positional arguments: {args}")
        print(f"Keyword arguments: {kwargs}")

        result = func(*args, **kwargs)

        print(f"Returned result: {result}")

        return result

    return wrapper


@detailed_log
def chai_bill(chai_type, cups, price_per_cup=40):
    total_price = cups * price_per_cup

    return {
        "chai_type": chai_type,
        "cups": cups,
        "total_price": total_price,
    }


bill = chai_bill(
    "Masala Chai",
    4,
    price_per_cup=50
)

print("Final bill:", bill)

print("-" * 50)


# =================================================
# Notes
# =================================================

# Decorator:
# A function that accepts another function
# and returns a modified or wrapped function.
#
#
# Basic syntax:
#
# def decorator(func):
#     @wraps(func)
#     def wrapper(*args, **kwargs):
#         result = func(*args, **kwargs)
#         return result
#
#     return wrapper
#
#
# Applying a decorator:
#
# @decorator
# def function():
#     pass
#
#
# Equivalent form:
#
# function = decorator(function)
#
#
# functools.wraps:
# Preserves metadata such as:
# - Function name
# - Documentation string
# - Module
# - Type annotations
#
#
# *args:
# Collects positional arguments.
#
#
# **kwargs:
# Collects keyword arguments.
#
#
# Important:
# Always return the original function result
# when callers expect the decorated function
# to return a value.
