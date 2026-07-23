# Pydantic Product Model

## Overview

This lesson continues the basics of Pydantic.

The goal is to create another Pydantic model, this time for a product.

This helps reinforce:

* Importing `BaseModel`
* Creating a Pydantic model class
* Using type annotations
* Setting default values
* Creating valid model objects
* Handling missing required fields
* Understanding automatic type conversion

---

# 1. Import BaseModel

Most Pydantic models inherit from `BaseModel`.

```python
from pydantic import BaseModel
```

`BaseModel` gives the class Pydantic's validation features.

---

# 2. Create a Product Model

A Pydantic model defines the structure of the data.

```python
class Product(BaseModel):
    id: int
    name: str
    price: float
    in_stock: bool = True
```

This model says:

* `id` should be an integer
* `name` should be a string
* `price` should be a float
* `in_stock` should be a boolean
* `in_stock` has a default value of `True`

---

# 3. Type Annotations Are Required

Type annotations are very important in Pydantic.

```python
id: int
name: str
price: float
in_stock: bool
```

Pydantic uses these annotations to validate the data.

Without type annotations, Pydantic does not know what type of data each field should contain.

---

# 4. Creating a Valid Product

```python
product_one = Product(
    id=1,
    name="Laptop",
    price=999.99,
    in_stock=True,
)
```

This is valid because all contain.

---

# 4. Creating a Valid Product

````python
product_one required fields are provided with the correct types.

---

# 5. Using Default Values

The `in_stock` field has a default value.

```python
in_stock: bool = True
````

So this is also valid:

```python
product_two = Product(
    id=2,
    name="Mouse",
    price=24.33,
)
```

Since `in_stock` is not provided, Pydantic uses the default value:

```python
in_stock=True
```

---

# 6. Missing Required Fields

This is invalid:

```python
product_three = Product(
    name="Keyboard",
)
```

The model requires:

```python
id
price
```

Since these fields are missing, Pydantic raises a validation error.

---

# 7. Validation Error

When required fields are missing or invalid, Pydantic raises a `ValidationError`.

Example:

```text
Field required
```

This helps catch problems early instead of allowing bad data to move deeper into the application.

---

# 8. Automatic Type Conversion

Pydantic tries to convert compatible values.

Example:

```python
product = Product(
    id="123",
    name="Monitor",
    price="499.99",
    in_stock="true",
)
```

Pydantic may convert:

```text
"123" → 123
"499.99" → 499.99
"true" → True
```

This is useful, but you should not fully depend on automatic conversion.

It is always better to pass clean and correct data.

---

# 9. Type Conversion Examples

## Integer Conversion

```python
id="123"
```

can become:

```python
id=123
```

## Float Conversion

```python
price="123"
```

can become:

```python
price=123.0
```

## Boolean Conversion

```python
in_stock="true"
```

can become:

```python
in_stock=True
```

---

# 10. When Conversion Fails

Pydantic cannot convert every value.

Example:

```python
Product(
    id="abc",
    name="Keyboard",
    price="free",
)
```

This fails because:

* `"abc"` cannot become an integer
* `"free"` cannot become a float

---

# 11. Best Practices

## Always Use Type Annotations

This is non-negotiable in Pydantic.

```python
id: int
name: str
price: float
```

## Use Appropriate Types

Choose the right type for each field.

Examples:

```python
id: int
name: str
price: float
in_stock: bool
```

## Use Sensible Defaults

Use default values when it makes sense.

```python
in_stock: bool = True
```

This keeps object creation simple when a field has a common default value.

## Do Not Rely Too Much on Conversion

Pydantic can convert values, but the best practice is still to send clean input data.

---

# 12. Why This Is Useful

In real applications, product data may come from:

* APIs
* Forms
* Databases
* CSV files
* JSON files
* External services

Pydantic ensures that the data is valid before it is used.

This reduces bugs caused by missing or incorrect fields.

---

# Key Takeaways

* Pydantic models inherit from `BaseModel`.
* A model defines how data should look.
* Type annotations are required for validation.
* Fields without default values are required.
* Fields with default values are optional during object creation.
* Pydantic raises validation errors for missing required fields.
* Pydantic may convert compatible values automatically.
* Always prefer clean and correct input data.
* Use sensible default values where appropriate.
