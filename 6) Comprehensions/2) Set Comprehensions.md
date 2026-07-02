# Python Comprehensions: Set Comprehension

## Overview

This lecture explains **set comprehension** in Python.

Set comprehension is similar to list comprehension, but it creates a `set` instead of a `list`.

A set automatically stores only unique values.

## List vs Set Comprehension

### List Comprehension

```python
[expression for item in iterable if condition]
```

### Set Comprehension

```python
{expression for item in iterable if condition}
```

The main difference is the bracket type.

| Comprehension Type | Brackets Used | Result |
| ------------------ | ------------- | ------ |
| List comprehension | `[]`          | List   |
| Set comprehension  | `{}`          | Set    |

## Why Use Set Comprehension?

Set comprehension is useful when we want:

* Unique values
* Duplicate removal
* Cleaner filtering logic
* A new set created from an iterable

## Example 1: Unique Chai Orders

Suppose we have a list of chai orders.

Some items are repeated.

```python
favorite_chais = [
    "masala chai",
    "green tea",
    "masala chai",
    "lemon tea",
    "green tea",
    "elaichi chai"
]
```

We want to find only the unique chai types.

## Set Comprehension Example

```python
unique_chais = {chai for chai in favorite_chais}

print(unique_chais)
```

Output:

```text
{'masala chai', 'green tea', 'lemon tea', 'elaichi chai'}
```

The order may be different because sets are unordered.

## How It Works

```python
unique_chais = {chai for chai in favorite_chais}
```

Here:

* `chai` before `for` is the expression
* `for chai in favorite_chais` loops through the list
* `{}` creates a set
* Duplicate values are automatically removed

## Adding a Condition

We can also add an `if` condition.

Example:

```python
unique_long_chais = {
    chai for chai in favorite_chais if len(chai) > 8
}
```

This keeps only chai names whose length is greater than `8`.

## Example 2: Unique Spices from Recipes

Now let us take a more complex example.

We have a dictionary of chai recipes.

Each chai has a list of ingredients.

```python
recipes = {
    "masala chai": ["ginger", "cardamom", "clove"],
    "elaichi chai": ["cardamom", "milk"],
    "spicy chai": ["ginger", "black pepper", "clove"]
}
```

We want to find all unique ingredients from all recipes.

Expected unique ingredients:

```text
ginger
cardamom
clove
milk
black pepper
```

## Nested Set Comprehension

```python
unique_spices = {
    spice
    for ingredients in recipes.values()
    for spice in ingredients
}
```

Output:

```python
{'ginger', 'cardamom', 'clove', 'milk', 'black pepper'}
```

The order may vary because sets are unordered.

## Understanding the Nested Comprehension

```python
unique_spices = {
    spice
    for ingredients in recipes.values()
    for spice in ingredients
}
```

This means:

```text
Go through each recipe's ingredient list.
Then go through each spice inside that ingredient list.
Add each spice to a set.
```

## Why expression is spice, not ingredients

In this example:

```python
for ingredients in recipes.values()
```

`ingredients` is one full list at a time.

Example:

```python
["ginger", "cardamom", "clove"]
```

Then:

```python
for spice in ingredients
```

loops through each individual item inside that list.

Example:

```python
"ginger"
"cardamom"
"clove"
```

So the final value we want to store is `spice`, not `ingredients`.

That is why we write:

```python
{spice for ingredients in recipes.values() for spice in ingredients}
```

## Key Takeaways

* Set comprehension creates a set.
* Set comprehension uses `{}`.
* Sets automatically remove duplicate values.
* Syntax: `{expression for item in iterable if condition}`
* The `if` condition is optional.
* Nested comprehensions can be used for nested data.
* In nested comprehensions, the final expression should be the value we want to collect.
* Set comprehension is useful for finding unique values from lists, dictionaries, and nested structures.
