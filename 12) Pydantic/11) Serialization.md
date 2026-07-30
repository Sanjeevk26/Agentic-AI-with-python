# Pydantic Serialization

## Overview

Serialization means converting a complex Python object into a format that is easier to store, transmit, or process.

In Pydantic, serialization usually means converting a Pydantic model into:

* Python dictionary
* JSON string
* JSON-compatible data
* Custom formatted output

Common use cases:

* Returning API responses
* Saving data
* Sending data between services
* Logging model data
* Converting nested models into dictionaries
* Converting datetime values into readable strings

---

# 1. What Is Serialization?

Serialization is the process of converting complex data into a simpler format.

Example:

```python
User(...)
```

can be converted into:

```python
{
    "id": 1,
    "name": "Hitesh",
    "email": "h@example.com"
}
```

or into a JSON string:

```json
{"id":1,"name":"Hitesh","email":"h@example.com"}
```

---

# 2. Common Serialization Formats

| Format            | Example                                        |
| ----------------- | ---------------------------------------------- |
| Python dictionary | `dict`                                         |
| JSON string       | `str` containing JSON                          |
| XML               | Less common in modern Python APIs              |
| Custom format     | Any special format required by the application |

In most modern APIs, JSON is the most common format.

---

# 3. Required Imports

```python
from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict, Field
```

Here:

* `BaseModel` is used to create Pydantic models.
* `ConfigDict` is used to configure model behavior.
* `Field` is used for safe default list creation.
* `datetime` is used to show serialization issues with date and time.
* `List` is used for list fields.

---

# 4. Address Model

```python
class Address(BaseModel):
    street: str
    city: str
    zip_code: str
```

This is a nested model.

It will be used inside the `User` model.

---

# 5. User Model

```python
class User(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: List[str] = Field(default_factory=list)
```

This model contains:

* Basic fields
* Boolean default value
* Datetime field
* Nested model
* List field

---

# 6. Why Datetime Needs Attention

Datetime values can be tricky during serialization.

A Python `datetime` object is easy to use inside Python, but JSON does not directly understand Python datetime objects.

Example Python object:

```python
datetime(2024, 3, 15, 14, 30, 20)
```

This may need to become a string like:

```text
15-03-2024 14:30:20
```

or:

```text
2024-03-15T14:30:20
```

---

# 7. Custom Datetime Serialization

Pydantic allows custom JSON encoding using `ConfigDict`.

```python
class User(BaseModel):
    model_config = ConfigDict(
        json_encoders={
            datetime: lambda value: value.strftime(
                "%d-%m-%Y %H:%M:%S"
            )
        }
    )

    id: int
    name: str
    email: str
    created_at: datetime
    address: Address
```

This tells Pydantic how to convert `datetime` into a JSON-friendly string.

---

# 8. strftime Format

```python
"%d-%m-%Y %H:%M:%S"
```

Means:

| Code | Meaning                |
| ---- | ---------------------- |
| `%d` | Day                    |
| `%m` | Month                  |
| `%Y` | Year with 4 digits     |
| `%H` | Hour in 24-hour format |
| `%M` | Minute                 |
| `%S` | Second                 |

Example:

```text
15-03-2024 14:30:20
```

Datetime formats are hard to remember, so checking documentation while working is normal.

---

# 9. Creating a User Object

```python
user = User(
    id=1,
    name="Hitesh",
    email="h@hitesh.ai",
    is_active=False,
    created_at=datetime(2024, 3, 15, 14, 30, 20),
    address=Address(
        street="123 Main Street",
        city="Jaipur",
        zip_code="009988",
    ),
    tags=["premium", "subscriber"],
)
```

This creates a Pydantic model with nested data.

---

# 10. Printing the Model Directly

```python
print(user)
```

This prints the Pydantic model representation.

Example:

```text
id=1 name='Hitesh' email='h@hitesh.ai' is_active=False ...
```

This is useful for debugging, but it is not the same as serialization.

---

# 11. model_dump()

`model_dump()` converts a Pydantic model into a Python dictionary.

```python
python_dict = user.model_dump()
```

Example output:

```python
{
    "id": 1,
    "name": "Hitesh",
    "email": "h@hitesh.ai",
    "is_active": False,
    "created_at": datetime(2024, 3, 15, 14, 30, 20),
    "address": {
        "street": "123 Main Street",
        "city": "Jaipur",
        "zip_code": "009988",
    },
    "tags": ["premium", "subscriber"],
}
```

Important point:

`model_dump()` returns a Python dictionary.

By default, some Python objects such as `datetime` may remain as Python objects.

---

# 12. model_dump(mode="json")

To get JSON-compatible Python data, use:

```python
json_ready_dict = user.model_dump(mode="json")
```

This converts values like `datetime` into JSON-friendly values.

Example:

```python
{
    "id": 1,
    "name": "Hitesh",
    "created_at": "15-03-2024 14:30:20",
}
```

This is still a Python dictionary, but the values are JSON-friendly.

---

# 13. model_dump_json()

`model_dump_json()` converts the Pydantic model directly into a JSON string.

```python
json_string = user.model_dump_json()
```

Example output:

```json
{"id":1,"name":"Hitesh","email":"h@hitesh.ai","is_active":false}
```

This is not a dictionary.

It is a string.

---

# 14. Difference Between model_dump() and model_dump_json()

| Method                    | Output                            |
| ------------------------- | --------------------------------- |
| `model_dump()`            | Python dictionary                 |
| `model_dump(mode="json")` | JSON-compatible Python dictionary |
| `model_dump_json()`       | JSON encoded string               |

Simple way to remember:

```text
model_dump()       → dictionary
model_dump_json()  → JSON string
```

---

# 15. Nested Model Serialization

When a model contains another Pydantic model, `model_dump()` converts the nested model too.

Example:

```python
class User(BaseModel):
    address: Address
```

After serialization:

```python
{
    "address": {
        "street": "123 Main Street",
        "city": "Jaipur",
        "zip_code": "009988"
    }
}
```

So nested models become nested dictionaries.

---

# 16. Safe Default List

Avoid this:

```python
tags: List[str] = []
```

Better:

```python
tags: List[str] = Field(default_factory=list)
```

This ensures each model instance gets its own separate empty list.

---

# 17. Common Mistakes

## Confusing Dictionary and JSON String

This is a dictionary:

```python
user.model_dump()
```

This is a JSON string:

```python
user.model_dump_json()
```

## Expecting JSON to Understand datetime Automatically

JSON does not directly understand Python datetime objects.

Use:

```python
model_dump(mode="json")
```

or:

```python
model_dump_json()
```

## Forgetting Custom Datetime Format

If a specific date format is required, configure it using `ConfigDict`.

## Writing Incorrect strftime Codes

Example mistake:

```python
"%d-%m-%Y %H:%M:%"
```

Correct:

```python
"%d-%m-%Y %H:%M:%S"
```

---

# 18. When to Use Which Method

Use `model_dump()` when you need a Python dictionary.

Use `model_dump(mode="json")` when you need a dictionary that is safe for JSON conversion.

Use `model_dump_json()` when you need a JSON string directly.

---

# Key Takeaways

* Serialization converts Pydantic models into simpler formats.
* `model_dump()` converts a model into a Python dictionary.
* `model_dump(mode="json")` creates a JSON-compatible dictionary.
* `model_dump_json()` creates a JSON encoded string.
* Nested Pydantic models are recursively converted.
* Datetime values need attention during serialization.
* `ConfigDict` can customize JSON encoding.
* `Field(default_factory=list)` is safer than using an empty list directly.
