# Pydantic Field Validator and Model Validator

## Overview

Pydantic gives us multiple ways to validate data.

So far, we have seen validation using:

```python id="znm2jx"
Field(...)
```

Example:

```python id="cjgvg6"
name: str = Field(
    ...,
    min_length=3,
    max_length=50,
)
```

But sometimes field constraints are not enough.

For custom validation logic, Pydantic provides:

* `field_validator`
* `model_validator`

---

# 1. Field Validation vs Model Validation

| Type              | Purpose                                         |
| ----------------- | ----------------------------------------------- |
| `field_validator` | Validates one specific field                    |
| `model_validator` | Validates the whole model using multiple fields |

Use `field_validator` when the validation depends on one field.

Use `model_validator` when the validation depends on multiple fields together.

---

# 2. Importing Validators

```python id="hx6eqs"
from pydantic import BaseModel, field_validator, model_validator
```

`BaseModel` is used to create Pydantic models.

`field_validator` is used for custom validation on one field.

`model_validator` is used for validation across the full model.

---

# 3. Field Validator

A field validator applies to a specific field.

Example:

```python id="y5txrr"
class User(BaseModel):
    username: str

    @field_validator("username")
    @classmethod
    def username_length(cls, value):
        if len(value) < 4:
            raise ValueError(
                "Username must be at least 4 characters"
            )

        return value
```

Here, the validator applies only to:

```python id="zra24z"
username
```

---

# 4. How field_validator Works

```python id="34v8gz"
@field_validator("username")
```

This decorator tells Pydantic:

```text id="xvwpmr"
Run this validation function for the username field.
```

The validation method receives the field value.

```python id="kgzkrm"
def username_length(cls, value):
```

Here:

* `cls` refers to the model class.
* `value` is the value being validated.

---

# 5. Returning the Value Is Important

A validator must return the value after validation.

Correct:

```python id="zhcd0f"
return value
```

If you forget to return the value, Pydantic may store `None` or raise unexpected errors.

This is one of the most common mistakes while writing validators.

---

# 6. Raising Validation Errors

Inside a validator, raise `ValueError` when validation fails.

```python id="b9l9en"
if len(value) < 4:
    raise ValueError(
        "Username must be at least 4 characters"
    )
```

Pydantic catches this and converts it into a `ValidationError`.

---

# 7. Field Validator Example

Valid:

```python id="0zys8q"
User(username="hitesh")
```

Invalid:

```python id="tlejbq"
User(username="abc")
```

The invalid example fails because the username has fewer than 4 characters.

---

# 8. Model Validator

A model validator validates the entire model.

It is useful when one field depends on another field.

Example:

```text id="3s5qxw"
password and confirm_password must match
```

This cannot be checked properly by validating only one field independently.

---

# 9. Model Validator Example

```python id="8bj9dg"
from pydantic import BaseModel, model_validator


class SignupData(BaseModel):
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def passwords_match(self):
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")

        return self
```

Here, the model validator checks both:

```python id="yx8wcl"
password
confirm_password
```

---

# 10. mode="after"

```python id="vpu3cw"
@model_validator(mode="after")
```

This means the model validator runs after individual field validation has completed.

So before this runs, Pydantic has already checked that:

```python id="tdwyqu"
password: str
confirm_password: str
```

are valid string fields.

---

# 11. Correct Pydantic v2 Style

In Pydantic v2, an `after` model validator is usually written as an instance method.

Correct:

```python id="xwmba0"
@model_validator(mode="after")
def passwords_match(self):
    ...
    return self
```

This means you access values using:

```python id="d775kb"
self.password
self.confirm_password
```

and return:

```python id="dkdykf"
return self
```

---

# 12. Field Validator vs Model Validator Example

## Field Validator

Use when checking one field:

```python id="qisckg"
username must be at least 4 characters
```

## Model Validator

Use when checking multiple fields:

```python id="b8f4r4"
password and confirm_password must match
```

---

# 13. Validation Order

A simple validation flow:

```text id="vpob0j"
Input data received
        ↓
Field types are checked
        ↓
field_validator runs
        ↓
model_validator(mode="after") runs
        ↓
Model object is created
```

---

# 14. Common Mistakes

## Forgetting to Return the Value

Incorrect:

```python id="kwdypc"
@field_validator("username")
@classmethod
def username_length(cls, value):
    if len(value) < 4:
        raise ValueError("Too short")
```

Correct:

```python id="v9xt83"
@field_validator("username")
@classmethod
def username_length(cls, value):
    if len(value) < 4:
        raise ValueError("Too short")

    return value
```

## Forgetting to Return self in Model Validator

Incorrect:

```python id="nb294i"
@model_validator(mode="after")
def passwords_match(self):
    if self.password != self.confirm_password:
        raise ValueError("Passwords do not match")
```

Correct:

```python id="xcx4jr"
@model_validator(mode="after")
def passwords_match(self):
    if self.password != self.confirm_password:
        raise ValueError("Passwords do not match")

    return self
```

## Using Field When Custom Logic Is Needed

`Field` is good for simple validation.

Example:

```python id="q15x0u"
min_length=3
max_length=50
ge=0
le=100
```

But for custom business rules, use validators.

---

# 15. When to Use Field

Use `Field` for simple constraints:

```python id="1g6e11"
name: str = Field(..., min_length=3)
age: int = Field(..., ge=0, le=150)
discount: float = Field(..., ge=0, le=100)
```

---

# 16. When to Use field_validator

Use `field_validator` when one field needs custom logic.

Examples:

* Username must not contain spaces.
* Username must be lowercase.
* Email domain must be allowed.
* Product code must start with a prefix.
* Password must have a minimum strength rule.

---

# 17. When to Use model_validator

Use `model_validator` when validation depends on multiple fields.

Examples:

* Password and confirm password must match.
* Start date must be before end date.
* Discount price must be less than original price.
* If payment method is card, card number is required.
* If user type is employee, employee ID is required.

---

# Key Takeaways

* `field_validator` validates one specific field.
* `model_validator` validates the full model.
* Use decorators to attach validators to Pydantic models.
* Field validators receive the value being validated.
* Field validators must return the value.
* Model validators can compare multiple fields.
* In Pydantic v2, `mode="after"` model validators usually return `self`.
* Raise `ValueError` when validation fails.
* Pydantic converts validator errors into `ValidationError`.
* Use `Field` for simple constraints and validators for custom logic.
