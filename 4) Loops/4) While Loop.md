## While Loop Overview

This lecture introduces the `while` loop in Python.

A `while` loop is used when we want to repeat a task until a condition becomes false.

## What is a while Loop?

A `while` loop keeps running as long as the condition is true.

Basic syntax:

```python
while condition:
    # code to repeat
```

Example:

```python
temperature = 40

while temperature < 100:
    print(temperature)
    temperature += 15
```

The loop continues until `temperature` becomes `100` or more.

## for Loop vs while Loop

| Loop Type    | Best Used When                               |
| ------------ | -------------------------------------------- |
| `for` loop   | We know the sequence or number of iterations |
| `while` loop | We repeat until a condition changes          |

Example:

Use `for` when looping through:

```python
range(1, 10)
```

Use `while` when checking a condition like:

```python
temperature < 100
```

## Mini Project: Tea Heating Simulation

### Problem Statement

We want to simulate tea heating.

Rules:

* Temperature starts at `40°C`
* Tea boils at `100°C`
* Increase temperature by `15°C` each step
* Print every temperature step
* Stop when temperature reaches or exceeds `100°C`

## Code Logic

```text
Start temperature = 40

While temperature is less than 100:
    Print current temperature
    Increase temperature by 15

Print final message
```

## while Loop Example

```python
temperature = 40

while temperature < 100:
    print(f"Current temperature: {temperature}")
    temperature += 15

print("Tea is ready to boil.")
```

## Output

```text
Current temperature: 40
Current temperature: 55
Current temperature: 70
Current temperature: 85
Tea is ready to boil.
```

## Incrementing a Value

This line increases the temperature by `15`:

```python
temperature = temperature + 15
```

Python also provides a shorter version:

```python
temperature += 15
```

Both mean the same thing.

## Why Order Matters

If we print the temperature before increasing it:

```python
print(temperature)
temperature += 15
```

The output starts from `40`.

If we increase first and print later:

```python
temperature += 15
print(temperature)
```

The output starts from `55`.

So, the order of code execution matters.

## Important Notes

* `while` loop depends on a condition.
* The condition must eventually become false.
* If the condition never becomes false, the loop may run forever.
* Updating the variable inside the loop is important.
* Indentation decides what code belongs inside the loop.

## Key Takeaways

* `while` loop repeats code while a condition is true.
* It is useful when we do not know the exact number of repetitions in advance.
* `temperature += 15` is shorthand for `temperature = temperature + 15`.
* Code order affects the output.
* Always make sure the loop condition will eventually stop.
