# Python Functions

## Overview

Functions are reusable blocks of code.

They help us wrap logic into a named block so that the same code can be used multiple times without repeating it.

Functions make code:

* Reusable
* Modular
* Readable
* Maintainable
* Easier to debug
* Easier to trace

## Why Functions Are Needed

Without functions, we may write the same code again and again.

With functions, we write the logic once and call it whenever needed.

## Defining a Function

In Python, functions are created using the `def` keyword.

```python
def function_name():
    # code goes here
```

Example:

```python
def say_hello():
    print("Hello")
```

To run a function, we call it using its name:

```python
say_hello()
```

## Parameters and Arguments

A function can accept values.

Values written inside the function definition are called **parameters**.

```python
def print_order(name, chai_type):
    print(f"{name} ordered {chai_type} chai")
```

Here:

* `name` is a parameter
* `chai_type` is a parameter

Values passed while calling the function are called **arguments**.

```python
print_order("Aman", "Masala")
```

Here:

* `"Aman"` is an argument
* `"Masala"` is an argument

## 1. Reducing Code Duplication

Functions reduce repeated code.

### Example

```python
def print_order(name, chai_type):
    print(f"{name} ordered {chai_type} chai!")
```

Now we can call it multiple times:

```python
print_order("Aman", "Masala")
print_order("Hitesh", "Ginger")
print_order("Jia", "Tulsi")
```

If we want to change the message format, we only change it inside the function.

## 2. Splitting Complex Tasks

Functions help break a large task into smaller steps.

### Example

A cafe wants to generate a monthly sales report.

Instead of putting everything in one place, we can create separate functions:

```python
def fetch_sales():
    print("Fetching sales data")

def filter_valid_sales():
    print("Filtering valid sales data")

def summarize_sales():
    print("Summarizing sales data")

def generate_report():
    fetch_sales()
    filter_valid_sales()
    summarize_sales()
    print("Report is ready")
```

This makes the program easier to understand and manage.

## 3. Hiding Implementation Details

Functions hide internal complexity.

The user of the function only needs to know what the function does, not how it does it.

### Example

```python
def get_user_input():
    print("Getting user input")

def validate_user_info():
    print("Validating user info")

def save_to_db():
    print("Saving to database")

def register_user():
    get_user_input()
    validate_user_info()
    save_to_db()
    print("User registration complete")
```

Here, `register_user()` clearly shows the workflow.

The complex logic inside each step can be handled separately.

## 4. Improving Readability

Well-named functions make code easy to read.

Example:

```python
def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup
```

The function name clearly tells us what it does.

## print vs return

`print()` only displays output.

`return` sends a value back from the function.

### Using print

```python
def show_bill():
    print(45)
```

This only prints the value.

### Using return

```python
def calculate_bill(cups, price_per_cup):
    return cups * price_per_cup
```

Now the returned value can be stored in a variable:

```python
bill = calculate_bill(3, 15)
print(bill)
```

Output:

```text
45
```

## 5. Improving Traceability

Functions help keep important logic in one place.

Example: adding 10% VAT to every order.

```python
def add_vat(price, vat_rate):
    return price * (100 + vat_rate) / 100
```

Now the same VAT logic can be reused everywhere.

```python
orders = [100, 150, 200]

for price in orders:
    final_amount = add_vat(price, 10)
    print(f"Original: {price}, Final with VAT: {final_amount}")
```

If the VAT formula changes, we only update the function once.

## Good Function Naming

Function names should clearly describe what they do.

Good examples:

```python
calculate_bill()
generate_report()
save_to_db()
validate_user_info()
```

Avoid unclear names like:

```python
do_work()
process()
thing()
```

## Key Takeaways

* Functions are reusable blocks of code.
* Use `def` to create a function.
* Parameters are defined inside the function.
* Arguments are passed while calling the function.
* Functions reduce code duplication.
* Functions help split complex tasks.
* Functions improve readability and maintainability.
* `print()` displays output.
* `return` gives a value back.
* Well-named functions make code easier to understand.
