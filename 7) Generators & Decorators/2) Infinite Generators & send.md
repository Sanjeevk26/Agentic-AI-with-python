# Python Generators: Infinite Generators and send()

## Overview

This lesson covers two advanced generator concepts:

* Infinite generators
* Sending values into generators using `send()`

Generators produce values one at a time using `yield`. They maintain their own execution state and resume from where they were paused.

---

# 1. Infinite Generators

An infinite generator can continue producing values without a fixed ending point.

It usually contains:

```python
while True:
```

Unlike a normal infinite loop, an infinite generator pauses whenever it reaches `yield`.

## Basic Example

```python
def infinite_chai():
    count = 1

    while True:
        yield f"Refill #{count}"
        count += 1
```

This generator can produce an unlimited number of refill messages.

## Creating the Generator

```python
refill_station = infinite_chai()
```

This does not start an endless loop immediately.

It creates a generator object and stores its current state.

## Requesting Values

```python
print(next(refill_station))
print(next(refill_station))
print(next(refill_station))
```

Output:

```text
Refill #1
Refill #2
Refill #3
```

Each call to `next()`:

1. Resumes the generator
2. Runs until the next `yield`
3. Returns the yielded value
4. Pauses the generator again

## Controlling an Infinite Generator

An infinite generator does not stop on its own, so the caller must control how many values are requested.

```python
refill_station = infinite_chai()

for _ in range(3):
    print(next(refill_station))
```

The underscore `_` is used because the loop variable is not needed.

## Separate Generator Objects

Every generator object maintains its own independent state.

```python
user_one = infinite_chai()
user_two = infinite_chai()
```

Both users start from refill number `1`.

```python
print(next(user_one))
print(next(user_one))

print(next(user_two))
```

Output:

```text
Refill #1
Refill #2
Refill #1
```

The state of `user_one` does not affect `user_two`.

## Common Use Cases

Infinite generators can be useful for:

* Real-time data streams
* Log processing
* Sequence numbers
* Event streams
* Sensor readings
* AI token streaming
* Repeated status updates
* Message queues

An infinite generator itself does not build an infinite collection in memory. However, continuously consuming it without control can use excessive CPU, produce unlimited output, or create memory issues elsewhere in the program.

---

# 2. Sending Data into a Generator

Generators can do more than produce values.

They can also receive values using:

```python
generator.send(value)
```

Inside the generator, the received value is captured using:

```python
value = yield
```

## Chai Customer Example

```python
def chai_customer():
    print("Welcome! What chai would you like?")

    order = yield

    while True:
        print(f"Preparing {order}")
        order = yield
```

Here, the generator pauses at:

```python
order = yield
```

It waits for another part of the program to send an order.

## Priming the Generator

Before sending the first meaningful value, the generator must be started or primed.

```python
stall = chai_customer()
next(stall)
```

This runs the function until the first `yield`.

Output:

```text
Welcome! What chai would you like?
```

The generator is now paused and ready to receive a value.

## Sending the First Order

```python
stall.send("Masala Chai")
```

Output:

```text
Preparing Masala Chai
```

The sent value becomes the result of the paused `yield` expression:

```python
order = yield
```

Therefore:

```python
order = "Masala Chai"
```

## Sending More Orders

```python
stall.send("Lemon Chai")
stall.send("Ginger Chai")
```

Output:

```text
Preparing Lemon Chai
Preparing Ginger Chai
```

After every order, the generator reaches another `yield` and pauses until the next order arrives.

## Why the Second yield Is Required

Consider this incorrect version:

```python
def chai_customer():
    order = yield

    while True:
        print(f"Preparing {order}")
```

After receiving the first order, the `while True` loop runs continuously because there is no new `yield` inside it.

The corrected version pauses during every iteration:

```python
def chai_customer():
    order = yield

    while True:
        print(f"Preparing {order}")
        order = yield
```

## How send() Works

The sequence is:

```text
Create generator
        ↓
Call next() to reach the first yield
        ↓
Generator pauses
        ↓
Call send("Masala Chai")
        ↓
The yield expression receives "Masala Chai"
        ↓
Generator continues running
        ↓
Generator reaches the next yield and pauses again
```

## next() and send(None)

These two statements are commonly equivalent when priming a generator:

```python
next(stall)
```

```python
stall.send(None)
```

A newly created generator cannot normally receive a non-`None` value before reaching its first `yield`.

## Closing a Generator

A generator can be closed when it is no longer needed:

```python
stall.close()
```

After closing, it cannot continue receiving or producing values.

---

# Key Takeaways

* An infinite generator can produce an unlimited sequence of values.
* `while True` creates the continuous behavior.
* `yield` pauses the generator and prevents it from running continuously.
* The caller controls how many generated values are consumed.
* Each generator object maintains separate state.
* `send()` passes a value into a paused generator.
* A generator must be primed before receiving its first non-`None` value.
* `value = yield` captures the value sent into the generator.
* A repeated generator loop needs a `yield` inside it to pause between iterations.
* `close()` stops a generator when it is no longer required.
