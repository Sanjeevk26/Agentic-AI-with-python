# Python Object-Oriented Programming
# Topics:
# 1. Inheritance
# 2. Parent and child classes
# 3. Inherited constructors
# 4. super()
# 5. Method overriding
# 6. Composition
# 7. Inheritance and composition together
# -------------------------------------------------


# =================================================
# 1. Base Class
# =================================================

class BaseChai:
    """
    Represent the common behaviour of a chai.
    """

    def __init__(self, chai_type):
        self.chai_type = chai_type

    def prepare(self):
        return f"Preparing {self.chai_type}..."


regular_chai = BaseChai("Regular Chai")

print(regular_chai.prepare())

print("-" * 50)


# =================================================
# 2. Basic Inheritance
# =================================================

class MasalaChai(BaseChai):
    """
    MasalaChai inherits from BaseChai.
    """

    def add_spices(self):
        return "Adding cardamom, ginger, and clove"


# MasalaChai inherits BaseChai.__init__.
masala_chai = MasalaChai("Masala Chai")

print(masala_chai.prepare())
print(masala_chai.add_spices())

print("-" * 50)


# =================================================
# 3. Child Constructor with super()
# =================================================

class PremiumMasalaChai(BaseChai):
    def __init__(self, chai_type, spice_level):
        # Initialize attributes defined by the parent.
        super().__init__(chai_type)

        # Initialize a child-specific attribute.
        self.spice_level = spice_level

    def describe(self):
        return (
            f"{self.chai_type} with "
            f"{self.spice_level.lower()} spice level"
        )


premium_chai = PremiumMasalaChai(
    "Premium Masala Chai",
    "Strong",
)

print(premium_chai.prepare())
print(premium_chai.describe())

print("-" * 50)


# =================================================
# 4. Method Overriding
# =================================================

class GingerChai(BaseChai):
    def prepare(self):
        return f"Preparing {self.chai_type} with fresh ginger..."


ginger_chai = GingerChai("Ginger Chai")

# Uses the overridden method.
print(ginger_chai.prepare())

print("-" * 50)


# =================================================
# 5. Extending a Parent Method
# =================================================

class ElaichiChai(BaseChai):
    def prepare(self):
        # Call the parent method first.
        base_preparation = super().prepare()

        return f"{base_preparation} Adding crushed cardamom."


elaichi_chai = ElaichiChai("Elaichi Chai")

print(elaichi_chai.prepare())

print("-" * 50)


# =================================================
# 6. Composition
# =================================================

class ChaiShop:
    """
    A ChaiShop has a chai object.

    This is composition, not inheritance.
    """

    def __init__(self, chai):
        self.chai = chai

    def serve(self):
        preparation_message = self.chai.prepare()

        return (
            f"{preparation_message}\n"
            f"Serving {self.chai.chai_type}"
        )


regular_shop = ChaiShop(regular_chai)

print("Regular shop:")
print(regular_shop.serve())

print("-" * 50)


# =================================================
# 7. Composition with a Child-Class Object
# =================================================

# ChaiShop can also contain a MasalaChai object.
masala_shop = ChaiShop(masala_chai)

print("Masala chai shop:")
print(masala_shop.serve())

print("-" * 50)


# =================================================
# 8. Access Child-Specific Behaviour Safely
# =================================================

class SpiceAwareChaiShop:
    def __init__(self, chai):
        self.chai = chai

    def serve(self):
        messages = [self.chai.prepare()]

        # Not every chai object is guaranteed
        # to provide add_spices().
        if hasattr(self.chai, "add_spices"):
            messages.append(self.chai.add_spices())

        messages.append(f"Serving {self.chai.chai_type}")

        return "\n".join(messages)


spice_shop = SpiceAwareChaiShop(masala_chai)

print(spice_shop.serve())

print("-" * 50)


# =================================================
# 9. Inheritance and Composition Together
# =================================================

class FancyChaiShop(ChaiShop):
    """
    FancyChaiShop is a ChaiShop.

    It also has a chai through the ChaiShop constructor.
    """

    def serve_with_style(self):
        normal_service = self.serve()

        return (
            f"{normal_service}\n"
            "Served in a premium cup"
        )


fancy_shop = FancyChaiShop(masala_chai)

print(fancy_shop.serve_with_style())

print("-" * 50)


# =================================================
# 10. Class Reference vs Object Creation
# =================================================

# This stores the class itself.
chai_class = BaseChai

print("Class reference:")
print(chai_class)

# Parentheses create an object.
chai_object = chai_class("Lemon Tea")

print("Created object:")
print(chai_object.prepare())

print("-" * 50)


# =================================================
# 11. Factory-Style Composition
# =================================================

class ConfigurableChaiShop:
    """
    Accept a class and create chai objects when needed.

    This is useful when the shop should decide
    when objects are created.
    """

    def __init__(self, chai_class):
        self.chai_class = chai_class

    def create_chai(self, chai_type):
        return self.chai_class(chai_type)


configurable_shop = ConfigurableChaiShop(MasalaChai)

created_chai = configurable_shop.create_chai("Special Masala Chai")

print(created_chai.prepare())
print(created_chai.add_spices())

print("-" * 50)


# =================================================
# 12. isinstance() with Inheritance
# =================================================

print("Is masala_chai a MasalaChai?")
print(isinstance(masala_chai, MasalaChai))

print("Is masala_chai also a BaseChai?")
print(isinstance(masala_chai, BaseChai))

print("Is regular_shop a BaseChai?")
print(isinstance(regular_shop, BaseChai))

print("-" * 50)


# =================================================
# Notes
# =================================================

# Inheritance:
#
# class ChildClass(ParentClass):
#     pass
#
#
# Relationship:
# ChildClass is a ParentClass.
#
#
# Composition:
#
# class Container:
#     def __init__(self, object_):
#         self.object_ = object_
#
#
# Relationship:
# Container has an object.
#
#
# super():
# Used to call methods from the parent class.
#
#
# Method overriding:
# A child class defines a method with the same
# name as a method inherited from the parent.
#
#
# Class reference:
#
# chai_class = BaseChai
#
# No object is created.
#
#
# Object creation:
#
# chai = BaseChai("Regular Chai")
#
#
# General guidance:
# - Use inheritance for genuine "is-a" relationships.
# - Use composition for "has-a" relationships.
# - Composition often provides better flexibility.
