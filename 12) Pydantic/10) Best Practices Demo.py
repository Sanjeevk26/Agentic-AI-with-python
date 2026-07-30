# Pydantic Best Practices
# Topics:
# 1. Define leaf models first
# 2. Build models upward
# 3. Use clear naming
# 4. Optional nested models
# 5. Union types
# 6. Computed fields
# 7. Business rule validation
# 8. Performance-conscious design
# -------------------------------------------------

from typing import Literal

from pydantic import (
    BaseModel,
    Field,
    ValidationError,
    computed_field,
    model_validator,
)


# =================================================
# 1. Leaf Models First
# =================================================

class Country(BaseModel):
    """
    Leaf model.

    This model does not depend on other custom
    Pydantic models.
    """

    name: str
    code: str


class State(BaseModel):
    """
    State depends on Country.
    """

    name: str
    country: Country


class City(BaseModel):
    """
    City depends on State.
    """

    name: str
    state: State


class Address(BaseModel):
    """
    Address depends on City.
    """

    street: str
    city: City
    postal_code: str


# =================================================
# 2. Build Upward to Larger Models
# =================================================

class Organization(BaseModel):
    """
    Organization is built from smaller models.

    headquarters is required.
    branches defaults to an empty list.
    """

    name: str
    headquarters: Address
    branches: list[Address] = Field(
        default_factory=list,
    )


def organization_example() -> None:
    """
    Demonstrate building models upward.
    """

    organization = Organization(
        name="Chai Global",
        headquarters={
            "street": "123 Business Road",
            "city": {
                "name": "Ahmedabad",
                "state": {
                    "name": "Gujarat",
                    "country": {
                        "name": "India",
                        "code": "IN",
                    },
                },
            },
            "postal_code": "380001",
        },
        branches=[
            {
                "street": "22 Startup Street",
                "city": {
                    "name": "Bengaluru",
                    "state": {
                        "name": "Karnataka",
                        "country": {
                            "name": "India",
                            "code": "IN",
                        },
                    },
                },
                "postal_code": "560001",
            }
        ],
    )

    print("\nORGANIZATION EXAMPLE")
    print("-" * 50)

    print(organization)
    print("Headquarters city:", organization.headquarters.city.name)
    print("Branch count:", len(organization.branches))


# =================================================
# 3. Optional Nested Models
# =================================================

class Company(BaseModel):
    """
    Company may or may not have an address.

    This supports remote-first companies.
    """

    name: str
    address: Address | None = None


class Employee(BaseModel):
    """
    Employee may or may not belong to a company.

    This supports freelancers or contractors.
    """

    name: str
    company: Company | None = None


def optional_models_example() -> None:
    """
    Demonstrate optional nested models.
    """

    freelancer = Employee(
        name="Freelancer Ravi",
    )

    employee = Employee(
        name="Anita",
        company={
            "name": "Chai Office",
            "address": {
                "street": "12 Office Road",
                "city": {
                    "name": "Pune",
                    "state": {
                        "name": "Maharashtra",
                        "country": {
                            "name": "India",
                            "code": "IN",
                        },
                    },
                },
                "postal_code": "411001",
            },
        },
    )

    print("\nOPTIONAL MODELS EXAMPLE")
    print("-" * 50)

    print("Freelancer:", freelancer)
    print("Employee:", employee)


# =================================================
# 4. Union Types for Polymorphic Relationships
# =================================================

class TextSection(BaseModel):
    """
    Text content block.
    """

    type: Literal["text"] = "text"
    content: str


class ImageSection(BaseModel):
    """
    Image content block.
    """

    type: Literal["image"] = "image"
    url: str
    alt_text: str


class Article(BaseModel):
    """
    Article can contain multiple types of sections.

    Each section can be text or image.
    """

    title: str
    sections: list[TextSection | ImageSection]


def union_type_example() -> None:
    """
    Demonstrate union types.
    """

    article = Article(
        title="Learning Pydantic Best Practices",
        sections=[
            {
                "type": "text",
                "content": "Pydantic models should be clear.",
            },
            {
                "type": "image",
                "url": "https://example.com/model.png",
                "alt_text": "Pydantic model diagram",
            },
        ],
    )

    print("\nUNION TYPE EXAMPLE")
    print("-" * 50)

    print(article)

    for section in article.sections:
        print("Section:", section)


# =================================================
# 5. Computed Fields Should Stay Lightweight
# =================================================

class OrderItem(BaseModel):
    """
    Good computed field example.

    line_total is lightweight and derived from
    existing fields.
    """

    product_name: str
    unit_price: float = Field(..., ge=0)
    quantity: int = Field(..., ge=1)

    @computed_field
    @property
    def line_total(self) -> float:
        """
        Simple computed field.

        This is safe because it is a lightweight
        calculation.
        """

        return self.unit_price * self.quantity


def computed_field_example() -> None:
    """
    Demonstrate lightweight computed field usage.
    """

    item = OrderItem(
        product_name="Keyboard",
        unit_price=1500,
        quantity=2,
    )

    print("\nCOMPUTED FIELD EXAMPLE")
    print("-" * 50)

    print(item)
    print("Line total:", item.line_total)
    print("Model dump:", item.model_dump())


# =================================================
# 6. Business Rule Validation
# =================================================

class ProductOffer(BaseModel):
    """
    Business rule example.

    sale_price should not be greater than
    original_price.
    """

    product_name: str
    original_price: float = Field(..., ge=0)
    sale_price: float = Field(..., ge=0)

    @model_validator(mode="after")
    def validate_sale_price(self) -> "ProductOffer":
        """
        Validate business rule.
        """

        if self.sale_price > self.original_price:
            raise ValueError(
                "Sale price cannot be greater than original price"
            )

        return self


def business_rule_example() -> None:
    """
    Demonstrate business rule validation.
    """

    print("\nBUSINESS RULE VALIDATION")
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
# 7. Pagination-Friendly Models
# =================================================

class BranchSummary(BaseModel):
    """
    Summary model for large lists.

    Instead of returning a deeply nested full Address
    for every branch, a summary model can be used
    when only basic information is needed.
    """

    city_name: str
    state_name: str
    country_code: str


class OrganizationBranchResponse(BaseModel):
    """
    Example response model for paginated branch data.
    """

    organization_name: str
    page: int = Field(..., ge=1)
    page_size: int = Field(..., ge=1, le=100)
    total_branches: int = Field(..., ge=0)
    branches: list[BranchSummary]


def pagination_friendly_example() -> None:
    """
    Demonstrate a lighter response model for large
    nested lists.
    """

    response = OrganizationBranchResponse(
        organization_name="Chai Global",
        page=1,
        page_size=10,
        total_branches=2,
        branches=[
            {
                "city_name": "Ahmedabad",
                "state_name": "Gujarat",
                "country_code": "IN",
            },
            {
                "city_name": "Bengaluru",
                "state_name": "Karnataka",
                "country_code": "IN",
            },
        ],
    )

    print("\nPAGINATION-FRIENDLY MODEL")
    print("-" * 50)

    print(response)
    print("Model dump:", response.model_dump())


# =================================================
# 8. Main Program
# =================================================

def main() -> None:
    """
    Run all best-practice examples.
    """

    print("Pydantic Best Practices")
    print("=" * 50)

    organization_example()
    optional_models_example()
    union_type_example()
    computed_field_example()
    business_rule_example()
    pagination_friendly_example()


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
# python pydantic_best_practices.py
#
#
# =================================================
# Notes
# =================================================

# Best practice 1:
# Define leaf models first.
#
#
# Example:
# Country -> State -> City -> Address -> Organization
#
#
# Best practice 2:
# Build models upward gradually.
#
#
# Best practice 3:
# Use clear and meaningful names.
#
#
# Best practice 4:
# Group related models together.
#
#
# Best practice 5:
# Use Optional when a relationship may not exist.
#
#
# Example:
# company: Company | None = None
#
#
# Best practice 6:
# Use union types for polymorphic relationships.
#
#
# Example:
# sections: list[TextSection | ImageSection]
#
#
# Best practice 7:
# Validate business rules with validators.
#
#
# Example:
# Sale price should not exceed original price.
#
#
# Best practice 8:
# Keep computed fields lightweight.
#
#
# Good:
# line_total = unit_price * quantity
#
#
# Avoid:
# database calls, payment calls, API calls, or heavy
# calculations inside computed fields.
#
#
# Performance considerations:
# - Avoid unnecessary deep nesting.
# - Use pagination for large nested lists.
# - Be careful with circular references.
# - Be careful with recursive models.
# - Serialize only the data you need.
#
#
# Final reminder:
# Best practices are not fixed laws.
# Use what works for your application and team.
