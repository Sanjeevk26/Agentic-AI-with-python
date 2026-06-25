# Python Lists: Operator Overloading and Bytearray

## Overview

This lecture continues the topic of Python lists.

It covers:

* Operator overloading
* Combining lists using `+`
* Repeating lists using `*`
* Introduction to `operator.itemgetter`
* Converting text-like data into `bytearray`
* Replacing values inside a `bytearray`

## Operator Overloading

Operator overloading means using the same operator for more than one type of operation.

For example, the `+` operator is normally used to add numbers.

```python
10 + 20
```

But in Python, `+` can also combine lists.

```python
base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
```

Output:

```text
["water", "milk", "ginger"]
```

Here, `+` is not doing mathematical addition. It is combining two lists.

This is called operator overloading.

## Combining Lists with `+`

Lists can be combined using the `+` operator.

```python
base_liquid = ["water", "milk"]
extra_flavor = ["ginger"]

full_liquid_mix = base_liquid + extra_flavor
```

Output:

```text
["water", "milk", "ginger"]
```

This works like list concatenation.

## Repeating Lists with `*`

The `*` operator can repeat list items.

```python
strong_brew = ["black tea"] * 3
```

Output:

```text
["black tea", "black tea", "black tea"]
```

If the list has multiple items, the full list is repeated.

```python
strong_brew = ["black tea", "water"] * 3
```

Output:

```text
["black tea", "water", "black tea", "water", "black tea", "water"]
```

The original order is maintained.

## bytearray

A `bytearray` is a mutable sequence of bytes.

It is rarely used in beginner-level Python, but it is useful when working with raw data, files, encodings, or binary data.

Example:

```python
raw_spice_data = bytearray(b"cinnamon")
```

Output:

```text
bytearray(b'cinnamon')
```

## Replacing Data in bytearray

A `bytearray` supports methods like `replace()`.

```python
raw_spice_data = bytearray(b"cinnamon")

raw_spice_data = raw_spice_data.replace(b"cinnamon", b"cardamom")
```

Output:

```text
bytearray(b'cardamom')
```

Important point:

`replace()` returns a new value, so we need to store the result back into a variable.

## Key Takeaways

* Lists are mutable.
* `+` can combine two lists.
* `*` can repeat list items.
* Using operators for different behaviors is called operator overloading.
* `itemgetter` comes from the `operator` module and is useful in advanced list operations.
* `bytearray` is a mutable sequence of bytes.
* `bytearray.replace()` returns a new result, so store it back in a variable.
