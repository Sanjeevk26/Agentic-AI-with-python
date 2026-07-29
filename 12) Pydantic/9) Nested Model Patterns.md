# Pydantic Advanced Nested Models

## Overview

Advanced nested models in Pydantic are not a completely new concept.

They are practical examples of how nested models are used in real-world applications.

This lesson covers:

* Optional nested models
* Mixed data types using `Union`
* Lists of mixed model types
* Deeply nested structures
* Real-world hierarchical data modeling

---

# 1. What Are Advanced Nested Models?

A nested model means one Pydantic model is used inside another model.

Example:

```python id="ap4s6c"
class Company(BaseModel):
    name: str
    address: Address
```

Advanced nested models go further.

They allow things like:

```text id="4uuz5s"
Company may or may not have an address
Employee may or may not belong to a company
Article sections can be text or images
Organization can contain address, city, state, and country
```

---

# 2. Optional Nested Model

Sometimes a nested model may not always exist.

Example:

A company may have an address.

But some companies may be fully remote and may not have a physical office address.

For this, use `Optional`.

```python id="ixsjfe"
from typing import Optional
```

---

# 3. Address Model

```python id="9wil3n"
from pydantic import BaseModel


class Address(BaseModel):
    street: str
    city: str
    postal_code: str
```

This model defines a basic address.

---

# 4. Company with Optional Address

```python id="bq9iit"
class Company(BaseModel):
    name: str
    address: Optional[Address] = None
```

This means:

* `name` is required
* `address` can be an `Address`
* `address` can also be `None`
* if not provided, address defaults to `None`

---

# 5. Company Without Address

```python id="5w0xen"
company = Company(
    name="Remote Chai Startup",
)
```

This is valid.

The address becomes:

```python id="fkik0c"
address=None
```

---

# 6. Company With Address

```python id="264pn8"
company = Company(
    name="Chai Office",
    address={
        "street": "123 Market Road",
        "city": "Ahmedabad",
        "postal_code": "380001",
    },
)
```

Pydantic automatically converts the nested dictionary into an `Address` model.

---

# 7. Employee with Optional Company

An employee may belong to a company.

But an employee may also be a freelancer.

```python id="05x1kw"
class Employee(BaseModel):
    name: str
    company: Optional[Company] = None
```

This means:

* `name` is required
* `company` can be a `Company`
* `company` can be `None`

---

# 8. Employee Without Company

```python id="0svam5"
employee = Employee(
    name="Freelancer Ravi",
)
```

This is valid because company is optional.

---

# 9. Employee With Company

```python id="jta03i"
employee = Employee(
    name="Anita",
    company={
        "name": "Chai Office",
        "address": {
            "street": "123 Market Road",
            "city": "Ahmedabad",
            "postal_code": "380001",
        },
    },
)
```

Pydantic validates:

```text id="qee0su"
Employee
 └── Company
      └── Address
```

---

# 10. Mixed Data Types Using Union

Sometimes a field can accept more than one model type.

For this, use `Union`.

```python id="onq1im"
from typing import Union
```

Example:

An article may contain:

* Text sections
* Image sections

So one section can be either `TextContent` or `ImageContent`.

---

# 11. TextContent Model

```python id="b0a3zm"
class TextContent(BaseModel):
    type: str = "text"
    content: str
```

This represents a text section.

---

# 12. ImageContent Model

```python id="74bx10"
class ImageContent(BaseModel):
    type: str = "image"
    url: str
    alt_text: str
```

This represents an image section.

---

# 13. Article with Mixed Sections

```python id="5nqdoq"
from typing import List, Union


class Article(BaseModel):
    title: str
    sections: List[Union[TextContent, ImageContent]]
```

This means:

* `sections` must be a list
* each item in the list can be either:

  * `TextContent`
  * `ImageContent`

---

# 14. Article Example

```python id="g8me3d"
article = Article(
    title="Learning Pydantic",
    sections=[
        {
            "type": "text",
            "content": "Pydantic helps validate structured data.",
        },
        {
            "type": "image",
            "url": "https://example.com/pydantic.png",
            "alt_text": "Pydantic logo",
        },
    ],
)
```

This is useful for content-heavy applications like:

* Blogs
* CMS platforms
* Documentation systems
* Learning platforms
* News articles

---

# 15. Deeply Nested Structures

Sometimes models are nested across many levels.

Example:

```text id="k0jjwz"
Organization
 └── Address
      └── City
           └── State
                └── Country
```

This is called a deeply nested structure.

---

# 16. Country Model

```python id="0ec4uj"
class Country(BaseModel):
    name: str
    code: str
```

Example:

```text id="x5jtfl"
India, IN
United States, US
```

---

# 17. State Model

```python id="iss09f"
class State(BaseModel):
    name: str
    country: Country
```

A state belongs to a country.

---

# 18. City Model

```python id="ay92ck"
class City(BaseModel):
    name: str
    state: State
```

A city belongs to a state.

---

# 19. Address Model with City

```python id="mkgtn9"
class DetailedAddress(BaseModel):
    street: str
    city: City
    postal_code: str
```

An address belongs to a city.

---

# 20. Organization Model

```python id="6za4oi"
class Organization(BaseModel):
    name: str
    headquarters: DetailedAddress
    branches: List[DetailedAddress] = []
```

An organization has:

* a name
* a headquarters address
* a list of branch addresses

---

# 21. Better Default for Lists

Avoid this:

```python id="ozxcbc"
branches: List[DetailedAddress] = []
```

Better:

```python id="he5gko"
from pydantic import Field


branches: List[DetailedAddress] = Field(default_factory=list)
```

This ensures every organization gets its own separate empty list.

---

# 22. Deep Nesting Example

```python id="1j5tv3"
organization = Organization(
    name="Chai Global",
    headquarters={
        "street": "123 Business Road",
        "city": {
            "name": "Ahmedabad",
            "state": {
                "name": "Gujarat",
                "country": {
                    "name": "India",
                    "code": "IN",
                },
            },
        },
        "postal_code": "380001",
    },
)
```

Pydantic automatically validates the full structure.

---

# 23. Why Deeply Nested Models Are Useful

Deep nesting is useful when the application needs to represent structured real-world relationships.

Examples:

* Company and branches
* Country, state, city, and address
* Order, customer, product, and shipment
* Course, instructor, modules, and lessons
* Organization, departments, and employees

---

# 24. Important Concepts

## Optional Nested Model

```python id="nq5zb0"
address: Optional[Address] = None
```

The nested model may or may not exist.

## Mixed Data Types

```python id="d6ncer"
Union[TextContent, ImageContent]
```

The field can accept more than one model type.

## List of Mixed Types

```python id="stbrqr"
List[Union[TextContent, ImageContent]]
```

The field must be a list, and each item can be one of multiple allowed model types.

## Deep Nesting

```python id="tz52i0"
Organization → Address → City → State → Country
```

One model is nested inside another across multiple levels.

---

# 25. Common Mistakes

## Forgetting Optional Default

This can still be required:

```python id="og958w"
address: Optional[Address]
```

This is optional during object creation:

```python id="f5ydei"
address: Optional[Address] = None
```

## Using Plain dict Too Often

Less structured:

```python id="s3dhu3"
address: dict
```

Better:

```python id="6o3cih"
address: Address
```

## Using Mutable List Default

Avoid:

```python id="v8itlu"
branches: List[DetailedAddress] = []
```

Prefer:

```python id="usxhni"
branches: List[DetailedAddress] = Field(default_factory=list)
```

## Over-Nesting Without Need

Deep nesting is powerful, but too much nesting can make code harder to read.

Use it when the data relationship actually needs it.

---

# Key Takeaways

* Advanced nested models are practical real-world uses of nested Pydantic models.
* `Optional[Model] = None` allows a nested model to be absent.
* `Union[A, B]` allows a field to accept more than one model type.
* `List[Union[A, B]]` allows a list of mixed model types.
* Deeply nested structures can model real-world relationships.
* Pydantic validates nested structures automatically.
* Use `Field(default_factory=list)` for default empty lists.
* Keep nesting meaningful and readable.
