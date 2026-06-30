# function_scopes_demo.py

# ---------------------------------------
# Python Function Scopes Demo
# Topics:
# 1. Local scope
# 2. Enclosing scope
# 3. Global scope
# 4. nonlocal keyword
# 5. global keyword
# ---------------------------------------


# -----------------------------
# 1. Local Scope
# -----------------------------

# A variable created inside a function
# is available only inside that function.

def serve_chai():
    chai_type = "Masala Chai"  # local scope
    print("Inside function:", chai_type)


chai_type = "Lemon Chai"  # global scope

serve_chai()

print("Outside function:", chai_type)

print("-" * 40)


# -----------------------------
# 2. Enclosing Scope
# -----------------------------

# Enclosing scope happens when a function
# is created inside another function.

chai_order = "Tulsi Chai"  # global scope


def chai_counter():
    chai_order = "Lemon Chai"  # enclosing scope

    def print_order():
        chai_order = "Ginger Chai"  # local scope
        print("Inner:", chai_order)

    print_order()
    print("Outer:", chai_order)


chai_counter()

print("Global:", chai_order)

print("-" * 40)


# -----------------------------
# 3. nonlocal Keyword
# -----------------------------

# nonlocal is used inside a nested function.
# It allows the inner function to modify
# a variable from the outer function.

def update_order():
    chai_type = "Elaichi Chai"

    def kitchen():
        nonlocal chai_type
        chai_type = "Kesar Chai"

    kitchen()

    print("After kitchen update:", chai_type)


update_order()

print("-" * 40)


# -----------------------------
# 4. Without nonlocal
# -----------------------------

# Without nonlocal, Python creates a new local variable
# inside the inner function instead of changing the outer one.

def update_order_without_nonlocal():
    chai_type = "Elaichi Chai"

    def kitchen():
        chai_type = "Kesar Chai"
        print("Inside kitchen:", chai_type)

    kitchen()

    print("After kitchen update:", chai_type)


update_order_without_nonlocal()

print("-" * 40)


# -----------------------------
# 5. global Keyword
# -----------------------------

# global is used when we want to modify
# a variable from the global scope.

global_chai_type = "Plain Chai"


def front_desk():
    global global_chai_type
    global_chai_type = "Irani Chai"


front_desk()

print("Final global chai:", global_chai_type)

print("-" * 40)


# -----------------------------
# 6. Be Careful with global
# -----------------------------

# Global variables can be changed from anywhere
# if global keyword is used.
# This can make debugging difficult in large programs.

shop_status = "open"


def close_shop():
    global shop_status
    shop_status = "closed"


def print_shop_status():
    print("Shop status:", shop_status)


print_shop_status()
close_shop()
print_shop_status()

print("-" * 40)


# -----------------------------
# Notes
# -----------------------------

# LEGB Rule:
# L = Local
# E = Enclosing
# G = Global
# B = Built-in

# local:
# Variable inside the current function.

# enclosing:
# Variable inside the outer function.

# global:
# Variable outside all functions.

# built-in:
# Python-provided names like print, len, input, type.

# nonlocal:
# Used to modify a variable from an enclosing function.

# global:
# Used to modify a variable from the global scope.

# Best practice:
# Use local variables as much as possible.
# Avoid changing global variables unless necessary.
