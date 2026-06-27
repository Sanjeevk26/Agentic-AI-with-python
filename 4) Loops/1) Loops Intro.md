# Python Loops: for Loop, range, and Lists

## Overview

Loops are used when we want to repeat a task again and again.

So far, we used conditionals to decide between different paths.

Example:

```text
If condition is true  -> do this
If condition is false -> do that
```

Loops are different.

They help us repeat the same task multiple times.

Example:

```text
Print token number 1
Print token number 2
Print token number 3
...
Print token number 10
```

## Why Loops Are Needed

In real applications, we often need to process multiple items.

Examples:

* Displaying a list of books
* Printing customer tokens
* Showing order names
* Processing database records
* Sending notifications to many users

Instead of writing the same code again and again, we use loops.

## Types of Loops in Python

Python mainly uses two common loops:

* `for` loop
* `while` loop

This lecture focuses on the `for` loop.

## for Loop

A `for` loop is used to repeat a task for each item in a sequence.

Basic syntax:

```python
for item in sequence:
    # task to repeat
```

Example:

```python
for token in range(1, 11):
    print(token)
```

## range()

The `range()` function generates a sequence of numbers.

Example:

```python
range(1, 11)
```

This generates numbers from `1` to `10`.

Important:

The end value is not included.

So:

```python
range(1, 11)
```

Means:

```text
1, 2, 3, 4, 5, 6, 7, 8, 9, 10
```

It does not include `11`.

## Mini Project 1: Token Dispenser

### Problem

A tea stall owner has a digital token display.

For every customer in line, a token number is printed and chai is served.

### Task

Use a `for` loop to generate token numbers from `1` to `10`.

### Code Concept

```python
for token in range(1, 11):
    print(f"Serving chai to token #{token}")
```

### Output

```text
Serving chai to token #1
Serving chai to token #2
Serving chai to token #3
...
Serving chai to token #10
```

## How the Loop Works

In this loop:

```python
for token in range(1, 11):
    print(f"Serving chai to token #{token}")
```

Python does the following:

```text
token = 1 -> print message
token = 2 -> print message
token = 3 -> print message
...
token = 10 -> print message
```

When the range reaches `11`, the loop stops because `11` is not included.

## Mini Project 2: Chai Batch Simulation

### Problem

A chai shop makes tea in batches every 15 minutes.

We want to simulate 4 batches.

### Task

Use `range()` to print batch numbers.

### Code Concept

```python
for batch in range(1, 5):
    print(f"Preparing chai for batch #{batch}")
```

### Output

```text
Preparing chai for batch #1
Preparing chai for batch #2
Preparing chai for batch #3
Preparing chai for batch #4
```

Here, `range(1, 5)` gives values from `1` to `4`.

## Mini Project 3: Chai Order Queue

### Problem

We received a list of customer names for chai orders.

We need to print when each order is ready.

### Task

Loop through a list of names and print the order message.

### Code Concept

```python
orders = ["Hitesh", "Aman", "Becky", "Carlos"]

for name in orders:
    print(f"Order ready for {name}")
```

### Output

```text
Order ready for Hitesh
Order ready for Aman
Order ready for Becky
Order ready for Carlos
```

## Iterables

An iterable is anything Python can loop through.

Examples:

* List
* String
* Tuple
* Set
* Dictionary
* Range

In this lecture, we looped through:

```python
range(1, 11)
```

and:

```python
orders = ["Hitesh", "Aman", "Becky", "Carlos"]
```

## Key Takeaways

* Loops repeat a task multiple times.
* `for` loop is used to loop through a sequence.
* `range()` generates numbers.
* Python ranges do not include the ending value.
* `range(1, 11)` gives numbers from `1` to `10`.
* Lists can also be looped through.
* Each loop cycle is called an iteration.
* The loop variable changes value in every iteration.
* Loops are useful for processing repeated tasks in real applications.
