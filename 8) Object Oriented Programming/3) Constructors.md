# Python OOP: The **init** Method and Object Initialization

## Overview

The `__init__` method is used to initialize an object when it is created from a class.

It allows every object to receive its own starting values.

Example:

```python
order = ChaiOrder("Masala Chai", 200)
```

When this object is created, Python automatically calls the class's `__init__` method.

---

# 1. Why **init** Is Needed

Consider a basic class:

```python
class ChaiOrder:
    pass
```

We can create an object:

```python
order = ChaiOrder()
```

However, the object does not yet contain details such as:

* Chai type
* Cup size
* Sugar level
* Milk preference

The `__init__` method allows us to provide these values while creating the object.

---

# 2. Basic **init** Syntax

```python
class ChaiOrder:
    def __init__(self, chai_type, size):
        self.chai_type = chai_type
        self.size = size
```

Here:

* `self` refers to the object being created
* `chai_type` is a parameter
* `size` is a parameter
* `self.chai_type` is an instance attribute
* `self.size` is an instance attribute

## Creating an Object

```python
order = ChaiOrder("Masala Chai", 200)
```

Python automatically passes the new object as `self`.

Conceptually, Python performs something similar to:

```python
ChaiOrder.__init__(order, "Masala Chai", 200)
```

We do not pass `self` manually when using the normal object-creation syntax.

---

# 3. Instance Attributes

Attributes created with `self` belong to the individual object.

```python
self.chai_type = chai_type
self.size = size
```

Each object receives its own values.

```python
order_one = ChaiOrder("Masala Chai", 200)
order_two = ChaiOrder("Ginger Chai", 220)
```

Now:

```python
print(order_one.chai_type)
print(order_two.chai_type)
```

Output:

```text
Masala Chai
Ginger Chai
```

Changing one object's attributes does not change the other object.

---

# 4. Adding an Instance Method

A method can use the attributes initialized by `__init__`.

```python
class ChaiOrder:
    def __init__(self, chai_type, size):
        self.chai_type = chai_type
        self.size = size

    def summary(self):
        return f"{self.size} ml of {self.chai_type}"
```

Use it like this:

```python
order = ChaiOrder("Masala Chai", 200)

print(order.summary())
```

Output:

```text
200 ml of Masala Chai
```

---

# 5. Multiple Objects

```python
order_one = ChaiOrder("Masala Chai", 200)
order_two = ChaiOrder("Ginger Chai", 220)
```

Each object has a separate namespace.

```python
print(order_one.__dict__)
print(order_two.__dict__)
```

Possible output:

```text
{'chai_type': 'Masala Chai', 'size': 200}
{'chai_type': 'Ginger Chai', 'size': 220}
```

The objects were created from the same class but contain different data.

---

# 6. Parameters and Attributes

Consider:

```python
def __init__(self, chai_type, size):
    self.chai_type = chai_type
    self.size = size
```

The names on the right are parameters:

```python
chai_type
size
```

The names on the left are instance attributes:

```python
self.chai_type
self.size
```

This line:

```python
self.size = size
```

means:

```text
Store the received size value inside the current object.
```

Using matching names is common and readable, but it is not mandatory.

This also works:

```python
def __init__(self, order_type, cup_size):
    self.chai_type = order_type
    self.size = cup_size
```

---

# 7. Avoiding Built-in Names

Python has built-in names such as:

```python
type
list
str
dict
set
```

It is better not to reuse these names as variables or parameters.

Instead of:

```python
def __init__(self, type, size):
```

use:

```python
def __init__(self, chai_type, size):
```

Another common convention is to add a trailing underscore:

```python
def __init__(self, type_, size):
```

Then:

```python
self.type = type_
```

A clearer domain-specific name such as `chai_type` is usually preferable.

---

# 8. Default Initialization Values

Parameters can have default values.

```python
class ChaiOrder:
    def __init__(self, chai_type, size=150):
        self.chai_type = chai_type
        self.size = size
```

Now both calls are valid:

```python
order_one = ChaiOrder("Masala Chai")
order_two = ChaiOrder("Ginger Chai", 220)
```

The first object uses the default size of `150`.

---

# 9. Keyword Arguments

Objects can also be initialized using keyword arguments.

```python
order = ChaiOrder(
    chai_type="Lemon Tea",
    size=250
)
```

Keyword arguments improve readability when a class accepts several values.

---

# 10. Validating Values in **init**

The `__init__` method can validate incoming data.

```python
class ChaiOrder:
    def __init__(self, chai_type, size):
        if size <= 0:
            raise ValueError("Size must be greater than zero")

        self.chai_type = chai_type
        self.size = size
```

Now this is invalid:

```python
order = ChaiOrder("Masala Chai", -100)
```

It raises:

```text
ValueError: Size must be greater than zero
```

---

# 11. **init** and Constructors

The `__init__` method is commonly called a constructor in everyday Python discussions.

Technically:

* `__new__` creates the new object
* `__init__` initializes the already-created object

For most normal Python classes, developers mainly work with `__init__`.

---

# 12. Attributes Can Also Be Added Later

Although `__init__` is the preferred place for required instance attributes, Python also allows attributes to be added in other methods or after object creation.

Example:

```python
order.sugar = "Low"
```

A method can also create an attribute:

```python
class ChaiOrder:
    def add_note(self, note):
        self.note = note
```

However, attributes that every object requires should usually be initialized in `__init__`.

---

# Complete Example

```python
class ChaiOrder:
    def __init__(self, chai_type, size):
        self.chai_type = chai_type
        self.size = size

    def summary(self):
        return f"{self.size} ml of {self.chai_type}"


order_one = ChaiOrder("Masala Chai", 200)
order_two = ChaiOrder("Ginger Chai", 220)

print(order_one.summary())
print(order_two.summary())
```

Output:

```text
200 ml of Masala Chai
220 ml of Ginger Chai
```

---

# Key Takeaways

* `__init__` initializes a newly created object.
* Python calls `__init__` automatically during object creation.
* `self` refers to the current object.
* Parameters provide values to the initializer.
* `self.attribute` stores values on the object.
* Every object can have different attribute values.
* Instance methods can access attributes using `self`.
* Use clear parameter names and avoid shadowing Python built-ins.
* Required object attributes should normally be initialized inside `__init__`.
* Technically, `__new__` creates the object and `__init__` initializes it.
