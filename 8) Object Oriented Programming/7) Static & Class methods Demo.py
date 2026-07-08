# Python Object-Oriented Programming
# Topics:
# 1. Static methods
# 2. Utility methods
# 3. Class methods
# 4. Alternate constructors
# 5. Creating objects from dictionaries
# 6. Creating objects from strings
# 7. Difference between self, cls, and no argument
# -------------------------------------------------


# =================================================
# 1. Static Method Utility Class
# =================================================

class ChaiUtils:
    """
    Provide utility operations related to chai.
    """

    @staticmethod
    def clean_ingredients(text):
        """
        Split a comma-separated string and remove
        extra spaces from every ingredient.
        """

        return [
            item.strip()
            for item in text.split(",")
            if item.strip()
        ]

    @staticmethod
    def is_valid_size(size):
        """
        Return True when size is supported.
        """

        valid_sizes = {
            "small",
            "medium",
            "large",
        }

        return size.strip().lower() in valid_sizes


raw_ingredients = " water, milk , ginger, honey "

cleaned_ingredients = ChaiUtils.clean_ingredients(
    raw_ingredients
)

print("Cleaned ingredients:")
print(cleaned_ingredients)

print()

print("Is Medium valid?")
print(ChaiUtils.is_valid_size("Medium"))

print("Is Extra Large valid?")
print(ChaiUtils.is_valid_size("Extra Large"))

print("-" * 50)


# =================================================
# 2. Calling a Static Method Through an Object
# =================================================

# This works, but object creation is unnecessary
# because the method does not use instance state.

utils_object = ChaiUtils()

print("Called through an object:")
print(
    utils_object.clean_ingredients(
        "tea leaves, sugar , milk"
    )
)

print("-" * 50)


# =================================================
# 3. ChaiOrder with Normal Constructor
# =================================================

class ChaiOrder:
    """
    Represent one chai order.
    """

    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    def summary(self):
        return (
            f"{self.size} {self.tea_type} "
            f"with {self.sweetness} sweetness"
        )


normal_order = ChaiOrder(
    "Masala Chai",
    "Medium",
    "Large",
)

print("Normal constructor:")
print(normal_order.summary())
print(normal_order.__dict__)

print("-" * 50)


# =================================================
# 4. Class Method from Dictionary
# =================================================

class FlexibleChaiOrder:
    """
    Support multiple ways of creating an order.
    """

    def __init__(self, tea_type, sweetness, size):
        self.tea_type = tea_type
        self.sweetness = sweetness
        self.size = size

    @classmethod
    def from_dict(cls, order_data):
        """
        Create an object from dictionary data.
        """

        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )

    @classmethod
    def from_string(cls, order_string):
        """
        Create an object from a dash-separated string.

        Expected format:
        tea_type-sweetness-size
        """

        tea_type, sweetness, size = (
            order_string.split("-")
        )

        return cls(
            tea_type.strip(),
            sweetness.strip(),
            size.strip(),
        )

    def summary(self):
        return (
            f"{self.size} {self.tea_type} "
            f"with {self.sweetness} sweetness"
        )


dictionary_data = {
    "tea_type": "Masala Chai",
    "sweetness": "Medium",
    "size": "Large",
}

order_one = FlexibleChaiOrder.from_dict(
    dictionary_data
)

print("Order created from dictionary:")
print(order_one.summary())
print(order_one.__dict__)

print("-" * 50)


# =================================================
# 5. Class Method from String
# =================================================

order_two = FlexibleChaiOrder.from_string(
    "Ginger Chai-Low-Small"
)

print("Order created from string:")
print(order_two.summary())
print(order_two.__dict__)

print("-" * 50)


# =================================================
# 6. Normal Object Creation Still Works
# =================================================

order_three = FlexibleChaiOrder(
    "Green Tea",
    "Low",
    "Large",
)

print("Order created normally:")
print(order_three.summary())
print(order_three.__dict__)

print("-" * 50)


# =================================================
# 7. Class Method Supports Subclasses
# =================================================

class PremiumChaiOrder(FlexibleChaiOrder):
    """
    A specialized version of FlexibleChaiOrder.
    """

    pass


premium_order = PremiumChaiOrder.from_string(
    "Kesar Chai-Low-Large"
)

print("Subclass object created by class method:")
print(premium_order.summary())
print("Object type:", type(premium_order).__name__)

# Because from_string() uses cls(...),
# it creates PremiumChaiOrder instead of
# always creating FlexibleChaiOrder.

print("-" * 50)


# =================================================
# 8. Combined Static and Class Methods
# =================================================

class ValidatedChaiOrder:
    valid_sizes = {
        "small",
        "medium",
        "large",
    }

    def __init__(self, tea_type, sweetness, size):
        if not self.is_valid_size(size):
            raise ValueError(
                f"Unsupported chai size: {size}"
            )

        self.tea_type = tea_type.strip()
        self.sweetness = sweetness.strip()
        self.size = size.strip().lower()

    @staticmethod
    def is_valid_size(size):
        """
        Validate size without requiring an object.
        """

        return (
            isinstance(size, str)
            and size.strip().lower()
            in ValidatedChaiOrder.valid_sizes
        )

    @classmethod
    def from_dict(cls, order_data):
        """
        Create a validated order from a dictionary.
        """

        return cls(
            order_data["tea_type"],
            order_data["sweetness"],
            order_data["size"],
        )

    @classmethod
    def from_string(cls, order_string):
        """
        Create a validated order from a string.
        """

        parts = [
            part.strip()
            for part in order_string.split("-")
        ]

        if len(parts) != 3:
            raise ValueError(
                "Expected format: "
                "tea_type-sweetness-size"
            )

        tea_type, sweetness, size = parts

        return cls(
            tea_type,
            sweetness,
            size,
        )

    def summary(self):
        return (
            f"{self.size.title()} {self.tea_type} "
            f"with {self.sweetness} sweetness"
        )


validated_order = ValidatedChaiOrder.from_dict(
    {
        "tea_type": "Lemon Tea",
        "sweetness": "Low",
        "size": "Medium",
    }
)

print("Validated order:")
print(validated_order.summary())

print("-" * 50)


# =================================================
# 9. Handling Invalid Static Validation
# =================================================

try:
    invalid_order = ValidatedChaiOrder.from_string(
        "Masala Chai-Low-Extra Large"
    )
except ValueError as error:
    print("Could not create order:")
    print(error)

print("-" * 50)


# =================================================
# 10. Instance, Class, and Static Methods
# =================================================

class MethodDemo:
    class_message = "Shared class value"

    def __init__(self, instance_message):
        self.instance_message = instance_message

    def instance_method(self):
        """
        Receives the object as self.
        """

        return {
            "instance": self.instance_message,
            "class": self.class_message,
        }

    @classmethod
    def class_method(cls):
        """
        Receives the class as cls.
        """

        return {
            "class_name": cls.__name__,
            "class_message": cls.class_message,
        }

    @staticmethod
    def static_method(first, second):
        """
        Receives no automatic first argument.
        """

        return first + second


demo = MethodDemo("Object-specific value")

print("Instance method:")
print(demo.instance_method())

print()

print("Class method:")
print(MethodDemo.class_method())

print()

print("Static method:")
print(MethodDemo.static_method(10, 20))

print("-" * 50)


# =================================================
# Notes
# =================================================

# Instance method:
#
# def method(self):
#     pass
#
# Python automatically passes the object as self.
#
#
# Class method:
#
# @classmethod
# def method(cls):
#     pass
#
# Python automatically passes the class as cls.
#
#
# Static method:
#
# @staticmethod
# def method(value):
#     pass
#
# Python passes no automatic first argument.
#
#
# Static methods are commonly used for:
# - Validation
# - Parsing
# - Formatting
# - Conversion
# - Related utility calculations
#
#
# Class methods are commonly used for:
# - Alternate constructors
# - Factory methods
# - Accessing class-level state
# - Creating subclass-aware objects
#
#
# Alternate constructor:
#
# @classmethod
# def from_dict(cls, data):
#     return cls(...)
#
#
# Why use cls instead of a hardcoded class name?
#
# return cls(...)
#
# supports subclasses correctly.
#
#
# __dict__:
# Shows attributes stored directly on an object.
#
#
# Important:
# Python does not support multiple active __init__
# definitions in one class. The last definition would
# replace earlier ones. Class methods provide additional
# ways to create objects while reusing one __init__.
