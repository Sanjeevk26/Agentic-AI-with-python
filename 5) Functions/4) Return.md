# Python Functions: return Keyword

## Overview

The `return` keyword is used to send a value back from a function.

A function can:

* Print a value
* Return a value
* Return nothing
* Return one value
* Return multiple values
* Return early before finishing the full function

## print vs return

`print()` only displays something on the screen.

`return` sends a value back to the place where the function was called.

## Basic return Example

```python
def make_chai():
    return "Here is your masala chai"
```

The function does not print anything by itself.

To see the returned value, we can store it in a variable and print it.

```python
return_value = make_chai()
print(return_value)
```

Output:

```text
Here is your masala chai
```

We can also print the function call directly.

```python
print(make_chai())
```

## Function Returning Nothing

If a function does not return anything, Python automatically returns `None`.

```python
def idle_chaiwala():
    pass

print(idle_chaiwala())
```

Output:

```text
None
```

This is called an implicit return.

## Returning One Value

A function can return one value.

```python
def sold_cups():
    return 120

total = sold_cups()
print(total)
```

Output:

```text
120
```

Here, `120` is returned and stored in the variable `total`.

## Early Return

A function stops immediately when it hits the `return` keyword.

Any code written after `return` inside the same block will not run.

```python
def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai is over"

    return "Chai is ready"
```

Example:

```python
print(chai_status(0))
print(chai_status(5))
```

Output:

```text
Sorry, chai is over
Chai is ready
```

In the first call, the function returns early because `cups_left` is `0`.

## Code After return Does Not Run

```python
def chai_status(cups_left):
    if cups_left == 0:
        return "Sorry, chai is over"
        print("This will never run")

    return "Chai is ready"
```

Once Python reaches `return`, it exits the function.

## Returning Multiple Values

Python functions can return multiple values.

```python
def chai_report():
    return 100, 20
```

We can store them in separate variables.

```python
sold, remaining = chai_report()

print(sold)
print(remaining)
```

Output:

```text
100
20
```

## Returning More Values

```python
def chai_report():
    return 100, 20, 10
```

Now we need three variables to receive the values.

```python
sold, remaining, not_paid = chai_report()
```

If we use only two variables, Python will give an unpacking error.

## Ignoring a Returned Value

If we do not need one returned value, we can use `_`.

```python
sold, remaining, _ = chai_report()
```

The underscore means:

```text
I know this value exists, but I do not plan to use it.
```

## Key Takeaways

* `return` sends a value back from a function.
* `print()` only displays output.
* A function without `return` gives `None`.
* A function can return one value.
* A function can return multiple values.
* Once `return` runs, the function stops.
* Code after `return` in the same block does not execute.
* Use `_` when you want to ignore a returned value.
