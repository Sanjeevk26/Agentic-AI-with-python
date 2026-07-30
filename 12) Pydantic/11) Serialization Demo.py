# Pydantic Serialization
# Topics:
# 1. Serialization basics
# 2. model_dump()
# 3. model_dump(mode="json")
# 4. model_dump_json()
# 5. Nested model serialization
# 6. Custom datetime formatting
# 7. JSON encoded strings
# -------------------------------------------------

from datetime import datetime
from typing import List

from pydantic import BaseModel, ConfigDict, Field


# =================================================
# 1. Address Model
# =================================================

class Address(BaseModel):
    """
    Nested model used inside User.
    """

    street: str
    city: str
    zip_code: str


# =================================================
# 2. User Model
# =================================================

class User(BaseModel):
    """
    User model with multiple field types.

    This model includes:
    - basic fields
    - datetime field
    - nested Address model
    - list of tags
    - custom datetime serialization
    """

    model_config = ConfigDict(
        json_encoders={
            datetime: lambda value: value.strftime(
                "%d-%m-%Y %H:%M:%S"
            )
        }
    )

    id: int
    name: str
    email: str
    is_active: bool = True
    created_at: datetime
    address: Address
    tags: List[str] = Field(default_factory=list)


# =================================================
# 3. Create User Object
# =================================================

def create_user() -> User:
    """
    Create and return a sample User object.
    """

    user = User(
        id=1,
        name="Hitesh",
        email="h@hitesh.ai",
        is_active=False,
        created_at=datetime(
            2024,
            3,
            15,
            14,
            30,
            20,
        ),
        address=Address(
            street="123 Main Street",
            city="Jaipur",
            zip_code="009988",
        ),
        tags=[
            "premium",
            "subscriber",
        ],
    )

    return user


# =================================================
# 4. Print Model Directly
# =================================================

def print_model_directly(user: User) -> None:
    """
    Print the Pydantic model directly.

    This is useful for debugging, but it is not the
    same as serializing to dictionary or JSON.
    """

    print("\nPRINT MODEL DIRECTLY")
    print("-" * 50)

    print(user)


# =================================================
# 5. model_dump()
# =================================================

def model_dump_example(user: User) -> None:
    """
    Convert the Pydantic model into a Python
    dictionary using model_dump().
    """

    python_dict = user.model_dump()

    print("\nMODEL DUMP")
    print("-" * 50)

    print(python_dict)
    print("Output type:", type(python_dict))
    print("created_at type:", type(python_dict["created_at"]))
    print("address type:", type(python_dict["address"]))


# =================================================
# 6. model_dump(mode='json')
# =================================================

def model_dump_json_mode_example(user: User) -> None:
    """
    Convert the Pydantic model into a JSON-compatible
    Python dictionary.

    This is still a dictionary, not a JSON string.
    """

    json_ready_dict = user.model_dump(
        mode="json",
    )

    print("\nMODEL DUMP WITH JSON MODE")
    print("-" * 50)

    print(json_ready_dict)
    print("Output type:", type(json_ready_dict))
    print("created_at type:", type(json_ready_dict["created_at"]))
    print("address type:", type(json_ready_dict["address"]))


# =================================================
# 7. model_dump_json()
# =================================================

def model_dump_json_example(user: User) -> None:
    """
    Convert the Pydantic model directly into a JSON
    encoded string.
    """

    json_string = user.model_dump_json()

    print("\nMODEL DUMP JSON")
    print("-" * 50)

    print(json_string)
    print("Output type:", type(json_string))


# =================================================
# 8. Pretty JSON Output
# =================================================

def pretty_json_example(user: User) -> None:
    """
    Convert the model into a formatted JSON string.

    indent=4 makes the output easier to read.
    """

    pretty_json = user.model_dump_json(
        indent=4,
    )

    print("\nPRETTY JSON")
    print("-" * 50)

    print(pretty_json)


# =================================================
# 9. Include and Exclude Fields
# =================================================

def include_exclude_example(user: User) -> None:
    """
    Demonstrate include and exclude during
    serialization.
    """

    public_user = user.model_dump(
        exclude={
            "email",
        }
    )

    only_basic_info = user.model_dump(
        include={
            "id",
            "name",
            "is_active",
        }
    )

    print("\nINCLUDE AND EXCLUDE")
    print("-" * 50)

    print("Public user without email:")
    print(public_user)

    print("\nOnly basic info:")
    print(only_basic_info)


# =================================================
# 10. Default Value Serialization
# =================================================

def exclude_defaults_example(user: User) -> None:
    """
    Demonstrate excluding default values.

    Since is_active is explicitly set to False in
    this example, it is not the default value.
    """

    data = user.model_dump(
        exclude_defaults=True,
    )

    print("\nEXCLUDE DEFAULTS")
    print("-" * 50)

    print(data)


# =================================================
# 11. User with Default Tags
# =================================================

def default_tags_example() -> None:
    """
    Demonstrate Field(default_factory=list).

    Each User gets its own separate empty list.
    """

    user = User(
        id=2,
        name="Ravi",
        email="ravi@example.com",
        created_at=datetime(
            2024,
            4,
            10,
            9,
            15,
            0,
        ),
        address={
            "street": "456 Market Road",
            "city": "Ahmedabad",
            "zip_code": "380001",
        },
    )

    print("\nDEFAULT TAGS")
    print("-" * 50)

    print(user)
    print("Tags:", user.tags)
    print("Model dump JSON:")
    print(user.model_dump_json(indent=4))


# =================================================
# 12. Main Program
# =================================================

def main() -> None:
    """
    Run all serialization examples.
    """

    print("Pydantic Serialization")
    print("=" * 50)

    user = create_user()

    print_model_directly(user)
    model_dump_example(user)
    model_dump_json_mode_example(user)
    model_dump_json_example(user)
    pretty_json_example(user)
    include_exclude_example(user)
    exclude_defaults_example(user)
    default_tags_example()


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
# python pydantic_serialization.py
#
#
# =================================================
# Notes
# =================================================

# Serialization:
# Converting complex data into a simpler format
# such as dictionary or JSON string.
#
#
# model_dump():
# Converts a Pydantic model into a Python dictionary.
#
#
# Example:
#
# data = user.model_dump()
#
#
# model_dump(mode="json"):
# Converts a Pydantic model into a JSON-compatible
# Python dictionary.
#
#
# Example:
#
# data = user.model_dump(mode="json")
#
#
# model_dump_json():
# Converts a Pydantic model into a JSON encoded
# string.
#
#
# Example:
#
# json_string = user.model_dump_json()
#
#
# Nested models:
# Nested Pydantic models are also serialized.
#
#
# Datetime:
# Python datetime objects need special attention
# during JSON serialization.
#
#
# Custom datetime format:
#
# model_config = ConfigDict(
#     json_encoders={
#         datetime: lambda value: value.strftime(
#             "%d-%m-%Y %H:%M:%S"
#         )
#     }
# )
#
#
# strftime format used:
#
# %d = day
# %m = month
# %Y = four-digit year
# %H = hour
# %M = minute
# %S = second
#
#
# Difference:
#
# model_dump() returns a dictionary.
# model_dump_json() returns a JSON string.
#
#
# Safer list default:
#
# tags: List[str] = Field(default_factory=list)
