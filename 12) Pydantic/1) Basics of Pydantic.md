# Python Pydantic Basics

## Overview

Pydantic is a Python library used for:

* Data validation
* Data parsing
* Data serialization
* Data deserialization
* Settings management
* API request and response validation

It is widely used in modern Python applications, especially with frameworks like FastAPI.

---

# 1. What Is Pydantic?

Pydantic helps ensure that data follows the expected structure and type.

For example, if a field should be a string, integer, or boolean, Pydantic can validate that automatically.

Without Pydantic, Python allows this:

```python id="afvn57"
name = "Chai Code"
name = 87
```

Python does not stop the variable from changing type.

Pydantic helps prevent such unexpected data issues when working with structured data.

---

# 2. Why Use Pydantic?

Pydantic is useful when working with data coming from:

* APIs
* Forms
* JSON files
* Databases
* Environment variables
* Configuration files
* User input
* External services

It helps catch bad data early.

---

# 3. Main Uses of Pydantic

## Data Validation

Checks whether the data matches the expected type and structure.

Example:

```text id="r98w7e"
id should be an integer
name should be a string
is_active should be a boolean
```

## Data Parsing

Pydantic can convert compatible values automatically.

Example:

```python id="g0feny"
"id": "101"
```

can be converted into:

```python id="otv733"
id = 101
```

## Settings Management

Pydantic can also help manage application configuration, such as environment variables.

This is common in web applications.

## API Development

FastAPI uses Pydantic heavily for request and response models.

---

# 4. Installing Pydantic

Create a virtual environment:

```bash id="solxy7"
python -m venv venv
```

Activate it on macOS or Linux:

```bash id="q6h1wj"
source venv/bin/activate
```

Activate it on Windows:

```bash id="z0z5o7"
venv\Scripts\activate
```

Install Pydantic:

```bash id="muu7ma"
pip install pydantic
```

---

# 5. Basic Project Structure

Example folder structure:

```text id="d7xduw"
14_pydantic/
│
├── venv/
│
└── 01_basics/
    └── first_model.py
```

Run the file:

```bash id="ru6m36"
python 01_basics/first_model.py
```

---

# 6. BaseModel

Most Pydantic models inherit from `BaseModel`.

```python id="bxvfds"
from pydantic import BaseModel
```

A Pydantic model is usually a class that defines the expected data structure.

```python id="en2v7m"
class User(BaseModel):
    id: int
    name: str
    is_active: bool
```

This model says:

* `id` must be an integer
* `name` must be a string
* `is_active` must be a boolean

---

# 7. Type Annotations

Pydantic uses Python type annotations.

```python id="rz2krw"
id: int
name: str
is_active: bool
```

These annotations tell Pydantic what kind of data is expected.

Common types include:

```python id="e1xyj9"
int
str
bool
float
list
dict
datetime
```

---

# 8. Creating a Model Object

Input data usually comes as a dictionary.

```python id="svm9zm"
input_data = {
    "id": 101,
    "name": "Chai Code",
    "is_active": True,
}
```

Create the Pydantic object:

```python id="bkj12m"
user = User(**input_data)
```

The `**` unpacks the dictionary.

---

# 9. Why Use **input_data?

This is correct:

```python id="qkxsgh"
user = User(**input_data)
```

This passes dictionary keys as named arguments.

It becomes similar to:

```python id="e747f5"
user = User(
    id=101,
    name="Chai Code",
    is_active=True,
)
```

This is incorrect:

```python id="55mye8"
user = User(input_data)
```

That passes the whole dictionary as one positional argument, which is not what the model expects.

---

# 10. Automatic Validation

When a Pydantic model object is created, Pydantic validates the data immediately.

```python id="zc7589"
user = User(**input_data)
```

At this moment, Pydantic checks each field.

If the data is valid, the object is created.

If the data is invalid, Pydantic raises a validation error.

---

# 11. Validation Error Example

```python id="klrhkp"
bad_data = {
    "id": 101,
    "name": "Chai Code",
    "is_active": 25,
}

user = User(**bad_data)
```

`is_active` expects a boolean value.

Pydantic may reject values that cannot be interpreted as valid booleans.

The error is usually a `ValidationError`.

---

# 12. Importing ValidationError

```python id="zvs0yu"
from pydantic import ValidationError
```

Example:

```python id="qf1oka"
try:
    user = User(**bad_data)
except ValidationError as error:
    print(error)
```

This allows the program to handle bad data gracefully instead of crashing unexpectedly.

---

# 13. Pydantic Type Conversion

Pydantic often tries to convert compatible values.

Example:

```python id="fl8i4g"
input_data = {
    "id": "101",
    "name": "Chai Code",
    "is_active": True,
}
```

Although `"101"` is a string, Pydantic can convert it into an integer.

```python id="tm0j5p"
user = User(**input_data)

print(user.id)
print(type(user.id))
```

Output:

```text id="dofofv"
101
<class 'int'>
```

---

# 14. When Conversion Fails

This value cannot be converted into an integer:

```python id="iqhmxd"
"id": "101A"
```

Example:

```python id="wokfsp"
bad_data = {
    "id": "101A",
    "name": "Chai Code",
    "is_active": True,
}
```

Pydantic raises a validation error because `"101A"` is not a valid integer.

---

# 15. Pydantic Model Output

When printed, a Pydantic model shows its validated fields.

```python id="d1gsgb"
print(user)
```

Example output:

```text id="qk9tsn"
id=101 name='Chai Code' is_active=True
```

---

# 16. Converting Model to Dictionary

In Pydantic v2, use:

```python id="yzf1zf"
user.model_dump()
```

Example:

```python id="n5ofxn"
print(user.model_dump())
```

Output:

```python id="z2l8xh"
{
    "id": 101,
    "name": "Chai Code",
    "is_active": True,
}
```

---

# 17. Strict Validation

By default, Pydantic may convert compatible values.

For example:

```python id="rf8vc5"
"id": "101"
```

may become:

```python id="m50oc9"
id = 101
```

Sometimes strict validation is preferred.

```python id="1y7lqi"
from pydantic import BaseModel, StrictInt


class StrictUser(BaseModel):
    id: StrictInt
    name: str
```

Now `"101"` as a string will not be accepted for `id`.

---

# 18. Important Concepts

## BaseModel

The parent class used to create Pydantic models.

## Field

A model attribute with a type annotation.

```python id="sq5k8m"
name: str
```

## Validation

Checking whether input data is correct.

## Parsing

Converting input data into the expected type when possible.

## Model Instantiation

Creating an object from the model class.

```python id="su2xjf"
user = User(**input_data)
```

---

# 19. Common Mistakes

## Not Installing Pydantic

```bash id="pmgpqc"
pip install pydantic
```

## Misspelling Pydantic

Correct:

```python id="za8im6"
from pydantic import BaseModel
```

Incorrect:

```python id="xr6qk6"
from pydentic import BaseModel
```

## Passing Dictionary Without Unpacking

Incorrect:

```python id="lapn1g"
user = User(input_data)
```

Correct:

```python id="ncbjz1"
user = User(**input_data)
```

## Expecting No Type Conversion

Pydantic may convert values when conversion is safe.

Use strict types when conversion should not happen.

---

# 20. Why Pydantic Is Powerful

Pydantic helps keep data clean at the point of creation.

This is useful because many application bugs happen when wrong data enters the system.

Instead of discovering the problem much later, Pydantic catches it early.

Example:

```text id="zudmcq"
Bad input comes in
        ↓
Pydantic validates it
        ↓
Valid data becomes a model object
        ↓
Invalid data raises a clear error
```

---

# Key Takeaways

* Pydantic is used for data validation and parsing.
* It is also used for settings management.
* FastAPI uses Pydantic heavily.
* Most models inherit from `BaseModel`.
* Pydantic models use type annotations.
* Data is validated when the model object is created.
* Use `**dictionary` to unpack data into a model.
* Pydantic can convert compatible values automatically.
* Invalid data raises a `ValidationError`.
* Use strict types when automatic conversion is not desired.
