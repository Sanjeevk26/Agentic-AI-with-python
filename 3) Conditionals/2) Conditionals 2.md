# Python Conditionals: Nested If, Ternary Operator, and Match Case

## Overview

This lecture continues the topic of Python conditionals.

It covers three important concepts:

* Nested `if` statements
* Ternary operator
* `match-case` statement

These concepts help us write decision-based programs for real-world problems.

## 1. Nested If Statements

Nested `if` means writing one `if` condition inside another `if` condition.

This is useful when one condition should be checked only after another condition is true.

## Mini Project 1: Smart Thermostat Alert System

### Problem

Build a smart thermostat alert system.

Rules:

* If the device status is `active`

  * Check the temperature
  * If temperature is above `35`, show a high temperature alert
  * Otherwise, show temperature is normal
* If the device is not active, show device is offline

### Code Concept

```python
device_status = "active"
temperature = 38

if device_status == "active":
    if temperature > 35:
        print("High temperature alert!")
    else:
        print("Temperature is normal.")
else:
    print("Device is offline.")
```

## pass Keyword

The `pass` keyword is used as a temporary placeholder.

It tells Python:

```text
Do nothing for now.
```

Example:

```python
if device_status == "active":
    pass
else:
    print("Device is offline.")
```

This is useful when we want to write the structure first and fill the logic later.

## 2. Ternary Operator

A ternary operator is a short way to write simple `if-else` logic in one line.

## Mini Project 2: Delivery Fee Waiver

### Problem

You run an online tea store.

Rules:

* If order amount is more than `300`, delivery is free
* Otherwise, delivery fee is `30`

### Normal If-Else Approach

```python
order_amount = 400

if order_amount > 300:
    delivery_fee = 0
else:
    delivery_fee = 30
```

### Ternary Operator Approach

```python
delivery_fee = 0 if order_amount > 300 else 30
```

This means:

```text
Set delivery_fee to 0 if order_amount > 300, otherwise set it to 30.
```

## input() Always Returns String

When we take input from the user, Python returns it as a string.

```python
order_amount = input("Enter the order amount: ")
```

Even if the user enters `400`, Python treats it as:

```python
"400"
```

To use it as a number, convert it using `int()`.

```python
order_amount = int(input("Enter the order amount: "))
```

## 3. Match Case

`match-case` is useful when we need to compare one value with many possible options.

It is cleaner than writing many `if-elif-else` statements.

## Mini Project 3: Railway Seat Info System

### Problem

Build a railway ticket info system.

Based on seat type, show its features.

Seat types:

* `sleeper`
* `ac`
* `general`
* `luxury`

If the seat type is unknown, show an invalid message.

### Code Concept

```python
seat_type = input("Enter seat type: ").lower()

match seat_type:
    case "sleeper":
        print("Sleeper: No AC, beds available.")
    case "ac":
        print("AC: Air conditioned, comfy ride.")
    case "general":
        print("General: Cheapest option, no reservation.")
    case "luxury":
        print("Luxury: Premium seats with meals.")
    case _:
        print("Invalid seat type.")
```

## case _

The underscore `_` is used as a default case.

It runs when no other case matches.

It works like the `else` part of `if-else`.

## Key Takeaways

* Nested `if` is used when one condition depends on another condition.
* `pass` is used as a placeholder when we want to write code later.
* `input()` returns user input as a string.
* `int()` converts string input into an integer.
* Ternary operator writes simple `if-else` logic in one line.
* `match-case` is useful when checking many fixed values.
* `case _` handles unknown or invalid inputs.
* Use `.lower()` to make user input easier to compare.
