# Pydantic Nested Models

## Overview

Pydantic nested models allow one Pydantic model to be used inside another Pydantic model.

This is useful when real-world data has relationships.

Example:

```text id="gkj78i"
User
 └── Address
```

A user may have an address.

The address itself can have fields like:

* Street
* City
* Postal code

Instead of keeping everything as plain strings or dictionaries, we can create a separate `Address` model and use it inside the `User` model.

---

# 1. What Is a Nested Model?

A nested model means one model is embedded inside another model.

Example:

```python id="d3hvgx"
class Address(BaseModel):
    street: str
    city: str
    postal_code: str


class User(BaseModel):
    id: int
    name: str
    address: Address
```

Here, `User` has a field called `address`.

But `address` is not just a string.

It is an `Address` model.

---

# 2. Why Use Nested Models?

Nested models help represent real-world data more clearly.

Examples:

* User has an address
* Order has multiple products
* Blog post has author details
* Invoice has customer details
* Course has instructor details
* Company has employee details

Nested models make validation cleaner and more structured.

---

# 3. Importing BaseModel

Every Pydantic model usually inherits from `BaseModel`.

```python id="ptzz1f"
from pydantic import BaseModel
```

For advanced structures, we can also import from `typing`.

```python id="h41x60"
from typing import List, Optional
```

---

# 4. Address Model

```python id="tsk7nm"
class Address(BaseModel):
    street: str
    city: str
    postal_code: str
```

This model says:

* `street` must be a string
* `city` must be a string
* `postal_code` must be a string

Postal code is kept as a string because some countries use letters in postal codes.

---

# 5. User Model with Nested Address

```python id="2cf4at"
class User(BaseModel):
    id: int
    name: str
    address: Address
```

Here:

```python id="r1jthh"
address: Address
```

means the `address` field must follow the structure of the `Address` model.

---

# 6. Creating Address Separately

One way is to create the nested model first.

```python id="85xlcl"
address = Address(
    street="123 MG Road",
    city="Bengaluru",
    postal_code="560001",
)
```

Then pass it to the `User` model.

```python id="ifhxoe"
user = User(
    id=1,
    name="Hitesh",
    address=address,
)
```

This is valid because `address` is already an `Address` object.

---

# 7. Creating Nested Model from Dictionary

Pydantic can also create nested models automatically from dictionaries.

```python id="ru6v76"
user_data = {
    "id": 1,
    "name": "Hitesh",
    "address": {
        "street": "321 Park Street",
        "city": "Delhi",
        "postal_code": "110001",
    },
}
```

Create the user:

```python id="ep6k0k"
user = User(**user_data)
```

Pydantic automatically converts the nested `address` dictionary into an `Address` model.

---

# 8. Dictionary Unpacking Reminder

This is correct:

```python id="uzuh2w"
user = User(**user_data)
```

This unpacks the dictionary into keyword arguments.

It is similar to writing:

```python id="nx5sa0"
user = User(
    id=1,
    name="Hitesh",
    address={
        "street": "321 Park Street",
        "city": "Delhi",
        "postal_code": "110001",
    },
)
```

This is incorrect:

```python id="nafcpe"
user = User(user_data)
```

That passes the entire dictionary as one positional argument.

---

# 9. Automatic Nested Validation

Pydantic validates both levels:

```text id="drlvux"
User validation
    ↓
Address validation
```

So Pydantic checks:

* `id` is an integer
* `name` is a string
* `address` follows the `Address` model
* `street` is a string
* `city` is a string
* `postal_code` is a string

---

# 10. Invalid Nested Data Example

```python id="o2av4o"
bad_user_data = {
    "id": 1,
    "name": "Hitesh",
    "address": {
        "street": "321 Park Street",
        "city": "Delhi",
    },
}
```

This is invalid because `postal_code` is missing.

Pydantic raises a `ValidationError`.

---

# 11. Nested Model Output

When printed, the nested model appears inside the parent model.

```python id="fybv5i"
print(user)
```

Example output:

```text id="5prk12"
id=1 name='Hitesh' address=Address(street='321 Park Street', city='Delhi', postal_code='110001')
```

---

# 12. model_dump() with Nested Models

```python id="zqf9vg"
print(user.model_dump())
```

Output:

```python id="g7dtmz"
{
    "id": 1,
    "name": "Hitesh",
    "address": {
        "street": "321 Park Street",
        "city": "Delhi",
        "postal_code": "110001",
    },
}
```

`model_dump()` converts nested Pydantic models into nested dictionaries.

---

# 13. Model Composition

This concept is called model composition.

```text id="t1zilu"
User contains Address
```

Instead of putting all fields in one large model, we create smaller reusable models.

This makes the code cleaner.

---

# 14. Type Annotation with Model Class

Usually, we write type annotations like:

```python id="3hxnfg"
id: int
name: str
```

With nested models, we use another model class as the type.

```python id="lt2wnj"
address: Address
```

This tells Pydantic that `address` should be validated using the `Address` model.

---

# 15. More Complex Nested Structure

A user can also have multiple addresses.

```python id="amqczt"
from typing import List


class UserWithAddresses(BaseModel):
    id: int
    name: str
    addresses: List[Address]
```

This means:

```text id="997mld"
addresses must be a list
each item inside the list must be an Address model
```

---

# 16. Optional Nested Model

Sometimes a nested field may not always exist.

```python id="sjq3n7"
from typing import Optional


class UserProfile(BaseModel):
    id: int
    name: str
    address: Optional[Address] = None
```

This means:

* `address` can be an `Address`
* or it can be `None`
* if not provided, it defaults to `None`

---

# 17. Real-World Examples

Nested Pydantic models are useful for:

* API request bodies
* API response schemas
* User profiles
* Order management systems
* Invoice data
* E-commerce carts
* Address books
* Booking systems
* Form validation

---

# 18. Common Mistakes

## Forgetting to Inherit BaseModel

Incorrect:

```python id="gse1he"
class Address:
    street: str
```

Correct:

```python id="l8sb44"
class Address(BaseModel):
    street: str
```

## Using dict Instead of a Model

Less structured:

```python id="41z9kg"
address: dict
```

Better:

```python id="whizej"
address: Address
```

## Passing Dictionary Without Unpacking

Incorrect:

```python id="sq6l6m"
user = User(user_data)
```

Correct:

```python id="z3dzyh"
user = User(**user_data)
```

---

# Key Takeaways

* Nested models allow one Pydantic model inside another.
* They are useful for real-world hierarchical data.
* A nested field can use another model class as its type annotation.
* Pydantic validates the parent model and the nested model.
* Nested dictionaries can automatically become nested Pydantic models.
* Use `model_dump()` to convert nested models into dictionaries.
* Nested models make complex data cleaner, reusable, and easier to validate.
