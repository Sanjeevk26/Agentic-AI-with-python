# Python Walrus Operator

## Overview

This lecture introduces the **Walrus Operator** in Python.

The walrus operator looks like this:

```python
:=
```

It is used to assign a value to a variable as part of an expression.

It was introduced in Python 3.8.

## Statement vs Expression

Before understanding the walrus operator, it is important to know the difference between a statement and an expression.

## Statement

A statement performs an action.

Example:

```python
x = 5
```

This assigns the value `5` to `x`.

It does not return a value.

## Expression

An expression returns a value.

Example:

```python
3 + 3
```

This returns:

```text
6
```

## Why Walrus Operator Is Useful

Normally, we write assignment and condition checking separately.

Example:

```python
value = 13
remainder = value % 5

if remainder:
    print(f"Not divisible. Remainder is {remainder}")
```

Using the walrus operator, we can assign and check the value in the same line.

```python
value = 13

if remainder := value % 5:
    print(f"Not divisible. Remainder is {remainder}")
```

Here:

```python
remainder := value % 5
```

means:

```text
Calculate value % 5 and store it in remainder.
```

Then Python checks whether `remainder` is truthy.

## Example 1: Remainder Check

```python
value = 13

if remainder := value % 5:
    print(f"Not divisible. Remainder is {remainder}")
```

Output:

```text
Not divisible. Remainder is 3
```

## Example 2: Checking Available Cup Sizes

```python
available_sizes = ["small", "medium", "large"]

if requested_size := input("Enter your chai cup size: "):
    if requested_size in available_sizes:
        print(f"Serving {requested_size} chai")
    else:
        print(f"Size unavailable: {requested_size}")
```

The input is assigned to `requested_size` inside the condition.

## Example 3: Using Walrus Operator in while Loop

The walrus operator is useful when we want to take input and check it at the same time.

```python
flavors = ["masala", "ginger", "lemon", "mint"]

while (flavor := input("Choose your flavor: ")) not in flavors:
    print(f"Sorry, {flavor} is not available.")

print(f"You chose {flavor} chai.")
```

This keeps asking the user until they choose a valid flavor.

## How It Works

If the user enters:

```text
oolong
```

Python checks:

```python
"oolong" not in flavors
```

Since it is not available, the loop continues.

If the user enters:

```text
masala
```

Python checks:

```python
"masala" not in flavors
```

This becomes false, so the loop stops.

## Key Takeaways

* The walrus operator is written as `:=`.
* It assigns a value inside an expression.
* It helps reduce extra lines of code.
* It is useful in `if` statements and `while` loops.
* It should be used carefully because it can make code harder to read.
* Assignment using `=` is a statement.
* Assignment using `:=` works inside expressions.
* The walrus operator requires Python 3.8 or later.
