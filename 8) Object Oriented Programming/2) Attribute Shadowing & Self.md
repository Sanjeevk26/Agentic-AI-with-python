# Python OOP: Attribute Shadowing, Methods, and self

## Overview

This lesson covers three important object-oriented programming concepts:

* Class attributes
* Attribute shadowing
* Instance methods and the `self` parameter

These concepts explain how Python stores and accesses data inside classes and objects.

---

# 1. Attributes in Python

A variable associated with a class or object is called an **attribute**.

Example:

```python
class Chai:
    temperature = "Hot"
    strength = "Strong"
```

Here:

* `temperature` is a class attribute
* `strength` is a class attribute

They belong to the `Chai` class.

## Accessing Class Attributes

```python
print(Chai.temperature)
print(Chai.strength)
```

Output:

```text
Hot
Strong
```

Objects created from the class can also access these attributes.

```python
cutting_chai = Chai()

print(cutting_chai.temperature)
print(cutting_chai.strength)
```

---

# 2. Attribute Shadowing

Attribute shadowing happens when an object defines an attribute with the same name as an attribute available on its class.

Example:

```python
class Chai:
    temperature = "Hot"


cutting_chai = Chai()

cutting_chai.temperature = "Mild"
```

The object now has its own `temperature` attribute.

## Checking the Values

```python
print(cutting_chai.temperature)
print(Chai.temperature)
```

Output:

```text
Mild
Hot
```

The instance value shadows the class value.

It does not change the original class attribute.

## How Python Finds an Attribute

When Python evaluates:

```python
cutting_chai.temperature
```

it generally checks:

1. The object's namespace
2. The object's class
3. Parent classes, if inheritance is involved

After this assignment:

```python
cutting_chai.temperature = "Mild"
```

the object has its own value, so Python uses it before checking the class.

---

# 3. Deleting a Shadowing Attribute

We can delete the instance attribute using `del`.

```python
del cutting_chai.temperature
```

After deletion:

```python
print(cutting_chai.temperature)
```

Output:

```text
Hot
```

The object no longer has its own `temperature` attribute, so Python falls back to the class attribute.

## Attribute Lookup Before and After Deletion

Before deletion:

```text
cutting_chai.temperature
        ↓
Instance namespace contains "Mild"
        ↓
Result: Mild
```

After deletion:

```text
cutting_chai.temperature
        ↓
Instance namespace does not contain temperature
        ↓
Class namespace contains "Hot"
        ↓
Result: Hot
```

---

# 4. Deleting an Instance-Only Attribute

An object can have an attribute that does not exist on the class.

```python
cutting_chai.cup_size = "Small"
```

This attribute exists only on `cutting_chai`.

```python
print(cutting_chai.cup_size)
```

Output:

```text
Small
```

If it is deleted:

```python
del cutting_chai.cup_size
```

and then accessed again:

```python
print(cutting_chai.cup_size)
```

Python raises:

```text
AttributeError
```

This happens because:

* The object no longer has `cup_size`
* The class does not have `cup_size`
* No fallback value exists

## Safe Attribute Check

Use `hasattr()` before accessing an optional attribute.

```python
if hasattr(cutting_chai, "cup_size"):
    print(cutting_chai.cup_size)
else:
    print("cup_size does not exist")
```

---

# 5. Inspecting Shadowing with **dict**

The object's `__dict__` shows attributes stored directly on that object.

```python
class Chai:
    temperature = "Hot"


cutting_chai = Chai()

print(cutting_chai.__dict__)
```

Output:

```text
{}
```

The object initially has no instance attributes.

After shadowing:

```python
cutting_chai.temperature = "Mild"

print(cutting_chai.__dict__)
```

Output:

```text
{'temperature': 'Mild'}
```

After deletion:

```python
del cutting_chai.temperature

print(cutting_chai.__dict__)
```

Output:

```text
{}
```

The class attribute still exists:

```python
print(Chai.temperature)
```

---

# 6. Functions and Methods

A function defined inside a class is usually called a **method**.

Example:

```python
class ChaiCup:
    def describe(self):
        return "This is a chai cup"
```

Here, `describe()` is an instance method.

The indentation shows that it belongs to the class.

---

# 7. Understanding self

`self` refers to the specific object that called the method.

Example:

```python
class ChaiCup:
    size = 150

    def describe(self):
        return f"A {self.size} ml chai cup"
```

Create an object:

```python
cup = ChaiCup()
```

Call the method:

```python
print(cup.describe())
```

Output:

```text
A 150 ml chai cup
```

When we write:

```python
cup.describe()
```

Python effectively behaves like:

```python
ChaiCup.describe(cup)
```

The object `cup` is automatically passed as the first argument.

Inside the method, that object is referenced using `self`.

---

# 8. Why self Is Required

Consider:

```python
class ChaiCup:
    size = 150

    def describe(self):
        return f"A {self.size} ml chai cup"
```

The method needs to know which object is calling it.

There may be multiple objects:

```python
cup_one = ChaiCup()
cup_two = ChaiCup()

cup_two.size = 100
```

Now:

```python
print(cup_one.describe())
print(cup_two.describe())
```

Output:

```text
A 150 ml chai cup
A 100 ml chai cup
```

`self` allows the method to access the correct object's data.

For `cup_one.describe()`, `self` refers to `cup_one`.

For `cup_two.describe()`, `self` refers to `cup_two`.

---

# 9. Calling a Method Through the Class

An instance method can also be called through the class.

```python
print(ChaiCup.describe(cup_one))
print(ChaiCup.describe(cup_two))
```

In this form, the instance must be passed manually.

This works:

```python
ChaiCup.describe(cup_one)
```

This does not work:

```python
ChaiCup.describe()
```

Python raises a `TypeError` because the required `self` argument is missing.

---

# 10. self Is a Convention

The word `self` is not a reserved Python keyword.

Technically, another parameter name could be used:

```python
class ChaiCup:
    size = 150

    def describe(current_object):
        return current_object.size
```

This works, but it is strongly recommended to use `self`.

```python
def describe(self):
```

Using `self` makes the code familiar and readable for other Python developers.

---

# 11. Class Attributes and Instance Attributes Inside Methods

Consider:

```python
class ChaiCup:
    size = 150

    def describe(self):
        return self.size
```

If the object has no instance-specific `size`, Python gets it from the class.

```python
cup = ChaiCup()

print(cup.size)
```

Output:

```text
150
```

If we assign:

```python
cup.size = 100
```

the object now shadows the class attribute.

```python
print(cup.describe())
```

Output:

```text
100
```

The expression `self.size` follows normal attribute lookup rules.

---

# Key Takeaways

* Variables associated with classes or objects are called attributes.
* Class attributes belong to the class.
* Instance attributes belong to individual objects.
* Attribute shadowing occurs when an instance attribute has the same name as a class attribute.
* Shadowing does not modify the original class attribute.
* Deleting the instance attribute reveals the class attribute again.
* If no class fallback exists, accessing a deleted attribute raises `AttributeError`.
* A function inside a class is called a method.
* `self` refers to the object calling an instance method.
* Python automatically passes the object when calling `object.method()`.
* Calling a method through the class requires passing the instance manually.
* `self` is a convention, not a reserved keyword.
