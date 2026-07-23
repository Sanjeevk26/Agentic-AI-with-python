# Pydantic Advanced Field Types
# Topics:
# 1. BaseModel
# 2. List
# 3. Dict
# 4. Optional
# 5. ValidationError
# 6. Complex field validation
# -------------------------------------------------

from typing import Dict, List, Optional

from pydantic import BaseModel, ValidationError


# =================================================
# 1. Cart Model
# =================================================

class Cart(BaseModel):
    """
    A cart model using advanced field types.

    user_id:
        Must be an integer.

    items:
        Must be a list of strings.

    quantities:
        Must be a dictionary where:
        - keys are strings
        - values are integers
    """

    user_id: int
    items: List[str]
    quantities: Dict[str, int]


# =================================================
# 2. Blog Post Model
# =================================================

class BlogPost(BaseModel):
    """
    A blog post model with an optional image URL.

    image_url can be:
    - a string
    - None

    Because it has a default value of None, it is
    not required during object creation.
    """

    title: str
    content: str
    image_url: Optional[str] = None


# =================================================
# 3. Valid Cart Example
# =================================================

def valid_cart_example() -> None:
    """
    Create a valid Cart object.
    """

    cart = Cart(
        user_id=101,
        items=[
            "tea",
            "milk",
            "sugar",
        ],
        quantities={
            "tea": 2,
            "milk": 1,
            "sugar": 3,
        },
    )

    print("\nVALID CART")
    print("-" * 50)

    print(cart)
    print("User ID:", cart.user_id)
    print("Items:", cart.items)
    print("Quantities:", cart.quantities)
    print("As dictionary:", cart.model_dump())


# =================================================
# 4. Invalid List Example
# =================================================

def invalid_list_example() -> None:
    """
    Show what happens when items contains a value
    that is not a string.
    """

    print("\nINVALID LIST EXAMPLE")
    print("-" * 50)

    try:
        Cart(
            user_id=102,
            items=[
                "tea",
                123,
                "sugar",
            ],
            quantities={
                "tea": 2,
                "sugar": 3,
            },
        )

    except ValidationError as error:
        print("Validation failed:")
        print(error)


# =================================================
# 5. Invalid Dictionary Example
# =================================================

def invalid_dictionary_example() -> None:
    """
    Show what happens when quantities contains a
    value that cannot be converted into an integer.
    """

    print("\nINVALID DICTIONARY EXAMPLE")
    print("-" * 50)

    try:
        Cart(
            user_id=103,
            items=[
                "tea",
                "milk",
            ],
            quantities={
                "tea": "two",
                "milk": 1,
            },
        )

    except ValidationError as error:
        print("Validation failed:")
        print(error)


# =================================================
# 6. Blog Post Without Image
# =================================================

def blog_without_image_example() -> None:
    """
    Create a BlogPost without image_url.

    Since image_url has a default value of None,
    this is valid.
    """

    post = BlogPost(
        title="Learning Pydantic",
        content="Pydantic helps validate data.",
    )

    print("\nBLOG POST WITHOUT IMAGE")
    print("-" * 50)

    print(post)
    print("Image URL:", post.image_url)


# =================================================
# 7. Blog Post With Image
# =================================================

def blog_with_image_example() -> None:
    """
    Create a BlogPost with image_url.
    """

    post = BlogPost(
        title="Advanced Pydantic Fields",
        content="List, Dict, and Optional are useful.",
        image_url="https://example.com/pydantic.png",
    )

    print("\nBLOG POST WITH IMAGE")
    print("-" * 50)

    print(post)
    print("Image URL:", post.image_url)


# =================================================
# 8. Invalid Blog Post Example
# =================================================

def invalid_blog_post_example() -> None:
    """
    Show what happens when a required field is missing.
    """

    print("\nINVALID BLOG POST EXAMPLE")
    print("-" * 50)

    try:
        BlogPost(
            title="Missing Content Example",
        )

    except ValidationError as error:
        print("Validation failed:")
        print(error)


# =================================================
# 9. Type Conversion Example
# =================================================

def type_conversion_example() -> None:
    """
    Pydantic may convert compatible values.

    Here user_id is passed as a string, but it can
    be converted into an integer.

    Quantity values are also passed as strings that
    can be converted into integers.
    """

    cart = Cart(
        user_id="104",
        items=[
            "ginger tea",
            "masala tea",
        ],
        quantities={
            "ginger tea": "2",
            "masala tea": "5",
        },
    )

    print("\nTYPE CONVERSION EXAMPLE")
    print("-" * 50)

    print(cart)
    print("user_id type:", type(cart.user_id))
    print(
        "quantity value type:",
        type(cart.quantities["ginger tea"]),
    )


# =================================================
# 10. Modern Syntax Example
# =================================================

class ModernCart(BaseModel):
    """
    The same idea using modern Python syntax.

    This requires Python 3.9+ for list[str] and
    dict[str, int].

    The str | None syntax requires Python 3.10+.
    """

    user_id: int
    items: list[str]
    quantities: dict[str, int]
    coupon_code: str | None = None


def modern_syntax_example() -> None:
    """
    Demonstrate modern built-in generic syntax.
    """

    cart = ModernCart(
        user_id=105,
        items=[
            "black tea",
            "green tea",
        ],
        quantities={
            "black tea": 1,
            "green tea": 2,
        },
    )

    print("\nMODERN SYNTAX EXAMPLE")
    print("-" * 50)

    print(cart)


# =================================================
# 11. Main Program
# =================================================

def main() -> None:
    """
    Run all advanced field type examples.
    """

    print("Pydantic Advanced Field Types")
    print("=" * 50)

    valid_cart_example()
    invalid_list_example()
    invalid_dictionary_example()
    blog_without_image_example()
    blog_with_image_example()
    invalid_blog_post_example()
    type_conversion_example()
    modern_syntax_example()


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
# python pydantic_advanced_field_types.py
#
#
# =================================================
# Notes
# =================================================

# BaseModel:
# Parent class for Pydantic models.
#
#
# List:
#
# from typing import List
#
# items: List[str]
#
# Means:
# items must be a list of strings.
#
#
# Dict:
#
# from typing import Dict
#
# quantities: Dict[str, int]
#
# Means:
# dictionary keys must be strings and values must
# be integers.
#
#
# Optional:
#
# from typing import Optional
#
# image_url: Optional[str] = None
#
# Means:
# image_url can be a string or None.
#
#
# Important:
# Optional[str] without = None means the field can
# be None, but it may still be required.
#
#
# Python built-in types:
# str, int, bool, float
#
#
# typing module types:
# List, Dict, Optional
#
#
# Modern syntax:
#
# items: list[str]
# quantities: dict[str, int]
# coupon_code: str | None = None
#
#
# Pydantic validates nested structures and raises
# ValidationError when values do not match the
# expected type.
