# Pydantic Field Validator and Model Validator
# Topics:
# 1. field_validator
# 2. model_validator
# 3. Custom field validation
# 4. Full model validation
# 5. ValidationError
# -------------------------------------------------

from pydantic import (
    BaseModel,
    ValidationError,
    field_validator,
    model_validator,
)


# =================================================
# 1. Field Validator Example
# =================================================

class User(BaseModel):
    """
    A simple user model.

    username is validated using a custom
    field_validator.
    """

    username: str

    @field_validator("username")
    @classmethod
    def username_length(cls, value: str) -> str:
        """
        Validate the username field.

        The username must have at least 4 characters.
        """

        value = value.strip()

        if len(value) < 4:
            raise ValueError(
                "Username must be at least 4 characters"
            )

        return value


def valid_user_example() -> None:
    """
    Create a valid User object.
    """

    user = User(
        username="hitesh",
    )

    print("\nVALID USER")
    print("-" * 50)

    print(user)
    print("Username:", user.username)


def invalid_user_example() -> None:
    """
    Show field validation failure.
    """

    print("\nINVALID USER")
    print("-" * 50)

    try:
        User(
            username="abc",
        )

    except ValidationError as error:
        print("Validation failed:")
        print(error)


# =================================================
# 2. Another Field Validator Example
# =================================================

class ProductCode(BaseModel):
    """
    Product code must start with CHAI-.
    """

    code: str

    @field_validator("code")
    @classmethod
    def code_must_start_with_chai(cls, value: str) -> str:
        """
        Validate product code format.
        """

        value = value.strip().upper()

        if not value.startswith("CHAI-"):
            raise ValueError(
                "Product code must start with CHAI-"
            )

        return value


def product_code_example() -> None:
    """
    Demonstrate custom field validation.
    """

    print("\nPRODUCT CODE VALIDATION")
    print("-" * 50)

    valid_code = ProductCode(
        code="chai-101",
    )

    print("Valid product code:", valid_code)

    try:
        ProductCode(
            code="coffee-101",
        )

    except ValidationError as error:
        print("Invalid product code:")
        print(error)


# =================================================
# 3. Model Validator Example
# =================================================

class SignupData(BaseModel):
    """
    Signup data model.

    password and confirm_password must match.
    """

    password: str
    confirm_password: str

    @model_validator(mode="after")
    def passwords_match(self) -> "SignupData":
        """
        Validate the whole model after field
        validation is complete.
        """

        if self.password != self.confirm_password:
            raise ValueError(
                "Passwords do not match"
            )

        return self


def valid_signup_example() -> None:
    """
    Create valid signup data.
    """

    signup = SignupData(
        password="secret123",
        confirm_password="secret123",
    )

    print("\nVALID SIGNUP")
    print("-" * 50)

    print(signup)


def invalid_signup_example() -> None:
    """
    Show model validation failure.
    """

    print("\nINVALID SIGNUP")
    print("-" * 50)

    try:
        SignupData(
            password="secret123",
            confirm_password="different123",
        )

    except ValidationError as error:
        print("Validation failed:")
        print(error)


# =================================================
# 4. Model Validator with Price Rules
# =================================================

class ProductOffer(BaseModel):
    """
    Product offer model.

    sale_price must be less than or equal to
    original_price.
    """

    product_name: str
    original_price: float
    sale_price: float

    @model_validator(mode="after")
    def sale_price_must_be_valid(self) -> "ProductOffer":
        """
        Validate price relationship.
        """

        if self.sale_price > self.original_price:
            raise ValueError(
                "Sale price cannot be greater than original price"
            )

        return self


def product_offer_example() -> None:
    """
    Demonstrate model-level validation with prices.
    """

    print("\nPRODUCT OFFER VALIDATION")
    print("-" * 50)

    valid_offer = ProductOffer(
        product_name="Masala Chai Pack",
        original_price=500,
        sale_price=399,
    )

    print("Valid offer:", valid_offer)

    try:
        ProductOffer(
            product_name="Ginger Chai Pack",
            original_price=300,
            sale_price=450,
        )

    except ValidationError as error:
        print("Invalid offer:")
        print(error)


# =================================================
# 5. Model Validator with Conditional Rule
# =================================================

class PaymentData(BaseModel):
    """
    Payment model.

    If payment_method is card, card_number must be
    provided.
    """

    payment_method: str
    card_number: str | None = None

    @field_validator("payment_method")
    @classmethod
    def normalize_payment_method(cls, value: str) -> str:
        """
        Normalize payment method to lowercase.
        """

        value = value.strip().lower()

        allowed_methods = {
            "cash",
            "upi",
            "card",
        }

        if value not in allowed_methods:
            raise ValueError(
                "Payment method must be cash, upi, or card"
            )

        return value

    @model_validator(mode="after")
    def card_number_required_for_card(self) -> "PaymentData":
        """
        Validate dependency between fields.
        """

        if self.payment_method == "card" and not self.card_number:
            raise ValueError(
                "card_number is required when payment_method is card"
            )

        return self


def payment_data_example() -> None:
    """
    Demonstrate field and model validators together.
    """

    print("\nPAYMENT DATA VALIDATION")
    print("-" * 50)

    valid_payment = PaymentData(
        payment_method="UPI",
    )

    print("Valid payment:", valid_payment)

    try:
        PaymentData(
            payment_method="card",
        )

    except ValidationError as error:
        print("Invalid payment:")
        print(error)


# =================================================
# 6. Main Program
# =================================================

def main() -> None:
    """
    Run all validator examples.
    """

    print("Pydantic Field and Model Validators")
    print("=" * 50)

    valid_user_example()
    invalid_user_example()
    product_code_example()
    valid_signup_example()
    invalid_signup_example()
    product_offer_example()
    payment_data_example()


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
# python pydantic_field_and_model_validators.py
#
#
# =================================================
# Notes
# =================================================

# field_validator:
# Validates one specific field.
#
#
# Example:
#
# @field_validator("username")
# @classmethod
# def username_length(cls, value):
#     ...
#     return value
#
#
# model_validator:
# Validates the whole model.
#
#
# Example:
#
# @model_validator(mode="after")
# def passwords_match(self):
#     ...
#     return self
#
#
# mode="after":
# Runs after individual fields have already been
# validated.
#
#
# ValueError:
# Raise ValueError when validation fails.
#
#
# ValidationError:
# Pydantic collects validation problems and raises
# ValidationError.
#
#
# Important:
# Always return the validated value from a
# field_validator.
#
#
# Important:
# Always return self from a Pydantic v2
# model_validator(mode="after").
#
#
# Use field_validator when:
# - One field needs custom validation.
#
#
# Use model_validator when:
# - Multiple fields must be checked together.
