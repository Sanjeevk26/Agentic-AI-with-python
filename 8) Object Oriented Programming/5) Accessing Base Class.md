# Python OOP: Accessing the Base Class with super()

## Overview

When one class inherits from another class, the child class may need to access attributes or methods defined in the parent class.

There are three common approaches:

1. Repeat the parent logic
2. Call the parent class explicitly
3. Use `super()`

The recommended approach in most cases is `super()`.

---

# 1. Base Class

Consider a base class named `Chai`.

```python
class Chai:
    def __init__(self, chai_type, strength):
        self.chai_type = chai_type
        self.strength = strength
```

The constructor initializes:

* `chai_type`
* `strength`

## Creating an Object

```python
chai = Chai("Masala Chai", "Strong")
```

The object receives both attributes.

---

# 2. Child Class

Suppose we create a specialized chai called `GingerChai`.

```python
class GingerChai(Chai):
    pass
```

This means:

```text
GingerChai is a Chai
```

The `GingerChai` class inherits from `Chai`.

---

# 3. Approach One: Repeating the Parent Logic

The child class can repeat the same initialization code.

```python
class GingerChai(Chai):
    def __init__(self, chai_type, strength, spice_level):
        self.chai_type = chai_type
        self.strength = strength
        self.spice_level = spice_level
```

This code works correctly.

However, these lines duplicate the parent logic:

```python
self.chai_type = chai_type
self.strength = strength
```

## Why Duplication Can Be a Problem

Suppose the parent class later changes:

```python
class Chai:
    def __init__(self, chai_type, strength):
        self.chai_type = chai_type
        self.strength = strength
        self.category = "Beverage"
```

The child class would not automatically receive the new `category` initialization if it repeated the old logic.

Duplicated code can become:

* Harder to maintain
* Easier to forget
* Inconsistent
* More difficult to update

---

# 4. Approach Two: Explicit Parent-Class Call

The child class can directly call the parent constructor.

```python
class GingerChai(Chai):
    def __init__(self, chai_type, strength, spice_level):
        Chai.__init__(self, chai_type, strength)
        self.spice_level = spice_level
```

Here:

```python
Chai.__init__(self, chai_type, strength)
```

explicitly calls the constructor of `Chai`.

## Why self Is Passed Explicitly

When a method is called using an object:

```python
chai.prepare()
```

Python automatically passes the object as `self`.

But when calling a method directly through the class:

```python
Chai.__init__(...)
```

we must pass the object manually:

```python
Chai.__init__(self, chai_type, strength)
```

## Complete Example

```python
class Chai:
    def __init__(self, chai_type, strength):
        self.chai_type = chai_type
        self.strength = strength


class GingerChai(Chai):
    def __init__(self, chai_type, strength, spice_level):
        Chai.__init__(self, chai_type, strength)
        self.spice_level = spice_level
```

This avoids repeating the parent's attribute assignments.

---

# 5. Approach Three: Using super()

The preferred approach is usually `super()`.

```python
class GingerChai(Chai):
    def __init__(self, chai_type, strength, spice_level):
        super().__init__(chai_type, strength)
        self.spice_level = spice_level
```

Here:

```python
super().__init__(chai_type, strength)
```

calls the appropriate parent constructor.

## Why self Is Not Passed

When using:

```python
super().__init__(chai_type, strength)
```

Python automatically binds the current object.

Therefore, we do not write:

```python
super().__init__(self, chai_type, strength)
```

That would pass `self` twice and cause incorrect behavior.

---

# 6. Complete super() Example

```python
class Chai:
    def __init__(self, chai_type, strength):
        self.chai_type = chai_type
        self.strength = strength


class GingerChai(Chai):
    def __init__(self, chai_type, strength, spice_level):
        super().__init__(chai_type, strength)
        self.spice_level = spice_level
```

Create an object:

```python
ginger_chai = GingerChai(
    "Ginger Chai",
    "Strong",
    "High"
)
```

Access its attributes:

```python
print(ginger_chai.chai_type)
print(ginger_chai.strength)
print(ginger_chai.spice_level)
```

Output:

```text
Ginger Chai
Strong
High
```

---

# 7. Using super() with Parent Methods

`super()` is not limited to constructors.

It can call other parent methods too.

```python
class Chai:
    def prepare(self):
        return "Boiling water and tea leaves"


class GingerChai(Chai):
    def prepare(self):
        base_steps = super().prepare()
        return f"{base_steps}, then adding ginger"
```

Use it:

```python
chai = GingerChai()

print(chai.prepare())
```

Output:

```text
Boiling water and tea leaves, then adding ginger
```

The child class extends the parent method instead of replacing all its logic.

---

# 8. Explicit Call vs super()

## Explicit Parent Call

```python
Chai.__init__(self, chai_type, strength)
```

This names the parent class directly.

## super() Call

```python
super().__init__(chai_type, strength)
```

This follows Python's method resolution order.

## Comparison

| Explicit call                        | `super()`                             |
| ------------------------------------ | ------------------------------------- |
| Names a specific parent directly     | Uses method resolution order          |
| Requires passing `self`              | Binds `self` automatically            |
| Can be suitable in specific cases    | Preferred in most inheritance designs |
| Less flexible if hierarchy changes   | Better for multiple inheritance       |
| Tightly connected to one parent name | Easier to maintain                    |

---

# 9. Method Resolution Order

Python uses the Method Resolution Order, or MRO, to determine where to look for methods in an inheritance hierarchy.

Example:

```python
print(GingerChai.mro())
```

Possible output:

```text
[
    <class '__main__.GingerChai'>,
    <class '__main__.Chai'>,
    <class 'object'>
]
```

Python checks:

1. `GingerChai`
2. `Chai`
3. `object`

`super()` follows this order.

It does not simply mean “call the parent named in the class declaration.” It means “continue searching from the next class in the MRO.”

---

# 10. Why super() Is Preferred

`super()` is usually preferred because it:

* Reduces code duplication
* Avoids hardcoding the parent class name
* Supports multiple inheritance
* Follows Python's MRO
* Makes refactoring easier
* Keeps parent initialization centralized

---

# 11. Common Mistakes

## Forgetting to Call the Parent Constructor

```python
class GingerChai(Chai):
    def __init__(self, spice_level):
        self.spice_level = spice_level
```

The object will not automatically receive attributes created by `Chai.__init__()` because the child defined its own constructor.

Accessing:

```python
ginger_chai.chai_type
```

may raise `AttributeError`.

## Passing self to super()

Incorrect:

```python
super().__init__(self, chai_type, strength)
```

Correct:

```python
super().__init__(chai_type, strength)
```

## Using the Wrong Parent Name

Explicit calls can break during refactoring:

```python
Chai.__init__(self, chai_type, strength)
```

If the parent class changes, this line must also be updated.

`super()` avoids directly hardcoding the parent name.

---

# Key Takeaways

* A child class can access logic from its base class.
* Repeating parent logic works but creates duplication.
* Explicit parent calls use `ParentClass.method(self, ...)`.
* `super()` is usually the preferred approach.
* `super().__init__()` calls the next constructor in the MRO.
* Do not manually pass `self` when using `super()`.
* `super()` can call constructors and regular methods.
* Parent constructors must be called when their initialization is required.
* `super()` is especially useful in larger and multiple-inheritance designs.
