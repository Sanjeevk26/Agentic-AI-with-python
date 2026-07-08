# Python OOP: Static Methods and Class Methods

## Overview

Python classes can contain different types of methods:

* Instance methods
* Static methods
* Class methods

They differ mainly in what Python automatically passes as the first argument.

| Method type     | Decorator       | Automatic first argument |
| --------------- | --------------- | ------------------------ |
| Instance method | None            | `self`                   |
| Class method    | `@classmethod`  | `cls`                    |
| Static method   | `@staticmethod` | Nothing                  |

---

# 1. Instance Methods

An instance method works with a specific object.

```python
class ChaiOrder:
    def summary(self):
        return "Order summary"
```

Call it through an object:

```python
order = ChaiOrder()
print(order.summary())
```

Python automatically passes `order` as `self`.

Instance methods can access:

* Instance attributes
* Class attributes
* Other instance methods
* Class methods
* Static methods

---

# 2. Static Methods

A static method is a function placed inside a class for organizational purposes.

It does not automatically receive:

* `self`
* `cls`

Static methods are useful for operations related to a class but independent of any particular object or class state.

## Syntax

```python
class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [
            item.strip()
            for item in text.split(",")
        ]
```

## Calling the Static Method

```python
raw = " water, milk , ginger, honey "

cleaned = ChaiUtils.clean_ingredients(raw)

print(cleaned)
```

Output:

```text
['water', 'milk', 'ginger', 'honey']
```

No object is required.

## How the Method Works

```python
text.split(",")
```

splits the string at every comma.

For example:

```text
" water, milk , ginger, honey "
```

becomes approximately:

```python
[
    " water",
    " milk ",
    " ginger",
    " honey "
]
```

The list comprehension then removes extra spaces:

```python
item.strip()
```

Final result:

```python
['water', 'milk', 'ginger', 'honey']
```

---

# 3. Static Methods Through Objects

A static method can also be called through an object:

```python
utils = ChaiUtils()

cleaned = utils.clean_ingredients(raw)
```

However, creating an object is unnecessary when the method does not use instance data.

The clearer form is:

```python
ChaiUtils.clean_ingredients(raw)
```

---

# 4. Why Use @staticmethod?

Consider a utility function:

```python
def clean_ingredients(text):
    return [item.strip() for item in text.split(",")]
```

If it is strongly related to chai processing, it can be grouped inside a class:

```python
class ChaiUtils:
    @staticmethod
    def clean_ingredients(text):
        return [item.strip() for item in text.split(",")]
```

Benefits include:

* Better organization
* Clear relationship with the class
* No unnecessary object creation
* Easy reuse
* Clear intention that no object state is required

---

# 5. Static Method Example: Validate Cup Size

```python
class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size.lower() in {
            "small",
            "medium",
            "large",
        }
```

Use it:

```python
print(ChaiUtils.is_valid_size("Medium"))
print(ChaiUtils.is_valid_size("Extra Large"))
```

Output:

```text
True
False
```

The method validates a value but does not create or modify an object.

---

# 6. Class Methods

A class method receives the class itself as its first automatic argument.

The conventional parameter name is:

```python
cls
```

## Syntax

```python
class ChaiOrder:
    @classmethod
    def method_name(cls):
        pass
```

Python automatically passes `ChaiOrder` as `cls`.

---

# 7. Normal Object Initialization

Consider this class:

```python
class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size
```

A normal object is created like this:

```python
order = ChaiOrder(
    "Masala Chai",
    "Medium",
    "Large",
)
```

This is the primary initialization method.

---

# 8. Alternate Constructors

Python does not support multiple `__init__` methods with different signatures.

Defining another `__init__` replaces the previous one.

Class methods can provide additional ways to create objects. These are commonly called **alternate constructors** or **factory methods**.

For example, an order might be created from:

* Individual arguments
* A dictionary
* A formatted string

All approaches eventually call the same class.

---

# 9. Alternate Constructor from a Dictionary

```python
class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )
```

Use it:

```python
data = {
    "tea_type": "Masala Chai",
    "sweetness": "Medium",
    "size": "Large",
}

order = ChaiOrder.from_dict(data)
```

Inside the class method:

```python
return cls(...)
```

creates and returns a new object.

It is similar to:

```python
return ChaiOrder(...)
```

but `cls` is preferred because it supports inheritance.

---

# 10. Alternate Constructor from a String

Suppose the input is:

```text
Ginger Chai-Low-Small
```

We can parse it using a class method:

```python
class ChaiOrder:
    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")

        return cls(
            tea_type,
            sweetness,
            size,
        )
```

Use it:

```python
order = ChaiOrder.from_string(
    "Ginger Chai-Low-Small"
)
```

The class method:

1. Receives the string
2. Splits it into values
3. Calls `cls(...)`
4. Returns a new object

---

# 11. Why cls Is Better Than the Class Name

This works:

```python
return ChaiOrder(
    tea_type,
    sweetness,
    size,
)
```

But this is preferable:

```python
return cls(
    tea_type,
    sweetness,
    size,
)
```

Using `cls` supports subclasses.

Example:

```python
class PremiumChaiOrder(ChaiOrder):
    pass
```

Calling:

```python
premium_order = PremiumChaiOrder.from_string(
    "Kesar Chai-Low-Large"
)
```

creates a `PremiumChaiOrder` object because `cls` refers to the class through which the method was called.

If `ChaiOrder(...)` had been hardcoded, it would always create a `ChaiOrder`.

---

# 12. Inspecting Object Attributes with **dict**

Every regular object commonly has a `__dict__` containing its instance attributes.

```python
order = ChaiOrder(
    "Masala Chai",
    "Medium",
    "Large",
)

print(order.__dict__)
```

Output:

```python
{
    'tea_type': 'Masala Chai',
    'sweetness': 'Medium',
    'size': 'Large'
}
```

This is useful for learning and debugging.

Application code should generally access attributes normally:

```python
print(order.tea_type)
```

---

# 13. Static Method vs Class Method

## Static Method

```python
class ChaiUtils:
    @staticmethod
    def is_valid_size(size):
        return size in {"small", "medium", "large"}
```

It:

* Receives no automatic first argument
* Does not access instance state
* Does not access class state automatically
* Usually performs a utility operation
* Usually does not create an object

## Class Method

```python
class ChaiOrder:
    @classmethod
    def from_dict(cls, data):
        return cls(
            data["tea_type"],
            data["sweetness"],
            data["size"],
        )
```

It:

* Automatically receives `cls`
* Can access class attributes
* Can call other class methods
* Can create class instances
* Is useful for alternate constructors

---

# 14. Instance, Class, and Static Method Comparison

| Feature                    | Instance method  | Class method          | Static method           |
| -------------------------- | ---------------- | --------------------- | ----------------------- |
| Automatic argument         | `self`           | `cls`                 | None                    |
| Access instance attributes | Yes              | No direct instance    | No direct instance      |
| Access class attributes    | Yes              | Yes                   | Only through class name |
| Create class objects       | Possible         | Common use            | Possible but uncommon   |
| Typical use                | Object behaviour | Alternate constructor | Utility logic           |
| Decorator                  | None             | `@classmethod`        | `@staticmethod`         |

---

# 15. Complete Example

```python
class ChaiOrder:
    valid_sizes = {
        "small",
        "medium",
        "large",
    }

    def __init__(self, tea_type, sweetness, size):
        if not self.is_valid_size(size):
            raise ValueError("Invalid chai size")

        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @staticmethod
    def is_valid_size(size):
        return size.lower() in ChaiOrder.valid_sizes

    @classmethod
    def from_dict(cls, order_data):
        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )

    @classmethod
    def from_string(cls, order_string):
        tea_type, sweetness, size = order_string.split("-")

        return cls(
            tea_type,
            sweetness,
            size,
        )

    def summary(self):
        return (
            f"{self.size} {self.tea_type} "
            f"with {self.sweetness} sweetness"
        )
```

---

# Key Takeaways

* Static methods use the `@staticmethod` decorator.
* Static methods receive no automatic `self` or `cls`.
* They are useful for related utility functions.
* Class methods use the `@classmethod` decorator.
* Class methods receive the class as `cls`.
* Python supports only one active `__init__` definition per class.
* Class methods can provide alternate ways to create objects.
* `return cls(...)` creates an object of the current class.
* Using `cls` works correctly with subclasses.
* `__dict__` shows attributes stored on an object.
* Instance methods work with objects, class methods work with classes, and static methods perform independent utility logic.
