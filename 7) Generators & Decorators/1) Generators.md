# Python Generators: Basics, yield, and next()

## Overview

Generators are a memory-efficient way to produce values one at a time.

They are similar to functions, but instead of using `return`, generators use the `yield` keyword.

Generators are useful when:

* Working with large amounts of data
* Processing values one at a time
* Saving memory
* Delaying calculations until needed
* Streaming data
* Reading large files or database results

## Functions vs Generators

A normal function usually calculates and returns its result immediately.

```python
def get_chai_list():
    return ["cup 1", "cup 2", "cup 3"]
```

This creates the entire list in memory.

A generator produces one value at a time.

```python
def get_chai_generator():
    yield "cup 1"
    yield "cup 2"
    yield "cup 3"
```

The values are generated only when requested.

## The yield Keyword

The `yield` keyword:

* Produces one value
* Pauses the function
* Remembers the current position
* Resumes from the same position when called again

Example:

```python
def serve_chai():
    yield "Masala Chai"
    yield "Ginger Chai"
    yield "Elaichi Chai"
```

Calling the generator does not immediately execute all its code.

```python
stall = serve_chai()
```

`stall` stores a generator object.

## Generator Object

```python
stall = serve_chai()
print(stall)
```

The output will look similar to:

```text
<generator object serve_chai at ...>
```

This means Python has created a generator object, but its values have not yet been fully processed.

## Using a Generator with a for Loop

A `for` loop automatically requests values from the generator one at a time.

```python
def serve_chai():
    yield "Masala Chai"
    yield "Ginger Chai"
    yield "Elaichi Chai"

stall = serve_chai()

for cup in stall:
    print(cup)
```

Output:

```text
Masala Chai
Ginger Chai
Elaichi Chai
```

## Using next()

The built-in `next()` function manually requests the next value from a generator.

```python
chai = serve_chai()

print(next(chai))
print(next(chai))
print(next(chai))
```

Output:

```text
Masala Chai
Ginger Chai
Elaichi Chai
```

Each call resumes the generator from where it was previously paused.

## StopIteration

When a generator has no more values to produce, calling `next()` again raises a `StopIteration` exception.

```python
chai = serve_chai()

print(next(chai))
print(next(chai))
print(next(chai))
print(next(chai))
```

The fourth call produces:

```text
StopIteration
```

A `for` loop handles this automatically, so we normally do not see the exception.

## Lazy Evaluation

Generators use lazy evaluation.

Lazy evaluation means values are calculated only when they are requested.

Example:

```python
def serve_chai():
    print("Preparing first cup")
    yield "Masala Chai"

    print("Preparing second cup")
    yield "Ginger Chai"
```

Creating the generator does not print anything:

```python
stall = serve_chai()
```

The first part runs only after:

```python
next(stall)
```

## Generator State

A generator remembers:

* Its current position
* Its local variables
* Where execution was paused
* Which value should be produced next

This is why it can resume instead of restarting from the beginning.

## Return vs yield

| `return`                    | `yield`                              |
| --------------------------- | ------------------------------------ |
| Ends the function           | Pauses the function                  |
| Returns one final result    | Produces values one at a time        |
| Does not resume             | Resumes from the paused position     |
| Common in normal functions  | Used in generator functions          |
| May create full collections | Supports memory-efficient processing |

## Important Generator Behaviour

A generator is normally consumed only once.

```python
chai = serve_chai()

for cup in chai:
    print(cup)

for cup in chai:
    print(cup)
```

The second loop prints nothing because the generator has already been exhausted.

To use it again, create a new generator object:

```python
chai = serve_chai()
```

## Key Takeaways

* Generators produce values one at a time.
* Generator functions use `yield`.
* Calling a generator function creates a generator object.
* `yield` pauses the function instead of ending it.
* `next()` requests the next generated value.
* A generator resumes from where it was paused.
* `StopIteration` occurs when no more values are available.
* `for` loops handle `StopIteration` automatically.
* Generators use lazy evaluation.
* Generators are useful for memory-efficient processing.
