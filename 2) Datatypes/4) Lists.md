# Python Lists

## Overview

This lecture introduces **lists**, one of the most commonly used mutable data types in Python.

So far, we studied immutable data types like:

* Numbers
* Strings
* Tuples

Immutable means once the value is created in memory, it cannot be changed directly.

Lists are different because they are **mutable**.

Mutable means the values inside the list can be changed, added, removed, reordered, or updated.

## What Is a List?

A list is a collection of values stored in a single variable.

Lists are created using square brackets `[]`.

```python
ingredients = ["water", "milk", "black tea"]
```

Lists are similar to arrays in other programming languages.

In Python, we usually call them **lists**, not arrays.

## Lists Are Mutable

Lists can be changed after creation.

Example:

```python
ingredients = ["water", "milk", "black tea"]

ingredients.append("sugar")
```

Now the list becomes:

```text
["water", "milk", "black tea", "sugar"]
```

## Adding Items with append()

The `append()` method adds an item at the end of the list.

```python
ingredients.append("sugar")
```

Output:

```text
["water", "milk", "black tea", "sugar"]
```

## Removing Items with remove()

The `remove()` method removes a specific item from the list.

```python
ingredients.remove("water")
```

Output:

```text
["milk", "black tea", "sugar"]
```

If the item exists, Python removes it from the list.

## Combining Lists with extend()

The `extend()` method combines another list with the current list.

```python
spice_options = ["ginger", "cardamom"]
chai_ingredients = ["water", "milk"]

chai_ingredients.extend(spice_options)
```

Output:

```text
["water", "milk", "ginger", "cardamom"]
```

## List Indexing

Every item in a list has a position called an index.

Indexing starts from `0`.

Example:

```python
chai_ingredients = ["water", "milk", "ginger", "cardamom"]
```

| Index | Value    |
| ----- | -------- |
| `0`   | water    |
| `1`   | milk     |
| `2`   | ginger   |
| `3`   | cardamom |

## Inserting Items with insert()

The `insert()` method adds an item at a specific position.

```python
chai_ingredients.insert(2, "black tea")
```

Output:

```text
["water", "milk", "black tea", "ginger", "cardamom"]
```

Here, `"black tea"` is added at index `2`.

The existing values shift to the right.

## Removing Last Item with pop()

The `pop()` method removes the last item from the list and returns it.

```python
last_added = chai_ingredients.pop()
```

If the list is:

```text
["water", "milk", "black tea", "ginger", "cardamom"]
```

Then `pop()` removes:

```text
cardamom
```

The updated list becomes:

```text
["water", "milk", "black tea", "ginger"]
```

## Reversing a List

The `reverse()` method reverses the order of the list.

```python
chai_ingredients.reverse()
```

Example output:

```text
["ginger", "black tea", "milk", "water"]
```

Important: `reverse()` changes the original list.

## Sorting a List

The `sort()` method sorts the list alphabetically or numerically.

```python
chai_ingredients.sort()
```

Example output:

```text
["black tea", "ginger", "milk", "water"]
```

Sorting is useful in real applications, such as sorting products by name, price, or rating.

## max() and min()

Python provides built-in functions to find the maximum and minimum values from a list.

```python
sugar_levels = [1, 2, 3, 4, 5]

maximum_sugar = max(sugar_levels)
minimum_sugar = min(sugar_levels)
```

Output:

```text
Maximum sugar level: 5
Minimum sugar level: 1
```

## Key Takeaways

* Lists are created using square brackets `[]`.
* Lists are mutable.
* `append()` adds an item at the end.
* `remove()` removes a specific item.
* `extend()` combines two lists.
* Indexing starts from `0`.
* `insert()` adds an item at a specific index.
* `pop()` removes and returns the last item.
* `reverse()` reverses the list.
* `sort()` sorts the list.
* `max()` returns the largest value.
* `min()` returns the smallest value.
