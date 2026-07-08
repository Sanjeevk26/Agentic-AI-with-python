# Python Object-Oriented Programming
# Topics:
# 1. Multiple inheritance
# 2. Diamond inheritance
# 3. Method Resolution Order
# 4. mro() and __mro__
# 5. Attribute resolution
# 6. Method resolution
# 7. super() with multiple inheritance
# 8. Invalid MRO
# -------------------------------------------------


# =================================================
# 1. Diamond Inheritance
# =================================================

class A:
    label = "Base Class"


class B(A):
    label = "Masala Blend"


class C(A):
    label = "Herbal Blend"


class D(B, C):
    pass


cup = D()

print("D inherits from B first and C second:")
print("Selected label:", cup.label)

print("-" * 50)


# =================================================
# 2. Display the Method Resolution Order
# =================================================

print("D.mro():")

for class_ in D.mro():
    print(class_.__name__)

print()

print("D.__mro__:")
print(D.__mro__)

print("-" * 50)


# =================================================
# 3. Reverse the Parent Order
# =================================================

class ReversedD(C, B):
    pass


reversed_cup = ReversedD()

print("ReversedD inherits from C first and B second:")
print("Selected label:", reversed_cup.label)

print()

print("ReversedD MRO:")

for class_ in ReversedD.mro():
    print(class_.__name__)

print("-" * 50)


# =================================================
# 4. MRO Continues When an Attribute Is Missing
# =================================================

class Base:
    category = "Beverage"


class FirstParent(Base):
    pass


class SecondParent(Base):
    category = "Tea"


class Child(FirstParent, SecondParent):
    pass


child = Child()

# FirstParent does not directly contain category,
# so Python continues to SecondParent.
print("Category:", child.category)

print("Child MRO:")

for class_ in Child.mro():
    print(class_.__name__)

print("-" * 50)


# =================================================
# 5. MRO with Methods
# =================================================

class BaseChai:
    def prepare(self):
        return "Preparing base chai"


class MasalaChai(BaseChai):
    def prepare(self):
        return "Preparing masala chai"


class HerbalChai(BaseChai):
    def prepare(self):
        return "Preparing herbal chai"


class SpecialChai(MasalaChai, HerbalChai):
    pass


special_chai = SpecialChai()

print("Method selected through MRO:")
print(special_chai.prepare())

print()

print("SpecialChai MRO:")

for class_ in SpecialChai.mro():
    print(class_.__name__)

print("-" * 50)


# =================================================
# 6. Cooperative super()
# =================================================

class Root:
    def prepare(self):
        print("Root: completing preparation")


class MasalaStep(Root):
    def prepare(self):
        print("MasalaStep: adding spices")
        super().prepare()


class HerbalStep(Root):
    def prepare(self):
        print("HerbalStep: adding herbs")
        super().prepare()


class CompleteChai(MasalaStep, HerbalStep):
    def prepare(self):
        print("CompleteChai: starting")
        super().prepare()


print("Cooperative super() execution:")

complete_chai = CompleteChai()
complete_chai.prepare()

print()

print("CompleteChai MRO:")

for class_ in CompleteChai.mro():
    print(class_.__name__)

print("-" * 50)


# =================================================
# 7. Why Direct Parent Calls Can Be Problematic
# =================================================

class DirectRoot:
    def prepare(self):
        print("DirectRoot: completing preparation")


class DirectMasala(DirectRoot):
    def prepare(self):
        print("DirectMasala: adding spices")

        # This directly names one class.
        DirectRoot.prepare(self)


class DirectHerbal(DirectRoot):
    def prepare(self):
        print("DirectHerbal: adding herbs")

        # This directly names one class.
        DirectRoot.prepare(self)


class DirectComplete(DirectMasala, DirectHerbal):
    def prepare(self):
        print("DirectComplete: starting")

        # Only DirectMasala is called directly.
        DirectMasala.prepare(self)


print("Direct parent-call execution:")
DirectComplete().prepare()

# DirectHerbal.prepare() is skipped because the calls
# do not cooperate through the MRO.

print("-" * 50)


# =================================================
# 8. A Practical Mixin Example
# =================================================

class LoggingMixin:
    def log(self, message):
        print(f"LOG: {message}")


class ValidationMixin:
    def validate_quantity(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than zero")


class ChaiOrder:
    def place_order(self, chai_type, quantity):
        return f"Placed order for {quantity} cup(s) of {chai_type}"


class ManagedChaiOrder(
    LoggingMixin,
    ValidationMixin,
    ChaiOrder,
):
    def create_order(self, chai_type, quantity):
        self.validate_quantity(quantity)

        result = self.place_order(chai_type, quantity)

        self.log(result)

        return result


managed_order = ManagedChaiOrder()

print("Mixin example:")
print(managed_order.create_order("Masala Chai", 2))

print()

print("ManagedChaiOrder MRO:")

for class_ in ManagedChaiOrder.mro():
    print(class_.__name__)

print("-" * 50)


# =================================================
# 9. Cooperative Constructors
# =================================================

class ConstructorRoot:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        print("ConstructorRoot initialized")


class ConstructorB(ConstructorRoot):
    def __init__(self, masala_level, **kwargs):
        self.masala_level = masala_level
        super().__init__(**kwargs)
        print("ConstructorB initialized")


class ConstructorC(ConstructorRoot):
    def __init__(self, herb_level, **kwargs):
        self.herb_level = herb_level
        super().__init__(**kwargs)
        print("ConstructorC initialized")


class ConstructorD(ConstructorB, ConstructorC):
    def __init__(
        self,
        masala_level,
        herb_level,
        **kwargs,
    ):
        super().__init__(
            masala_level=masala_level,
            herb_level=herb_level,
            **kwargs,
        )

        print("ConstructorD initialized")


print("Cooperative constructor execution:")

constructor_object = ConstructorD(
    masala_level="Strong",
    herb_level="Mild",
)

print("Masala level:", constructor_object.masala_level)
print("Herb level:", constructor_object.herb_level)

print("-" * 50)


# =================================================
# 10. Invalid MRO Example
# =================================================

class ParentA:
    pass


class ParentB:
    pass


class X(ParentA, ParentB):
    pass


class Y(ParentB, ParentA):
    pass


try:
    # X requires ParentA before ParentB.
    # Y requires ParentB before ParentA.
    # Python cannot create one consistent MRO.
    class Z(X, Y):
        pass

except TypeError as error:
    print("Invalid MRO error:")
    print(error)

print("-" * 50)


# =================================================
# Notes
# =================================================

# Multiple inheritance:
#
# class Child(ParentOne, ParentTwo):
#     pass
#
#
# Method Resolution Order:
# Determines where Python searches for inherited
# attributes and methods.
#
#
# View the MRO:
#
# Child.mro()
#
# Or:
#
# Child.__mro__
#
#
# Diamond inheritance:
#
#       A
#      / \
#     B   C
#      \ /
#       D
#
#
# For:
#
# class D(B, C):
#     pass
#
# The typical MRO is:
#
# D -> B -> C -> A -> object
#
#
# super():
# Calls the next matching method in the MRO.
#
#
# Important:
# The first parent has priority when both direct
# parents define the same member, but Python follows
# the complete MRO rather than checking only one class.
#
#
# C3 linearization:
# The algorithm Python uses to calculate a consistent
# Method Resolution Order.
#
#
# Recommendation:
# Keep multiple-inheritance hierarchies simple and use
# cooperative super() when several classes participate
# in the same operation.
