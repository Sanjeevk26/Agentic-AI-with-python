# Python Exception Handling
# Topics:
# 1. Common exceptions
# 2. try and except
# 3. Capturing exception objects
# 4. raise
# 5. else
# 6. finally
# 7. Multiple exception handlers
# -------------------------------------------------


# =================================================
# 1. IndexError Example
# =================================================

orders = [
    "Masala Chai",
    "Ginger Chai",
]

try:
    print("Third order:", orders[2])
except IndexError as error:
    print("IndexError handled:", error)

print("Program continues after IndexError.")

print("-" * 50)


# =================================================
# 2. KeyError Example
# =================================================

chai_menu = {
    "masala": 30,
    "ginger": 40,
}

try:
    print("Elaichi price:", chai_menu["elaichi"])
except KeyError as error:
    print("The requested chai does not exist.")
    print("Missing key:", error)

print("Welcome to the chai shop.")

print("-" * 50)


# =================================================
# 3. ZeroDivisionError Example
# =================================================

total_price = 100
number_of_customers = 0

try:
    price_per_customer = (
        total_price / number_of_customers
    )
except ZeroDivisionError as error:
    print("Cannot divide by zero:", error)

print("-" * 50)


# =================================================
# 4. TypeError Example
# =================================================

try:
    total = "50" + 20
except TypeError as error:
    print("TypeError handled:", error)

print("-" * 50)


# =================================================
# 5. NameError Example
# =================================================

try:
    print(undefined_chai_price)
except NameError as error:
    print("NameError handled:", error)

print("-" * 50)


# =================================================
# 6. Basic try, except, else, and finally
# =================================================

def find_chai_price(flavor):
    """
    Find a chai price and demonstrate the full
    exception-handling structure.
    """

    try:
        price = chai_menu[flavor]

    except KeyError:
        print(f"{flavor.title()} chai is unavailable.")

    else:
        print(
            f"{flavor.title()} chai costs "
            f"₹{price}."
        )

    finally:
        print("Menu lookup completed.")


find_chai_price("masala")

print()

find_chai_price("elaichi")

print("-" * 50)


# =================================================
# 7. Raising a Custom ValueError
# =================================================

def serve_chai(flavor):
    """
    Serve a valid flavor or deliberately raise
    a ValueError for an unknown flavor.
    """

    try:
        print(f"Preparing {flavor} chai...")

        if flavor.strip().lower() == "unknown":
            raise ValueError(
                "We do not know that flavor"
            )

    except ValueError as error:
        print("Order error:", error)

    else:
        print(
            f"{flavor.strip().title()} "
            f"chai is served."
        )

    finally:
        print("Next customer, please.")


serve_chai("masala")

print()

serve_chai("unknown")

print("-" * 50)


# =================================================
# 8. Validating More Than One Flavor
# =================================================

AVAILABLE_FLAVORS = {
    "masala",
    "ginger",
    "elaichi",
    "lemon",
}


def validate_and_serve(flavor):
    normalized_flavor = flavor.strip().lower()

    try:
        if normalized_flavor not in AVAILABLE_FLAVORS:
            raise ValueError(
                f"{flavor} is not available"
            )

    except ValueError as error:
        print("Could not serve order:", error)

    else:
        print(
            f"Serving "
            f"{normalized_flavor.title()} Chai"
        )

    finally:
        print("Order processing finished.")


validate_and_serve("Ginger")

print()

validate_and_serve("Chocolate")

print("-" * 50)


# =================================================
# 9. Multiple except Blocks
# =================================================

def calculate_order_total(
    price_per_cup,
    quantity_text,
):
    """
    Handle invalid numbers and zero quantity
    using different except blocks.
    """

    try:
        quantity = int(quantity_text)

        if quantity == 0:
            average_price = price_per_cup / quantity
        else:
            average_price = price_per_cup
            total = price_per_cup * quantity

    except ValueError:
        print("Quantity must contain a valid integer.")
        return None

    except ZeroDivisionError:
        print("Quantity cannot be zero.")
        return None

    else:
        print("Average price:", average_price)
        return total

    finally:
        print("Calculation attempt completed.")


result = calculate_order_total(40, "3")
print("Total:", result)

print()

calculate_order_total(40, "three")

print()

calculate_order_total(40, "0")

print("-" * 50)


# =================================================
# 10. Handling Multiple Exceptions Together
# =================================================

def divide_order_cost(cost_text, customers_text):
    try:
        cost = float(cost_text)
        customers = int(customers_text)

        return cost / customers

    except (
        ValueError,
        ZeroDivisionError,
    ) as error:
        print("Invalid calculation:", error)
        return None


print(
    "Valid division:",
    divide_order_cost("100", "4"),
)

print(
    "Invalid number:",
    divide_order_cost("chai", "4"),
)

print(
    "Zero customers:",
    divide_order_cost("100", "0"),
)

print("-" * 50)


# =================================================
# 11. Specific and General Exception Handlers
# =================================================

def process_menu_request(menu, flavor):
    try:
        price = menu[flavor]
        quantity = int("2")

    except KeyError:
        print("The flavor is missing from the menu.")

    except ValueError:
        print("The quantity is invalid.")

    except Exception as error:
        # General fallback should come after
        # specific handlers.
        print("Unexpected error:", error)

    else:
        print(
            f"Order total: ₹{price * quantity}"
        )


process_menu_request(chai_menu, "masala")
process_menu_request(chai_menu, "lemon")

print("-" * 50)


# =================================================
# 12. finally for Resource Cleanup
# =================================================

def simulate_resource_usage(should_fail):
    resource_open = False

    try:
        print("Opening resource...")
        resource_open = True

        if should_fail:
            raise RuntimeError(
                "Resource operation failed"
            )

        print("Using resource successfully.")

    except RuntimeError as error:
        print("Operation error:", error)

    finally:
        if resource_open:
            print("Closing resource.")

        print("Cleanup completed.")


simulate_resource_usage(False)

print()

simulate_resource_usage(True)

print("-" * 50)


# =================================================
# 13. Using dict.get() for an Expected Missing Key
# =================================================

requested_flavor = "lemon"

price = chai_menu.get(requested_flavor)

if price is None:
    print(
        f"{requested_flavor.title()} "
        f"chai is not on the menu."
    )
else:
    print("Price:", price)

print("-" * 50)


# =================================================
# Notes
# =================================================

# Basic syntax:
#
# try:
#     risky_operation()
# except SpecificError as error:
#     handle_error(error)
# else:
#     handle_success()
# finally:
#     clean_up()
#
#
# try:
# Contains code that may raise an exception.
#
#
# except:
# Handles a matching exception.
#
#
# else:
# Runs only when the try block completes
# without raising an exception.
#
#
# finally:
# Runs whether the try block succeeds or fails.
#
#
# raise:
# Creates an exception deliberately.
#
# Example:
#
# raise ValueError("Invalid chai flavor")
#
#
# Common exceptions:
# - IndexError
# - KeyError
# - ZeroDivisionError
# - TypeError
# - NameError
# - ValueError
#
#
# Best practices:
# - Catch specific exceptions
# - Keep try blocks small
# - Use clear error messages
# - Avoid bare except
# - Use finally for cleanup
# - Do not silently ignore unexpected errors
