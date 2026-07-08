# Python Object-Oriented Programming
# Topics:
# 1. Property getters
# 2. Property setters
# 3. Value validation
# 4. Read-only properties
# 5. Calculated properties
# 6. Property deleters
# -------------------------------------------------


# =================================================
# 1. Basic Property
# =================================================

class BasicTeaLeaf:
    def __init__(self, age):
        # Internal attribute by convention
        self._age = age

    @property
    def age(self):
        return self._age


basic_leaf = BasicTeaLeaf(2)

print("Basic property:")
print("Age:", basic_leaf.age)

print("-" * 50)


# =================================================
# 2. Calculated Property
# =================================================

class DisplayTeaLeaf:
    def __init__(self, age):
        self._age = age

    @property
    def age(self):
        # Demonstrates that a property can transform
        # the stored value before returning it.
        return self._age + 2


display_leaf = DisplayTeaLeaf(2)

print("Calculated property:")
print("Stored age:", display_leaf._age)
print("Displayed age:", display_leaf.age)

print("-" * 50)


# =================================================
# 3. Property with Getter and Setter
# =================================================

class TeaLeaf:
    def __init__(self, age):
        # Assign through the property so that
        # initialization also uses validation.
        self.age = age

    @property
    def age(self):
        """
        Return the stored tea leaf age.
        """

        return self._age

    @age.setter
    def age(self, value):
        """
        Validate and update the tea leaf age.
        """

        if not isinstance(value, int):
            raise TypeError(
                "Tea leaf age must be an integer"
            )

        if not 1 <= value <= 5:
            raise ValueError(
                "Tea leaf age must be between "
                "1 and 5 years"
            )

        self._age = value


leaf = TeaLeaf(2)

print("Initial valid age:")
print(leaf.age)

leaf.age = 4

print("Updated valid age:")
print(leaf.age)

print("-" * 50)


# =================================================
# 4. Invalid Property Update
# =================================================

try:
    leaf.age = 6
except ValueError as error:
    print("Invalid update rejected:")
    print(error)

print("Age remains:", leaf.age)

print("-" * 50)


# =================================================
# 5. Invalid Object Initialization
# =================================================

try:
    invalid_leaf = TeaLeaf(10)
except ValueError as error:
    print("Invalid object creation rejected:")
    print(error)

print("-" * 50)


# =================================================
# 6. Invalid Data Type
# =================================================

try:
    leaf.age = "four"
except TypeError as error:
    print("Invalid data type rejected:")
    print(error)

print("-" * 50)


# =================================================
# 7. Read-Only Property
# =================================================

class TeaBatch:
    def __init__(self, batch_id):
        self._batch_id = batch_id

    @property
    def batch_id(self):
        """
        A read-only property because no setter exists.
        """

        return self._batch_id


batch = TeaBatch("BATCH-101")

print("Read-only batch ID:")
print(batch.batch_id)

try:
    batch.batch_id = "BATCH-202"
except AttributeError as error:
    print("Read-only update rejected:")
    print(error)

print("-" * 50)


# =================================================
# 8. Calculated Read-Only Property
# =================================================

class MatureTeaLeaf:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")

        if not 1 <= value <= 5:
            raise ValueError(
                "Age must be between 1 and 5"
            )

        self._age = value

    @property
    def maturity(self):
        """
        Calculate maturity from the current age.
        """

        if self.age <= 2:
            return "Young"

        if self.age <= 4:
            return "Mature"

        return "Aged"


mature_leaf = MatureTeaLeaf(4)

print("Calculated maturity:")
print("Age:", mature_leaf.age)
print("Maturity:", mature_leaf.maturity)

mature_leaf.age = 5

print("Updated maturity:")
print("Age:", mature_leaf.age)
print("Maturity:", mature_leaf.maturity)

print("-" * 50)


# =================================================
# 9. Property Deleter
# =================================================

class DeletableTeaLeaf:
    def __init__(self, age):
        self.age = age

    @property
    def age(self):
        if not hasattr(self, "_age"):
            raise AttributeError(
                "Tea leaf age has been deleted"
            )

        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("Age must be an integer")

        if not 1 <= value <= 5:
            raise ValueError(
                "Age must be between 1 and 5"
            )

        self._age = value

    @age.deleter
    def age(self):
        print("Deleting tea leaf age")

        if hasattr(self, "_age"):
            del self._age


deletable_leaf = DeletableTeaLeaf(3)

print("Before deletion:")
print(deletable_leaf.age)

del deletable_leaf.age

try:
    print(deletable_leaf.age)
except AttributeError as error:
    print("After deletion:")
    print(error)

print("-" * 50)


# =================================================
# 10. Multiple Controlled Properties
# =================================================

class TeaOrder:
    valid_sizes = {
        "small",
        "medium",
        "large",
    }

    def __init__(self, tea_type, size, sweetness):
        self.tea_type = tea_type
        self.size = size
        self.sweetness = sweetness

    @property
    def tea_type(self):
        return self._tea_type

    @tea_type.setter
    def tea_type(self, value):
        if not isinstance(value, str):
            raise TypeError("Tea type must be a string")

        cleaned_value = value.strip()

        if not cleaned_value:
            raise ValueError("Tea type cannot be empty")

        self._tea_type = cleaned_value

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, str):
            raise TypeError("Size must be a string")

        normalized_value = value.strip().lower()

        if normalized_value not in self.valid_sizes:
            raise ValueError(
                f"Size must be one of: "
                f"{', '.join(sorted(self.valid_sizes))}"
            )

        self._size = normalized_value

    @property
    def sweetness(self):
        return self._sweetness

    @sweetness.setter
    def sweetness(self, value):
        if not isinstance(value, int):
            raise TypeError(
                "Sweetness must be an integer"
            )

        if not 0 <= value <= 100:
            raise ValueError(
                "Sweetness must be between 0 and 100"
            )

        self._sweetness = value

    @property
    def summary(self):
        return (
            f"{self.size.title()} {self.tea_type} "
            f"with {self.sweetness}% sweetness"
        )


order = TeaOrder(
    tea_type=" Masala Chai ",
    size="Large",
    sweetness=40,
)

print("Controlled tea order:")
print(order.summary)

order.size = "medium"
order.sweetness = 20

print("Updated tea order:")
print(order.summary)

print("-" * 50)


# =================================================
# 11. Inspect Internal Object Data
# =================================================

print("Internal TeaOrder attributes:")
print(order.__dict__)

# The object stores:
# _tea_type
# _size
# _sweetness
#
# Public access is provided through:
# tea_type
# size
# sweetness

print("-" * 50)


# =================================================
# Notes
# =================================================

# Property getter:
#
# @property
# def age(self):
#     return self._age
#
#
# Property setter:
#
# @age.setter
# def age(self, value):
#     self._age = value
#
#
# Property deleter:
#
# @age.deleter
# def age(self):
#     del self._age
#
#
# Public property:
#
# leaf.age
#
#
# Internal storage:
#
# leaf._age
#
#
# Important:
# A leading underscore is only a convention.
# It does not make an attribute truly private.
#
#
# Useful property use cases:
# - Input validation
# - Read-only values
# - Calculated values
# - Data normalization
# - Controlled updates
#
#
# Recommended initialization:
#
# def __init__(self, age):
#     self.age = age
#
# This calls the property setter and reuses
# the same validation during object creation.
