# Python Comprehensions: Generator Expressions

## Overview

This lecture explains **generator expressions** in Python.

Generator expressions look similar to list, set, and dictionary comprehensions, but they behave differently.

They are mainly used to save memory.

## Why Generators Are Important

In small examples, generators may not look very special.

But in real projects, we may work with:

* Thousands of records
* Millions of records
* Large files
* Database results
* API responses
* Streaming data

In such cases, storing everything in memory at once can be expensive.

Generators help by producing one item at a time.

## Generator Expression Syntax

Basic syntax:

```python
(expression for item in iterable if condition)
```

It looks very similar to list comprehension.

## List Comprehension vs Generator Expression

### List Comprehension

```python
[x for x in items]
```

This creates the full list in memory immediately.

### Generator Expression

```python
(x for x in items)
```

This does not create the full list immediately.

It produces values one by one when needed.

## Key Difference

| Type                 | Brackets | Memory Behavior             |
| -------------------- | -------- | --------------------------- |
| List comprehension   | `[]`     | Creates full list in memory |
| Generator expression | `()`     | Produces one item at a time |

## Memory Difference

List comprehension:

```python
[x for x in items]
```

This creates the entire list first.

Generator expression:

```python
(x for x in items)
```

This works like a stream.

It gives values one by one as they are needed.

## Example: Daily Sales

Suppose we have daily sales data.

```python
daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]
```

We want to calculate the total sales where the sale value is greater than `5`.

## Using List Comprehension

```python
above_five_sales = [sale for sale in daily_sales if sale > 5]

print(above_five_sales)
```

Output:

```text
[10, 12, 7, 8, 9, 15]
```

This creates a complete list in memory.

## Using Generator Expression

```python
above_five_sales = (sale for sale in daily_sales if sale > 5)

print(above_five_sales)
```

Output:

```text
<generator object ...>
```

This does not directly print the values.

It creates a generator object.

## Consuming a Generator

A generator must be consumed.

One way to consume it is by using `sum()`.

```python
daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

total_sales = sum(sale for sale in daily_sales if sale > 5)

print(total_sales)
```

Output:

```text
61
```

Here, values are passed to `sum()` one by one.

## Why This Is Memory Efficient

This code:

```python
sum(sale for sale in daily_sales if sale > 5)
```

does not create a separate list.

It streams values directly into `sum()`.

This saves memory.

## Generator Object

When we write:

```python
total_cups = (sale for sale in daily_sales if sale > 5)
```

Python creates a generator object.

To see its values, we can loop through it.

```python
for sale in total_cups:
    print(sale)
```

## Important Note

A generator can usually be consumed only once.

Example:

```python
sales_generator = (sale for sale in daily_sales if sale > 5)

print(list(sales_generator))
print(list(sales_generator))
```

First output:

```text
[10, 12, 7, 8, 9, 15]
```

Second output:

```text
[]
```

The second list is empty because the generator was already used.

## Key Takeaways

* Generator expressions use parentheses `()`.
* They look similar to comprehensions.
* They produce values one at a time.
* They are memory efficient.
* They are useful for large data.
* List comprehensions create the full list in memory.
* Generator expressions work like a stream.
* Generators must be consumed using tools like `sum()`, `list()`, `for` loop, etc.
* A generator is usually consumed only once.
