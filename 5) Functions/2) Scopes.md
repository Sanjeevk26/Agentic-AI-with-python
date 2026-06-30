# Python Function Scopes: Local, Enclosing, Global, nonlocal and global

## Overview

Scope means the area where a variable can be accessed.

In Python, the same variable name can exist in different places, but each one may belong to a different scope.

This is also called **name resolution**.

Python decides which variable to use based on where the variable is created and where it is accessed.

## Why Scope Matters

Imagine a chai cafe where every team member has their own notepad.

One person writing an order in their own notepad does not change another person's notepad.

Similarly, a variable created inside a function does not automatically affect a variable outside the function.

## Types of Scope in Python

Python mainly follows this scope order:

```text
Local -> Enclosing -> Global -> Built-in
```

This is also called the **LEGB Rule**.

## 1. Local Scope

A variable created inside a function belongs to the local scope.

It can only be used inside that function.

```python
def serve_chai():
    chai_type = "Masala Chai"
    print(chai_type)
```

Here, `chai_type` exists only inside `serve_chai()`.

## Local and Global Variable with Same Name

```python
chai_type = "Lemon Chai"

def serve_chai():
    chai_type = "Masala Chai"
    print("Inside function:", chai_type)

serve_chai()
print("Outside function:", chai_type)
```

Output:

```text
Inside function: Masala Chai
Outside function: Lemon Chai
```

The inside variable and outside variable are different, even though they have the same name.

## 2. Enclosing Scope

Enclosing scope happens when one function is defined inside another function.

The inner function can access variables from the outer function.

```python
def chai_counter():
    chai_order = "Lemon Chai"

    def print_order():
        print("Inner:", chai_order)

    print_order()
    print("Outer:", chai_order)
```

Here, `print_order()` can access `chai_order` from `chai_counter()`.

## 3. Global Scope

A variable created outside all functions belongs to the global scope.

```python
chai_order = "Tulsi Chai"

def chai_counter():
    print(chai_order)

chai_counter()
```

Global variables can be accessed inside functions, but changing them directly requires the `global` keyword.

## 4. Built-in Scope

Built-in scope contains names already provided by Python.

Examples:

```python
print()
len()
type()
input()
```

These are available everywhere unless overwritten, which should be avoided.

## nonlocal Keyword

The `nonlocal` keyword is used inside a nested function to modify a variable from the enclosing function.

```python
def update_order():
    chai_type = "Elaichi Chai"

    def kitchen():
        nonlocal chai_type
        chai_type = "Kesar Chai"

    kitchen()
    print(chai_type)

update_order()
```

Output:

```text
Kesar Chai
```

Without `nonlocal`, Python would create a new local variable inside `kitchen()` instead of updating the outer one.

## global Keyword

The `global` keyword is used to modify a variable from the global scope.

```python
chai_type = "Plain Chai"

def front_desk():
    global chai_type
    chai_type = "Irani Chai"

front_desk()
print(chai_type)
```

Output:

```text
Irani Chai
```

## Difference Between nonlocal and global

| Keyword    | Used For                                   |
| ---------- | ------------------------------------------ |
| `nonlocal` | Accessing variable from enclosing function |
| `global`   | Accessing variable from global scope       |

## Be Careful with global

Using `global` can make code risky.

If multiple functions change the same global variable, it can create bugs.

Example:

```text
Function A expects chai_type to be True
Function B changes chai_type to "Ginger Chai"
Function A may break
```

So, use `global` only when really needed.

## Key Takeaways

* Scope decides where a variable can be accessed.
* Local variables exist inside a function.
* Enclosing variables exist in outer functions.
* Global variables exist outside all functions.
* Built-in names are provided by Python.
* Python follows the LEGB rule.
* `nonlocal` modifies variables from an enclosing function.
* `global` modifies variables from the global scope.
* Avoid overusing global variables because they can make code harder to debug.
