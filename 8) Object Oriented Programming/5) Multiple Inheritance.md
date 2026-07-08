# Python OOP: Multiple Inheritance and Method Resolution Order

## Overview

Multiple inheritance allows a Python class to inherit from more than one parent class.

Example:

```python
class Child(ParentOne, ParentTwo):
    pass
```

The child class receives access to attributes and methods available through both parent classes.

However, multiple parent classes may contain attributes or methods with the same name.

Python must then decide which implementation should be used.

This search order is called the **Method Resolution Order**, commonly known as **MRO**.

---

# 1. Basic Multiple Inheritance

```python
class MasalaBlend:
    label = "Masala Blend"


class HerbalBlend:
    label = "Herbal Blend"


class SpecialBlend(MasalaBlend, HerbalBlend):
    pass
```

Create an object:

```python
cup = SpecialBlend()

print(cup.label)
```

Output:

```text
Masala Blend
```

Python checks `MasalaBlend` before `HerbalBlend` because it appears first in the inheritance list.

```python
class SpecialBlend(MasalaBlend, HerbalBlend):
```

If the order is reversed:

```python
class SpecialBlend(HerbalBlend, MasalaBlend):
    pass
```

the output becomes:

```text
Herbal Blend
```

---

# 2. What Is Method Resolution Order?

Method Resolution Order is the order Python follows when searching for:

* Methods
* Class attributes
* Properties
* Other inherited members

For an expression such as:

```python
cup.label
```

Python follows the MRO until it finds `label`.

---

# 3. Diamond Inheritance

A common multiple-inheritance structure is called the **diamond pattern**.

```text
        A
       / \
      B   C
       \ /
        D
```

Here:

* `B` inherits from `A`
* `C` inherits from `A`
* `D` inherits from both `B` and `C`

Python must search this hierarchy in a consistent order.

## Example

```python
class A:
    label = "Base Class"


class B(A):
    label = "Masala Blend"


class C(A):
    label = "Herbal Blend"


class D(B, C):
    pass
```

Create an object:

```python
cup = D()

print(cup.label)
```

Output:

```text
Masala Blend
```

Python finds `label` in `B` before checking `C`.

---

# 4. MRO for the Diamond Example

For:

```python
class D(B, C):
    pass
```

the MRO is:

```text
D
B
C
A
object
```

Python searches for an attribute in that order.

When evaluating:

```python
cup.label
```

Python checks:

1. `D`
2. `B`
3. `C`
4. `A`
5. `object`

Since `B` contains `label`, the search stops there.

---

# 5. Changing the Parent Order

If the inheritance order changes:

```python
class D(C, B):
    pass
```

the MRO becomes:

```text
D
C
B
A
object
```

Now:

```python
cup = D()
print(cup.label)
```

Output:

```text
Herbal Blend
```

The order of base classes matters.

---

# 6. Viewing the MRO

Python provides multiple ways to inspect a class's MRO.

## Using mro()

```python
print(D.mro())
```

This returns a list of classes.

## Using **mro**

```python
print(D.__mro__)
```

This returns a tuple of classes.

A readable version can be printed like this:

```python
for class_ in D.mro():
    print(class_.__name__)
```

Output:

```text
D
B
C
A
object
```

---

# 7. MRO Applies to Methods Too

MRO is not limited to class attributes.

It also determines which method is called.

```python
class A:
    def prepare(self):
        return "Preparing base chai"


class B(A):
    def prepare(self):
        return "Preparing masala chai"


class C(A):
    def prepare(self):
        return "Preparing herbal chai"


class D(B, C):
    pass
```

Now:

```python
cup = D()

print(cup.prepare())
```

Output:

```text
Preparing masala chai
```

Python finds `prepare()` in `B` first.

---

# 8. When the First Parent Does Not Have the Attribute

Python does not automatically stop at the first parent.

It continues through the complete MRO.

```python
class A:
    label = "Base Class"


class B(A):
    pass


class C(A):
    label = "Herbal Blend"


class D(B, C):
    pass
```

The MRO is:

```text
D
B
C
A
object
```

When Python searches for `label`:

1. `D` does not contain it
2. `B` does not contain it directly
3. `C` contains it

Therefore:

```python
print(D().label)
```

Output:

```text
Herbal Blend
```

This is why MRO is more than simply “always use the first parent.”

---

# 9. C3 Linearization

Python calculates the MRO using an algorithm called **C3 linearization**.

Its purpose is to produce an order that is:

* Consistent
* Predictable
* Respectful of the declared parent order
* Suitable for diamond inheritance
* Compatible with cooperative `super()` calls

You normally do not need to calculate C3 linearization manually.

Use:

```python
ClassName.mro()
```

to inspect the result.

---

# 10. Invalid Multiple-Inheritance Order

Some class hierarchies cannot produce a consistent MRO.

Example:

```python
class A:
    pass


class B:
    pass


class X(A, B):
    pass


class Y(B, A):
    pass
```

Trying to create:

```python
class Z(X, Y):
    pass
```

raises a `TypeError`.

The problem is:

* `X` requires `A` before `B`
* `Y` requires `B` before `A`

Python cannot create one consistent resolution order.

---

# 11. Multiple Inheritance and super()

`super()` follows the MRO.

It does not always mean “call my direct parent.”

Example:

```python
class A:
    def prepare(self):
        print("A preparing")


class B(A):
    def prepare(self):
        print("B preparing")
        super().prepare()


class C(A):
    def prepare(self):
        print("C preparing")
        super().prepare()


class D(B, C):
    def prepare(self):
        print("D preparing")
        super().prepare()
```

For `D`, the MRO is:

```text
D → B → C → A → object
```

Calling:

```python
D().prepare()
```

produces:

```text
D preparing
B preparing
C preparing
A preparing
```

Each `super()` call moves to the next class in the MRO.

---

# 12. Cooperative Multiple Inheritance

When multiple classes participate in the same operation, they should generally:

* Use `super()`
* Accept compatible parameters
* Avoid directly calling one named parent
* Pass remaining arguments forward when necessary

Example:

```python
class A:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("A initialized")


class B(A):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("B initialized")


class C(A):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("C initialized")


class D(B, C):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("D initialized")
```

This allows every class in the MRO to participate.

---

# 13. Advantages of Multiple Inheritance

Multiple inheritance can help:

* Combine independent behaviours
* Create reusable mixins
* Share framework functionality
* Avoid copying common methods
* Build flexible class hierarchies

Example:

```python
class LoggingMixin:
    def log(self, message):
        print(f"LOG: {message}")


class ChaiOrder:
    def place_order(self):
        print("Order placed")


class LoggedChaiOrder(LoggingMixin, ChaiOrder):
    pass
```

The child receives behaviour from both classes.

---

# 14. Risks of Multiple Inheritance

Multiple inheritance can also create:

* Confusing class hierarchies
* Name conflicts
* Unexpected method selection
* Constructor compatibility problems
* Difficult debugging
* Strong coupling between classes

Use it carefully and inspect the MRO when behaviour is unclear.

---

# Key Takeaways

* Multiple inheritance allows a class to inherit from multiple classes.
* Parent classes are separated using commas.
* MRO determines where Python searches for attributes and methods.
* The order of parent classes affects the MRO.
* Python uses C3 linearization to calculate a consistent order.
* Use `ClassName.mro()` or `ClassName.__mro__` to inspect it.
* In a diamond hierarchy, shared ancestors appear only once in the MRO.
* `super()` moves to the next class in the MRO.
* Python continues searching if the first parent does not contain the requested member.
* Conflicting inheritance requirements can cause a `TypeError`.
* Multiple inheritance is useful, but it should be used carefully.
