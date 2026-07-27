# Pydantic Nested Models
# Topics:
# 1. BaseModel
# 2. Nested models
# 3. Model composition
# 4. Nested dictionary validation
# 5. List of nested models
# 6. Optional nested model
# 7. ValidationError
# -------------------------------------------------

from typing import List, Optional

from pydantic import BaseModel, ValidationError


# =================================================
# 1. Address Model
# =================================================

class Address(BaseModel):
    """
    Address is a standalone Pydantic model.

    It can also be used inside another model.
    """

    street: str
    city: str
    postal_code: str


# =================================================
# 2. User Model with Nested Address
# =================================================

class User(BaseModel):
    """
    User contains another Pydantic model.

    address is not a plain string or dictionary.
    It is an Address model.
    """

    id: int
    name: str
    address: Address


# =================================================
# 3. Creating Nested Model Separately
# =================================================

def separate_address_example() -> None:
    """
    Create Address first, then pass it to User.
    """

    address = Address(
        street="123 MG Road",
        city="Bengaluru",
        postal_code="560001",
    )

    user = User(
        id=1,
        name="Hitesh",
        address=address,
    )

    print("\nSEPARATE ADDRESS OBJECT")
    print("-" * 50)

    print(user)
    print("City:", user.address.city)
    print("Postal code:", user.address.postal_code)


# =================================================
# 4. Creating Nested Model from Dictionary
# =================================================

def nested_dictionary_example() -> None:
    """
    Pydantic can automatically convert a nested
    dictionary into a nested Pydantic model.
    """

    user_data = {
        "id": 2,
        "name": "Amit",
        "address": {
            "street": "321 Park Street",
            "city": "Delhi",
            "postal_code": "110001",
        },
    }

    user = User(**user_data)

    print("\nNESTED DICTIONARY")
    print("-" * 50)

    print(user)
    print("Address object type:", type(user.address))
    print("Model dump:", user.model_dump())


# =================================================
# 5. Invalid Nested Data
# =================================================

def invalid_nested_data_example() -> None:
    """
    Show validation error when nested data is missing
    a required field.
    """

    bad_user_data = {
        "id": 3,
        "name": "Ravi",
        "address": {
            "street": "456 Lake Road",
            "city": "Mumbai",
            # postal_code is missing
        },
    }

    print("\nINVALID NESTED DATA")
    print("-" * 50)

    try:
        User(**bad_user_data)

    except ValidationError as error:
        print("Validation failed:")
        print(error)


# =================================================
# 6. List of Nested Models
# =================================================

class UserWithAddresses(BaseModel):
    """
    A user can have multiple addresses.

    addresses is a list of Address models.
    """

    id: int
    name: str
    addresses: List[Address]


def list_of_nested_models_example() -> None:
    """
    Demonstrate a list of nested Pydantic models.
    """

    user_data = {
        "id": 4,
        "name": "Neha",
        "addresses": [
            {
                "street": "10 Green Avenue",
                "city": "Pune",
                "postal_code": "411001",
            },
            {
                "street": "22 Hill View",
                "city": "Ahmedabad",
                "postal_code": "380001",
            },
        ],
    }

    user = UserWithAddresses(**user_data)

    print("\nLIST OF NESTED MODELS")
    print("-" * 50)

    print(user)

    for address in user.addresses:
        print(f"{address.city}: {address.postal_code}")

    print("Model dump:", user.model_dump())


# =================================================
# 7. Optional Nested Model
# =================================================

class UserProfile(BaseModel):
    """
    A user profile may or may not have an address.
    """

    id: int
    name: str
    address: Optional[Address] = None


def optional_nested_model_example() -> None:
    """
    Demonstrate optional nested model.
    """

    profile_without_address = UserProfile(
        id=5,
        name="Kiran",
    )

    profile_with_address = UserProfile(
        id=6,
        name="Meera",
        address={
            "street": "89 River Road",
            "city": "Jaipur",
            "postal_code": "302001",
        },
    )

    print("\nOPTIONAL NESTED MODEL")
    print("-" * 50)

    print("Without address:", profile_without_address)
    print("With address:", profile_with_address)
    print(
        "Address type:",
        type(profile_with_address.address),
    )


# =================================================
# 8. More Realistic Order Example
# =================================================

class Product(BaseModel):
    """
    Product model used inside an order.
    """

    id: int
    name: str
    price: float


class Order(BaseModel):
    """
    Order model containing user and product details.
    """

    order_id: int
    customer: User
    products: List[Product]


def order_nested_model_example() -> None:
    """
    Demonstrate deeper nesting.

    Order contains:
    - customer, which is a User model
    - products, which is a list of Product models
    """

    order_data = {
        "order_id": 1001,
        "customer": {
            "id": 7,
            "name": "Sanjay",
            "address": {
                "street": "11 Market Road",
                "city": "Hyderabad",
                "postal_code": "500001",
            },
        },
        "products": [
            {
                "id": 101,
                "name": "Laptop",
                "price": 75000,
            },
            {
                "id": 102,
                "name": "Mouse",
                "price": 799,
            },
        ],
    }

    order = Order(**order_data)

    print("\nORDER NESTED MODEL")
    print("-" * 50)

    print(order)
    print("Customer city:", order.customer.address.city)

    for product in order.products:
        print(f"{product.name}: ₹{product.price}")

    print("Model dump:", order.model_dump())


# =================================================
# 9. Main Program
# =================================================

def main() -> None:
    """
    Run all nested model examples.
    """

    print("Pydantic Nested Models")
    print("=" * 50)

    separate_address_example()
    nested_dictionary_example()
    invalid_nested_data_example()
    list_of_nested_models_example()
    optional_nested_model_example()
    order_nested_model_example()


if __name__ == "__main__":
    main()


# =================================================
# Setup Commands
# =================================================

# Create a virtual environment:
#
# python -m venv venv
#
#
# Activate on macOS/Linux:
#
# source venv/bin/activate
#
#
# Activate on Windows:
#
# venv\Scripts\activate
#
#
# Install Pydantic:
#
# pip install pydantic
#
#
# Run this file:
#
# python pydantic_nested_models.py
#
#
# =================================================
# Notes
# =================================================

# Nested model:
# One Pydantic model used inside another Pydantic
# model.
#
#
# Example:
#
# class User(BaseModel):
#     address: Address
#
#
# Model composition:
# Building larger models by combining smaller models.
#
#
# Nested dictionary:
# Pydantic can convert a nested dictionary into the
# nested model automatically.
#
#
# Dictionary unpacking:
#
# user = User(**user_data)
#
#
# List of nested models:
#
# addresses: List[Address]
#
# Means:
# addresses must be a list, and each item must
# follow the Address model.
#
#
# Optional nested model:
#
# address: Optional[Address] = None
#
# Means:
# address can be an Address object or None.
#
#
# model_dump():
# Converts nested Pydantic models into nested
# dictionaries.
#
#
# Benefit:
# Nested models make complex data structures easier
# to validate, reuse, and understand.
