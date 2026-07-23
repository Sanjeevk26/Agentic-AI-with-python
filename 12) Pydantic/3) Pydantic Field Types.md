# Pydantic Advanced Field Types

## Overview

Pydantic models can use simple Python types such as:

```python id="2exnna"
int
str
bool
float
```

But real-world data is often more complex.

For example:

* A cart may contain a list of items.
* A product quantity may be stored in a dictionary.
* A blog post may or may not have an image URL.

For these cases, Pydantic can work with types from Python's built-in `typing` module.

---

# 1. Pydantic and typing Module

Pydantic uses Python type annotations to validate data.

Some types are simple:

```python id="rsmxac"
user_id: int
title: str
is_active: bool
```

For advanced structures, we can import types from `typing`.

```python id="d8e0xe"
from typing import List, Dict, Optional
```

These help us define more complex data shapes.

---

# 2. Importing BaseModel

Every Pydantic model usually starts with `BaseModel`.

```python id="5sqoau"
from pydantic import BaseModel
```

Then we create a class that inherits from `BaseModel`.

```python id="4evamh"
class Cart(BaseModel):
    pass
```

---

# 3. List Type

A list field can be defined using `List`.

```python id="wq42og"
from typing import List
```

Example:

```python id="tqep7o"
items: List[str]
```

This means:

```text id="r8sdk3"
items must be a list
each item inside the list must be a string
```

Example valid value:

```python id="7w22hv"
items = ["tea", "milk", "sugar"]
```

Invalid value:

```python id="f7skna"
items = ["tea", 123, "sugar"]
```

The integer `123` is not a string.

---

# 4. Dictionary Type

A dictionary field can be defined using `Dict`.

```python id="dahfhx"
from typing import Dict
```

Example:

```python id="8gs9sv"
quantities: Dict[str, int]
```

This means:

```text id="vscx7f"
dictionary keys must be strings
dictionary values must be integers
```

Example valid value:

```python id="9j2w9h"
quantities = {
    "tea": 2,
    "milk": 1,
}
```

Invalid value:

```python id="x56wc7"
quantities = {
    "tea": "two",
    "milk": 1,
}
```

The value `"two"` cannot be used as an integer.

---

# 5. Optional Type

Sometimes a field may or may not have a value.

For this, use `Optional`.

```python id="1n1uwd"
from typing import Optional
```

Example:

```python id="b2ugf7"
image_url: Optional[str] = None
```

This means:

```text id="yzw58o"
image_url can be a string
or image_url can be None
```

This is useful when a field is not mandatory.

---

# 6. Cart Model Example

```python id="g7q80r"
from typing import Dict, List
from pydantic import BaseModel


class Cart(BaseModel):
    user_id: int
    items: List[str]
    quantities: Dict[str, int]
```

This model says:

* `user_id` must be an integer
* `items` must be a list of strings
* `quantities` must be a dictionary with string keys and integer values

---

# 7. Valid Cart Example

```python id="rzponb"
cart = Cart(
    user_id=101,
    items=["tea", "milk", "sugar"],
    quantities={
        "tea": 2,
        "milk": 1,
        "sugar": 3,
    },
)
```

This is valid because all fields match the expected types.

---

# 8. BlogPost Model Example

```python id="s83k4g"
from typing import Optional
from pydantic import BaseModel


class BlogPost(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None
```

This model says:

* `title` must be a string
* `content` must be a string
* `image_url` can be a string or `None`

---

# 9. Blog Post Without Image

```python id="1b1yfs"
post = BlogPost(
    title="Learning Pydantic",
    content="Pydantic helps validate data.",
)
```

This is valid.

Since `image_url` has a default value of `None`, it does not need to be passed.

---

# 10. Blog Post With Image

```python id="0drbin"
post = BlogPost(
    title="Learning Pydantic",
    content="Pydantic helps validate data.",
    image_url="https://example.com/image.png",
)
```

This is also valid.

Here, `image_url` is provided as a string.

---

# 11. Key Advanced Field Types

| Type             | Meaning                                          |
| ---------------- | ------------------------------------------------ |
| `List[str]`      | A list containing only strings                   |
| `List[int]`      | A list containing only integers                  |
| `Dict[str, int]` | A dictionary with string keys and integer values |
| `Dict[str, str]` | A dictionary with string keys and string values  |
| `Optional[str]`  | A string or `None`                               |
| `Optional[int]`  | An integer or `None`                             |

---

# 12. Important Correction

In the transcript, the explanation says that `str` comes from Pydantic.

More accurately:

```text id="2flfwm"
str, int, bool, and float are Python built-in types.
```

Pydantic uses these type annotations for validation.

The advanced container types such as `List`, `Dict`, and `Optional` are imported from Python's `typing` module.

---

# 13. Modern Python Syntax

In newer Python versions, you can also write:

```python id="27h8si"
items: list[str]
quantities: dict[str, int]
image_url: str | None = None
```

However, this lesson uses:

```python id="hpfdwb"
List[str]
Dict[str, int]
Optional[str]
```

because it clearly shows the role of the `typing` module.

---

# 14. Common Mistakes

## Forgetting BaseModel

Incorrect:

```python id="ucvlbu"
class Cart:
    user_id: int
```

Correct:

```python id="oal5ji"
class Cart(BaseModel):
    user_id: int
```

## Using List Without Importing It

Incorrect:

```python id="xxagdk"
items: List[str]
```

without:

```python id="l8dw0q"
from typing import List
```

## Forgetting Default Value for Optional Field

This means the field can be `None`, but it is still required unless a default is provided:

```python id="xfces0"
image_url: Optional[str]
```

This makes the field optional during object creation:

```python id="rvhmua"
image_url: Optional[str] = None
```

---

# 15. Why Advanced Field Types Matter

Real-world data is rarely flat.

Applications often deal with:

* Lists of products
* Dictionaries of quantities
* Optional profile images
* Optional descriptions
* Lists of tags
* Nested data structures

Pydantic helps validate these structures clearly.

---

# Key Takeaways

* Pydantic works with Python type annotations.
* `BaseModel` is used to create Pydantic models.
* `List[str]` means a list of strings.
* `Dict[str, int]` means a dictionary with string keys and integer values.
* `Optional[str] = None` means the field can be a string or `None`.
* Types such as `List`, `Dict`, and `Optional` come from Python's `typing` module.
* Types such as `str`, `int`, `bool`, and `float` are Python built-in types.
* Advanced field types make Pydantic useful for real-world data validation.
