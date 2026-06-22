# Python Numbers, Booleans, and Basic Operations

## Overview

This lecture covers the main number types in Python and how to perform basic mathematical and logical operations.

Python supports different types of numbers, such as integers, booleans, floating-point numbers, and complex numbers.

## Types of Numbers in Python

### 1. Integers

Integers are whole numbers without decimals.

Example:

```python
black_tea_grams = 14
ginger_grams = 3
```

Integers are commonly used for counting, quantities, IDs, and simple calculations.

## Integer Operations

### Addition

```python
total_grams = black_tea_grams + ginger_grams
```

### Subtraction

```python
remaining_tea = black_tea_grams - ginger_grams
```

### Multiplication

```python
total_strength = black_tea_grams * ginger_grams
```

### Normal Division

Normal division uses `/` and returns a decimal value.

```python
milk_per_serving = 7 / 4
```

Output:

```text
1.75
```

### Floor Division

Floor division uses `//` and ignores the decimal part.

```python
bags_per_pot = 7 // 4
```

Output:

```text
1
```

### Modulo Operator

Modulo uses `%` and gives the remainder.

```python
leftover_pods = 10 % 3
```

Output:

```text
1
```

### Exponent / Power

Exponent uses `**`.

```python
powerful_flavor = 2 ** 3
```

Output:

```text
8
```

This means:

```text
2 x 2 x 2
```

## Large Number Readability

Python allows underscores in large numbers for better readability.

```python
tea_leaves_harvested = 1_000_000_000
```

Python treats it as:

```text
1000000000
```

The underscores do not affect the value.

## Comments in Python

Comments are notes written inside code.

They are ignored during execution.

```python
# This is a comment
```

Comments are useful for:

* Explaining code
* Writing notes
* Planning logic
* Making code easier to understand

## 2. Booleans

Booleans represent only two values:

```python
True
False
```

Example:

```python
is_boiling = True
```

Booleans are used in decision-making, such as:

* Is user logged in?
* Is payment completed?
* Is tea ready?
* Is temperature above limit?

## Boolean as Numbers

In Python:

```text
True = 1
False = 0
```

Example:

```python
stir_count = 5
is_boiling = True

total_actions = stir_count + is_boiling
```

Output:

```text
6
```

Here, `True` is treated as `1`.

## bool() Function

The `bool()` function converts values into boolean form.

```python
bool(0)
```

Output:

```text
False
```

```python
bool(1)
```

Output:

```text
True
```

```python
bool(11)
```

Output:

```text
True
```

```python
bool("Python")
```

Output:

```text
True
```

```python
bool(None)
```

Output:

```text
False
```

## Logical Operators

Python has three main logical operators:

| Operator | Meaning                             |
| -------- | ----------------------------------- |
| `and`    | Both conditions must be true        |
| `or`     | At least one condition must be true |
| `not`    | Reverses the boolean value          |

### and Example

```python
water_hot = True
tea_added = True

can_serve_chai = water_hot and tea_added
```

Output:

```text
True
```

If either value is false, the result becomes false.

### or Example

```python
tea_available = True
coffee_available = False

can_drink = tea_available or coffee_available
```

Output:

```text
True
```

### not Example

```python
is_empty = False

print(not is_empty)
```

Output:

```text
True
```

## 3. Floating-Point Numbers

Floating-point numbers are decimal numbers.

Example:

```python
ideal_temp = 95.5
current_temp = 95.4
```

They are used where precision is important, such as:

* Temperature
* Stock prices
* Money
* Scientific calculations

## Floating-Point Precision

Sometimes decimal calculations may not return the exact expected result because of how computers store floating-point numbers.

Example:

```python
ideal_temp = 95.5
current_temp = 95.499999999

difference = ideal_temp - current_temp
```

The result may show a very small decimal difference.

## sys.float_info

Python provides information about floating-point limits using the `sys` module.

```python
import sys

print(sys.float_info)
```

This shows details such as:

* Maximum float value
* Minimum float value
* Precision limit

## Fractions and Decimals

Python also supports more precise number handling using modules.

### Fractions

```python
from fractions import Fraction
```

Useful for exact fractional values.

### Decimal

```python
from decimal import Decimal
```

Useful when higher decimal precision is required, especially in financial calculations.

## 4. Complex Numbers

Python supports complex numbers.

Example:

```python
complex_number = 2 + 3j
```

Complex numbers are mostly used in scientific, mathematical, or engineering use cases.

## Key Takeaways

* Integers are whole numbers.
* Floating-point numbers are decimal numbers.
* Booleans store `True` or `False`.
* `True` behaves like `1`, and `False` behaves like `0`.
* `/` gives normal division.
* `//` gives floor division.
* `%` gives the remainder.
* `**` is used for power.
* Underscores improve large number readability.
* `and`, `or`, and `not` are used for logical operations.
* Python supports advanced number types like fractions, decimals, and complex numbers.

---

