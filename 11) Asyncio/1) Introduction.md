# Python Asyncio: Asynchronous Programming Basics

## Overview

Asynchronous programming allows Python to handle many waiting-heavy tasks efficiently without creating many threads or processes.

It is especially useful for I/O-bound work such as:

* API calls
* Database queries
* File operations
* Network requests
* Web server requests
* Waiting for external systems

Frameworks like FastAPI use asynchronous programming heavily to handle many requests efficiently.

---

# 1. Why Async Programming?

In normal synchronous code, one operation blocks the next operation.

Example:

```text id="ot0wyr"
Task 1 starts
Task 1 waits
Task 1 finishes
Task 2 starts
Task 2 waits
Task 2 finishes
```

If each task waits for 2 seconds, three tasks may take around 6 seconds.

With async programming, waiting time can overlap.

```text id="uwp9t3"
Task 1 starts waiting
Task 2 starts waiting
Task 3 starts waiting
All complete around the same time
```

This is useful when the program spends time waiting rather than calculating.

---

# 2. Async Is Not the Same as Multiprocessing

Multiprocessing creates separate processes.

Each process has its own:

* Python interpreter
* Memory
* GIL
* Process ID

Asyncio does not need to create new processes for every task.

It works mainly through:

* Coroutines
* `await`
* Event loop
* Cooperative scheduling

Asyncio is lightweight compared to multiprocessing when the task is I/O-bound.

---

# 3. Async Is Not the Same as Threading

Threading creates multiple threads inside the same process.

Asyncio usually runs many tasks in a single thread using an event loop.

| Threading                    | Asyncio                          |
| ---------------------------- | -------------------------------- |
| Uses multiple threads        | Usually uses one main thread     |
| OS schedules threads         | Event loop schedules coroutines  |
| Good for I/O-bound tasks     | Good for I/O-bound tasks         |
| Shared-state issues possible | Fewer shared-state problems      |
| Uses `threading.Thread`      | Uses `async`, `await`, `asyncio` |

---

# 4. Blocking vs Non-Blocking Code

## Blocking Code

Blocking code stops the current flow until the operation completes.

```python id="ve6evz"
import time

time.sleep(2)
```

During `time.sleep(2)`, the current thread is blocked.

## Non-Blocking Async Code

```python id="igbifb"
import asyncio

await asyncio.sleep(2)
```

This pauses the coroutine, but allows the event loop to run other coroutines while waiting.

This is one of the most important ideas in async programming.

---

# 5. Coroutine

A coroutine is a special function that can pause and resume.

Create a coroutine using:

```python id="aec0s0"
async def function_name():
    pass
```

Example:

```python id="ojkmyt"
async def brew_chai():
    print("Brewing chai...")
    await asyncio.sleep(2)
    print("Chai is ready")
```

The keyword `async` creates a coroutine function.

---

# 6. async def

A normal function is defined using:

```python id="j5rtyf"
def brew_chai():
    pass
```

An async function is defined using:

```python id="cpum85"
async def brew_chai():
    pass
```

Calling an async function does not immediately execute it like a normal function.

It returns a coroutine object.

```python id="hzvjfh"
coroutine = brew_chai()
```

To run it, use an event loop.

---

# 7. asyncio.run()

`asyncio.run()` starts an event loop and runs the given coroutine.

```python id="38hkzt"
import asyncio


async def brew_chai():
    print("Brewing chai...")
    await asyncio.sleep(2)
    print("Chai is ready")


asyncio.run(brew_chai())
```

Output:

```text id="sus0ac"
Brewing chai...
Chai is ready
```

`asyncio.run()` is commonly used as the entry point for async programs.

---

# 8. await

`await` pauses the current coroutine until the awaited operation completes.

```python id="aowuuf"
await asyncio.sleep(2)
```

Important rule:

```text id="2p8h04"
await can only be used inside async def.
```

This is invalid:

```python id="v6efvz"
def normal_function():
    await asyncio.sleep(2)
```

This is valid:

```python id="fzd0w9"
async def async_function():
    await asyncio.sleep(2)
```

---

# 9. Event Loop

The event loop is the engine that runs async tasks.

It:

* Schedules coroutines
* Pauses coroutines when they await
* Resumes coroutines when results are ready
* Manages async task execution
* Helps avoid blocking the main flow

Simple idea:

```text id="wp6qi8"
Coroutine starts
    ↓
Coroutine reaches await
    ↓
Event loop pauses it
    ↓
Other coroutine runs
    ↓
Result is ready
    ↓
Event loop resumes first coroutine
```

---

# 10. First Async Example

```python id="ivv2yj"
import asyncio


async def brew_chai():
    print("Brewing chai...")
    await asyncio.sleep(2)
    print("Chai is ready")


asyncio.run(brew_chai())
```

Here:

* `async def` defines a coroutine
* `await asyncio.sleep(2)` pauses without blocking the event loop
* `asyncio.run()` runs the coroutine

---

# 11. Running Multiple Coroutines

Use `asyncio.gather()` to run multiple coroutines concurrently.

```python id="xectki"
import asyncio


async def brew(chai_name):
    print(f"Brewing {chai_name}...")
    await asyncio.sleep(2)
    print(f"{chai_name} is ready")


async def main():
    await asyncio.gather(
        brew("Masala Chai"),
        brew("Green Chai"),
        brew("Ginger Chai"),
    )


asyncio.run(main())
```

Even though each coroutine waits for 2 seconds, the total time is close to 2 seconds, not 6 seconds.

---

# 12. Why gather() Is Useful

`asyncio.gather()` waits for multiple awaitable objects.

```python id="n2qmkz"
await asyncio.gather(
    task_one(),
    task_two(),
    task_three(),
)
```

It schedules them concurrently and waits until all are complete.

The order of actual execution may vary, but the returned results are in the same order as the awaitables passed to `gather()`.

---

# 13. Blocking Sleep vs Async Sleep

## Blocking Version

```python id="kux87h"
import time


async def brew(chai_name):
    print(f"Brewing {chai_name}...")
    time.sleep(2)
    print(f"{chai_name} is ready")
```

Even though the function is marked `async`, `time.sleep(2)` blocks the thread.

This makes the coroutines run one after another.

## Non-Blocking Version

```python id="vi0lrl"
import asyncio


async def brew(chai_name):
    print(f"Brewing {chai_name}...")
    await asyncio.sleep(2)
    print(f"{chai_name} is ready")
```

This allows other coroutines to run while one coroutine is waiting.

---

# 14. Async HTTP Requests

For async HTTP requests, a common third-party library is:

```text id="y9xbb5"
aiohttp
```

Install it using:

```bash id="7e0563"
pip install aiohttp
```

Basic example:

```python id="yx57j9"
import aiohttp
import asyncio


async def fetch_url(session, url):
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")


async def main():
    async with aiohttp.ClientSession() as session:
        await fetch_url(
            session,
            "https://httpbin.org/delay/2",
        )


asyncio.run(main())
```

The request waits for the server response without blocking the whole event loop.

---

# 15. Running Multiple Async HTTP Requests

```python id="dnb7bj"
import aiohttp
import asyncio


async def fetch_url(session, url):
    async with session.get(url) as response:
        print(f"Fetched {url} with status {response.status}")


async def main():
    urls = [
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/2",
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_url(session, url)
            for url in urls
        ]

        await asyncio.gather(*tasks)


asyncio.run(main())
```

Even though each URL waits for 2 seconds, the total time is close to 2 seconds because the requests are concurrent.

---

# 16. What Does *tasks Mean?

Suppose we have:

```python id="cun35n"
tasks = [
    task_one(),
    task_two(),
    task_three(),
]
```

`asyncio.gather()` expects separate arguments:

```python id="7bm1es"
await asyncio.gather(
    task_one(),
    task_two(),
    task_three(),
)
```

Instead of writing each task manually, use unpacking:

```python id="g3n1f4"
await asyncio.gather(*tasks)
```

The `*` unpacks the list.

This:

```python id="wfh99e"
await asyncio.gather(*tasks)
```

is similar to:

```python id="xurpy4"
await asyncio.gather(
    tasks[0],
    tasks[1],
    tasks[2],
)
```

---

# 17. Async Context Manager

In aiohttp, this syntax is common:

```python id="y9xvwq"
async with aiohttp.ClientSession() as session:
    ...
```

and:

```python id="7ypp5b"
async with session.get(url) as response:
    ...
```

`async with` is used when entering or exiting a context may involve asynchronous operations.

Examples:

* Opening async network sessions
* Waiting for async cleanup
* Closing async connections

---

# 18. What Asyncio Is Good For

Asyncio is useful for I/O-bound operations such as:

* Fetching many web pages
* Sending many API requests
* Handling many web users
* Waiting for database responses
* Managing network connections
* Running async web servers

It is not mainly for CPU-heavy calculation.

---

# 19. What Asyncio Is Not Good For

Asyncio does not automatically speed up CPU-heavy work.

CPU-heavy work includes:

* Large mathematical loops
* Image processing
* Video processing
* Compression
* Heavy data transformations

For CPU-heavy pure Python work, consider:

* `multiprocessing`
* `ProcessPoolExecutor`
* Native libraries that release the GIL

---

# 20. Common Mistakes

## Using await Outside async def

Incorrect:

```python id="ueqj4z"
await asyncio.sleep(2)
```

Correct:

```python id="n3n08k"
async def main():
    await asyncio.sleep(2)
```

## Forgetting asyncio.run()

Incorrect:

```python id="bosc47"
brew_chai()
```

This creates a coroutine but does not run it.

Correct:

```python id="gen3zh"
asyncio.run(brew_chai())
```

## Using time.sleep() Inside async def

Incorrect:

```python id="8alr0p"
async def main():
    time.sleep(2)
```

Correct:

```python id="xepwcw"
async def main():
    await asyncio.sleep(2)
```

## Forgetting * When Passing a List to gather()

Incorrect:

```python id="2t1j81"
await asyncio.gather(tasks)
```

Correct:

```python 
await asyncio.gather(*tasks)
```

---

# 21. Async Flow Summary

```text id="8i7c9o"
async def creates a coroutine
        ↓
await pauses a coroutine
        ↓
event loop runs other tasks
        ↓
awaited operation completes
        ↓
event loop resumes coroutine
        ↓
asyncio.gather runs many coroutines together
```

---

# Key Takeaways

* Asyncio is used for asynchronous programming in Python.
* Asyncio is best suited for I/O-bound work.
* `async def` defines a coroutine function.
* A coroutine can pause and resume.
* `await` pauses the coroutine until a result is ready.
* `await` can only be used inside `async def`.
* `asyncio.run()` starts the event loop and runs a coroutine.
* `asyncio.sleep()` is non-blocking.
* `time.sleep()` is blocking.
* `asyncio.gather()` runs multiple coroutines concurrently.
* `*tasks` unpacks a list of tasks into separate arguments.
* `async with` is used for asynchronous context managers.
* Asyncio improves scalability without creating many threads or processes.
* Asyncio does not automatically speed up CPU-heavy code.
