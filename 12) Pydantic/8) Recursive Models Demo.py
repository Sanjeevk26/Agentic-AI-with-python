# Pydantic Recursive / Self-Referencing Models
# Topics:
# 1. Recursive models
# 2. Self references
# 3. Forward references
# 4. model_rebuild()
# 5. Optional nested lists
# 6. Recursive validation
# 7. default_factory for empty lists
# -------------------------------------------------

from typing import List, Optional

from pydantic import BaseModel, Field, ValidationError


# =================================================
# 1. Recursive Comment Model
# =================================================

class Comment(BaseModel):
    """
    A recursive model.

    A comment can have replies.
    Each reply is also a Comment.
    """

    id: int
    content: str

    # Forward reference:
    # "Comment" is written as a string because the
    # Comment class is still being defined.
    replies: Optional[List["Comment"]] = None


# Resolve forward references explicitly.
Comment.model_rebuild()


# =================================================
# 2. Simple Comment Example
# =================================================

def simple_comment_example() -> None:
    """
    Create a comment without replies.
    """

    comment = Comment(
        id=1,
        content="First comment",
    )

    print("\nSIMPLE COMMENT")
    print("-" * 50)

    print(comment)
    print("Replies:", comment.replies)


# =================================================
# 3. Comment with Replies
# =================================================

def comment_with_replies_example() -> None:
    """
    Create a comment with direct replies.
    """

    comment = Comment(
        id=1,
        content="First comment",
        replies=[
            Comment(
                id=2,
                content="Reply one",
            ),
            Comment(
                id=3,
                content="Reply two",
            ),
        ],
    )

    print("\nCOMMENT WITH REPLIES")
    print("-" * 50)

    print(comment)

    if comment.replies:
        for reply in comment.replies:
            print(f"Reply {reply.id}: {reply.content}")


# =================================================
# 4. Nested Replies Example
# =================================================

def nested_replies_example() -> None:
    """
    Create a comment with nested replies.
    """

    comment = Comment(
        id=1,
        content="First comment",
        replies=[
            Comment(
                id=2,
                content="Reply one",
            ),
            Comment(
                id=3,
                content="Reply two",
                replies=[
                    Comment(
                        id=4,
                        content="Nested reply",
                    )
                ],
            ),
        ],
    )

    print("\nNESTED REPLIES")
    print("-" * 50)

    print(comment)
    print("Model dump:")
    print(comment.model_dump())


# =================================================
# 5. Recursive Model from Dictionary
# =================================================

def recursive_dictionary_example() -> None:
    """
    Create a recursive model from nested dictionary
    data.

    Pydantic automatically converts nested
    dictionaries into Comment objects.
    """

    comment_data = {
        "id": 1,
        "content": "First comment from dictionary",
        "replies": [
            {
                "id": 2,
                "content": "Reply one from dictionary",
            },
            {
                "id": 3,
                "content": "Reply two from dictionary",
                "replies": [
                    {
                        "id": 4,
                        "content": "Nested reply from dictionary",
                    }
                ],
            },
        ],
    }

    comment = Comment(**comment_data)

    print("\nRECURSIVE DICTIONARY")
    print("-" * 50)

    print(comment)
    print("Type of first reply:", type(comment.replies[0]))
    print("Model dump:")
    print(comment.model_dump())


# =================================================
# 6. Recursive Validation Error
# =================================================

def recursive_validation_error_example() -> None:
    """
    Show validation error inside nested replies.
    """

    bad_comment_data = {
        "id": 1,
        "content": "Parent comment",
        "replies": [
            {
                "id": "wrong-id",
                "content": "Invalid reply",
            }
        ],
    }

    print("\nRECURSIVE VALIDATION ERROR")
    print("-" * 50)

    try:
        Comment(**bad_comment_data)

    except ValidationError as error:
        print("Validation failed:")
        print(error)


# =================================================
# 7. Printing Comment Tree
# =================================================

def print_comment_tree(
    comment: Comment,
    level: int = 0,
) -> None:
    """
    Recursively print a comment and its replies.
    """

    indent = "  " * level

    print(f"{indent}- {comment.content}")

    if comment.replies:
        for reply in comment.replies:
            print_comment_tree(
                reply,
                level + 1,
            )


def print_tree_example() -> None:
    """
    Demonstrate recursive traversal of the model.
    """

    comment = Comment(
        id=1,
        content="Root comment",
        replies=[
            Comment(
                id=2,
                content="First reply",
            ),
            Comment(
                id=3,
                content="Second reply",
                replies=[
                    Comment(
                        id=4,
                        content="Nested reply",
                    ),
                    Comment(
                        id=5,
                        content="Another nested reply",
                    ),
                ],
            ),
        ],
    )

    print("\nCOMMENT TREE")
    print("-" * 50)

    print_comment_tree(comment)


# =================================================
# 8. Alternative Model with Empty List Default
# =================================================

class CommentWithList(BaseModel):
    """
    Recursive model where replies default to an
    empty list instead of None.
    """

    id: int
    content: str

    # Use default_factory to avoid mutable default
    # problems.
    replies: List["CommentWithList"] = Field(
        default_factory=list,
    )


CommentWithList.model_rebuild()


def empty_list_default_example() -> None:
    """
    Demonstrate replies as an empty list by default.
    """

    comment = CommentWithList(
        id=1,
        content="Comment with empty replies list",
    )

    print("\nEMPTY LIST DEFAULT")
    print("-" * 50)

    print(comment)
    print("Replies:", comment.replies)
    print("Replies type:", type(comment.replies))


# =================================================
# 9. Category Tree Example
# =================================================

class Category(BaseModel):
    """
    Another recursive model example.

    A category can have child categories.
    """

    id: int
    name: str
    children: List["Category"] = Field(
        default_factory=list,
    )


Category.model_rebuild()


def category_tree_example() -> None:
    """
    Demonstrate recursive category data.
    """

    category = Category(
        id=1,
        name="Electronics",
        children=[
            Category(
                id=2,
                name="Laptops",
            ),
            Category(
                id=3,
                name="Accessories",
                children=[
                    Category(
                        id=4,
                        name="Mouse",
                    ),
                    Category(
                        id=5,
                        name="Keyboard",
                    ),
                ],
            ),
        ],
    )

    print("\nCATEGORY TREE")
    print("-" * 50)

    print(category)
    print("Model dump:")
    print(category.model_dump())


# =================================================
# 10. Main Program
# =================================================

def main() -> None:
    """
    Run all recursive model examples.
    """

    print("Pydantic Recursive Models")
    print("=" * 50)

    simple_comment_example()
    comment_with_replies_example()
    nested_replies_example()
    recursive_dictionary_example()
    recursive_validation_error_example()
    print_tree_example()
    empty_list_default_example()
    category_tree_example()


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
# python pydantic_recursive_models.py
#
#
# =================================================
# Notes
# =================================================

# Recursive model:
# A model that refers to itself.
#
#
# Self-referencing model:
# Another name for recursive model.
#
#
# Forward reference:
#
# replies: Optional[List["Comment"]] = None
#
# "Comment" is written in quotes because the class
# is still being defined.
#
#
# model_rebuild:
#
# Comment.model_rebuild()
#
# Helps Pydantic resolve forward references.
#
#
# Optional replies:
#
# replies: Optional[List["Comment"]] = None
#
# Means replies can be None or a list of Comment
# objects.
#
#
# Empty list replies:
#
# replies: List["Comment"] = Field(default_factory=list)
#
# Means replies will default to an empty list.
#
#
# Avoid:
#
# replies: List["Comment"] = []
#
# Use default_factory instead.
#
#
# Common use cases:
# - comments and replies
# - folder trees
# - category trees
# - nested menus
# - organization hierarchy
