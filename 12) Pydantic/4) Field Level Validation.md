# Pydantic Field and Field-Level Validation

## Overview

In Pydantic, we usually start by creating models with `BaseModel`.

Basic model example:

```python id="emyd0m"
from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    price: float
```

This validates the basic type of each field.

But sometimes basic type validation is not enough.

For example:

* A name should be at least 3 characters long.
* A salary should be greater than or equal to a minimum amount.
* A discount should be between 0 and 100.
* An email or phone number should follow a pattern.
* A field should include documentation for API schemas.

For these cases, Pydantic provides `Field`.

---

# 1. What Is Field?

`Field` is used to add extra rules, metadata, and documentation to a model field.

Import it from Pydantic:

```python id="qha2fd"
from pydantic import BaseModel, Field
```

Example:

```python id="73tuyf"
class Employee(BaseModel):
    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee name",
        examples=["Hitesh"],
    )
```

---

# 2. Why Use Field?

Use `Field` when you need more control over a field.

It can help with:

* Required fields
* Minimum length
* Maximum length
* Minimum numeric value
* Maximum numeric value
* Descriptions
* Examples
* Pattern-based validation
* Better API documentation

---

# 3. Required Field Using ...

In Pydantic, three dots mean the field is required.

```python id="4iclt7"
name: str = Field(...)
```

This means `name` must be provided.

Example:

```python id="2io58n"
class Employee(BaseModel):
    name: str = Field(...)
```

Invalid:

```python id="w6n3uu"
Employee()
```

This raises a validation error because `name` is missing.

---

# 4. String Length Validation

You can validate string length using:

```python id="vv6vxt"
min_length
max_length
```

Example:

```python id="8fmhla"
name: str = Field(
    ...,
    min_length=3,
    max_length=50,
)
```

This means:

* The name must be at least 3 characters long.
* The name cannot be longer than 50 characters.

Invalid examples:

```python id="scnzob"
name="Hi"
```

Too short.

```python id="s3hgad"
name="A very very very very very very very long employee name"
```

Too long.

---

# 5. Description and Examples

`Field` can also add documentation metadata.

```python id="5yivse"
name: str = Field(
    ...,
    description="Employee name",
    examples=["Hitesh"],
)
```

This is especially useful in API frameworks such as FastAPI.

The description and examples can appear in generated API documentation.

---

# 6. Numeric Validation

For numbers, Pydantic supports constraints such as:

| Constraint | Meaning                  |
| ---------- | ------------------------ |
| `gt`       | Greater than             |
| `ge`       | Greater than or equal to |
| `lt`       | Less than                |
| `le`       | Less than or equal to    |

Example:

```python id="9r01oe"
salary: float = Field(
    ...,
    ge=10000,
    le=100000,
)
```

This means:

* Salary must be greater than or equal to 10,000.
* Salary must be less than or equal to 100,000.

---

# 7. Employee Model Example

```python id="l9gqdb"
from typing import Optional

from pydantic import BaseModel, Field


class Employee(BaseModel):
    id: int

    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee name",
        examples=["Hitesh"],
    )

    department: Optional[str] = "General"

    salary: float = Field(
        ...,
        ge=10000,
        le=100000,
        description="Annual salary in INR",
    )
```

Here:

* `id` is a normal integer field.
* `name` has length validation.
* `department` is optional and defaults to `"General"`.
* `salary` has minimum and maximum validation.

---

# 8. Optional Field with Default

```python id="94byf1"
department: Optional[str] = "General"
```

This means:

* The field may be a string.
* The field may also be `None`.
* If no value is provided, `"General"` is used.

Example:

```python id="o05ay3"
employee = Employee(
    id=1,
    name="Ravi",
    salary=50000,
)
```

The department becomes:

```python id="hh458o"
department="General"
```

---

# 9. Validation Error Example

This is invalid:

```python id="buidt7"
Employee(
    id=1,
    name="Al",
    salary=5000,
)
```

Problems:

* `name` is shorter than 3 characters.
* `salary` is below the minimum value.

Pydantic raises a `ValidationError`.

---

# 10. Pattern Validation

Pydantic can validate strings using a pattern.

In Pydantic v2, use:

```python id="jod1c7"
pattern=
```

Example:

```python id="ru1v7j"
email: str = Field(
    ...,
    pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$",
)
```

This checks whether the email roughly matches an email-like format.

For production email validation, Pydantic also provides `EmailStr`, which is usually better than writing your own pattern.

---

# 11. Phone Number Pattern Example

```python id="4yu2qk"
phone: str = Field(
    ...,
    pattern=r"^\+?[0-9]{10,15}$",
)
```

This means:

* Optional `+` at the start
* Digits only
* Length between 10 and 15 digits

Valid examples:

```text id="ohvdjq"
9876543210
+919876543210
```

Invalid examples:

```text id="q5dfaa"
phone-123
abc9876543
```

---

# 12. Age Validation

```python id="9alke4"
age: int = Field(
    ...,
    ge=0,
    le=150,
    description="Age in years",
)
```

This means age must be between 0 and 150.

---

# 13. Discount Validation

```python id="xpgbks"
discount: float = Field(
    ...,
    ge=0,
    le=100,
    description="Discount percentage",
)
```

This means discount must be between 0 and 100.

This is useful because a discount below 0 or above 100 usually does not make business sense.

---

# 14. Field in One Line vs Multiple Lines

One-line version:

```python id="r01xhc"
name: str = Field(..., min_length=3, max_length=50)
```

Multi-line version:

```python id="fc5tjf"
name: str = Field(
    ...,
    min_length=3,
    max_length=50,
)
```

Both are valid.

Multi-line format is usually easier to read when there are many field options.

---

# 15. Field Parameters Used in This Lesson

| Field parameter | Use                                   |
| --------------- | ------------------------------------- |
| `...`           | Marks the field as required           |
| `min_length`    | Minimum string length                 |
| `max_length`    | Maximum string length                 |
| `description`   | Adds documentation                    |
| `examples`      | Adds example values                   |
| `ge`            | Greater than or equal to              |
| `gt`            | Greater than                          |
| `le`            | Less than or equal to                 |
| `lt`            | Less than                             |
| `pattern`       | Regex-style string pattern validation |

---

# 16. Cart Data Reminder

From the previous example, a cart model may look like this:

```python id="yy3r2x"
from typing import Dict, List

from pydantic import BaseModel


class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]
```

Cart data:

```python id="rs6vlr"
cart_data = {
    "user_id": 123,
    "items": ["laptop", "mouse", "keyboard"],
    "quantities": {
        "laptop": 1,
        "mouse": 2,
        "keyboard": 3,
    },
}
```

Create the model object using dictionary unpacking:

```python id="6v8q48"
cart = Cart(**cart_data)
```

Do not pass the dictionary directly:

```python id="37ngnh"
cart = Cart(cart_data)
```

That is incorrect.

---

# 17. Common Mistakes

## Forgetting to Import Field

Incorrect:

```python id="o1dnm2"
from pydantic import BaseModel
```

when using:

```python id="ep0dlh"
Field(...)
```

Correct:

```python id="xvtldi"
from pydantic import BaseModel, Field
```

## Forgetting Parentheses

Incorrect:

```python id="72z48g"
name: str = Field
```

Correct:

```python id="w68qdy"
name: str = Field(...)
```

## Using regex in Pydantic v2

In Pydantic v2, prefer:

```python id="ax7p6x"
pattern=r"..."
```

instead of older `regex=` style.

## Thinking Optional Means Default Automatically

This can still be required:

```python id="j3q5u6"
department: Optional[str]
```

This is optional during creation because it has a default:

```python id="k6h3h0"
department: Optional[str] = "General"
```

---

# 18. Why Field Is Important

`Field` helps make models more expressive.

Instead of only saying:

```python id="p6oj1s"
salary: float
```

you can say:

```python id="bai33r"
salary: float = Field(
    ...,
    ge=10000,
    le=100000,
    description="Annual salary in INR",
)
```

This makes your model safer and better documented.

---

# Key Takeaways

* `Field` comes from Pydantic.
* `Field` adds extra validation and metadata to model fields.
* `...` means the field is required.
* Use `min_length` and `max_length` for string length validation.
* Use `ge`, `gt`, `le`, and `lt` for numeric validation.
* Use `description` and `examples` for documentation.
* Use `pattern` for pattern-based string validation.
* Use `Optional` when a field can be `None`.
* Add a default value when the field should not be required.
* `Field` is very useful in FastAPI-style API schemas.
