# Python Exception Handling
# Topics:
# 1. Multiple except blocks
# 2. KeyError
# 3. ValueError
# 4. TypeError
# 5. Numeric conversion
# 6. raise
# 7. Built-in and custom exceptions
# -------------------------------------------------


# =================================================
# 1. Chai Menu
# =================================================

CHAI_MENU = {
    "masala": 20,
    "ginger": 30,
    "elaichi": 35,
}


# =================================================
# 2. Basic Multiple Exception Handling
# =================================================

def process_order(item, quantity):
    """
    Process an order while handling different
    possible exceptions separately.
    """

    normalized_item = item.strip().lower()

    try:
        # Can raise KeyError.
        price = CHAI_MENU[normalized_item]

        # Can raise ValueError or TypeError.
        numeric_quantity = int(quantity)

        if numeric_quantity <= 0:
            raise ValueError(
                "Quantity must be greater than zero"
            )

        total = price * numeric_quantity

    except KeyError:
        print(
            f"Sorry, {normalized_item.title()} "
            f"Chai is not on the menu."
        )
        return None

    except ValueError as error:
        print("Invalid quantity:", error)
        return None

    except TypeError as error:
        print("Invalid input type:", error)
        return None

    else:
        print(
            f"{numeric_quantity} cup(s) of "
            f"{normalized_item.title()} Chai"
        )
        print(f"Total cost: ₹{total}")

        return total

    finally:
        print("Order processing completed.")


print("Valid order:")
process_order("masala", 2)

print("-" * 50)

print("Missing menu item:")
process_order("chocolate", 2)

print("-" * 50)

print("Invalid quantity text:")
process_order("masala", "two")

print("-" * 50)

print("Zero quantity:")
process_order("ginger", 0)

print("-" * 50)


# =================================================
# 3. Why String Multiplication Is Dangerous Here
# =================================================

price = 20
quantity_text = "2"

print("Integer multiplied by a string:")
print(price * quantity_text)

# Output is the string "2" repeated 20 times.
# It is not numeric multiplication.

numeric_quantity = int(quantity_text)

print("Integer multiplied by converted quantity:")
print(price * numeric_quantity)

print("-" * 50)


# =================================================
# 4. Handling Multiple Exceptions Together
# =================================================

def calculate_share(total_text, people_text):
    """
    Handle ValueError and ZeroDivisionError
    using the same except block.
    """

    try:
        total = float(total_text)
        people = int(people_text)

        return total / people

    except (
        ValueError,
        ZeroDivisionError,
    ) as error:
        print("Could not calculate share:", error)
        return None


print("Valid share:")
print(calculate_share("120", "4"))

print()

print("Invalid total:")
print(calculate_share("chai", "4"))

print()

print("Zero people:")
print(calculate_share("120", "0"))

print("-" * 50)


# =================================================
# 5. Raising a Built-in Exception
# =================================================

SUPPORTED_FLAVORS = {
    "masala",
    "ginger",
    "elaichi",
}


def brew_chai(flavor):
    """
    Raise ValueError when the flavor is unsupported.
    """

    normalized_flavor = flavor.strip().lower()

    if normalized_flavor not in SUPPORTED_FLAVORS:
        raise ValueError(
            f"Unsupported chai flavor: {flavor}"
        )

    print(
        f"Brewing "
        f"{normalized_flavor.title()} Chai..."
    )


print("Supported flavor:")
brew_chai("ginger")

print("-" * 50)

print("Unsupported flavor:")

try:
    brew_chai("chocolate")
except ValueError as error:
    print("Order rejected:", error)

print("-" * 50)


# =================================================
# 6. Raising an Error for a Business Rule
# =================================================

def calculate_total(price, quantity):
    """
    Reject zero and negative quantities.
    """

    if not isinstance(price, (int, float)):
        raise TypeError(
            "Price must be a number"
        )

    if not isinstance(quantity, int):
        raise TypeError(
            "Quantity must be an integer"
        )

    if quantity <= 0:
        raise ValueError(
            "Quantity must be greater than zero"
        )

    return price * quantity


try:
    total = calculate_total(30, 3)
except (TypeError, ValueError) as error:
    print("Calculation error:", error)
else:
    print("Calculated total:", total)

print("-" * 50)


# =================================================
# 7. A Real Custom Exception Class
# =================================================

class UnsupportedChaiError(Exception):
    """
    Raised when an unsupported chai flavor
    is requested.
    """

    pass


def brew_with_custom_exception(flavor):
    normalized_flavor = flavor.strip().lower()

    if normalized_flavor not in SUPPORTED_FLAVORS:
        raise UnsupportedChaiError(
            f"{flavor!r} is not supported"
        )

    return (
        f"Brewing "
        f"{normalized_flavor.title()} Chai"
    )


try:
    print(
        brew_with_custom_exception(
            "vanilla"
        )
    )
except UnsupportedChaiError as error:
    print("Custom exception handled:", error)

print("-" * 50)


# =================================================
# 8. Specific Handlers Before General Handlers
# =================================================

def demonstrate_handler_order(value):
    try:
        if value == "missing":
            raise KeyError("masala")

        if value == "invalid":
            raise ValueError(
                "Invalid order value"
            )

        if value == "unexpected":
            raise RuntimeError(
                "Unexpected processing problem"
            )

        print("Order accepted.")

    except KeyError as error:
        print("Missing key:", error)

    except ValueError as error:
        print("Invalid value:", error)

    except Exception as error:
        print("Unexpected error:", error)


demonstrate_handler_order("missing")
demonstrate_handler_order("invalid")
demonstrate_handler_order("unexpected")
demonstrate_handler_order("valid")

print("-" * 50)


# =================================================
# 9. Exception Handling with Return Values
# =================================================

def get_order_total(item, quantity):
    """
    Return the total when successful.
    Return None when validation fails.
    """

    try:
        normalized_item = item.strip().lower()
        price = CHAI_MENU[normalized_item]
        quantity = int(quantity)

        if quantity <= 0:
            raise ValueError(
                "Quantity must be positive"
            )

    except AttributeError:
        print("Item must be a string.")
        return None

    except KeyError:
        print("Requested chai is unavailable.")
        return None

    except (TypeError, ValueError) as error:
        print("Invalid quantity:", error)
        return None

    return price * quantity


order_total = get_order_total("elaichi", "3")

if order_total is not None:
    print("Order total:", order_total)

print("-" * 50)


# =================================================
# 10. Processing Several Orders
# =================================================

orders = [
    ("masala", 2),
    ("ginger", "3"),
    ("chocolate", 1),
    ("elaichi", "many"),
    ("masala", -2),
]


for item, quantity in orders:
    print(
        f"Processing: item={item!r}, "
        f"quantity={quantity!r}"
    )

    process_order(item, quantity)

    print()


# =================================================
# Notes
# =================================================

# Multiple handlers:
#
# try:
#     risky_operation()
#
# except KeyError:
#     handle_missing_key()
#
# except ValueError:
#     handle_invalid_value()
#
# except TypeError:
#     handle_invalid_type()
#
#
# Handle several types together:
#
# except (ValueError, TypeError) as error:
#     print(error)
#
#
# Raise a built-in exception:
#
# raise ValueError("Invalid quantity")
#
#
# Define a custom exception:
#
# class UnsupportedChaiError(Exception):
#     pass
#
#
# Raise a custom exception:
#
# raise UnsupportedChaiError(
#     "Unsupported chai flavor"
# )
#
#
# Important:
# Only one active exception normally propagates
# through a given execution path at a time.
#
#
# String repetition:
#
# 20 * "2"
#
# repeats the string instead of performing
# numeric multiplication.
#
#
# Convert numeric input first:
#
# quantity = int(quantity_text)
#
#
# Handler order:
# - Specific exceptions first
# - General Exception handler last
