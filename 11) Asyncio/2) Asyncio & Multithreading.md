# Python Asyncio with Multithreading

## Overview

Asyncio and multithreading can work together in Python.

Asyncio is not a replacement for threading or multiprocessing. It is another tool used for asynchronous programming, especially for I/O-bound tasks.

Sometimes we already have a normal blocking function, but we want to call it from async code without blocking the event loop.

For this, Python provides tools such as:

* `loop.run_in_executor()`
* `ThreadPoolExecutor`
* `asyncio.to_thread()`

---

# 1. Why Mix Asyncio and Threads?

Asyncio works best when the code is async-aware.

Example:

```python id="nss5l4"
await asyncio.sleep(2)
```

This is non-blocking.

But many existing functions are normal blocking functions.

Example:

```python id="n9g0tr"
time.sleep(3)
```

This blocks the current thread.

If blocking code runs directly inside async code, it can freeze the event loop.

To avoid this, we can run blocking code in a separate thread while asyncio continues managing the event loop.

---

# 2. Blocking Function Example

```python id="c52p1t"
import time


def check_stock(item):
    print(f"Checking {item} in store...")
    time.sleep(3)
    return f"{item} stock: 42"
```

This is a normal function.

It is not async.

It uses:

```python id="mpy85m"
time.sleep(3)
```

which is blocking.

If we call this directly inside async code, the event loop will be blocked.

---

# 3. The Problem

Bad async code:

```python id="g2slja"
async def main():
    result = check_stock("Masala Chai")
    print(result)
```

Even though `main()` is async, `check_stock()` still blocks.

The event loop cannot run other async tasks during `time.sleep(3)`.

---

# 4. ThreadPoolExecutor

Python provides `ThreadPoolExecutor` from `concurrent.futures`.

```python id="v0ckrc"
from concurrent.futures import ThreadPoolExecutor
```

A thread pool manages a group of worker threads.

Instead of manually creating threads, we can submit blocking work to the pool.

---

# 5. Getting the Running Event Loop

Inside an async function, we can get the currently running event loop:

```python id="d29wu3"
loop = asyncio.get_running_loop()
```

The event loop is responsible for scheduling async tasks.

Once we have the loop, we can ask it to run blocking code in an executor.

---

# 6. run_in_executor()

The method is:

```python id="16hnko"
loop.run_in_executor(
    executor,
    function,
    *args
)
```

Example:

```python id="wxjdh6"
result = await loop.run_in_executor(
    pool,
    check_stock,
    "Masala Chai"
)
```

This means:

* Run `check_stock("Masala Chai")`
* Use the thread pool named `pool`
* Do not block the event loop
* Wait asynchronously until the result is ready

---

# 7. Complete Example

```python id="k2bd83"
import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


def check_stock(item):
    print(f"Checking {item} in store...")
    time.sleep(3)
    return f"{item} stock: 42"


async def main():
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool,
            check_stock,
            "Masala Chai",
        )

    print(result)


asyncio.run(main())
```

Output:

```text id="yi7t2h"
Checking Masala Chai in store...
Masala Chai stock: 42
```

---

# 8. Why Use await Here?

This line:

```python id="gtcxem"
result = await loop.run_in_executor(...)
```

waits for the thread result without blocking the event loop.

The blocking function runs in another thread.

The async function pauses until the thread returns a result.

During that pause, the event loop can continue running other async tasks.

---

# 9. Running Multiple Blocking Functions

We can run several blocking functions in the thread pool.

```python id="5clm6v"
async def main():
    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor() as pool:
        tasks = [
            loop.run_in_executor(
                pool,
                check_stock,
                "Masala Chai",
            ),
            loop.run_in_executor(
                pool,
                check_stock,
                "Ginger Chai",
            ),
            loop.run_in_executor(
                pool,
                check_stock,
                "Elaichi Chai",
            ),
        ]

        results = await asyncio.gather(*tasks)

    print(results)
```

Even if each stock check takes 3 seconds, the total time may be close to 3 seconds instead of 9 seconds.

---

# 10. ThreadPoolExecutor as a Context Manager

Use:

```python id="elzwb8"
with ThreadPoolExecutor() as pool:
    ...
```

The parentheses are important.

Correct:

```python id="y4sa8s"
with ThreadPoolExecutor() as pool:
```

Incorrect:

```python id="1q3c94"
with ThreadPoolExecutor as pool:
```

`ThreadPoolExecutor` is a class. We need to create an instance using `()`.

---

# 11. Default Executor

We can also pass `None` as the executor.

```python id="8kz7tk"
result = await loop.run_in_executor(
    None,
    check_stock,
    "Masala Chai",
)
```

When the executor is `None`, asyncio uses the default thread pool executor.

This is useful for simple cases.

---

# 12. asyncio.to_thread()

Modern Python also provides a simpler helper:

```python id="5idv9y"
result = await asyncio.to_thread(
    check_stock,
    "Masala Chai",
)
```

This runs the blocking function in a separate thread.

It is often easier to read than `run_in_executor()`.

Example:

```python id="qz9j1j"
async def main():
    result = await asyncio.to_thread(
        check_stock,
        "Masala Chai",
    )

    print(result)
```

---

# 13. run_in_executor() vs asyncio.to_thread()

| Feature                       | `run_in_executor()` | `asyncio.to_thread()` |
| ----------------------------- | ------------------- | --------------------- |
| More control                  | Yes                 | Less                  |
| Can use custom executor       | Yes                 | Not directly          |
| Simpler syntax                | No                  | Yes                   |
| Good for advanced cases       | Yes                 | Basic use cases       |
| Good for quick thread offload | Yes                 | Yes                   |

Use `asyncio.to_thread()` for simple cases.

Use `run_in_executor()` when you need more control over the executor.

---

# 14. When This Pattern Is Useful

This pattern is useful when async code must call blocking functions such as:

* Old database libraries
* File operations
* Legacy APIs
* Blocking SDKs
* Slow calculations that are not too CPU-heavy
* Existing synchronous helper functions

It helps async applications stay responsive.

---

# 15. Important Warning

Running blocking code in a thread is useful, but it is not always the best solution.

For CPU-heavy work, threads may still be limited by the GIL.

For CPU-heavy pure Python tasks, consider:

* `multiprocessing`
* `ProcessPoolExecutor`
* Native libraries that release the GIL

For I/O-heavy blocking functions, thread executors are usually useful.

---

# 16. Asyncio + Threading Flow

```text id="9091r7"
Async function starts
        ↓
Gets running event loop
        ↓
Creates or uses thread pool
        ↓
Sends blocking function to thread
        ↓
Async function awaits result
        ↓
Event loop can run other tasks
        ↓
Thread completes work
        ↓
Result returns to async function
```

---

# 17. Common Mistakes

## Forgetting Parentheses

Incorrect:

```python id="rz6anv"
with ThreadPoolExecutor as pool:
```

Correct:

```python id="xl8fwk"
with ThreadPoolExecutor() as pool:
```

## Calling the Function Immediately

Incorrect:

```python id="vvc99h"
await loop.run_in_executor(
    pool,
    check_stock("Masala Chai"),
)
```

Correct:

```python id="gqfjtn"
await loop.run_in_executor(
    pool,
    check_stock,
    "Masala Chai",
)
```

The function name and arguments are passed separately.

## Using time.sleep() Directly in async Code

Incorrect:

```python id="ogskkk"
async def main():
    time.sleep(3)
```

Correct:

```
async def main():
    await asyncio.sleep(3)
```

Or, for a blocking existing function:

```python id="pl0ziz"
await asyncio.to_thread(blocking_function)
```

---

# Key Takeaways

* Asyncio and multithreading can work together.
* Asyncio is not a replacement for threading or multiprocessing.
* Blocking functions can freeze the event loop.
* `ThreadPoolExecutor` runs blocking functions in worker threads.
* `asyncio.get_running_loop()` gets the active event loop.
* `loop.run_in_executor()` runs blocking code outside the event loop thread.
* `await` waits for the result without blocking the event loop.
* `asyncio.gather()` can collect multiple executor results.
* `asyncio.to_thread()` is a simpler way to run blocking functions in a thread.
* Use this pattern mainly for blocking I/O work.
* For CPU-heavy pure Python work, multiprocessing is usually better.
