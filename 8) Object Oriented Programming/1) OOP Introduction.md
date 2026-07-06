# Python OOP: Classes, Objects, and Namespaces

## Overview

Object-Oriented Programming, commonly called **OOP**, is a programming style used to organize code around classes and objects.

Python supports multiple programming styles, including:

* Procedural programming
* Functional programming
* Object-oriented programming

Real-world applications often use a combination of these styles.

## What Is a Class?

A class is a blueprint used to create objects.

For example, a `Chai` class can describe common properties and behaviour shared by different chai objects.

Basic syntax:

```python
class Chai:
    pass
```

Here:

* `class` is a Python keyword
* `Chai` is the class name
* `pass` creates an empty class

Class names usually follow PascalCase naming.

Examples:

```python
class Chai:
    pass


class ChaiTime:
    pass
```

## What Is an Object?

An object is an individual instance created from a class.

```python
class Chai:
    pass


ginger_tea = Chai()
```

Here:

* `Chai` is the class
* `ginger_tea` is an object of the `Chai` class

Multiple objects can be created from one class:

```python
masala_chai = Chai()
ginger_chai = Chai()
lemon_chai = Chai()
```

Each object is independent.

## Classes Are Also Objects in Python

In Python, classes themselves are objects.

```python
class Chai:
    pass


print(type(Chai))
```

Output:

```text
<class 'type'>
```

The class `Chai` is an object created by Python's built-in `type` class.

## Checking an Object's Type

```python
class Chai:
    pass


ginger_tea = Chai()

print(type(ginger_tea))
```

Output:

```text
<class '__main__.Chai'>
```

This tells us that `ginger_tea` is an instance of the `Chai` class.

## Using isinstance()

`isinstance()` checks whether an object belongs to a particular class.

```python
class Chai:
    pass


class ChaiTime:
    pass


ginger_tea = Chai()

print(isinstance(ginger_tea, Chai))
print(isinstance(ginger_tea, ChaiTime))
```

Output:

```text
True
False
```

`ginger_tea` belongs to `Chai`, but not to `ChaiTime`.

## Class Attributes

A variable defined inside a class is called a class attribute.

```python
class Chai:
    origin = "India"
```

It can be accessed using the class:

```python
print(Chai.origin)
```

Output:

```text
India
```

It can also be accessed through an object:

```python
masala_chai = Chai()

print(masala_chai.origin)
```

Output:

```text
India
```

## Adding a Class Attribute Later

Python allows attributes to be added after the class has been created.

```python
class Chai:
    origin = "India"


Chai.is_hot = True
```

Now both attributes are available:

```python
print(Chai.origin)
print(Chai.is_hot)
```

However, defining known class attributes inside the class is normally clearer.

## Instance Attributes

An attribute stored directly on an object is called an instance attribute.

```python
class Chai:
    origin = "India"
    is_hot = True


masala_chai = Chai()

masala_chai.flavor = "Masala"
```

The `flavor` attribute belongs specifically to `masala_chai`.

```python
print(masala_chai.flavor)
```

## Class Namespace and Instance Namespace

A namespace is a place where Python stores names and their values.

A class has its own namespace.

Each object also has its own namespace.

Example:

```python
class Chai:
    origin = "India"
    is_hot = True


masala_chai = Chai()
ginger_chai = Chai()
```

Initially, both objects can access the class attributes:

```python
print(masala_chai.is_hot)
print(ginger_chai.is_hot)
```

Output:

```text
True
True
```

## Overriding a Class Attribute on an Object

An object can have its own value for an attribute.

```python
masala_chai.is_hot = False
```

Now:

```python
print(Chai.is_hot)
print(masala_chai.is_hot)
print(ginger_chai.is_hot)
```

Output:

```text
True
False
True
```

Changing `masala_chai.is_hot` does not change:

* The class attribute
* Other objects
* Future objects created from the class

Python stores `False` inside the namespace of `masala_chai`.

## Attribute Lookup

When we access:

```python
masala_chai.is_hot
```

Python generally checks:

1. The object's namespace
2. The object's class
3. Parent classes, if inheritance is involved

Before the override, `masala_chai` reads `is_hot` from the class.

After this line:

```python
masala_chai.is_hot = False
```

the object has its own `is_hot` value, which takes priority over the class value.

## Inspecting Namespaces with **dict**

Python allows us to inspect many class and object namespaces using `__dict__`.

```python
class Chai:
    origin = "India"
    is_hot = True


masala_chai = Chai()
masala_chai.is_hot = False
masala_chai.flavor = "Masala"

print(masala_chai.__dict__)
```

Output:

```text
{'is_hot': False, 'flavor': 'Masala'}
```

The object only stores attributes specifically assigned to it.

The inherited `origin` attribute remains in the class namespace.

```python
print(Chai.__dict__)
```

This contains the attributes defined on the class.

## Adding Unique Attributes to Objects

Different objects can have different attributes.

```python
class Chai:
    origin = "India"


masala_chai = Chai()
green_tea = Chai()

masala_chai.flavor = "Spiced"
green_tea.flavor = "Fresh"

masala_chai.milk = True
green_tea.milk = False
```

These values remain separate because every object has its own namespace.

## Important Terminology

| Term               | Meaning                                     |
| ------------------ | ------------------------------------------- |
| Class              | Blueprint used to create objects            |
| Object             | Individual instance of a class              |
| Attribute          | Data associated with a class or object      |
| Class attribute    | Shared attribute defined on the class       |
| Instance attribute | Attribute stored on one object              |
| Namespace          | Mapping between names and values            |
| `type()`           | Returns the type of an object               |
| `isinstance()`     | Checks whether an object belongs to a class |

## Key Takeaways

* OOP is a way of organizing programs using classes and objects.
* A class acts as a blueprint.
* An object is an instance of a class.
* Classes are also objects in Python.
* `type()` shows the type of a class or object.
* `isinstance()` checks class membership.
* Class attributes are shared through the class.
* Objects can override class attributes without changing the class.
* Every object can maintain its own independent namespace.
* Instance attributes belong only to the object on which they are created.
