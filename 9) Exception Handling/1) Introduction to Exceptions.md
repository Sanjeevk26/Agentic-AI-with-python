# Python Exception Handling: try, except, else, finally, and raise

## Overview

Errors can occur while a Python program is running.

Examples include:

* Accessing a missing list index
* Accessing a missing dictionary key
* Dividing by zero
* Using incompatible data types
* Referring to an undefined variable
* Opening a missing file
* Receiving invalid input

Exception handling allows the program to respond gracefully instead of stopping immediately.

---

# 1. What Is an Exception?

An exception is an error that occurs while a program is running.

Example:

```python
orders = ["Masala Chai", "Ginger Chai"]

print(orders[2])
```

The list contains only two values:

```text
Index 0: Masala Chai
Index 1: Ginger Chai
```

Accessing index `2` raises:

```text
IndexError: list index out of range
```

If the exception is not handled, the program stops at that line.

---

# 2. Common Python Exceptions

## IndexError

Raised when a sequence index does not exist.

```python
orders = ["Masala Chai"]

print(orders[5])
```

## KeyError

Raised when a dictionary key does not exist.

```python
chai_menu = {
    "masala": 30,
    "ginger": 40,
}

print(chai_menu["elaichi"])
```

## ZeroDivisionError

Raised when dividing by zero.

```python
result = 10 / 0
```

## TypeError

Raised when an operation receives an inappropriate type.

```python
result = "10" + 5
```

## NameError

Raised when a name has not been defined.

```python
print(chai_price)
```

## ValueError

Raised when a value has the correct general type but an invalid value.

```python
number = int("chai")
```

---

# 3. Basic try and except

Code that may fail is placed inside a `try` block.

The matching error is handled inside an `except` block.

```python
chai_menu = {
    "masala": 30,
    "ginger": 40,
}

try:
    print(chai_menu["elaichi"])
except KeyError:
    print("The requested chai does not exist")
```

Output:

```text
The requested chai does not exist
```

The program continues instead of crashing.

---

# 4. Program Flow After Handling an Exception

```python
try:
    print(chai_menu["elaichi"])
except KeyError:
    print("The requested chai does not exist")

print("Welcome to the chai shop")
```

Output:

```text
The requested chai does not exist
Welcome to the chai shop
```

Because the exception was handled, the final statement still runs.

---

# 5. Capturing the Exception Object

The exception can be stored in a variable.

```python
try:
    print(chai_menu["elaichi"])
except KeyError as error:
    print("Missing key:", error)
```

The name `error` is only a variable.

Common short names include:

```python
error
err
exc
```

Using `e` also works, although descriptive names are often clearer.

---

# 6. Catch Specific Exceptions

It is normally better to catch the exact exception expected.

Preferred:

```python
try:
    price = chai_menu["elaichi"]
except KeyError:
    print("Chai is not available")
```

Less preferred:

```python
try:
    price = chai_menu["elaichi"]
except Exception:
    print("Something went wrong")
```

Catching specific exceptions:

* Makes errors easier to understand
* Avoids hiding unrelated programming bugs
* Allows different responses for different failures

---

# 7. Raising an Exception

The `raise` keyword creates an exception deliberately.

```python
flavor = "unknown"

if flavor == "unknown":
    raise ValueError("We do not know that flavor")
```

This is useful when:

* Input is invalid
* A business rule is violated
* Required data is missing
* An operation cannot continue safely

---

# 8. Raising and Handling an Exception

```python
def serve_chai(flavor):
    try:
        if flavor == "unknown":
            raise ValueError("We do not know that flavor")

        print(f"Preparing {flavor} chai")

    except ValueError as error:
        print("Order error:", error)
```

The exception is created with `raise` and handled by `except`.

---

# 9. The else Block

The `else` block runs only when the `try` block finishes without an exception.

```python
try:
    price = chai_menu["masala"]
except KeyError:
    print("Chai is unavailable")
else:
    print("Price:", price)
```

Output:

```text
Price: 30
```

If a `KeyError` occurs, the `else` block does not run.

## Why Use else?

This is valid:

```python
try:
    price = chai_menu["masala"]
    print("Price:", price)
except KeyError:
    print("Chai is unavailable")
```

A clearer version is:

```python
try:
    price = chai_menu["masala"]
except KeyError:
    print("Chai is unavailable")
else:
    print("Price:", price)
```

Only the sensitive operation remains inside `try`.

---

# 10. The finally Block

The `finally` block runs whether an exception occurs or not.

```python
try:
    price = chai_menu["masala"]
except KeyError:
    print("Chai is unavailable")
finally:
    print("Next customer, please")
```

`finally` is commonly used for cleanup operations such as:

* Closing files
* Closing database connections
* Releasing locks
* Closing network connections
* Cleaning temporary resources

---

# 11. Complete Exception Flow

```python
def serve_chai(flavor):
    try:
        print(f"Preparing {flavor} chai...")

        if flavor == "unknown":
            raise ValueError("We do not know that flavor")

    except ValueError as error:
        print("Order error:", error)

    else:
        print(f"{flavor.title()} chai is served")

    finally:
        print("Next customer, please")
```

## Valid Flavor

```python
serve_chai("masala")
```

Output:

```text
Preparing masala chai...
Masala chai is served
Next customer, please
```

Execution flow:

1. `try` runs
2. No exception occurs
3. `else` runs
4. `finally` runs

## Invalid Flavor

```python
serve_chai("unknown")
```

Output:

```text
Preparing unknown chai...
Order error: We do not know that flavor
Next customer, please
```

Execution flow:

1. `try` begins
2. `ValueError` is raised
3. Remaining code in `try` is skipped
4. Matching `except` runs
5. `else` is skipped
6. `finally` runs

---

# 12. try, except, else, and finally Structure

```python
try:
    # Code that may raise an exception
    risky_operation()

except SpecificError as error:
    # Handle the expected exception
    handle_error(error)

else:
    # Runs only when no exception occurred
    process_success()

finally:
    # Runs whether the operation succeeded or failed
    clean_up()
```

Not every block is mandatory.

Valid combinations include:

```python
try:
    ...
except SomeError:
    ...
```

```python
try:
    ...
finally:
    ...
```

```python
try:
    ...
except SomeError:
    ...
else:
    ...
finally:
    ...
```

---

# 13. Multiple except Blocks

Different exceptions can be handled separately.

```python
try:
    quantity = int(input("Enter quantity: "))
    price_per_cup = 100 / quantity

except ValueError:
    print("Quantity must be a number")

except ZeroDivisionError:
    print("Quantity cannot be zero")
```

This produces a more accurate response for each problem.

---

# 14. Handling Multiple Exceptions Together

Multiple exception types can also share one handler.

```python
try:
    quantity = int(user_input)
    result = 100 / quantity

except (ValueError, ZeroDivisionError) as error:
    print("Invalid quantity:", error)
```

Use this when the same response is appropriate for all listed exceptions.

---

# 15. Exception Hierarchy

Most normal Python exceptions inherit from `Exception`.

For example:

```text
BaseException
└── Exception
    ├── ValueError
    ├── TypeError
    ├── KeyError
    ├── IndexError
    └── ZeroDivisionError
```

A general handler can be written as:

```python
except Exception as error:
```

However, it should usually appear after specific exception handlers.

```python
try:
    risky_operation()

except KeyError:
    print("Missing key")

except ValueError:
    print("Invalid value")

except Exception as error:
    print("Unexpected error:", error)
```

Python checks `except` blocks from top to bottom.

---

# 16. Avoid Bare except

This catches almost everything:

```python
try:
    risky_operation()
except:
    print("Something went wrong")
```

A bare `except` can also catch exceptions used to stop or interrupt a program.

Prefer:

```python
except Exception as error:
```

Even better, catch the specific expected exception.

---

# 17. Keep try Blocks Small

Avoid placing unrelated code inside one large `try` block.

Less clear:

```python
try:
    price = chai_menu[flavor]
    quantity = int(user_quantity)
    total = price * quantity
    print(total)
except Exception:
    print("Something failed")
```

Clearer:

```python
try:
    price = chai_menu[flavor]
except KeyError:
    print("Flavor is unavailable")
    return

try:
    quantity = int(user_quantity)
except ValueError:
    print("Quantity must be a number")
    return

total = price * quantity
print(total)
```

Small `try` blocks make it easier to identify which operation failed.

---

# 18. Exceptions vs Normal Conditions

Exceptions should generally represent exceptional or invalid situations.

For expected dictionary lookups, alternatives may be more suitable.

Using exception handling:

```python
try:
    price = chai_menu[flavor]
except KeyError:
    price = None
```

Using `dict.get()`:

```python
price = chai_menu.get(flavor)
```

Both approaches are valid. The best choice depends on whether the missing value is expected or exceptional.

---

# Key Takeaways

* Exceptions are runtime errors.
* Unhandled exceptions stop normal program execution.
* Use `try` for code that may fail.
* Use `except` to handle expected exceptions.
* Catch specific exception types whenever possible.
* Use `as error` to inspect the exception object.
* Use `raise` to create an exception deliberately.
* `else` runs only when no exception occurs.
* `finally` runs whether the operation succeeds or fails.
* `finally` is commonly used for cleanup.
* Code after the line that raises an exception inside `try` is skipped.
* Multiple exceptions can be handled separately or together.
* Keep `try` blocks focused and small.
* Avoid using a bare `except`.
