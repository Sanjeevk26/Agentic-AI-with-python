# Pydantic Field and Field-Level Validation
# Topics:
# 1. BaseModel
# 2. Field
# 3. Required fields using ...
# 4. min_length and max_length
# 5. ge, gt, le, lt
# 6. description and examples
# 7. pattern validation
# 8. Optional fields
# 9. ValidationError
# -------------------------------------------------

from typing import Dict, List, Optional

from pydantic import BaseModel, Field, ValidationError


# =================================================
# 1. Cart Model from Previous Example
# =================================================

class Cart(BaseModel):
    """
    A cart model using List and Dict field types.
    """

    user_id: int
    items: List[str]
    quantities: Dict[str, int]


def cart_example() -> None:
    """
    Create a Cart model from dictionary data.
    """

    cart_data = {
        "user_id": 123,
        "items": [
            "laptop",
            "mouse",
            "keyboard",
        ],
        "quantities": {
            "laptop": 1,
            "mouse": 2,
            "keyboard": 3,
        },
    }

    # ** unpacks the dictionary into keyword arguments.
    cart = Cart(**cart_data)

    print("\nCART EXAMPLE")
    print("-" * 50)

    print(cart)
    print("Cart as dictionary:", cart.model_dump())


# =================================================
# 2. Employee Model Using Field
# =================================================

class Employee(BaseModel):
    """
    Employee model using Pydantic Field.

    Field allows us to add validation rules and
    documentation metadata.
    """

    id: int

    name: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Employee name",
        examples=["Hitesh"],
    )

    department: Optional[str] = "General"

    salary: float = Field(
        ...,
        ge=10_000,
        le=100_000,
        description="Annual salary in INR",
        examples=[50_000],
    )


def valid_employee_example() -> None:
    """
    Create a valid Employee object.
    """

    employee = Employee(
        id=1,
        name="Ravi Kumar",
        salary=75_000,
    )

    print("\nVALID EMPLOYEE")
    print("-" * 50)

    print(employee)
    print("Department default:", employee.department)
    print("As dictionary:", employee.model_dump())


def invalid_employee_example() -> None:
    """
    Show validation errors for invalid employee data.
    """

    print("\nINVALID EMPLOYEE")
    print("-" * 50)

    try:
        Employee(
            id=2,
            name="Al",
            salary=5_000,
        )

    except ValidationError as error:
        print("Validation failed:")
        print(error)


# =================================================
# 3. User Contact Model with Pattern Validation
# =================================================

class UserContact(BaseModel):
    """
    User contact model using pattern validation.

    In Pydantic v2, use pattern= instead of regex=.
    """

    email: str = Field(
        ...,
        pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$",
        description="User email address",
        examples=["user@example.com"],
    )

    phone: str = Field(
        ...,
        pattern=r"^\+?[0-9]{10,15}$",
        description="Phone number with optional country code",
        examples=["+919876543210"],
    )


def valid_contact_example() -> None:
    """
    Create a valid UserContact object.
    """

    contact = UserContact(
        email="chai@example.com",
        phone="+919876543210",
    )

    print("\nVALID CONTACT")
    print("-" * 50)

    print(contact)


def invalid_contact_example() -> None:
    """
    Show validation errors for invalid email and phone.
    """

    print("\nINVALID CONTACT")
    print("-" * 50)

    try:
        UserContact(
            email="not-an-email",
            phone="phone-123",
        )

    except ValidationError as error:
        print("Validation failed:")
        print(error)


# =================================================
# 4. Validation Model for Age and Discount
# =================================================

class Offer(BaseModel):
    """
    Model showing common numeric validations.
    """

    age: int = Field(
        ...,
        ge=0,
        le=150,
        description="Age in years",
    )

    discount: float = Field(
        ...,
        ge=0,
        le=100,
        description="Discount percentage",
    )


def valid_offer_example() -> None:
    """
    Create a valid Offer object.
    """

    offer = Offer(
        age=30,
        discount=25.5,
    )

    print("\nVALID OFFER")
    print("-" * 50)

    print(offer)


def invalid_offer_example() -> None:
    """
    Show validation errors for invalid numeric values.
    """

    print("\nINVALID OFFER")
    print("-" * 50)

    try:
        Offer(
            age=180,
            discount=150,
        )

    except ValidationError as error:
        print("Validation failed:")
        print(error)


# =================================================
# 5. Greater Than and Less Than Example
# =================================================

class TemperatureReading(BaseModel):
    """
    Model using gt and lt.

    gt means greater than.
    lt means less than.
    """

    temperature_celsius: float = Field(
        ...,
        gt=-273.15,
        lt=1000,
        description="Temperature in Celsius",
    )


def temperature_example() -> None:
    """
    Demonstrate gt and lt validation.
    """

    print("\nTEMPERATURE VALIDATION")
    print("-" * 50)

    valid_reading = TemperatureReading(
        temperature_celsius=36.6,
    )

    print("Valid reading:", valid_reading)

    try:
        TemperatureReading(
            temperature_celsius=-273.15,
        )

    except ValidationError as error:
        print("Invalid reading:")
        print(error)


# =================================================
# 6. Model Schema Example
# =================================================

def schema_example() -> None:
    """
    Show model schema.

    Descriptions and examples are useful when
    generating API documentation.
    """

    print("\nEMPLOYEE JSON SCHEMA")
    print("-" * 50)

    schema = Employee.model_json_schema()

    print(schema)


# =================================================
# 7. Main Program
# =================================================

def main() -> None:
    """
    Run all Pydantic Field examples.
    """

    print("Pydantic Field Validation")
    print("=" * 50)

    cart_example()
    valid_employee_example()
    invalid_employee_example()
    valid_contact_example()
    invalid_contact_example()
    valid_offer_example()
    invalid_offer_example()
    temperature_example()
    schema_example()


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
# python pydantic_field_validation.py
#
#
# =================================================
# Notes
# =================================================

# Field:
#
# from pydantic import Field
#
#
# Required field:
#
# name: str = Field(...)
#
#
# String constraints:
#
# min_length=3
# max_length=50
#
#
# Numeric constraints:
#
# ge = greater than or equal to
# gt = greater than
# le = less than or equal to
# lt = less than
#
#
# Documentation metadata:
#
# description="Employee name"
# examples=["Hitesh"]
#
#
# Pattern validation:
#
# pattern=r"^[\w\.-]+@[\w\.-]+\.\w+$"
#
#
# Pydantic v2 note:
# Use pattern= instead of regex=.
#
#
# Optional field:
#
# department: Optional[str] = "General"
#
#
# Dictionary unpacking:
#
# cart = Cart(**cart_data)
#
#
# ValidationError:
# Raised when input data does not satisfy the model
# type rules or Field constraints.
