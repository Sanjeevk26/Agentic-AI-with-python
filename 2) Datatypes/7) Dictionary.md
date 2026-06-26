# Python Dictionaries

## Overview

A dictionary is a built-in Python data type used to store data in **key-value pairs**.

Unlike lists, where values are accessed using numeric indexes like `0`, `1`, and `2`, dictionaries allow us to access values using meaningful names called **keys**.

## Why Dictionaries Are Needed

In a list, values are accessed using index numbers.

```python
chai_items = ["ginger", "lemon"]
```

To access `"ginger"`, we use:

```python
chai_items[0]
```

But sometimes, using numbers is not clear.

A dictionary solves this by allowing named access.

```python
user = {
    "first_name": "Sanjeev",
    "last_name": "Khatwani"
}
```

Now we can access data using names:

```python
user["first_name"]
```

## Creating a Dictionary

A dictionary can be created using the `dict()` function.

```python
chai_order = dict(
    type="Masala Chai",
    size="Large",
    sugar=2
)
```

Output:

```text
{'type': 'Masala Chai', 'size': 'Large', 'sugar': 2}
```

## Creating an Empty Dictionary

An empty dictionary is created using curly braces `{}`.

```python
chai_recipe = {}
```

## Adding Data to a Dictionary

Data can be added using square brackets and a key name.

```python
chai_recipe["base"] = "Black Tea"
chai_recipe["liquid"] = "Milk"
```

Now the dictionary contains:

```python
{
    "base": "Black Tea",
    "liquid": "Milk"
}
```

## Accessing Data

Dictionary values are accessed using their keys.

```python
print(chai_recipe["base"])
```

Output:

```text
Black Tea
```

## Deleting Data

The `del` keyword is used to delete a key-value pair.

```python
del chai_recipe["liquid"]
```

After deletion:

```python
{
    "base": "Black Tea"
}
```

## Membership Testing

The `in` keyword checks whether a key exists in a dictionary.

```python
"sugar" in chai_order
```

Output:

```text
True
```

Important: By default, membership testing checks keys, not values.

## Dictionary keys()

The `keys()` method returns all keys from the dictionary.

```python
chai_order.keys()
```

Example output:

```text
dict_keys(['type', 'size', 'sugar'])
```

## Dictionary values()

The `values()` method returns all values from the dictionary.

```python
chai_order.values()
```

Example output:

```text
dict_values(['Ginger Chai', 'Medium', 1])
```

## Dictionary items()

The `items()` method returns key-value pairs.

```python
chai_order.items()
```

Example output:

```text
dict_items([('type', 'Ginger Chai'), ('size', 'Medium'), ('sugar', 1)])
```

Each item is returned as a tuple containing a key and a value.

## popitem()

The `popitem()` method removes and returns the last inserted key-value pair.

```python
last_item = chai_order.popitem()
```

Example output:

```text
('sugar', 1)
```

## Updating a Dictionary

The `update()` method adds new key-value pairs or updates existing ones.

```python
extra_spices = {
    "cardamom": "crushed",
    "ginger": "sliced"
}

chai_recipe.update(extra_spices)
```

Updated dictionary:

```python
{
    "base": "Black Tea",
    "cardamom": "crushed",
    "ginger": "sliced"
}
```

## Safe Access with get()

Accessing a missing key directly can crash the program.

```python
chai_order["customer_note"]
```

If the key does not exist, Python gives an error.

A safer way is to use `get()`.

```python
customer_note = chai_order.get("customer_note", "No note given")
```

If `"customer_note"` does not exist, the default value is returned.

Output:

```text
No note given
```

## Key Takeaways

* Dictionaries store data in key-value pairs.
* Keys make data easier to access than numeric indexes.
* Dictionaries are created using `{}` or `dict()`.
* Use square brackets `[]` to add or access values.
* Use `del` to remove a specific key-value pair.
* Use `in` to check whether a key exists.
* Use `keys()` to get all keys.
* Use `values()` to get all values.
* Use `items()` to get key-value pairs.
* Use `popitem()` to remove the last item.
* Use `update()` to merge or update data.
* Use `get()` for safe access to avoid errors.
