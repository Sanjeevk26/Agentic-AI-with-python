# Python Comprehensions: Dictionary Comprehension

## Overview

This lecture explains **dictionary comprehension** in Python.

Dictionary comprehension is used to create a new dictionary in a short and clean way.

It works very similarly to list and set comprehensions.

## Dictionary Comprehension Syntax

Basic syntax:

```python
{key: value for item in iterable if condition}
```

The main difference between set comprehension and dictionary comprehension is the final expression.

## Set vs Dictionary Comprehension

### Set Comprehension

```python
{expression for item in iterable}
```

This creates a set.

### Dictionary Comprehension

```python
{key: value for item in iterable}
```

This creates a dictionary.

The `key: value` pair makes it a dictionary.

## Problem Statement

We have tea prices in INR.

We want to convert all prices into USD.

Assume:

```text
1 USD = 80 INR
```

## Original Dictionary

```python
tea_prices_inr = {
    "masala chai": 40,
    "green tea": 50,
    "lemon tea": 200
}
```

Expected result:

```python
{
    "masala chai": 0.5,
    "green tea": 0.625,
    "lemon tea": 2.5
}
```

## Using Dictionary Comprehension

```python
tea_prices_usd = {
    tea: price / 80
    for tea, price in tea_prices_inr.items()
}
```

## How It Works

```python
tea_prices_usd = {
    tea: price / 80
    for tea, price in tea_prices_inr.items()
}
```

Breakdown:

| Part                                       | Meaning                           |
| ------------------------------------------ | --------------------------------- |
| `tea: price / 80`                          | Creates key-value pair            |
| `tea`                                      | Key in the new dictionary         |
| `price / 80`                               | Converted price in USD            |
| `for tea, price in tea_prices_inr.items()` | Loops through original dictionary |

## Why items() Is Used

A dictionary contains keys and values.

To get both key and value together, we use `.items()`.

```python
tea_prices_inr.items()
```

This gives pairs like:

```text
("masala chai", 40)
("green tea", 50)
("lemon tea", 200)
```

That is why we can write:

```python
for tea, price in tea_prices_inr.items()
```

## Normal Loop Approach

The same logic can also be written using a normal loop.

```python
tea_prices_usd = {}

for tea, price in tea_prices_inr.items():
    tea_prices_usd[tea] = price / 80
```

## Dictionary Comprehension Approach

```python
tea_prices_usd = {
    tea: price / 80
    for tea, price in tea_prices_inr.items()
}
```

Both approaches give the same result, but dictionary comprehension is shorter and cleaner.

## Adding a Condition

We can also add an `if` condition.

Example: Convert only teas priced above 45 INR.

```python
expensive_teas_usd = {
    tea: price / 80
    for tea, price in tea_prices_inr.items()
    if price > 45
}
```

## Key Takeaways

* Dictionary comprehension creates a dictionary.
* It uses curly braces `{}`.
* Dictionary comprehension must have a `key: value` expression.
* `.items()` is used to loop through keys and values together.
* It is useful for transforming dictionary data.
* It can also include an optional `if` condition.
* It makes dictionary creation shorter and cleaner.
