# Python Conditionals

## Overview

This section starts the journey of processing data in Python.

So far, we studied Python data types like:

* Numbers
* Strings
* Tuples
* Lists
* Sets
* Dictionaries

Now we start learning how to apply logic to data.

Conditionals help a program make decisions.

## What Are Conditionals?

A conditional checks whether something is `True` or `False`.

Based on the result, the program decides what action to take.

Example:

```text
Do we have tea leaves?

Yes -> Make chai
No  -> Buy tea leaves
```

This is the basic idea of conditionals.

## if Statement

The `if` keyword is used to run code only when a condition is true.

```python
kettle_boiled = True

if kettle_boiled:
    print("Kettle done! Time to make chai.")
```

Output:

```text
Kettle done! Time to make chai.
```

If `kettle_boiled` is `False`, the message will not be printed.

## Important Rule: Indentation

Python uses indentation to define code blocks.

```python
if kettle_boiled:
    print("Kettle done! Time to make chai.")
```

The line inside the `if` block must be indented properly.

Wrong indentation can cause errors.

## Taking User Input

Python uses the `input()` function to take input from the user.

```python
snack = input("Enter your preferred snack: ")
```

The value entered by the user is stored as a string.

## Using lower()

User input can come in different formats.

Example:

```text
Samosa
SAMOSA
samosa
```

To make comparison easier, we convert input to lowercase.

```python
snack = input("Enter your preferred snack: ").lower()
```

Now all inputs become lowercase.

## Comparison Operator

The `==` operator is used to compare two values.

```python
snack == "cookies"
```

This checks whether `snack` is equal to `"cookies"`.

Important:

```python
snack = "cookies"
```

This assigns a value.

```python
snack == "cookies"
```

This compares a value.

## if-else Statement

The `else` block runs when the `if` condition is false.

```python
snack = input("Enter your preferred snack: ").lower()

if snack == "cookies" or snack == "samosa":
    print(f"Great choice! We will serve you {snack}.")
else:
    print("Sorry, we only serve cookies or samosa with tea.")
```

## or Operator

The `or` operator checks if at least one condition is true.

```python
if snack == "cookies" or snack == "samosa":
```

This means:

* If snack is cookies, run the code
* If snack is samosa, run the code
* If snack is anything else, go to `else`

## if-elif-else Statement

When there are multiple conditions, we use `elif`.

```python
cup = input("Choose your cup size - small, medium, large: ").lower()

if cup == "small":
    print("Price is 10 rupees.")
elif cup == "medium":
    print("Price is 15 rupees.")
elif cup == "large":
    print("Price is 20 rupees.")
else:
    print("Unknown cup size.")
```

## Mini Project 1: Smart Kettle Notification

### Problem

Create a notification system for a smart kettle.

It should remind the user only when the kettle has finished boiling.

### Logic

```text
If kettle_boiled is True:
    Show message: Kettle done! Time to make chai.
```

### Code Concept

```python
kettle_boiled = True

if kettle_boiled:
    print("Kettle done! Time to make chai.")
```

## Mini Project 2: Snack Suggestion System

### Problem

A local cafe wants a program that suggests snacks.

If the customer asks for `cookies` or `samosa`, confirm the order.

Otherwise, show that the snack is not available.

### Logic

```text
Take snack input

If snack is cookies or samosa:
    Confirm order
Else:
    Show unavailable message
```

### Code Concept

```python
snack = input("Enter your preferred snack: ").lower()

if snack == "cookies" or snack == "samosa":
    print(f"Great choice! We will serve you {snack}.")
else:
    print("Sorry, we only serve cookies or samosa with tea.")
```

## Mini Project 3: Chai Price Calculator

### Problem

A tea stall offers different prices for different cup sizes.

### Pricing

| Cup Size | Price     |
| -------- | --------- |
| small    | 10 rupees |
| medium   | 15 rupees |
| large    | 20 rupees |

### Logic

```text
Take cup size input

If small:
    Price is 10 rupees
Elif medium:
    Price is 15 rupees
Elif large:
    Price is 20 rupees
Else:
    Unknown cup size
```

## Key Takeaways

* Conditionals help programs make decisions.
* `if` runs code when a condition is true.
* `else` runs code when the condition is false.
* `elif` is used for multiple conditions.
* `input()` takes user input.
* `lower()` helps normalize user input.
* `==` is used for comparison.
* `or` checks if at least one condition is true.
* Proper indentation is very important in Python.
