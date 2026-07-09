# Python Exception Handling: Multiple Exceptions and raise

## Overview

A single operation may fail for different reasons.

For example, processing a chai order may fail because:

* The requested chai is not on the menu
* The quantity is not a valid number
* The quantity is zero or negative
* The input is missing
* A business rule is violated

Python allows different exception types to be handled using multiple `except` blocks.

A program does not normally raise several exceptions simultaneously from one statement. Instead, different inputs or operations may raise different exception types, and Python runs the first matching handler.

---

# 1. Handling Multiple Possible Exceptions

Consider a chai menu:

```python
chai_menu = {
    "masala": 20,
}
```

A function receives:

* The requested item
* The required quantity

```python
def process_order(item, quantity):
    price = chai_menu[item]
    cost = price * quantity

    print(f"Total cost is ₹{cost}")
```

Different problems can occur:

```python
process_order("ginger", 2)
```

This raises `KeyError` because `"ginger"` is not in the dictionary.

Another input may also be invalid:

```python
process_order("masala", "two")
```

However, multiplying an integer by a string does not raise `TypeError`:

```python
20 * "two"
```

It repeats the string 20 times.

Therefore, the quantity should be explicitly converted or validated before multiplication.

---

# 2. Multiple except Blocks

```python
def process_order(item, quantity):
    try:
        price = chai_menu[item]
        numeric_quantity = int(quantity)
        cost = price * numeric_quantity

    except KeyError:
        print("Sorry, that chai is not on the menu.")

    except ValueError:
        print("Quantity must be a valid integer.")

    else:
        print(f"Total cost is ₹{cost}")
```

Different handlers respond to different failures.

## Missing Menu Item

```python
process_order("ginger", 2)
```

Output:

```text
Sorry, that chai is not on the menu.
```

## Invalid Quantity

```python
process_order("masala", "two")
```

Output:

```text
Quantity must be a valid integer.
```

## Valid Order

```python
process_order("masala", 2)
```

Output:

```text
Total cost is ₹40
```

---

# 3. Why int() Is Important

This does not produce a numeric multiplication:

```python
20 * "2"
```

Instead, Python repeats the string:

```text
22222222222222222222
```

This is valid Python behaviour called sequence repetition.

To perform numeric multiplication, convert the value first:

```python
quantity = int("2")
cost = 20 * quantity
```

Output:

```text
40
```

Invalid text causes `int()` to raise `ValueError`:

```python
int("two")
```

Output:

```text
ValueError
```

---

# 4. TypeError vs ValueError

These exceptions represent different problems.

## TypeError

Raised when an operation receives an inappropriate type.

```python
20 + "2"
```

Output:

```text
TypeError
```

## ValueError

Raised when the type is acceptable, but its value cannot be processed.

```python
int("two")
```

The value is a string, which `int()` accepts as input, but `"two"` is not a valid numeric string.

Therefore, Python raises `ValueError`.

---

# 5. Validating Quantity

Converting the quantity to an integer is not enough.

Values such as zero or negative quantities may also be invalid.

```python
def process_order(item, quantity):
    try:
        price = chai_menu[item]
        numeric_quantity = int(quantity)

        if numeric_quantity <= 0:
            raise ValueError(
                "Quantity must be greater than zero."
            )

        cost = price * numeric_quantity

    except KeyError:
        print("Sorry, that chai is not on the menu.")

    except ValueError as error:
        print("Invalid quantity:", error)

    else:
        print(f"Total cost is ₹{cost}")
```

The `raise` keyword creates an exception deliberately when a business rule is violated.

---

# 6. Raising Exceptions Deliberately

Python provides the `raise` keyword:

```python
raise ValueError("Invalid value")
```

Example:

```python
def brew_chai(flavor):
    supported_flavors = {
        "masala",
        "ginger",
        "elaichi",
    }

    if flavor not in supported_flavors:
        raise ValueError(
            f"Unsupported chai flavor: {flavor}"
        )

    print(f"Brewing {flavor} chai")
```

Calling:

```python
brew_chai("chocolate")
```

raises:

```text
ValueError: Unsupported chai flavor: chocolate
```

---

# 7. Why Raise an Exception?

Raising an exception is useful when:

* Input violates a rule
* Required data is missing
* An operation cannot safely continue
* A caller should decide how to handle the failure
* Silent failure would produce incorrect results

Example:

```python
def calculate_total(price, quantity):
    if quantity <= 0:
        raise ValueError(
            "Quantity must be greater than zero"
        )

    return price * quantity
```

The function refuses to return an invalid total.

---

# 8. Handling a Raised Exception

A caller can handle an exception raised by another function.

```python
try:
    brew_chai("chocolate")
except ValueError as error:
    print("Order rejected:", error)
```

Output:

```text
Order rejected: Unsupported chai flavor: chocolate
```

This separates responsibilities:

* `brew_chai()` validates the flavor
* The caller decides how to display or log the error

---

# 9. Raising Built-in Exceptions vs Custom Exceptions

This example:

```python
raise ValueError("Unsupported chai flavor")
```

raises a built-in exception with a custom message.

It is not yet a new custom exception type.

A custom exception type is created by defining a class:

```python
class UnsupportedChaiError(Exception):
    pass
```

It can then be raised:

```python
raise UnsupportedChaiError(
    "Unsupported chai flavor"
)
```

Custom exception classes are useful when callers need to distinguish application-specific failures from general built-in errors.

---

# 10. Handling Several Exception Types Separately

```python
def process_order(menu, item, quantity):
    try:
        price = menu[item]
        quantity = int(quantity)

        if quantity <= 0:
            raise ValueError(
                "Quantity must be greater than zero"
            )

        total = price * quantity

    except KeyError:
        print(f"{item!r} is not available.")

    except ValueError as error:
        print("Invalid quantity:", error)

    except TypeError as error:
        print("Invalid input type:", error)

    else:
        print(f"Total cost: ₹{total}")
```

Python checks the handlers from top to bottom and executes the first compatible one.

---

# 11. Handling Several Exception Types Together

When different exceptions require the same response, they can share one handler.

```python
try:
    quantity = int(user_input)
    result = 100 / quantity

except (ValueError, ZeroDivisionError) as error:
    print("Invalid quantity:", error)
```

This handles either:

* `ValueError`
* `ZeroDivisionError`

Use separate handlers when each error needs a different response.

---

# 12. Exception Handler Order

Specific exception handlers should usually come before general ones.

Correct:

```python
try:
    process_order()

except KeyError:
    print("Missing menu item")

except ValueError:
    print("Invalid value")

except Exception as error:
    print("Unexpected error:", error)
```

Incorrect ordering:

```python
try:
    process_order()

except Exception:
    print("Something failed")

except KeyError:
    print("Missing menu item")
```

Because `KeyError` inherits from `Exception`, the general handler catches it first. The specific `KeyError` handler can never run.

---

# 13. Returning Values from Exception-Based Functions

A function can return the total when successful and `None` when unsuccessful.

```python
def process_order(item, quantity):
    try:
        price = chai_menu[item]
        quantity = int(quantity)

        if quantity <= 0:
            raise ValueError(
                "Quantity must be positive"
            )

    except KeyError:
        print("Chai not found.")
        return None

    except ValueError as error:
        print("Invalid quantity:", error)
        return None

    return price * quantity
```

Usage:

```python
total = process_order("masala", 3)

if total is not None:
    print("Total:", total)
```

---

# 14. Prefer Clear Validation

It is often better to validate expected conditions directly.

```python
if item not in chai_menu:
    print("Chai not available")
```

Exception handling is especially useful when:

* The operation itself naturally raises an exception
* Failure is uncommon
* Several nested operations may fail
* The caller needs to control error handling

Use normal conditions for ordinary, expected decisions.

---

# 15. Complete Example

```python
chai_menu = {
    "masala": 20,
    "ginger": 30,
    "elaichi": 35,
}


def process_order(item, quantity):
    normalized_item = item.strip().lower()

    try:
        price = chai_menu[normalized_item]
        quantity = int(quantity)

        if quantity <= 0:
            raise ValueError(
                "Quantity must be greater than zero"
            )

        total = price * quantity

    except KeyError:
        print(
            f"{normalized_item.title()} chai "
            f"is not on the menu."
        )

    except ValueError as error:
        print("Invalid quantity:", error)

    else:
        print(
            f"{quantity} cup(s) of "
            f"{normalized_item.title()} Chai"
        )
        print(f"Total cost: ₹{total}")

    finally:
        print("Order processing completed.")
```

---

# Key Takeaways

* A block of code may produce different exception types.
* Normally, only one exception propagates at a time.
* Use multiple `except` blocks for different errors.
* Python runs the first matching exception handler.
* Convert numeric text using `int()` before arithmetic.
* Multiplying a string by an integer repeats the string.
* Invalid numeric text passed to `int()` raises `ValueError`.
* Use `raise` to report invalid application conditions.
* A custom message on `ValueError` is not a custom exception type.
* Custom exception classes inherit from `Exception`.
* Put specific exception handlers before general handlers.
* Handle related exceptions together only when they require the same response.
