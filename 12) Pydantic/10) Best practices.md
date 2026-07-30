# Pydantic Best Practices

## Overview

This lesson covers best practices for building Pydantic models, especially when working with:

* Nested models
* Recursive models
* Optional fields
* Union types
* Computed fields
* Real-world data relationships
* Performance considerations

These are not strict rules, but practical guidelines that can help keep models clean, readable, and easier to maintain.

---

# 1. Model Organization

Good model organization makes Pydantic code easier to read and maintain.

When models become nested or complex, the order in which they are defined matters.

---

# 2. Define Leaf Models First

A useful practice is to define the smallest or lowest-level models first.

These are sometimes called leaf models.

Example:

```text id="gp9kwp"
Organization
 └── Address
      └── City
           └── State
                └── Country
```

In this structure, `Country` is the leaf model.

So define it first:

```python id="r1o4vl"
class Country(BaseModel):
    name: str
    code: str
```

Then build upward:

```python id="b57oab"
class State(BaseModel):
    name: str
    country: Country
```

Then:

```python id="h5edmb"
class City(BaseModel):
    name: str
    state: State
```

This makes the dependency flow clear.

---

# 3. Build Models Upward

After defining the leaf model, gradually compose larger models.

Example:

```text id="8vvokx"
Country
    ↓
State
    ↓
City
    ↓
Address
    ↓
Organization
```

This approach helps because every model depends only on models already defined above it.

---

# 4. Use Clear Naming

Naming is one of the hardest parts of programming.

Use meaningful names for:

* Models
* Fields
* Functions
* Validators
* Computed fields

Good names:

```python id="4uuxrq"
Address
Company
Employee
Organization
OrderItem
CustomerProfile
```

Poor names:

```python id="nwsbs3"
A
B
Data
Stuff
Obj
```

If the model name is not meaningful, the model itself may become hard to understand.

---

# 5. Group Related Models Together

Keep related models close to each other.

For example, these can stay in one file if they belong to the same domain:

```text id="4nm87l"
Country
State
City
Address
Organization
```

This helps readers understand the complete relationship in one place.

However, do not put unrelated models in the same file.

For larger applications, split models by domain.

Example:

```text id="2hksml"
models/
│
├── address.py
├── company.py
├── order.py
├── user.py
└── payment.py
```

---

# 6. Keep Models Modular

A model should represent one clear concept.

Instead of creating one huge model, break it into smaller models.

Less clean:

```python id="7bsfnj"
class Organization(BaseModel):
    country_name: str
    country_code: str
    state_name: str
    city_name: str
    street: str
    postal_code: str
```

Cleaner:

```python id="1oe67q"
class Country(BaseModel):
    name: str
    code: str


class State(BaseModel):
    name: str
    country: Country


class City(BaseModel):
    name: str
    state: State


class Address(BaseModel):
    street: str
    city: City
    postal_code: str
```

This is easier to reuse and validate.

---

# 7. Performance Considerations

Pydantic is powerful, but complex models can impact performance.

Be careful with:

* Deeply nested models
* Large lists of nested models
* Recursive models
* Circular references
* Overused computed fields

---

# 8. Deep Nesting Can Impact Performance

Deep nesting means one model contains another model, which contains another model, and so on.

Example:

```text id="81jjlx"
Organization
 └── Address
      └── City
           └── State
                └── Country
```

This is sometimes necessary, but avoid unnecessary nesting.

Very deep nesting can make validation slower and code harder to understand.

---

# 9. Large Lists of Nested Models

A large list of nested models can be expensive to validate.

Example:

```python id="85ji1m"
class Organization(BaseModel):
    branches: list[Address]
```

If `branches` contains thousands of addresses, Pydantic has to validate every item.

For very large lists, consider:

* Pagination
* Batch processing
* Validating only required fields
* Avoiding unnecessary nested data
* Returning summary models instead of full models

---

# 10. Be Careful with Circular References

Circular references happen when models point back to each other.

Example:

```text id="6bo04r"
Employee → Company → Employee
```

This can create complex validation and serialization issues.

Circular references can also increase memory usage if not handled carefully.

Try to avoid circular relationships unless they are truly required.

---

# 11. Recursive Models Need Care

Recursive models are useful for tree-like data.

Examples:

* Comments and replies
* Categories and subcategories
* Folder and subfolders

Example:

```python id="q5tlwl"
class Comment(BaseModel):
    id: int
    content: str
    replies: list["Comment"] = Field(default_factory=list)
```

Recursive models are powerful, but they can grow very large.

Be careful with:

* Deep reply chains
* Infinite loops in traversal logic
* Large recursive trees
* Serializing too much data at once

---

# 12. model_dump() and Serialization

`model_dump()` converts Pydantic models into dictionaries.

```python id="p2g0lc"
data = model.model_dump()
```

This is useful when sending data to:

* APIs
* Logs
* JSON responses
* Storage layers

Practical correction: `model_dump()` helps with serialization, but it is not automatically a performance fix. Good model design, pagination, and avoiding unnecessary nesting are still important.

---

# 13. Lazy Loading Concept

Lazy loading means loading or calculating data only when it is actually needed.

In Pydantic, be careful with computed fields.

A computed field is calculated when accessed or serialized.

Example:

```python id="91eysk"
@computed_field
@property
def total_price(self) -> float:
    return self.price * self.quantity
```

Computed fields are useful, but do not overuse them for heavy logic.

---

# 14. Do Not Overuse Computed Fields

Computed fields are good for simple derived values.

Good examples:

* Full name
* Total price
* Discount amount
* Final price
* Booking total

Avoid using computed fields for heavy work such as:

* Database queries
* API calls
* Payment processing
* Machine learning inference
* Large calculations
* File processing

Keep computed fields lightweight.

---

# 15. Data Modeling Tips

Pydantic models should represent real-world relationships clearly.

Before creating models, ask:

```text id="p9oy59"
What real-world object am I modeling?
What fields does it need?
Which fields are required?
Which fields are optional?
Which fields are nested relationships?
Which fields are computed?
```

---

# 16. Model Real-World Relationships

Design models based on the real problem.

Example:

A company may have an address.

```python id="fw01er"
class Company(BaseModel):
    name: str
    address: Address | None = None
```

An employee may belong to a company.

```python id="q1lzxx"
class Employee(BaseModel):
    name: str
    company: Company | None = None
```

These models match real-world relationships.

---

# 17. Use Optional Appropriately

Not every field is required.

Use optional fields when the data may not exist.

Example:

```python id="tdtv2b"
address: Address | None = None
```

This means the address can be missing.

Optional fields are useful for:

* Freelancers without a company
* Remote companies without an office
* Users without profile images
* Products without discounts
* Articles without images

---

# 18. Keep Models Close to Database Design

It often helps to keep Pydantic models close to database models.

Example:

Database table:

```text id="jfmhq3"
users
- id
- name
- email
- company_id
```

Pydantic model:

```python id="4cijy1"
class User(BaseModel):
    id: int
    name: str
    email: str
    company_id: int | None = None
```

This makes it easier to move data between the database and application.

However, not every Pydantic model must map directly to a database table.

Some models are only for:

* API requests
* API responses
* Validation
* Computed output
* Internal processing

---

# 19. Use Union Types for Polymorphic Relationships

Use union types when a field can contain more than one kind of model.

Example:

```python id="f5x4zc"
class Article(BaseModel):
    sections: list[TextContent | ImageContent]
```

This means each section can be either:

* `TextContent`
* `ImageContent`

This is useful for polymorphic relationships.

Examples:

* Article section can be text, image, or video.
* Payment method can be card, UPI, or wallet.
* Notification can be email, SMS, or push.
* Content block can be paragraph, image, code, or quote.

---

# 20. Validate Business Rules

Business rules are more important than technical elegance.

Examples:

* Discount cannot be greater than 100%.
* Sale price cannot be higher than original price.
* Start date must be before end date.
* Password and confirm password must match.
* A card payment must have a card number.
* A booking must have at least one night.

Use Pydantic validators for business rules.

Example:

```python id="3ufcv8"
@model_validator(mode="after")
def validate_prices(self):
    if self.sale_price > self.original_price:
        raise ValueError(
            "Sale price cannot be greater than original price"
        )

    return self
```

---

# 21. Model Organization Checklist

Use this checklist while organizing models:

```text id="jg3212"
Define leaf models first
Build upward gradually
Use clear names
Group related models together
Keep models modular
Avoid unnecessary nesting
Use optional fields where appropriate
Use validators for business rules
```

---

# 22. Performance Checklist

Use this checklist for performance-conscious modeling:

```text id="fn7zq9"
Avoid unnecessary deep nesting
Avoid huge nested lists where possible
Use pagination for large lists
Be careful with recursive models
Avoid circular references
Keep computed fields lightweight
Avoid expensive work inside models
Serialize only the data you need
```

---

# 23. Data Modeling Checklist

Use this checklist while designing Pydantic data models:

```text id="zseemo"
Model real-world relationships
Keep required fields truly required
Use Optional for fields that may be absent
Use Union for polymorphic structures
Keep API models close to expected payloads
Keep database models close to stored data
Validate business rules
Prefer clarity over cleverness
```

---

# Key Takeaways

* Define leaf models first.
* Build larger models upward from smaller models.
* Use clear and meaningful names.
* Group related models together.
* Keep models modular.
* Deep nesting can affect readability and performance.
* Large lists of nested models may need pagination.
* Be careful with circular and recursive references.
* Do not overuse computed fields.
* Use optional fields where relationships may not exist.
* Use union types for polymorphic relationships.
* Always validate important business rules.
* Best practices are not fixed rules; use what works for your application.
