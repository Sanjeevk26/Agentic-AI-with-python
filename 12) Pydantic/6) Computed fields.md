# Pydantic Computed Fields

## Overview

Pydantic supports computed fields using:

```python id="kwlv2p"
@computed_field
@property
```

A computed field is a value that is calculated from other model fields.

Instead of manually calculating values in controllers, services, or other application logic, we can keep simple derived logic inside the Pydantic model itself.

---

# 1. What Is a Computed Field?

A computed field is a field that is not directly provided by the user.

It is calculated from existing fields.

Example:

```text id="iwdlub"
price = 100
quantity = 3
total_price = price * quantity
```

Here, `total_price` can be computed from `price` and `quantity`.

---

# 2. Importing computed_field

```python id="m7bce9"
from pydantic import BaseModel, computed_field
```

`BaseModel` is used to create the model.

`computed_field` marks a property as a computed Pydantic field.

---

# 3. Basic Product Example

```python id="zatvr5"
from pydantic import BaseModel, computed_field


class Product(BaseModel):
    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        return self.price * self.quantity
```

Here:

* `price` is provided by the user.
* `quantity` is provided by the user.
* `total_price` is calculated automatically.

---

# 4. Why Use @property?

The `@property` decorator makes a method accessible like an attribute.

Without property-style access:

```python id="mesopq"
product.total_price()
```

With `@property`:

```python id="bot6n6"
product.total_price
```

So the computed field behaves like a normal model field.

---

# 5. Why Use @computed_field?

`@computed_field` tells Pydantic to include this property as a model field.

This means it can appear in:

```python id="adz1je"
model_dump()
```

Example:

```python id="1afowt"
product = Product(
    price=100,
    quantity=3,
)

print(product.total_price)
print(product.model_dump())
```

Output:

```python id="k48cp3"
300.0
{
    "price": 100.0,
    "quantity": 3,
    "total_price": 300.0,
}
```

---

# 6. Correct Decorator Order

Use this order:

```python id="p4lxe7"
@computed_field
@property
def total_price(self) -> float:
    return self.price * self.quantity
```

This makes the value both:

* A Python property
* A Pydantic computed field

---

# 7. Booking Example

A hotel booking may have:

* `user_id`
* `room_id`
* `nights`
* `rate_per_night`
* `total_amount`

The user provides:

```text id="b856sj"
user_id
room_id
nights
rate_per_night
```

The model computes:

```text id="006bg7"
total_amount = nights * rate_per_night
```

---

# 8. Booking Model

```python id="rh3iae"
from pydantic import BaseModel, Field, computed_field


class Booking(BaseModel):
    user_id: int
    room_id: int

    nights: int = Field(
        ...,
        ge=1,
    )

    rate_per_night: float

    @computed_field
    @property
    def total_amount(self) -> float:
        return self.nights * self.rate_per_night
```

Here:

```python id="dfo5b4"
nights: int = Field(..., ge=1)
```

means the number of nights must be at least 1.

---

# 9. Using the Booking Model

```python id="1ojras"
booking = Booking(
    user_id=123,
    room_id=456,
    nights=3,
    rate_per_night=2500,
)

print(booking.total_amount)
```

Output:

```text id="jviftg"
7500.0
```

The computed field is accessed like an attribute:

```python id="lzysyh"
booking.total_amount
```

not like a method:

```python id="l78jq5"
booking.total_amount()
```

---

# 10. Computed Fields in model_dump()

Computed fields are included in serialization.

```python id="ojs4x0"
print(booking.model_dump())
```

Output:

```python id="7un6y2"
{
    "user_id": 123,
    "room_id": 456,
    "nights": 3,
    "rate_per_night": 2500.0,
    "total_amount": 7500.0,
}
```

This is useful when returning API responses.

---

# 11. Why Computed Fields Are Useful

Computed fields help keep derived logic close to the data model.

Examples:

* Product total price
* Booking total amount
* Discounted price
* Full name from first and last name
* Invoice line total
* Cart subtotal
* Tax amount
* Final payable amount

---

# 12. Example: Discounted Product

```python id="hja3k8"
class DiscountedProduct(BaseModel):
    price: float
    discount_percent: float

    @computed_field
    @property
    def final_price(self) -> float:
        discount_amount = self.price * self.discount_percent / 100
        return self.price - discount_amount
```

If:

```text id="rh5z36"
price = 1000
discount_percent = 10
```

then:

```text id="0bo59e"
final_price = 900
```

---

# 13. Computed Field Is Not Input Data

Usually, computed fields should not be passed by the user.

This is wrong in concept:

```python id="wpoimr"
Booking(
    user_id=123,
    room_id=456,
    nights=3,
    rate_per_night=2500,
    total_amount=999999,
)
```

`total_amount` should be calculated by the model.

The user should provide only the source fields.

---

# 14. Common Mistakes

## Calling Computed Field Like a Method

Incorrect:

```python id="qlqy9q"
booking.total_amount()
```

Correct:

```python id="i113ui"
booking.total_amount
```

## Forgetting @property

Less ideal:

```python id="x2zphu"
@computed_field
def total_amount(self) -> float:
    return self.nights * self.rate_per_night
```

Better:

```python id="k3xlik"
@computed_field
@property
def total_amount(self) -> float:
    return self.nights * self.rate_per_night
```

## Putting Business-Heavy Logic Inside the Model

Computed fields are great for simple derived values.

Avoid putting very heavy business logic inside Pydantic models.

Good:

```text id="ox78wb"
total_amount = nights * rate_per_night
```

Avoid:

```text id="74f0d3"
calling payment gateways
updating databases
sending emails
running long workflows
```

---

# 15. Computed Field Flow

```text id="g9qz9i"
Input data is provided
        ↓
Pydantic validates normal fields
        ↓
Computed field calculates derived value
        ↓
Computed value is available as an attribute
        ↓
Computed value appears in model_dump()
```

---

# Key Takeaways

* `computed_field` is used for calculated fields in Pydantic.
* Use `@computed_field` with `@property`.
* Computed fields are accessed like attributes.
* Computed fields can appear in `model_dump()`.
* They are useful for totals, derived values, and simple calculations.
* They reduce repeated logic in controllers or services.
* Use them for simple derived logic, not heavy business workflows.
