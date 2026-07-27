# Pydantic Recursive Models

## Overview

A recursive model, also called a self-referencing model, is a model that contains another object of the same model type.

This is useful for data structures where the same structure can repeat inside itself.

Common examples:

* Comments and replies
* Folder and subfolders
* Categories and subcategories
* Menu items and submenu items
* Organization hierarchy
* Tree structures

Example:

```text id="rny99x"
Comment
 ├── Reply
 │    └── Nested reply
 └── Reply
```

Each reply is also a comment.

---

# 1. What Is a Self-Referencing Model?

A self-referencing model points back to itself.

Example:

```python id="tpx1ti"
class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List["Comment"]] = None
```

Here:

```python id="soz64s"
replies: Optional[List["Comment"]] = None
```

means:

* `replies` may be missing or `None`
* if replies exist, they must be a list
* each item inside the list must be another `Comment`

---

# 2. Why Use Quotes Around "Comment"?

At the time Python reads this line:

```python id="qcxien"
replies: Optional[List["Comment"]] = None
```

the `Comment` class is still being defined.

So we use `"Comment"` as a forward reference.

A forward reference means:

```text id="gp2g41"
This type will exist later.
```

Without quotes, Python may not know what `Comment` means at that point.

---

# 3. Import Required Types

```python id="qbrdor"
from typing import List, Optional

from pydantic import BaseModel
```

We use:

* `List` for a list of replies
* `Optional` because replies may be absent
* `BaseModel` for creating a Pydantic model

---

# 4. Comment Model

```python id="s7xu4l"
class Comment(BaseModel):
    id: int
    content: str
    replies: Optional[List["Comment"]] = None
```

This model supports nested replies.

A comment can have replies.

Each reply can also have its own replies.

---

# 5. model_rebuild()

After defining a self-referencing model, use:

```python id="r0sw6w"
Comment.model_rebuild()
```

This tells Pydantic to resolve the forward reference.

In many simple cases, Pydantic may handle this automatically, but calling `model_rebuild()` is a clear and safe habit when using forward references.

---

# 6. Creating a Simple Comment

```python id="x4bwxt"
comment = Comment(
    id=1,
    content="First comment",
)
```

Here, `replies` is not provided.

So it becomes:

```python id="ogewop"
replies=None
```

---

# 7. Creating a Comment with Replies

```python id="jfcfre"
comment = Comment(
    id=1,
    content="First comment",
    replies=[
        Comment(
            id=2,
            content="Reply one",
        ),
        Comment(
            id=3,
            content="Reply two",
        ),
    ],
)
```

Here, the parent comment has two replies.

Each reply is also a `Comment` object.

---

# 8. Creating Nested Replies

```python id="krscce"
comment = Comment(
    id=1,
    content="First comment",
    replies=[
        Comment(
            id=2,
            content="Reply one",
        ),
        Comment(
            id=3,
            content="Reply two",
            replies=[
                Comment(
                    id=4,
                    content="Nested reply",
                )
            ],
        ),
    ],
)
```

This creates a comment tree.

```text id="dvlelu"
First comment
 ├── Reply one
 └── Reply two
      └── Nested reply
```

---

# 9. Creating Recursive Model from Dictionary

Pydantic can also build recursive models from nested dictionaries.

```python id="b9xmh8"
comment_data = {
    "id": 1,
    "content": "First comment",
    "replies": [
        {
            "id": 2,
            "content": "Reply one",
        },
        {
            "id": 3,
            "content": "Reply two",
            "replies": [
                {
                    "id": 4,
                    "content": "Nested reply",
                }
            ],
        },
    ],
}

comment = Comment(**comment_data)
```

Pydantic automatically converts nested dictionaries into `Comment` objects.

---

# 10. Automatic Recursive Validation

Pydantic validates the complete structure.

It checks:

* Parent comment fields
* Reply comment fields
* Nested reply fields
* Deeper nested comments

Example invalid data:

```python id="vk55tz"
bad_comment_data = {
    "id": 1,
    "content": "First comment",
    "replies": [
        {
            "id": "wrong-id",
            "content": "Reply one",
        }
    ],
}
```

The nested reply has an invalid `id`.

Pydantic raises a `ValidationError`.

---

# 11. model_dump() with Recursive Models

```python id="r1p3b9"
print(comment.model_dump())
```

This converts the recursive model into nested dictionaries.

Example:

```python id="dgx8qw"
{
    "id": 1,
    "content": "First comment",
    "replies": [
        {
            "id": 2,
            "content": "Reply one",
            "replies": None,
        }
    ],
}
```

---

# 12. Optional[List["Comment"]] Explained

```python id="j69wgx"
replies: Optional[List["Comment"]] = None
```

Breakdown:

| Part            | Meaning                     |
| --------------- | --------------------------- |
| `replies`       | Field name                  |
| `Optional[...]` | Field can be `None`         |
| `List[...]`     | Field can be a list         |
| `"Comment"`     | Each item must be a Comment |
| `= None`        | Default value is None       |

So the full meaning is:

```text id="l6gg6w"
Replies can be missing.
If replies exist, they must be a list of Comment objects.
```

---

# 13. Alternative: Empty List by Default

Sometimes you may prefer replies to be an empty list instead of `None`.

Use `Field(default_factory=list)`.

```python id="07553l"
from pydantic import Field


class Comment(BaseModel):
    id: int
    content: str
    replies: List["Comment"] = Field(default_factory=list)
```

This means every comment gets its own empty list by default.

This avoids shared mutable default problems.

---

# 14. None vs Empty List

| Design         | Meaning                                      |
| -------------- | -------------------------------------------- |
| `replies=None` | Replies are absent or not loaded             |
| `replies=[]`   | Replies are loaded, but there are no replies |

Both are valid designs.

Choose based on your application requirement.

---

# 15. Real-World Use Cases

Recursive models are useful for:

* Comment threads
* File systems
* Category trees
* Organization charts
* Nested menus
* Discussion replies
* Parent-child task structures

Example:

```text id="m6jfss"
Category
 ├── Electronics
 │    ├── Laptop
 │    └── Mouse
 └── Clothing
      ├── Men
      └── Women
```

Each category can contain more categories.

---

# 16. Common Mistakes

## Not Quoting the Self Reference

Incorrect:

```python id="p2d1ox"
replies: Optional[List[Comment]] = None
```

Correct:

```python id="d6cgfr"
replies: Optional[List["Comment"]] = None
```

## Forgetting model_rebuild()

Recommended:

```python id="6opyhc"
Comment.model_rebuild()
```

This resolves forward references clearly.

## Using a Mutable Default List Directly

Avoid this:

```python id="nd314d"
replies: List["Comment"] = []
```

Prefer:

```python id="5n11kl"
replies: List["Comment"] = Field(default_factory=list)
```

## Forgetting That Every Reply Must Match the Same Model

If `replies` is a list of `Comment`, every reply must have the fields required by `Comment`.

---

# Key Takeaways

* Recursive models are also called self-referencing models.
* They are useful for tree-like data.
* A model can contain a list of itself.
* Use quotes for forward references like `"Comment"`.
* Use `model_rebuild()` after defining self-referencing models.
* Pydantic validates the entire recursive structure.
* Nested dictionaries can automatically become recursive Pydantic models.
* Use `Optional[List["Comment"]] = None` when replies may be absent.
* Use `Field(default_factory=list)` when you want an empty list by default.
