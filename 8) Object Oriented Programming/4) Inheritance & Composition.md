# Python OOP: Inheritance and Composition

## Overview

Inheritance and composition are two important ways to reuse code in object-oriented programming.

They solve different problems:

* **Inheritance** represents an **is-a** relationship.
* **Composition** represents a **has-a** relationship.

Example:

* `MasalaChai` **is a** type of `BaseChai`.
* `ChaiShop` **has a** chai object.

---

# 1. Inheritance

Inheritance allows one class to reuse the attributes and methods of another class.

The existing class is usually called the:

* Base class
* Parent class
* Superclass

The new class is usually called the:

* Derived class
* Child class
* Subclass

## Base Class

```python
class BaseChai:
    def __init__(self, chai_type):
        self.chai_type = chai_type

    def prepare(self):
        return f"Preparing {self.chai_type}..."
```

The `BaseChai` class provides common chai functionality.

## Child Class

```python
class MasalaChai(BaseChai):
    def add_spices(self):
        return "Adding cardamom, ginger, and clove"
```

The class name inside parentheses shows inheritance:

```python
class MasalaChai(BaseChai):
```

This means:

```text
MasalaChai is a BaseChai
```

## Creating an Object

```python
chai = MasalaChai("Masala Chai")

print(chai.prepare())
print(chai.add_spices())
```

Output:

```text
Preparing Masala Chai...
Adding cardamom, ginger, and clove
```

`MasalaChai` can use:

* Its own `add_spices()` method
* The inherited `prepare()` method
* The inherited `chai_type` attribute

---

# 2. Inherited Constructor

If a child class does not define its own `__init__`, Python uses the constructor inherited from the parent class.

```python
class BaseChai:
    def __init__(self, chai_type):
        self.chai_type = chai_type


class MasalaChai(BaseChai):
    pass
```

This works:

```python
chai = MasalaChai("Masala Chai")
```

The `BaseChai.__init__()` method initializes the object.

---

# 3. Child Constructor and super()

If the child class needs additional attributes, it can define its own constructor.

Use `super()` to call the parent constructor.

```python
class MasalaChai(BaseChai):
    def __init__(self, chai_type, spice_level):
        super().__init__(chai_type)
        self.spice_level = spice_level
```

Example:

```python
chai = MasalaChai("Masala Chai", "Strong")
```

Here:

```python
super().__init__(chai_type)
```

initializes the parent-class attributes.

Then:

```python
self.spice_level = spice_level
```

initializes the child-specific attribute.

---

# 4. Method Overriding

A child class can replace an inherited method with its own implementation.

```python
class BaseChai:
    def prepare(self):
        return "Preparing regular chai"


class MasalaChai(BaseChai):
    def prepare(self):
        return "Preparing masala chai with spices"
```

Now:

```python
chai = MasalaChai()
print(chai.prepare())
```

Output:

```text
Preparing masala chai with spices
```

The child method overrides the parent method.

## Calling the Parent Version

A child can still call the parent implementation using `super()`.

```python
class MasalaChai(BaseChai):
    def prepare(self):
        base_message = super().prepare()
        return f"{base_message} and adding spices"
```

---

# 5. Composition

Composition means one class stores and uses an object of another class.

Example:

```python
class ChaiShop:
    def __init__(self, chai):
        self.chai = chai
```

Here, `ChaiShop` does not inherit from `BaseChai`.

Instead, it contains a chai object.

This creates a:

```text
ChaiShop has a chai
```

relationship.

## Complete Composition Example

```python
class BaseChai:
    def __init__(self, chai_type):
        self.chai_type = chai_type

    def prepare(self):
        return f"Preparing {self.chai_type}..."


class ChaiShop:
    def __init__(self, chai):
        self.chai = chai

    def serve(self):
        preparation = self.chai.prepare()
        return f"{preparation}\nServing {self.chai.chai_type}"
```

Use it like this:

```python
regular_chai = BaseChai("Regular Chai")
shop = ChaiShop(regular_chai)

print(shop.serve())
```

Output:

```text
Preparing Regular Chai...
Serving Regular Chai
```

---

# 6. Why Composition Is Useful

Composition allows a class to work with different objects that provide the required behaviour.

Example:

```python
masala_chai = MasalaChai("Masala Chai")
shop = ChaiShop(masala_chai)

print(shop.serve())
```

The shop does not need to know every detail of `MasalaChai`.

It only needs a chai object that provides:

```python
prepare()
```

and:

```python
chai_type
```

This makes the code flexible.

---

# 7. Inheritance and Composition Together

A class can use both inheritance and composition.

```python
class FancyChaiShop(ChaiShop):
    def serve_with_style(self):
        normal_service = self.serve()
        return f"{normal_service}\nServed in a premium cup"
```

Here:

* `FancyChaiShop` inherits from `ChaiShop`
* `ChaiShop` contains a chai object

Example:

```python
masala_chai = MasalaChai("Masala Chai")
fancy_shop = FancyChaiShop(masala_chai)

print(fancy_shop.serve_with_style())
```

This combines:

```text
FancyChaiShop is a ChaiShop
```

and:

```text
FancyChaiShop has a chai
```

---

# 8. Accessing Composed Objects

If a shop contains a chai object:

```python
self.chai = chai
```

the shop can access the chai object's attributes and methods.

```python
self.chai.chai_type
self.chai.prepare()
```

If the contained object is a `MasalaChai`, it can also access child-specific methods:

```python
self.chai.add_spices()
```

However, this only works if the stored object actually provides that method.

A safer check is:

```python
if hasattr(self.chai, "add_spices"):
    print(self.chai.add_spices())
```

---

# 9. Class Reference vs Object

This stores a reference to a class:

```python
chai_class = BaseChai
```

No object has been created yet.

An object is created when parentheses are used:

```python
chai = chai_class("Regular Chai")
```

This distinction is important.

## Class Reference

```python
chai_class = BaseChai
```

## Object Creation

```python
chai = BaseChai("Regular Chai")
```

For normal composition, storing an already-created object is usually clearer:

```python
class ChaiShop:
    def __init__(self, chai):
        self.chai = chai
```

---

# 10. Inheritance vs Composition

| Inheritance                       | Composition                         |
| --------------------------------- | ----------------------------------- |
| Represents an `is-a` relationship | Represents a `has-a` relationship   |
| Child class extends a parent      | Class stores another object         |
| Uses class-name parentheses       | Uses instance attributes            |
| Can override parent methods       | Delegates work to contained objects |
| Creates tighter coupling          | Usually offers more flexibility     |

## Inheritance Example

```python
class MasalaChai(BaseChai):
    pass
```

`MasalaChai` is a `BaseChai`.

## Composition Example

```python
class ChaiShop:
    def __init__(self, chai):
        self.chai = chai
```

`ChaiShop` has a chai.

---

# 11. When to Use Inheritance

Inheritance is useful when:

* The child is genuinely a specialized form of the parent
* Parent behaviour should be reused
* Objects should be treated as the parent type
* Method overriding is useful

Examples:

* `MasalaChai` is a `BaseChai`
* `Manager` is an `Employee`
* `ElectricCar` is a `Car`

---

# 12. When to Use Composition

Composition is useful when:

* One class needs the services of another object
* Behaviour may change at runtime
* Different implementations should be interchangeable
* You want to avoid tightly coupled inheritance hierarchies

Examples:

* `ChaiShop` has a `Chai`
* `Car` has an `Engine`
* `OrderService` has a `PaymentProcessor`

Composition is commonly preferred in production code because it makes components easier to replace and test.

---

# Key Takeaways

* Inheritance lets one class reuse another class.
* Inheritance represents an `is-a` relationship.
* Composition stores an object inside another object.
* Composition represents a `has-a` relationship.
* A child inherits the parent constructor if it does not define one.
* Use `super()` to call parent-class methods and constructors.
* A child class can override inherited methods.
* Composition delegates work to contained objects.
* A class can use inheritance and composition together.
* Storing an object is different from storing a class reference.
* Prefer composition when interchangeable behaviour and flexibility are important.
