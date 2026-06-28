# Python Loops: zip()

## Overview

This lecture explains how to use `zip()` in Python.

`zip()` is useful when we want to loop through multiple lists at the same time.

## Problem Statement

We are preparing an order summary with:

* Customer names
* Their total bill amounts

We have two lists:

```python
names = ["Hitesh", "Meera", "Sam", "Ali"]
bills = [50, 70, 100, 55]
```

We want to print:

```text
Hitesh paid 50 rupees
Meera paid 70 rupees
Sam paid 100 rupees
Ali paid 55 rupees
```

## Why zip() Is Needed

If we have two related lists, looping through them separately is not convenient.

Example:

```python
names = ["Hitesh", "Meera", "Sam", "Ali"]
bills = [50, 70, 100, 55]
```

Here:

| Name   | Bill |
| ------ | ---- |
| Hitesh | 50   |
| Meera  | 70   |
| Sam    | 100  |
| Ali    | 55   |

`zip()` helps combine both lists item by item.

## What is zip()?

`zip()` takes multiple iterables and combines their values position-wise.

Example:

```python
zip(names, bills)
```

It creates pairs like:

```text
("Hitesh", 50)
("Meera", 70)
("Sam", 100)
("Ali", 55)
```

Each pair is returned as a tuple.

## Using zip() in a Loop

```python
names = ["Hitesh", "Meera", "Sam", "Ali"]
bills = [50, 70, 100, 55]

for name, amount in zip(names, bills):
    print(f"{name} paid {amount} rupees")
```

Output:

```text
Hitesh paid 50 rupees
Meera paid 70 rupees
Sam paid 100 rupees
Ali paid 55 rupees
```

## How zip() Works

During each loop:

```text
First loop  -> name = Hitesh, amount = 50
Second loop -> name = Meera, amount = 70
Third loop  -> name = Sam, amount = 100
Fourth loop -> name = Ali, amount = 55
```

## Tuple Unpacking

`zip()` returns pairs of values.

That is why we can unpack them like this:

```python
for name, amount in zip(names, bills):
```

Here:

* `name` gets the customer name
* `amount` gets the bill value

## Important Note

`zip()` stops when the shortest list ends.

Example:

```python
names = ["Hitesh", "Meera", "Sam"]
bills = [50, 70]
```

Only two pairs will be created:

```text
("Hitesh", 50)
("Meera", 70)
```

`Sam` will be ignored because there is no matching bill.

## Key Takeaways

* `zip()` is used to loop through multiple lists together.
* It combines values based on their positions.
* It returns pairs as tuples.
* Tuple unpacking helps store each value in separate variables.
* `zip()` is useful for summaries, reports, bills, paired data, and parallel lists.
* `zip()` stops at the shortest list.
