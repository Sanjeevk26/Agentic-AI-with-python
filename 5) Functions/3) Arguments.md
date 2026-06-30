# Python Functions: Parameters, Arguments, args, kwargs, and Default Values

## Overview

This lecture explains how values are passed into Python functions.

It covers:

* Parameters
* Arguments
* Mutable and immutable values
* Positional arguments
* Keyword arguments
* `*args`
* `**kwargs`
* Default parameter values
* Default mutable argument trap

## Function Parameters

Parameters are placeholders written inside a function definition.

```python
def prepare_chai(order):
    print(f"Preparing {order}")
```

Here, `order` is a parameter.

## Function Arguments

Arguments are actual values passed while calling the function.

```python
chai = "Ginger Chai"

prepare_chai(chai)
```

Here, `chai` is passed as an argument.

## Passing Immutable Values

Strings are immutable.

That means they cannot be changed directly.

Example:

```python
chai = "Ginger Chai"

def prepare_chai(order):
    print(f"Preparing {order}")

prepare_chai(chai)

print(chai)
```

Output:

```text
Preparing Ginger Chai
Ginger Chai
```

The original value of `chai` does not change.

## Passing Mutable Values

Lists are mutable.

That means they can be changed.

Example:

```python
chai = [1, 2, 3]

def edit_chai(cups):
    cups[1] = 42

edit_chai(chai)

print(chai)
```

Output:

```text
[1, 42, 3]
```

The original list changes because lists are mutable.

## Positional Arguments

Positional arguments are passed based on position.

```python
def make_chai(tea, milk, sugar):
    print(tea, milk, sugar)

make_chai("Darjeeling", "yes", "low")
```

Here:

```text
tea   -> Darjeeling
milk  -> yes
sugar -> low
```

The order matters.

## Keyword Arguments

Keyword arguments are passed using parameter names.

```python
make_chai(tea="Green", sugar="medium", milk="no")
```

Here, order does not matter because values are assigned by name.

```text
tea   -> Green
milk  -> no
sugar -> medium
```

## *args

`*args` is used when we want to accept multiple positional arguments.

Example:

```python
def special_chai(*ingredients):
    print(ingredients)

special_chai("cinnamon", "cardamom")
```

Output:

```text
('cinnamon', 'cardamom')
```

`*args` collects values into a tuple.

The name `args` is common, but we can use any valid name.

Example:

```python
def special_chai(*ingredients):
    print(ingredients)
```

## **kwargs

`**kwargs` is used when we want to accept multiple keyword arguments.

Example:

```python
def special_chai(**extras):
    print(extras)

special_chai(sweetener="honey", foam="yes")
```

Output:

```text
{'sweetener': 'honey', 'foam': 'yes'}
```

`**kwargs` collects values into a dictionary.

The name `kwargs` is common, but we can use any valid name.

## Using *args and **kwargs Together

```python
def special_chai(*ingredients, **extras):
    print("Ingredients:", ingredients)
    print("Extras:", extras)

special_chai("cinnamon", "cardamom", sweetener="honey", foam="yes")
```

Output:

```text
Ingredients: ('cinnamon', 'cardamom')
Extras: {'sweetener': 'honey', 'foam': 'yes'}
```

Here:

* Values without names go into `ingredients`
* Values with names go into `extras`

## Default Parameter Values

A function can have default values.

```python
def chai_order(order="Masala Chai"):
    print(order)

chai_order()
chai_order("Ginger Chai")
```

Output:

```text
Masala Chai
Ginger Chai
```

If no value is passed, the default value is used.

## Default Mutable Argument Trap

Be careful when using a mutable value like a list as a default parameter.

Bad example:

```python
def chai_order(order=[]):
    order.append("Masala Chai")
    print(order)

chai_order()
chai_order()
```

Output:

```text
['Masala Chai']
['Masala Chai', 'Masala Chai']
```

This happens because the same list is reused every time the function is called.

## Safer Approach

Use `None` as the default value.

```python
def chai_order(order=None):
    if order is None:
        order = []

    order.append("Masala Chai")
    print(order)

chai_order()
chai_order()
```

Output:

```text
['Masala Chai']
['Masala Chai']
```

Now a new list is created every time no value is passed.

## Key Takeaways

* Parameters are placeholders in function definitions.
* Arguments are actual values passed to functions.
* Strings are immutable, so original strings do not change.
* Lists are mutable, so original lists can change.
* Positional arguments depend on order.
* Keyword arguments depend on names.
* `*args` collects positional arguments into a tuple.
* `**kwargs` collects keyword arguments into a dictionary.
* Avoid using mutable values like lists as default parameters.
* Use `None` as a safe default when working with lists or dictionaries.
