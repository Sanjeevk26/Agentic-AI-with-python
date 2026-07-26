# Pydantic Computed Fields
# Topics:
# 1. computed_field
# 2. property
# 3. Derived values
# 4. model_dump()
# 5. Field validation with computed fields
# -------------------------------------------------

from pydantic import (
    BaseModel,
    Field,
    ValidationError,
    computed_field,
)


# =================================================
# 1. Basic Product Model
# =================================================

class Product(BaseModel):
    """
    Product model with a computed total price.

    total_price is not provided by the user.
    It is calculated from price and quantity.
    """

    price: float
    quantity: int

    @computed_field
    @property
    def total_price(self) -> float:
        """
        Calculate total product price.
        """

        return self.price * self.quantity


def product_example() -> None:
    """
    Demonstrate a basic computed field.
    """

    product = Product(
        price=100,
        quantity=3,
    )

    print("\nPRODUCT EXAMPLE")
    print("-" * 50)

    print("Price:", product.price)
    print("Quantity:", product.quantity)

    # Access computed field like an attribute.
    print("Total price:", product.total_price)

    # Computed field appears in model_dump().
    print("Model dump:", product.model_dump())


# =================================================
# 2. Booking Model
# =================================================

class Booking(BaseModel):
    """
    Hotel booking model.

    total_amount is calculated from:
    nights * rate_per_night
    """

    user_id: int
    room_id: int

    nights: int = Field(
        ...,
        ge=1,
        description="Number of nights must be at least 1",
    )

    rate_per_night: float = Field(
        ...,
        ge=0,
        description="Room rate per night in INR",
    )

    @computed_field
    @property
    def total_amount(self) -> float:
        """
        Calculate total booking amount.
        """

        return self.nights * self.rate_per_night


def booking_example() -> None:
    """
    Demonstrate computed total amount for booking.
    """

    booking = Booking(
        user_id=123,
        room_id=456,
        nights=3,
        rate_per_night=2500,
    )

    print("\nBOOKING EXAMPLE")
    print("-" * 50)

    print("Booking:", booking)
    print("Total amount:", booking.total_amount)
    print("Model dump:", booking.model_dump())


def invalid_booking_example() -> None:
    """
    Show validation error with Field and computed field.
    """

    print("\nINVALID BOOKING EXAMPLE")
    print("-" * 50)

    try:
        Booking(
            user_id=123,
            room_id=456,
            nights=0,
            rate_per_night=2500,
        )

    except ValidationError as error:
        print("Validation failed:")
        print(error)


# =================================================
# 3. Discounted Product Model
# =================================================

class DiscountedProduct(BaseModel):
    """
    Product model with discount calculation.
    """

    name: str

    price: float = Field(
        ...,
        ge=0,
        description="Original product price in INR",
    )

    discount_percent: float = Field(
        0,
        ge=0,
        le=100,
        description="Discount percentage from 0 to 100",
    )

    @computed_field
    @property
    def discount_amount(self) -> float:
        """
        Calculate discount amount.
        """

        return self.price * self.discount_percent / 100

    @computed_field
    @property
    def final_price(self) -> float:
        """
        Calculate final price after discount.
        """

        return self.price - self.discount_amount


def discounted_product_example() -> None:
    """
    Demonstrate multiple computed fields.
    """

    product = DiscountedProduct(
        name="Masala Chai Pack",
        price=1000,
        discount_percent=10,
    )

    print("\nDISCOUNTED PRODUCT EXAMPLE")
    print("-" * 50)

    print("Product:", product.name)
    print("Original price:", product.price)
    print("Discount percent:", product.discount_percent)
    print("Discount amount:", product.discount_amount)
    print("Final price:", product.final_price)
    print("Model dump:", product.model_dump())


# =================================================
# 4. Invoice Line Model
# =================================================

class InvoiceLine(BaseModel):
    """
    Invoice line item with computed line total.
    """

    item_name: str
    unit_price: float = Field(..., ge=0)
    quantity: int = Field(..., ge=1)

    @computed_field
    @property
    def line_total(self) -> float:
        """
        Calculate total amount for this invoice line.
        """

        return self.unit_price * self.quantity


def invoice_line_example() -> None:
    """
    Demonstrate invoice line total calculation.
    """

    line = InvoiceLine(
        item_name="Keyboard",
        unit_price=1500,
        quantity=2,
    )

    print("\nINVOICE LINE EXAMPLE")
    print("-" * 50)

    print(line)
    print("Line total:", line.line_total)
    print("Model dump:", line.model_dump())


# =================================================
# 5. Full Name Computed Field
# =================================================

class Customer(BaseModel):
    """
    Customer model with computed full name.
    """

    first_name: str
    last_name: str

    @computed_field
    @property
    def full_name(self) -> str:
        """
        Combine first name and last name.
        """

        return f"{self.first_name} {self.last_name}"


def customer_example() -> None:
    """
    Demonstrate string-based computed field.
    """

    customer = Customer(
        first_name="Amit",
        last_name="Sharma",
    )

    print("\nCUSTOMER EXAMPLE")
    print("-" * 50)

    print("Full name:", customer.full_name)
    print("Model dump:", customer.model_dump())


# =================================================
# 6. Main Program
# =================================================

def main() -> None:
    """
    Run all computed field examples.
    """

    print("Pydantic Computed Fields")
    print("=" * 50)

    product_example()
    booking_example()
    invalid_booking_example()
    discounted_product_example()
    invoice_line_example()
    customer_example()


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
# python pydantic_computed_fields.py
#
#
# =================================================
# Notes
# =================================================

# computed_field:
#
# from pydantic import computed_field
#
#
# Basic syntax:
#
# @computed_field
# @property
# def total_price(self) -> float:
#     return self.price * self.quantity
#
#
# @property:
# Makes the method accessible like an attribute.
#
# Correct:
#
# product.total_price
#
# Incorrect:
#
# product.total_price()
#
#
# model_dump():
# Computed fields are included in model_dump().
#
#
# Example:
#
# product.model_dump()
#
# Output includes:
# - price
# - quantity
# - total_price
#
#
# Good computed field use cases:
# - total price
# - total booking amount
# - discount amount
# - final price
# - full name
# - invoice line total
#
#
# Avoid computed fields for:
# - database writes
# - payment calls
# - email sending
# - long-running business workflows
#
#
# Computed fields are best for simple derived values.
