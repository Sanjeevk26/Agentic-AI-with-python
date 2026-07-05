# Python Generators: yield from and close()

## Overview

This lesson covers two additional generator concepts:

* `yield from`
* Closing a generator with `close()`

`yield from` delegates value generation to another generator or iterable.

`close()` stops a generator before it naturally finishes and allows cleanup logic to run.

---

# 1. yield from

Sometimes one generator needs to produce values from another generator.

Instead of manually looping through the second generator, Python provides:

```python
yield from iterable
```

## Example: Separate Chai Menus

```python
def local_chai():
    yield "Masala Chai"
    yield "Ginger Chai"


def imported_chai():
    yield "Matcha"
    yield "Oolong Chai"
```

We can combine both generators into one complete menu:

```python
def full_menu():
    yield from local_chai()
    yield from imported_chai()
```

## Using the Combined Generator

```python
for chai in full_menu():
    print(chai)
```

Output:

```text
Masala Chai
Ginger Chai
Matcha
Oolong Chai
```

## What yield from Does

This:

```python
def full_menu():
    yield from local_chai()
```

is similar to:

```python
def full_menu():
    for chai in local_chai():
        yield chai
```

`yield from` provides a shorter and cleaner way to delegate work to another iterable.

## Important: Call the Generator Function

Use parentheses when delegating to a generator function:

```python
yield from local_chai()
```

Without parentheses:

```python
yield from local_chai
```

Python receives the function itself instead of the generator object returned by calling it.

---

# 2. Closing a Generator

A generator normally stops when:

* It reaches the end of its function
* It executes `return`
* Its generator object is cleaned up
* It is explicitly closed

A generator can be explicitly stopped using:

```python
generator.close()
```

## Example: Chai Stall Generator

```python
def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
            print(f"Preparing {order}")
    finally:
        print("Stall closed. Cleaning up resources.")
```

## Starting the Generator

```python
stall = chai_stall()

message = next(stall)
print(message)
```

Output:

```text
Waiting for chai order
```

The generator is now paused at `yield`.

## Sending Orders

```python
print(stall.send("Masala Chai"))
print(stall.send("Ginger Chai"))
```

Output:

```text
Preparing Masala Chai
Waiting for chai order
Preparing Ginger Chai
Waiting for chai order
```

Each call to `send()`:

1. Sends an order into the paused `yield`
2. Continues the generator
3. Prints the order
4. Reaches the next `yield`
5. Returns the waiting message
6. Pauses again

## Closing the Generator

```python
stall.close()
```

Output:

```text
Stall closed. Cleaning up resources.
```

Calling `close()` raises a special `GeneratorExit` exception inside the generator.

This allows cleanup code to run before the generator stops.

---

# 3. GeneratorExit

`GeneratorExit` is raised internally when:

```python
generator.close()
```

is called.

It can be handled explicitly:

```python
def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
            print(f"Preparing {order}")
    except GeneratorExit:
        print("Stall closed. No more chai.")
```

However, `finally` is generally preferred for cleanup:

```python
def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
            print(f"Preparing {order}")
    finally:
        print("Cleaning up the chai stall.")
```

The `finally` block runs whenever the generator is closed or finishes through an exception.

---

# 4. Why Generator Cleanup Matters

Generators may manage resources such as:

* Database connections
* Open files
* Network connections
* Streaming responses
* Locks
* Temporary resources

Cleanup logic ensures these resources are released properly.

Example:

```python
def database_session():
    connection = open_connection()

    try:
        yield connection
    finally:
        connection.close()
```

This pattern is commonly used in web frameworks and database applications.

---

# Generator Keyword Summary

| Feature         | Purpose                                  |
| --------------- | ---------------------------------------- |
| `yield`         | Produces a value and pauses the function |
| `next()`        | Requests the next generated value        |
| `send(value)`   | Sends a value into a paused generator    |
| `yield from`    | Delegates generation to another iterable |
| `close()`       | Stops the generator                      |
| `GeneratorExit` | Signals that the generator is closing    |
| `finally`       | Runs cleanup logic                       |

## Key Takeaways

* `yield from` forwards values from another generator or iterable.
* It is a cleaner alternative to manually yielding inside a loop.
* Generator functions must be called before being passed to `yield from`.
* `close()` stops a generator before normal completion.
* Closing a generator raises `GeneratorExit` internally.
* Use `finally` for reliable cleanup.
* Explicit closing is especially useful when a generator owns files, connections, streams, or other resources.
