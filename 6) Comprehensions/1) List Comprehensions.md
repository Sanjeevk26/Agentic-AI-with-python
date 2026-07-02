# Python Comprehensions: Introduction and List Comprehension

## Overview

Comprehensions are a concise way to create collections in Python.

Almost everything done with comprehensions can also be done using loops.

However, comprehensions are often shorter, cleaner, and widely used in production code.

## What Are Comprehensions?

Comprehensions are a one-line way of creating:

* Lists
* Sets
* Dictionaries
* Generators

They allow us to write filtering, transformation, and collection-building logic in a compact way.

## Why Use Comprehensions?

Comprehensions are useful because they help write:

* Cleaner code
* Shorter code
* More Pythonic code
* Sometimes faster code
* Easy filtering and transformation logic

## Where Comprehensions Are Used

Comprehensions are commonly used for:

### 1. Filtering Items

Example: Pick only iced teas from a menu.

### 2. Transforming Items

Example: Convert prices from INR to USD.

### 3. Creating New Collections

Example: Map tea names to their prices.

### 4. Flattening Nested Structures

Example: Extract ingredients from nested recipes.

## Types of Comprehensions

Python supports different types of comprehensions:

| Type                     | Purpose              |
| ------------------------ | -------------------- |
| List comprehension       | Creates a list       |
| Set comprehension        | Creates a set        |
| Dictionary comprehension | Creates a dictionary |
| Generator expression     | Creates a generator  |

## List Comprehension

List comprehension is used to create a new list from an existing iterable.

Basic syntax:

```python
[expression for item in iterable if condition]
```

## Understanding the Syntax

```python
[expression for item in iterable if condition]
```

Meaning:

| Part         | Meaning                           |
| ------------ | --------------------------------- |
| `expression` | What value should be stored       |
| `item`       | Current item from the iterable    |
| `iterable`   | Collection we are looping through |
| `condition`  | Filter logic                      |

## Example Menu

```python
menu = [
    "masala chai",
    "iced lemon tea",
    "green tea",
    "iced peach tea",
    "ginger chai"
]
```

## Goal

From the menu, create a new list containing only iced tea items.

Expected result:

```python
["iced lemon tea", "iced peach tea"]
```

## Normal Loop Approach

```python
menu = [
    "masala chai",
    "iced lemon tea",
    "green tea",
    "iced peach tea",
    "ginger chai"
]

iced_teas = []

for tea in menu:
    if "iced" in tea:
        iced_teas.append(tea)

print(iced_teas)
```

## List Comprehension Approach

```python
menu = [
    "masala chai",
    "iced lemon tea",
    "green tea",
    "iced peach tea",
    "ginger chai"
]

iced_teas = [tea for tea in menu if "iced" in tea]

print(iced_teas)
```

Output:

```text
['iced lemon tea', 'iced peach tea']
```

## Breaking Down the List Comprehension

```python
iced_teas = [tea for tea in menu if "iced" in tea]
```

Here:

* `tea` before `for` is the expression
* `for tea in menu` loops through the menu
* `if "iced" in tea` filters only iced items
* The result is stored in `iced_teas`

## Variable Name Inside Comprehension

The loop variable can be named anything.

Example:

```python
iced_teas = [my_tea for my_tea in menu if "iced" in my_tea]
```

This also works.

But the same variable name must be used consistently inside the comprehension.

## Filtering by Length

We can also filter items based on length.

```python
long_items = [tea for tea in menu if len(tea) > 12]
```

This creates a list of menu items whose length is greater than `12`.

## Key Takeaways

* Comprehensions are a concise way to create collections.
* List comprehension creates a new list.
* Syntax: `[expression for item in iterable if condition]`
* It can replace simple loops.
* It is commonly used for filtering and transforming data.
* The `if` condition is optional but useful for filtering.
* Comprehensions are widely used in real Python projects.
