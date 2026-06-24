# Python Tuples

## Overview

A tuple is a built-in Python data type used to store multiple values in a single variable.

Tuples are written using parentheses `()`.

```python
masala_spices = ("cardamom", "clove", "cinnamon")
```

## Brackets in Python

Python uses different types of brackets for different purposes:

| Symbol | Name            | Common Use         |
| ------ | --------------- | ------------------ |
| `()`   | Parentheses     | Tuples, functions  |
| `[]`   | Square brackets | Lists, indexing    |
| `{}`   | Curly braces    | Dictionaries, sets |

## What Is a Tuple?

A tuple is an ordered collection of values.

Example:

```python
masala_spices = ("cardamom", "clove", "cinnamon")
```

Here, `masala_spices` contains three values:

* `cardamom`
* `clove`
* `cinnamon`

## Tuples Are Immutable

Tuples are immutable.

This means once a tuple is created, its values cannot be changed directly.

```python
masala_spices = ("cardamom", "clove", "cinnamon")
```

You cannot directly replace `"cardamom"` with another value inside the same tuple.

## Tuple Unpacking

Tuple unpacking means extracting values from a tuple into separate variables.

```python
masala_spices = ("cardamom", "clove", "cinnamon")

spice_one, spice_two, spice_three = masala_spices
```

Now:

```text
spice_one = cardamom
spice_two = clove
spice_three = cinnamon
```

Important: The number of variables should match the number of values in the tuple.

## Multiple Variable Assignment

Python allows assigning multiple values to multiple variables in one line.

```python
ginger_ratio, cardamom_ratio = 2, 1
```

Behind the scenes, Python uses tuple behavior for this.

## Swapping Variables

Python allows easy variable swapping without using a third variable.

```python
ginger_ratio, cardamom_ratio = cardamom_ratio, ginger_ratio
```

Before swapping:

```text
ginger_ratio = 2
cardamom_ratio = 1
```

After swapping:

```text
ginger_ratio = 1
cardamom_ratio = 2
```

## Membership Testing

Membership testing checks whether a value exists inside a tuple.

Python uses the `in` keyword for this.

```python
"cinnamon" in masala_spices
```

Output:

```text
True
```

Example:

```python
"ginger" in masala_spices
```

Output:

```text
False
```

## Case Sensitivity

Membership checks are case-sensitive.

```python
"Cinnamon" in masala_spices
```

Output:

```text
False
```

This is false because the tuple contains `"cinnamon"` with a lowercase `c`.

## Key Takeaways

* Tuples are created using parentheses `()`.
* Tuples store multiple values.
* Tuples are immutable.
* Tuple unpacking extracts values into variables.
* Python allows multiple variable assignment.
* Python allows easy variable swapping.
* The `in` keyword checks if a value exists in a tuple.
* Membership testing is case-sensitive.
