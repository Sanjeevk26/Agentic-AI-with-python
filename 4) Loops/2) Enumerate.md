# Python Loops: enumerate()

## Overview

This lecture explains how to use `enumerate()` in Python.

`enumerate()` is useful when we want to loop through a list and also get the item number or index.

## Problem Statement

We are creating a tea menu board.

Each menu item must be printed with a number.

Example:

```text
1. Green Chai
2. Lemon Chai
3. Spiced Chai
4. Mint Chai
```

## Normal for Loop

A normal `for` loop can print each item from a list.

```python
menu = ["green", "lemon", "spiced", "mint"]

for item in menu:
    print(f"Menu item is {item}")
```

Output:

```text
Menu item is green
Menu item is lemon
Menu item is spiced
Menu item is mint
```

This works, but it does not print item numbers.

## Why enumerate() Is Needed

Sometimes we need both:

* The item
* The item number

This is where `enumerate()` is useful.

## What is enumerate()?

`enumerate()` adds a counter/index to each item while looping.

Example:

```python
menu = ["green", "lemon", "spiced", "mint"]

for index, item in enumerate(menu):
    print(index, item)
```

Output:

```text
0 green
1 lemon
2 spiced
3 mint
```

By default, `enumerate()` starts counting from `0`.

## Starting from 1

For a menu board, starting from `1` looks better than starting from `0`.

We can use the `start` parameter.

```python
menu = ["green", "lemon", "spiced", "mint"]

for index, item in enumerate(menu, start=1):
    print(f"{index}. {item} chai")
```

Output:

```text
1. green chai
2. lemon chai
3. spiced chai
4. mint chai
```

## How enumerate() Works

`enumerate()` returns two values during each loop:

```text
index, item
```

Example:

```python
for index, item in enumerate(menu, start=1):
```

Here:

* `index` stores the number
* `item` stores the menu item

## Tuple Behavior Behind enumerate()

Internally, `enumerate()` gives pairs of values.

Example:

```text
(1, "green")
(2, "lemon")
(3, "spiced")
(4, "mint")
```

That is why we can unpack it into two variables:

```python
index, item
```

## Key Takeaways

* `enumerate()` is used when we need both index and item.
* By default, indexing starts from `0`.
* Use `start=1` to begin numbering from `1`.
* `enumerate()` is useful for menus, lists, reports, tables, and numbered outputs.
* It makes code cleaner than manually managing counters.
