# Pydantic Basics
# Topics:
# 1. Installing Pydantic
# 2. BaseModel
# 3. Type annotations
# 4. Dictionary unpacking with **
# 5. Automatic validation
# 6. Type conversion
# 7. ValidationError
# 8. Strict types
# -------------------------------------------------

from pydantic import (
    BaseModel,
    StrictBool,
    StrictInt,
    ValidationError,
)


# =================================================
# 1. Basic Pydantic Model
# =================================================

class User(BaseModel):
    """
    A Pydantic model defines the expected shape
    and type of data.
    """

    id: int
    name: str
    is_active: bool


# =================================================
# 2. Valid Input Data
# =================================================

def valid_user_example() -> None:
    """
    Create a valid User object.
    """

    input_data = {
        "id": 101,
        "name": "Chai Code",
        "is_active": True,
    }

    # ** unpacks the dictionary.
    user = User(**input_data)

    print("\nVALID USER")
    print("-" * 50)

    print(user)
    print("User ID:", user.id)
    print("User name:", user.name)
    print("Is active:", user.is_active)

    print("As dictionary:", user.model_dump())


# =================================================
# 3. Why Dictionary Unpacking Is Needed
# =================================================

def dictionary_unpacking_example() -> None:
    """
    Demonstrate what **input_data means.
    """

    input_data = {
        "id": 102,
        "name": "Masala Chai",
        "is_active": True,
    }

    user_one = User(**input_data)

    user_two = User(
        id=102,
        name="Masala Chai",
        is_active=True,
    )

    print("\nDICTIONARY UNPACKING")
    print("-" * 50)

    print("Using **input_data:", user_one)
    print("Using named arguments:", user_two)

    # This is intentionally shown as a comment
    # because it is incorrect:
    #
    # user = User(input_data)
    #
    # That passes the whole dictionary as one
    # positional argument instead of unpacking it.


# =================================================
# 4. Validation Error Example
# =================================================

def invalid_boolean_example() -> None:
    """
    Demonstrate validation failure.
    """

    bad_data = {
        "id": 103,
        "name": "Ginger Chai",
        "is_active": 25,
    }

    print("\nINVALID BOOLEAN EXAMPLE")
    print("-" * 50)

    try:
        User(**bad_data)

    except ValidationError as error:
        print("Validation failed:")
        print(error)


# =================================================
# 5. Pydantic Type Conversion
# =================================================

def type_conversion_example() -> None:
    """
    Pydantic may convert compatible values.

    Here, the string '101' can be converted into
    an integer.
    """

    input_data = {
        "id": "101",
        "name": "Elaichi Chai",
        "is_active": True,
    }

    user = User(**input_data)

    print("\nTYPE CONVERSION")
    print("-" * 50)

    print(user)
    print("user.id:", user.id)
    print("type(user.id):", type(user.id))


# =================================================
# 6. Conversion Failure Example
# =================================================

def conversion_failure_example() -> None:
    """
    Pydantic cannot convert every value.

    The string '101A' cannot be converted into
    an integer.
    """

    bad_data = {
        "id": "101A",
        "name": "Lemon Chai",
        "is_active": True,
    }

    print("\nCONVERSION FAILURE")
    print("-" * 50)

    try:
        User(**bad_data)

    except ValidationError as error:
        print("Validation failed:")
        print(error)


# =================================================
# 7. Strict Pydantic Model
# =================================================

class StrictUser(BaseModel):
    """
    Strict types prevent automatic conversion.

    StrictInt means the value must already be an int.
    StrictBool means the value must already be a bool.
    """

    id: StrictInt
    name: str
    is_active: StrictBool


def strict_validation_example() -> None:
    """
    Demonstrate strict validation.
    """

    input_data = {
        "id": "101",
        "name": "Strict Chai User",
        "is_active": True,
    }

    print("\nSTRICT VALIDATION")
    print("-" * 50)

    try:
        StrictUser(**input_data)

    except ValidationError as error:
        print("Strict validation failed:")
        print(error)


# =================================================
# 8. Direct Model Creation
# =================================================

def direct_model_creation_example() -> None:
    """
    A model can also be created directly using
    named arguments.
    """

    user = User(
        id=104,
        name="Direct User",
        is_active=False,
    )

    print("\nDIRECT MODEL CREATION")
    print("-" * 50)

    print(user)


# =================================================
# 9. Main Program
# =================================================

def main() -> None:
    """
    Run all Pydantic basics examples.
    """

    print("Pydantic Basics: First Model")
    print("=" * 50)

    valid_user_example()
    dictionary_unpacking_example()
    invalid_boolean_example()
    type_conversion_example()
    conversion_failure_example()
    strict_validation_example()
    direct_model_creation_example()


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
# python pydantic_basics_first_model.py
#
#
# =================================================
# Notes
# =================================================

# Pydantic:
# A Python library for data validation, parsing,
# serialization, and settings management.
#
#
# BaseModel:
# Parent class used for most Pydantic models.
#
#
# Type annotations:
#
# id: int
# name: str
# is_active: bool
#
#
# Model creation:
#
# user = User(
#     id=101,
#     name="Chai Code",
#     is_active=True,
# )
#
#
# Dictionary unpacking:
#
# user = User(**input_data)
#
#
# Validation:
# Pydantic validates data when the model object
# is created.
#
#
# Type conversion:
# Pydantic may convert compatible values.
#
# Example:
# "101" can become 101.
#
#
# ValidationError:
# Raised when data cannot be validated.
#
#
# Strict types:
# Use StrictInt, StrictBool, etc. when automatic
# conversion should not be allowed.
