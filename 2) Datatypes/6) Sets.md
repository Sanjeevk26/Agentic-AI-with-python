# Python Sets

## Overview

A set is a built-in Python data type used to store unique values.

Sets are useful when we want to remove duplicates or compare two groups of data.

```python
essential_spices = {"cardamom", "ginger", "cinnamon"}
```

## What Is a Set?

A set is a collection of unique items.

Sets are written using curly braces `{}`.

```python
essential_spices = {"cardamom", "ginger", "cinnamon"}
```

Important points:

* Sets store only unique values.
* Duplicate values are automatically removed.
* Sets are unordered.
* Sets are useful for comparison operations.

## Set Example

```python
essential_spices = {"cardamom", "ginger", "cinnamon"}
optional_spices = {"cloves", "ginger", "black pepper"}
```

Here, `"ginger"` is common in both sets.

## Union

Union combines all unique values from two sets.

It uses the `|` operator.

```python
all_spices = essential_spices | optional_spices
```

Output:

```text
{"cardamom", "ginger", "cinnamon", "cloves", "black pepper"}
```

Even though `"ginger"` exists in both sets, it appears only once.

## Intersection

Intersection gives only the common values between two sets.

It uses the `&` operator.

```python
common_spices = essential_spices & optional_spices
```

Output:

```text
{"ginger"}
```

This means `"ginger"` is available in both sets.

## Difference

Difference gives values that exist in one set but not in the other.

It uses the `-` operator.

```python
only_in_essential = essential_spices - optional_spices
```

Output:

```text
{"cardamom", "cinnamon"}
```

Here, `"ginger"` is removed because it is also present in `optional_spices`.

## Membership Test

The `in` keyword checks whether a value exists in a set.

```python
"cloves" in optional_spices
```

Output:

```text
True
```

Example:

```python
"cloves" in essential_spices
```

Output:

```text
False
```

## Case Sensitivity

Set membership is case-sensitive.

```python
"Cloves" in optional_spices
```

Output:

```text
False
```

`"Cloves"` and `"cloves"` are treated as different values.

## Frozen Set

A `frozenset` is an immutable version of a set.

Once created, it cannot be changed.

```python
fixed_spices = frozenset({"cardamom", "ginger", "cinnamon"})
```

Use `frozenset` when you want a set of unique values that should not be modified.

## Key Takeaways

* Sets are created using curly braces `{}`.
* Sets store only unique values.
* Sets are unordered.
* Union `|` combines all unique values.
* Intersection `&` gives common values.
* Difference `-` gives values present in one set but not the other.
* The `in` keyword is used for membership testing.
* Membership checks are case-sensitive.
* `frozenset` creates an immutable set.
