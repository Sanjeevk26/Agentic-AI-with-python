# Pydantic Product Model
# Topics:
# 1. BaseModel
# 2. Product model
# 3. Type annotations
# 4. Default values
# 5. Required fields
# 6. Automatic type conversion
# 7. ValidationError
# -------------------------------------------------

from pydantic import BaseModel, ValidationError


# =================================================
# 1. Product Model
# =================================================

class Product(BaseModel):
    """
    A Pydantic model that represents product data.

    Each field has a type annotation.
    Pydantic uses these annotations to validate data.
    """

    id: int
    name: str
    price: float
    in_stock: bool = True


# =================================================
# 2. Valid Product Example
# =================================================

def valid_product_example() -> None:
    """
    Create a product with all fields provided.
    """

    product_one = Product(
        id=1,
        name="Laptop",
        price=999.99,
        in_stock=True,
    )

    print("\nVALID PRODUCT")
    print("-" * 50)

    print(product_one)
    print("Product ID:", product_one.id)
    print("Product name:", product_one.name)
    print("Product price:", product_one.price)
    print("In stock:", product_one.in_stock)


# =================================================
# 3. Product with Default Value
# =================================================

def default_value_example() -> None:
    """
    Create a product without passing in_stock.

    Since in_stock has a default value of True,
    Pydantic will use that value automatically.
    """

    product_two = Product(
        id=2,
        name="Mouse",
        price=24.33,
    )

    print("\nPRODUCT WITH DEFAULT VALUE")
    print("-" * 50)

    print(product_two)
    print("In stock default value:", product_two.in_stock)


# =================================================
# 4. Missing Required Fields
# =================================================

def missing_required_fields_example() -> None:
    """
    Show what happens when required fields are missing.
    """

    print("\nMISSING REQUIRED FIELDS")
    print("-" * 50)

    try:
        Product(
            name="Keyboard",
        )

    except ValidationError as error:
        print("Validation failed:")
        print(error)


# =================================================
# 5. Automatic Type Conversion
# =================================================

def automatic_conversion_example() -> None:
    """
    Pydantic tries to convert compatible values.

    id is passed as a string but can be converted
    into an integer.

    price is passed as a string but can be converted
    into a float.

    in_stock is passed as a string but can be
    interpreted as a boolean.
    """

    product = Product(
        id="123",
        name="Monitor",
        price="499.99",
        in_stock="true",
    )

    print("\nAUTOMATIC TYPE CONVERSION")
    print("-" * 50)

    print(product)
    print("id value:", product.id)
    print("id type:", type(product.id))

    print("price value:", product.price)
    print("price type:", type(product.price))

    print("in_stock value:", product.in_stock)
    print("in_stock type:", type(product.in_stock))


# =================================================
# 6. Conversion Failure
# =================================================

def conversion_failure_example() -> None:
    """
    Show what happens when Pydantic cannot convert
    the provided values.
    """

    print("\nCONVERSION FAILURE")
    print("-" * 50)

    try:
        Product(
            id="abc",
            name="Keyboard",
            price="free",
        )

    except ValidationError as error:
        print("Validation failed:")
        print(error)


# =================================================
# 7. Model Dump Example
# =================================================

def model_dump_example() -> None:
    """
    Convert a Pydantic model object into a dictionary.
    """

    product = Product(
        id=3,
        name="USB Cable",
        price=9.99,
    )

    print("\nMODEL DUMP")
    print("-" * 50)

    print("Model object:")
    print(product)

    print("Dictionary:")
    print(product.model_dump())


# =================================================
# 8. Main Program
# =================================================

def main() -> None:
    """
    Run all Pydantic product model examples.
    """

    print("Pydantic Product Model")
    print("=" * 50)

    valid_product_example()
    default_value_example()
    missing_required_fields_example()
    automatic_conversion_example()
    conversion_failure_example()
    model_dump_example()


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
# python pydantic_product_model.py
#
#
# =================================================
# Notes
# =================================================

# Pydantic:
# Used for data validation and parsing.
#
#
# BaseModel:
# Parent class used for creating Pydantic models.
#
#
# Product model:
#
# class Product(BaseModel):
#     id: int
#     name: str
#     price: float
#     in_stock: bool = True
#
#
# Required fields:
# Fields without default values must be provided.
#
#
# Optional through default:
# A field with a default value does not need to be
# passed during object creation.
#
#
# Example:
#
# in_stock: bool = True
#
#
# Automatic conversion:
# Pydantic may convert compatible values.
#
# "123" can become 123
# "499.99" can become 499.99
# "true" can become True
#
#
# ValidationError:
# Raised when required fields are missing or values
# cannot be converted to the expected type.
#
#
# Best practices:
# - Always use type annotations.
# - Use appropriate field types.
# - Use sensible default values.
# - Do not rely too much on automatic conversion.
