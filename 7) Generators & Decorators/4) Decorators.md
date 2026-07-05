# Python Decorators: Basics and Logging Decorator

## Overview

A decorator is a function that adds extra behavior to another function without directly modifying the original function’s code.

Decorators can be used to:

* Log function activity
* Check permissions
* Validate inputs
* Measure execution time
* Cache results
* Handle errors
* Add framework-specific behavior

A decorator acts like a wrapper around another function.

---

# 1. Basic Decorator Structure

A decorator:

1. Accepts a function
2. Defines a wrapper function
3. Runs additional logic
4. Calls the original function
5. Returns the wrapper

Basic structure:

```python
def my_decorator(func):
    def wrapper():
        print("Before the function runs")

        func()

        print("After the function runs")

    return wrapper
```

## Applying the Decorator

Python uses the `@` syntax to apply a decorator.

```python
@my_decorator
def greet():
    print("Hello from the decorated function")
```

Calling:

```python
greet()
```

Output:

```text
Before the function runs
Hello from the decorated function
After the function runs
```

## What the @ Syntax Means

This:

```python
@my_decorator
def greet():
    print("Hello")
```

is equivalent to:

```python
def greet():
    print("Hello")

greet = my_decorator(greet)
```

The original `greet` function is passed into `my_decorator`, and the returned wrapper replaces it.

---

# 2. Decorator Execution Flow

Consider:

```python
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")

    return wrapper
```

The execution flow is:

```text
greet()
   ↓
wrapper()
   ↓
Print "Before"
   ↓
Run original greet()
   ↓
Print "After"
```

The decorator can execute code both before and after the original function.

---

# 3. Preserving Function Metadata

A basic decorator replaces the original function with the wrapper.

This can change metadata such as:

* Function name
* Documentation string
* Type annotations
* Module information

Example:

```python
def my_decorator(func):
    def wrapper():
        func()

    return wrapper


@my_decorator
def greet():
    print("Hello")


print(greet.__name__)
```

Output:

```text
wrapper
```

The original function was named `greet`, but Python now sees the returned `wrapper`.

## Using functools.wraps

Python provides `wraps` inside the built-in `functools` module.

```python
from functools import wraps
```

Use it above the wrapper:

```python
from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper():
        func()

    return wrapper
```

Now:

```python
print(greet.__name__)
```

Output:

```text
greet
```

`@wraps(func)` copies important metadata from the original function to the wrapper.

---

# 4. Functions with Arguments

The first decorator only works with functions that do not accept parameters.

To support different functions, the wrapper should accept:

```python
*args
```

and:

```python
**kwargs
```

Example:

```python
from functools import wraps


def my_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
```

Here:

* `*args` collects positional arguments
* `**kwargs` collects keyword arguments
* The arguments are forwarded to the original function

---

# 5. Returning the Original Result

The wrapper should normally return the result of the original function.

Correct:

```python
def wrapper(*args, **kwargs):
    result = func(*args, **kwargs)
    return result
```

Or more directly:

```python
def wrapper(*args, **kwargs):
    return func(*args, **kwargs)
```

Without `return`, the decorated function may unexpectedly return `None`.

---

# 6. Logging Decorator

A logging decorator can report when a function starts and finishes.

```python
from functools import wraps


def log_activity(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling {func.__name__}")

        result = func(*args, **kwargs)

        print(f"Finished calling {func.__name__}")

        return result

    return wrapper
```

## Applying the Logging Decorator

```python
@log_activity
def brew_chai(chai_type):
    print(f"Brewing {chai_type}")
```

Call the function:

```python
brew_chai("Masala Chai")
```

Output:

```text
Calling brew_chai
Brewing Masala Chai
Finished calling brew_chai
```

---

# 7. Logging Function Arguments

Because the wrapper accepts `*args` and `**kwargs`, the decorated function can receive different kinds of arguments.

```python
@log_activity
def brew_chai(chai_type, milk="No"):
    print(f"Brewing {chai_type}")
    print(f"Milk: {milk}")
```

Calls:

```python
brew_chai("Masala Chai")
brew_chai("Ginger Chai", milk="Yes")
```

The decorator does not need to know the exact function signature.

It forwards all arguments to the original function.

---

# 8. Returning Values Through a Decorator

Decorators should preserve returned values.

```python
@log_activity
def calculate_price(quantity, price):
    return quantity * price
```

Call:

```python
total = calculate_price(3, 40)
print(total)
```

Output:

```text
Calling calculate_price
Finished calling calculate_price
120
```

The wrapper receives the result and returns it to the caller.

---

# 9. Decorators Can Be Reused

The same decorator can be applied to many functions.

```python
@log_activity
def brew_chai(chai_type):
    print(f"Brewing {chai_type}")


@log_activity
def serve_customer(customer_name):
    print(f"Serving {customer_name}")
```

This avoids repeating logging code inside every function.

---

# 10. Multiple Decorators

A function can have more than one decorator.

```python
@decorator_one
@decorator_two
def greet():
    print("Hello")
```

This is equivalent to:

```python
greet = decorator_one(decorator_two(greet))
```

The decorator closest to the function is applied first.

---

# Key Takeaways

* A decorator is a function that wraps another function.
* Decorators add behavior without changing the original function body.
* The `@decorator_name` syntax applies a decorator.
* A decorator normally returns a wrapper function.
* Use `*args` and `**kwargs` to support different function parameters.
* Return the original function’s result from the wrapper.
* Use `functools.wraps` to preserve function metadata.
* Logging is a common decorator use case.
* Decorators are widely used in frameworks such as Django, Flask, and FastAPI.
