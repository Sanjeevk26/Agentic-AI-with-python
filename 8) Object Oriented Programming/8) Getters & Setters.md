# Python OOP: Property Decorators, Getters, and Setters

## Overview

Property decorators allow us to control how an object's attributes are:

* Read
* Updated
* Validated
* Calculated
* Protected from invalid values

Python provides:

* `@property` for reading a value
* `@property_name.setter` for updating a value
* `@property_name.deleter` for controlling deletion

Properties allow a method to be accessed like a normal attribute.

---

# 1. The Problem with Public Attributes

Consider a basic class:

```python
class TeaLeaf:
    def __init__(self, age):
        self.age = age
```

Create an object:

```python
leaf = TeaLeaf(2)
```

The attribute can be read directly:

```python
print(leaf.age)
```

It can also be changed to any value:

```python
leaf.age = -10
```

Python does not automatically stop this invalid update.

Property decorators allow us to add validation and control.

---

# 2. Internal Attribute Convention

A common convention is to store the internal value using a leading underscore:

```python
self._age = age
```

The underscore means:

```text
This attribute is intended for internal use.
```

It does not make the attribute truly private.

This is still technically possible:

```python
print(leaf._age)
```

However, Python developers understand that attributes beginning with `_` should normally not be accessed directly from outside the class.

---

# 3. Creating a Property Getter

Use `@property` to define how an attribute is read.

```python
class TeaLeaf:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age
```

Now the value can be accessed like a normal attribute:

```python
leaf = TeaLeaf(2)

print(leaf.age)
```

Notice that we do not write:

```python
leaf.age()
```

Although `age` is implemented using a method, `@property` allows it to behave like an attribute.

---

# 4. Calculated Properties

A property can transform or calculate a value before returning it.

```python
class TeaLeaf:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age + 2
```

Example:

```python
leaf = TeaLeaf(2)

print(leaf.age)
```

Output:

```text
4
```

The stored value is still `2`, but the property returns `4`.

Properties are useful for calculated or formatted values.

However, a property should ideally behave predictably. Returning an unrelated transformed value can confuse users of the class.

---

# 5. Creating a Property Setter

A setter controls how a property is updated.

```python
class TeaLeaf:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        self._age = value
```

Now this assignment:

```python
leaf.age = 4
```

does not directly update `_age`.

Python internally calls the setter:

```python
age(self, 4)
```

---

# 6. Validating Values with a Setter

The setter can reject invalid data.

```python
class TeaLeaf:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if 1 <= value <= 5:
            self._age = value
        else:
            raise ValueError(
                "Tea leaf age must be between 1 and 5 years"
            )
```

Valid update:

```python
leaf.age = 4
```

Invalid update:

```python
leaf.age = 10
```

Output:

```text
ValueError: Tea leaf age must be between 1 and 5 years
```

---

# 7. Validating During Object Creation

A useful pattern is to assign through the property inside `__init__`.

```python
class TeaLeaf:
    def __init__(self, age):
        self.age = age
```

Instead of:

```python
self._age = age
```

Using:

```python
self.age = age
```

calls the setter during object initialization.

This ensures that invalid objects cannot be created.

Example:

```python
leaf = TeaLeaf(10)
```

This immediately raises `ValueError`.

---

# 8. Complete Property Example

```python
class TeaLeaf:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Tea leaf age must be an integer")

        if not 1 <= value <= 5:
            raise ValueError(
                "Tea leaf age must be between 1 and 5 years"
            )

        self._age = value
```

Usage:

```python
leaf = TeaLeaf(2)

print(leaf.age)

leaf.age = 4

print(leaf.age)
```

Output:

```text
2
4
```

---

# 9. Read-Only Properties

A property becomes read-only when it has a getter but no setter.

```python
class TeaLeaf:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        return self._age
```

Reading works:

```python
print(leaf.age)
```

Updating does not:

```python
leaf.age = 4
```

Python raises:

```text
AttributeError: property 'age' has no setter
```

---

# 10. Write-Controlled Calculated Property

Properties can expose calculated information without storing another attribute.

```python
class TeaLeaf:
    def __init__(self, age):
        self.age = age

    @property
    def maturity(self):
        if self.age <= 2:
            return "Young"

        if self.age <= 4:
            return "Mature"

        return "Aged"
```

Usage:

```python
leaf = TeaLeaf(4)

print(leaf.maturity)
```

Output:

```text
Mature
```

No separate `maturity` attribute needs to be stored.

---

# 11. Property Deleter

A property can also control attribute deletion.

```python
class TeaLeaf:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not 1 <= value <= 5:
            raise ValueError("Invalid age")

        self._age = value

    @age.deleter
    def age(self):
        print("Deleting tea leaf age")
        del self._age
```

Usage:

```python
del leaf.age
```

The deleter method runs before the internal value is removed.

---

# 12. Getter and Setter Naming

The property name comes from the getter method name.

```python
@property
def age(self):
    return self._age
```

The setter must use the same property name:

```python
@age.setter
def age(self, value):
    self._age = value
```

The internal attribute can use another name:

```python
self._age
```

Common pattern:

```text
Public property: age
Internal storage: _age
```

---

# 13. Properties vs Regular Methods

Without a property:

```python
leaf.get_age()
leaf.set_age(4)
```

With a property:

```python
leaf.age
leaf.age = 4
```

Properties provide cleaner syntax while still running method logic internally.

---

# 14. Important Notes About Underscores

A leading underscore is a convention, not a security mechanism.

```python
self._age
```

means that the value should be treated as internal.

It does not automatically:

* Make the value private
* Require a property
* Prevent direct access
* Cause Python to rename it

Python developers are expected to respect the convention.

---

# 15. When to Use Properties

Properties are useful when:

* A value needs validation
* A value should be read-only
* A value is calculated dynamically
* Internal implementation may change
* Additional logic should run during assignment
* Existing attribute-style syntax should remain unchanged

Do not create properties for every attribute without a reason. Simple public attributes are acceptable when no control or validation is needed.

---

# Key Takeaways

* `@property` creates a getter.
* A property method is accessed like an attribute.
* `@property_name.setter` controls assignment.
* Setters can validate values before storing them.
* `@property_name.deleter` controls deletion.
* A leading underscore indicates internal use by convention.
* The underscore does not create true privacy.
* Assigning through the property inside `__init__` reuses validation.
* A property without a setter is read-only.
* Properties can expose calculated values without storing them.
* Property names and setter decorator names must match.
