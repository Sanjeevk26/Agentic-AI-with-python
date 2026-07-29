# Pydantic Advanced Nested Models
# Topics:
# 1. Optional nested models
# 2. Mixed data types with Union
# 3. List of mixed nested models
# 4. Deeply nested structures
# 5. ValidationError
# 6. Field(default_factory=list)
# -------------------------------------------------

from typing import List, Optional, Union

from pydantic import BaseModel, Field, ValidationError


# =================================================
# 1. Basic Address Model
# =================================================

class Address(BaseModel):
    """
    A simple address model.

    This will be used as an optional nested model
    inside Company.
    """

    street: str
    city: str
    postal_code: str


# =================================================
# 2. Optional Nested Model: Company
# =================================================

class Company(BaseModel):
    """
    A company may or may not have an address.

    Some companies are remote-first and may not
    have a physical office address.
    """

    name: str
    address: Optional[Address] = None


# =================================================
# 3. Optional Nested Model: Employee
# =================================================

class Employee(BaseModel):
    """
    An employee may or may not belong to a company.

    This can represent employees, contractors,
    or freelancers.
    """

    name: str
    company: Optional[Company] = None


def optional_nested_model_examples() -> None:
    """
    Demonstrate optional nested models.
    """

    print("\nOPTIONAL NESTED MODELS")
    print("-" * 50)

    remote_company = Company(
        name="Remote Chai Startup",
    )

    office_company = Company(
        name="Chai Office",
        address={
            "street": "123 Market Road",
            "city": "Ahmedabad",
            "postal_code": "380001",
        },
    )

    freelancer = Employee(
        name="Freelancer Ravi",
    )

    employee = Employee(
        name="Anita",
        company={
            "name": "Chai Office",
            "address": {
                "street": "123 Market Road",
                "city": "Ahmedabad",
                "postal_code": "380001",
            },
        },
    )

    print("Remote company:", remote_company)
    print("Office company:", office_company)
    print("Freelancer:", freelancer)
    print("Employee:", employee)

    if employee.company and employee.company.address:
        print(
            "Employee company city:",
            employee.company.address.city,
        )


# =================================================
# 4. Mixed Data Types: Text and Image Content
# =================================================

class TextContent(BaseModel):
    """
    Text section for an article.
    """

    type: str = "text"
    content: str


class ImageContent(BaseModel):
    """
    Image section for an article.
    """

    type: str = "image"
    url: str
    alt_text: str


class Article(BaseModel):
    """
    Article contains mixed section types.

    Each section can be TextContent or ImageContent.
    """

    title: str
    sections: List[Union[TextContent, ImageContent]]


def mixed_data_type_example() -> None:
    """
    Demonstrate List[Union[TextContent, ImageContent]].
    """

    print("\nMIXED DATA TYPES WITH UNION")
    print("-" * 50)

    article = Article(
        title="Learning Pydantic",
        sections=[
            {
                "type": "text",
                "content": "Pydantic helps validate structured data.",
            },
            {
                "type": "image",
                "url": "https://example.com/pydantic.png",
                "alt_text": "Pydantic logo",
            },
            TextContent(
                content="This is another text section.",
            ),
        ],
    )

    print(article)

    for section in article.sections:
        print("Section type:", type(section))
        print(section)

    print("Model dump:", article.model_dump())


def invalid_mixed_data_type_example() -> None:
    """
    Show validation error for invalid mixed content.
    """

    print("\nINVALID MIXED DATA TYPE")
    print("-" * 50)

    try:
        Article(
            title="Invalid Article",
            sections=[
                {
                    "type": "image",
                    "url": "https://example.com/image.png",
                    # alt_text is missing
                }
            ],
        )

    except ValidationError as error:
        print("Validation failed:")
        print(error)


# =================================================
# 5. Deeply Nested Structure
# =================================================

class Country(BaseModel):
    """
    Country model.
    """

    name: str
    code: str


class State(BaseModel):
    """
    State model.

    A state belongs to a country.
    """

    name: str
    country: Country


class City(BaseModel):
    """
    City model.

    A city belongs to a state.
    """

    name: str
    state: State


class DetailedAddress(BaseModel):
    """
    Detailed address model.

    Address contains city.
    City contains state.
    State contains country.
    """

    street: str
    city: City
    postal_code: str


class Organization(BaseModel):
    """
    Organization model with deeply nested data.

    headquarters is one DetailedAddress.
    branches is a list of DetailedAddress objects.
    """

    name: str
    headquarters: DetailedAddress
    branches: List[DetailedAddress] = Field(
        default_factory=list,
    )


def deeply_nested_structure_example() -> None:
    """
    Demonstrate deeply nested Pydantic models.
    """

    print("\nDEEPLY NESTED STRUCTURE")
    print("-" * 50)

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
            },
            {
                "street": "88 Tech Park",
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
        ],
    )

    print(organization)

    print(
        "Headquarters city:",
        organization.headquarters.city.name,
    )

    print(
        "Headquarters country:",
        organization.headquarters.city.state.country.name,
    )

    print("Branches:")
    for branch in organization.branches:
        print(
            f"- {branch.city.name}, "
            f"{branch.city.state.name}, "
            f"{branch.city.state.country.name}"
        )

    print("Model dump:")
    print(organization.model_dump())


def invalid_deeply_nested_structure_example() -> None:
    """
    Show validation error in deeply nested data.
    """

    print("\nINVALID DEEPLY NESTED STRUCTURE")
    print("-" * 50)

    try:
        Organization(
            name="Broken Organization",
            headquarters={
                "street": "123 Business Road",
                "city": {
                    "name": "Ahmedabad",
                    "state": {
                        "name": "Gujarat",
                        "country": {
                            "name": "India",
                            # code is missing
                        },
                    },
                },
                "postal_code": "380001",
            },
        )

    except ValidationError as error:
        print("Validation failed:")
        print(error)


# =================================================
# 6. Modern Union Syntax Example
# =================================================

class ModernArticle(BaseModel):
    """
    Same mixed-type idea using modern Python syntax.

    This requires Python 3.10+.
    """

    title: str
    sections: list[TextContent | ImageContent]


def modern_union_syntax_example() -> None:
    """
    Demonstrate modern union syntax.
    """

    print("\nMODERN UNION SYNTAX")
    print("-" * 50)

    article = ModernArticle(
        title="Modern Python Syntax",
        sections=[
            TextContent(
                content="This uses TextContent | ImageContent.",
            ),
            ImageContent(
                url="https://example.com/modern.png",
                alt_text="Modern syntax example",
            ),
        ],
    )

    print(article)
    print("Model dump:", article.model_dump())


# =================================================
# 7. Main Program
# =================================================

def main() -> None:
    """
    Run all advanced nested model examples.
    """

    print("Pydantic Advanced Nested Models")
    print("=" * 50)

    optional_nested_model_examples()
    mixed_data_type_example()
    invalid_mixed_data_type_example()
    deeply_nested_structure_example()
    invalid_deeply_nested_structure_example()
    modern_union_syntax_example()


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
# python pydantic_advanced_nested_models.py
#
#
# =================================================
# Notes
# =================================================

# Optional nested model:
#
# address: Optional[Address] = None
#
# Means address can be Address or None.
#
#
# Union:
#
# Union[TextContent, ImageContent]
#
# Means the value can be either TextContent or
# ImageContent.
#
#
# List of mixed types:
#
# List[Union[TextContent, ImageContent]]
#
# Means a list where each item can be one of the
# allowed model types.
#
#
# Deeply nested model:
#
# Organization
#   -> DetailedAddress
#       -> City
#           -> State
#               -> Country
#
#
# Field(default_factory=list):
# Use this for default empty lists.
#
#
# Avoid:
#
# branches: List[DetailedAddress] = []
#
#
# Prefer:
#
# branches: List[DetailedAddress] = Field(
#     default_factory=list,
# )
#
#
# Pydantic validates nested structures at all levels.
