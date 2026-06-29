This covers three important loop control concepts in Python:

* `continue`
* `break`
* `for-else`

These are used to control how loops behave while running.

## Why Loop Control Is Needed

Sometimes we do not want a loop to run normally for every item.

Examples:

* Skip an item if it is out of stock
* Stop the loop if a restricted or discontinued item is found
* Run fallback logic if nothing useful was found

Python gives us keywords like `continue` and `break` for this.

## continue Keyword

The `continue` keyword skips the current loop iteration and moves to the next item.

It does not stop the whole loop.

### Example Use Case

Some chai flavors are out of stock.

If the flavor is `"out of stock"`, skip it and continue checking the next flavor.

```python id="hw8jqd"
if flavor == "out of stock":
    continue
```

## break Keyword

The `break` keyword stops the loop completely.

Once `break` runs, Python exits the loop immediately.

### Example Use Case

If a discontinued flavor is found, stop processing all further flavors.

```python id="gtvfwr"
if flavor == "discontinued":
    break
```

## Mini Project 1: Chai Flavor Availability

### Problem

Some chai flavors are out of stock.

We want to:

* Skip flavors that are out of stock
* Stop completely if a discontinued flavor is found
* Print available flavors only

### Code Concept

```python id="njs1c9"
flavors = ["ginger", "out of stock", "lemon", "discontinued", "tulsi"]

for flavor in flavors:
    if flavor == "out of stock":
        continue

    if flavor == "discontinued":
        print("Discontinued item found.")
        break

    print(f"{flavor} item found.")

print("Outside of loop.")
```

### Output

```text id="9ry3ib"
ginger item found.
lemon item found.
Discontinued item found.
Outside of loop.
```

## How the Loop Works

Given this list:

```python id="ijz19c"
flavors = ["ginger", "out of stock", "lemon", "discontinued", "tulsi"]
```

Python checks each item:

| Flavor       | Action                                   |
| ------------ | ---------------------------------------- |
| ginger       | Print item                               |
| out of stock | Skip using `continue`                    |
| lemon        | Print item                               |
| discontinued | Print warning and stop using `break`     |
| tulsi        | Not reached because loop already stopped |

## Importance of Indentation

Indentation controls which block the code belongs to.

Example:

```python id="j39m38"
for flavor in flavors:
    if flavor == "out of stock":
        continue

    print(f"{flavor} item found.")
```

Here, `print()` is inside the loop but outside the `if`.

That means it runs for every item except the skipped ones.

## for-else in Python

Python also supports `else` with a `for` loop.

This is different from `if-else`.

The `else` block runs only when the loop completes normally without hitting `break`.

## Mini Project 2: Staff Eligibility Check

### Problem

We have a list of staff members with their ages.

We want to find the first staff member eligible to manage the store.

If nobody is eligible, print a fallback message.

### Code Concept

```python id="ws771z"
staff = [
    ("Amit", 16),
    ("Zara", 17),
    ("Raj", 15)
]

for name, age in staff:
    if age >= 18:
        print(f"{name} is eligible to manage the staff.")
        break
else:
    print("No one is eligible to manage the staff.")
```

### Output

```text id="htw8iy"
No one is eligible to manage the staff.
```

## How for-else Works

The `else` block runs only if the loop does not break.

Example:

```python id="q4yz1l"
for item in items:
    if condition:
        break
else:
    print("Nothing matched.")
```

This is useful when searching for something.

## When for-else Is Useful

Use `for-else` when:

* Searching for a matching item
* Checking eligibility
* Finding a valid record
* Running fallback logic if nothing is found

## Key Takeaways

* `continue` skips the current iteration.
* `break` stops the entire loop.
* Code after `break` inside the loop does not run.
* Indentation decides whether code is inside the loop, inside an `if`, or outside both.
* `for-else` is used for fallback logic.
* The `else` block of a loop runs only if the loop finishes without `break`.
