# Python Object-Oriented Programming
# Topics:
# 1. Code duplication in child classes
# 2. Explicit parent-class calls
# 3. Using super()
# 4. Calling parent methods
# 5. Method Resolution Order
# -------------------------------------------------


# =================================================
# 1. Base Class
# =================================================

class Chai:
    def __init__(self, chai_type, strength):
        self.chai_type = chai_type
        self.strength = strength

    def prepare(self):
        return f"Preparing {self.strength.lower()} {self.chai_type}"


# =================================================
# 2. Code Duplication Approach
# =================================================

class DuplicatedGingerChai(Chai):
    """
    This approach works, but repeats the logic
    already written in the parent constructor.
    """

    def __init__(self, chai_type, strength, spice_level):
        self.chai_type = chai_type
        self.strength = strength
        self.spice_level = spice_level


duplicated_chai = DuplicatedGingerChai(
    "Ginger Chai",
    "Strong",
    "High",
)

print("Code duplication approach:")
print("Type:", duplicated_chai.chai_type)
print("Strength:", duplicated_chai.strength)
print("Spice level:", duplicated_chai.spice_level)

print("-" * 50)


# =================================================
# 3. Explicit Parent Constructor Call
# =================================================

class ExplicitGingerChai(Chai):
    """
    Explicitly call Chai.__init__.

    Because the method is called through the class,
    self must be passed manually.
    """

    def __init__(self, chai_type, strength, spice_level):
        Chai.__init__(self, chai_type, strength)
        self.spice_level = spice_level


explicit_chai = ExplicitGingerChai(
    "Ginger Chai",
    "Strong",
    "Medium",
)

print("Explicit parent call:")
print("Type:", explicit_chai.chai_type)
print("Strength:", explicit_chai.strength)
print("Spice level:", explicit_chai.spice_level)

print("-" * 50)


# =================================================
# 4. Using super()
# =================================================

class GingerChai(Chai):
    """
    Use super() to call the next constructor
    in the Method Resolution Order.
    """

    def __init__(self, chai_type, strength, spice_level):
        super().__init__(chai_type, strength)
        self.spice_level = spice_level


ginger_chai = GingerChai(
    "Ginger Chai",
    "Strong",
    "High",
)

print("Using super():")
print("Type:", ginger_chai.chai_type)
print("Strength:", ginger_chai.strength)
print("Spice level:", ginger_chai.spice_level)

print("-" * 50)


# =================================================
# 5. Calling a Parent Method with super()
# =================================================

class SpecialGingerChai(Chai):
    def __init__(self, chai_type, strength, ginger_amount):
        super().__init__(chai_type, strength)
        self.ginger_amount = ginger_amount

    def prepare(self):
        # Get the result of the parent method.
        base_instructions = super().prepare()

        # Extend the parent's result.
        return (
            f"{base_instructions}, "
            f"then adding {self.ginger_amount} grams of ginger"
        )


special_chai = SpecialGingerChai(
    "Special Ginger Chai",
    "Strong",
    10,
)

print("Extending a parent method:")
print(special_chai.prepare())

print("-" * 50)


# =================================================
# 6. What Happens Without Parent Initialization
# =================================================

class IncompleteGingerChai(Chai):
    def __init__(self, spice_level):
        # Chai.__init__ is not called.
        self.spice_level = spice_level


incomplete_chai = IncompleteGingerChai("High")

print("Object without parent initialization:")
print("Spice level:", incomplete_chai.spice_level)

try:
    print("Type:", incomplete_chai.chai_type)
except AttributeError as error:
    print("AttributeError:", error)

print("-" * 50)


# =================================================
# 7. Method Resolution Order
# =================================================

print("GingerChai MRO:")

for class_ in GingerChai.mro():
    print(class_.__name__)

print("-" * 50)


# =================================================
# 8. Multi-Level Inheritance
# =================================================

class MasalaChai(Chai):
    def __init__(self, chai_type, strength, spices):
        super().__init__(chai_type, strength)
        self.spices = spices


class PremiumMasalaChai(MasalaChai):
    def __init__(
        self,
        chai_type,
        strength,
        spices,
        serving_style,
    ):
        super().__init__(chai_type, strength, spices)
        self.serving_style = serving_style


premium_chai = PremiumMasalaChai(
    chai_type="Premium Masala Chai",
    strength="Strong",
    spices=["ginger", "cardamom", "clove"],
    serving_style="Clay cup",
)

print("Multi-level inheritance:")
print("Type:", premium_chai.chai_type)
print("Strength:", premium_chai.strength)
print("Spices:", premium_chai.spices)
print("Serving style:", premium_chai.serving_style)

print("-" * 50)


# =================================================
# 9. Why super() Helps During Refactoring
# =================================================

class Beverage:
    def __init__(self, name):
        self.name = name


class HotBeverage(Beverage):
    def __init__(self, name, temperature):
        super().__init__(name)
        self.temperature = temperature


hot_chai = HotBeverage("Masala Chai", 85)

print("Refactoring-friendly example:")
print("Name:", hot_chai.name)
print("Temperature:", hot_chai.temperature)

print("-" * 50)


# =================================================
# Notes
# =================================================

# Code duplication:
#
# class Child(Parent):
#     def __init__(self, value):
#         self.value = value
#
# This repeats parent logic.
#
#
# Explicit parent call:
#
# Parent.__init__(self, value)
#
# self must be passed manually.
#
#
# super() call:
#
# super().__init__(value)
#
# self is handled automatically.
#
#
# super():
# Calls the next matching method in the MRO.
#
#
# MRO:
# Method Resolution Order determines the order
# in which Python searches classes for methods.
#
#
# Recommended approach:
# Use super() in most cooperative inheritance designs.
#
#
# Important:
# If a child defines its own __init__, Python does not
# automatically call the parent's __init__ method.
