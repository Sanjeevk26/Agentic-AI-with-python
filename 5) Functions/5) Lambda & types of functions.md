# Python Functions: Types of Functions

## Overview

Functions are core building blocks in Python.

In this lecture, we discuss different types or styles of functions:

* Pure functions
* Impure functions
* Recursive functions
* Lambda functions

These are not always official “types,” but they are common ways programmers describe function behavior.

## 1. Pure Functions

A pure function only works with the values passed to it.

It does not change anything outside the function.

Example:

```python
def pure_chai(cups):
    return cups * 10
```

Here, the function takes `cups`, multiplies it by `10`, and returns the result.

It does not touch any global variable.

## Pure Function Example

```python
def pure_chai(cups):
    return cups * 10

print(pure_chai(3))
```

Output:

```text
30
```

## Why Pure Functions Are Good

Pure functions are easier to:

* Understand
* Test
* Debug
* Reuse
* Maintain

They are safer because they do not change external data.

## 2. Impure Functions

An impure function changes something outside itself.

Example:

```python
total_chai = 0

def impure_chai(cups):
    global total_chai
    total_chai += cups
```

Here, the function changes the global variable `total_chai`.

This is called an impure function.

## Why Impure Functions Should Be Avoided

Impure functions are usually not recommended because they can create unexpected changes.

If many functions change the same global variable, debugging becomes difficult.

## 3. Recursive Functions

A recursive function is a function that calls itself.

It must have a stopping condition.

Without a stopping condition, the function will keep calling itself forever.

## Recursive Function Example

```python
def pour_chai(n):
    if n == 0:
        return "All cups poured"

    return pour_chai(n - 1)
```

Example:

```python
print(pour_chai(3))
```

## How Recursion Works

If we call:

```python
pour_chai(3)
```

The function works like this:

```text
pour_chai(3)
pour_chai(2)
pour_chai(1)
pour_chai(0)
```

When `n` becomes `0`, the function stops.

Output:

```text
All cups poured
```

## Important Point About Recursion

Every recursive function needs a base condition.

Example:

```python
if n == 0:
    return "All cups poured"
```

This condition stops the recursion.

## 4. Lambda Functions

Lambda functions are small anonymous functions.

Anonymous means the function does not have a normal name.

Normal function:

```python
def add_tax(price):
    return price + 10
```

Lambda version:

```python
add_tax = lambda price: price + 10
```

## Lambda Syntax

```python
lambda parameter: expression
```

Example:

```python
lambda chai: chai == "kadak"
```

This returns `True` if `chai` is equal to `"kadak"`.

## Lambda with filter()

Lambda functions are commonly used with `filter()`.

Example:

```python
chai_types = ["light", "kadak", "ginger", "kadak"]

strong_chai = list(filter(lambda chai: chai == "kadak", chai_types))

print(strong_chai)
```

Output:

```text
['kadak', 'kadak']
```

## How filter() Works

`filter()` checks every item in a sequence.

It keeps only the items where the condition returns `True`.

Example:

```python
lambda chai: chai == "kadak"
```

This means:

```text
Keep only chai values that are equal to kadak.
```

## Filtering Opposite Values

We can also keep values that are not equal to `"kadak"`.

```python
chai_types = ["light", "kadak", "ginger", "kadak"]

not_kadak = list(filter(lambda chai: chai != "kadak", chai_types))

print(not_kadak)
```

Output:

```text
['light', 'ginger']
```

## Key Takeaways

* Pure functions do not change external data.
* Impure functions change data outside themselves.
* Pure functions are usually safer and easier to debug.
* Recursive functions call themselves.
* Recursive functions need a stopping condition.
* Lambda functions are anonymous functions.
* Lambda functions are useful for short one-line logic.
* `filter()` keeps only values that match a condition.
* `list()` can convert the filtered result into a list.
