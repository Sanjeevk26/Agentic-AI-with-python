# Python Asyncio with Multiprocessing and Background Threads

## Overview

Asyncio can work with both:

* Multithreading
* Multiprocessing

Asyncio is not a replacement for threading or multiprocessing. It is another concurrency tool.

Sometimes an async application needs to run:

* Blocking I/O work in a separate thread
* CPU-heavy work in a separate process
* Background logging or monitoring alongside async tasks

Python provides tools to combine these approaches safely.

---

# 1. Why Combine Asyncio with Multiprocessing?

Asyncio is excellent for I/O-bound tasks such as:

* API calls
* Database queries
* Network requests
* File I/O with async libraries
* Web server request handling

But asyncio does not automatically speed up CPU-heavy work.

CPU-heavy work includes:

* Encryption
* Image processing
* Video processing
* Machine learning inference
* Mathematical calculations
* Large data transformations

For CPU-heavy work, multiprocessing is often better because it can run code in separate processes.

---

# 2. ThreadPoolExecutor vs ProcessPoolExecutor

Python provides executors in the `concurrent.futures` module.

```python id="5gfzou"
from concurrent.futures import ThreadPoolExecutor
from concurrent.futures import ProcessPoolExecutor
```

| Executor              | Best for          |
| --------------------- | ----------------- |
| `ThreadPoolExecutor`  | Blocking I/O work |
| `ProcessPoolExecutor` | CPU-heavy work    |

---

# 3. run_in_executor()

Asyncio provides:

```python id="48575c"
loop.run_in_executor()
```

It allows async code to run a normal blocking function in:

* A thread pool
* A process pool

Basic syntax:

```python id="ne0yfn"
result = await loop.run_in_executor(
    executor,
    function_name,
    argument_1,
    argument_2,
)
```

Important:

```python id="lc9n3z"
function_name
```

is passed without parentheses.

Correct:

```python id="63envj"
loop.run_in_executor(pool, encrypt_data, data)
```

Incorrect:

```python id="zdosvp"
loop.run_in_executor(pool, encrypt_data(data))
```

The incorrect version calls the function immediately.

---

# 4. Getting the Running Event Loop

Inside an async function, use:

```python id="m0m4az"
loop = asyncio.get_running_loop()
```

This gives the currently running event loop.

The event loop can then send blocking or CPU-heavy work to an executor.

---

# 5. CPU-Heavy Function Example

```python id="au9zby"
def encrypt_data(data):
    return f"encrypted({data})"
```

This is a normal function.

It is not async.

In a real application, encryption could be CPU-heavy.

For CPU-heavy work, we can move it to a separate process using `ProcessPoolExecutor`.

---

# 6. Asyncio with ProcessPoolExecutor

```python id="pb7put"
import asyncio
from concurrent.futures import ProcessPoolExecutor


def encrypt_data(data):
    return f"encrypted({data})"


async def main():
    loop = asyncio.get_running_loop()

    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool,
            encrypt_data,
            "credit-card-1234",
        )

    print(result)


if __name__ == "__main__":
    asyncio.run(main())
```

This offloads the CPU-heavy function to another process.

The async event loop does not have to perform the heavy work directly.

---

# 7. Why the **main** Guard Is Required

Multiprocessing code should be protected with:

```python id="w0s8z2"
if __name__ == "__main__":
```

This is especially important on Windows and platforms that use the `spawn` start method.

Without this guard, child processes may repeatedly import and execute the file.

This can cause errors related to process bootstrapping.

Correct:

```python id="3t3vbb"
if __name__ == "__main__":
    asyncio.run(main())
```

---

# 8. ProcessPoolExecutor Flow

```text id="h0r5ql"
Async function starts
        ↓
Gets running event loop
        ↓
Creates ProcessPoolExecutor
        ↓
Sends CPU-heavy function to process pool
        ↓
Async function awaits result
        ↓
Worker process completes task
        ↓
Result returns to async function
```

---

# 9. Running Multiple CPU-Heavy Tasks

```python id="ebj7q1"
async def main():
    loop = asyncio.get_running_loop()

    data_items = [
        "card-1111",
        "card-2222",
        "card-3333",
    ]

    with ProcessPoolExecutor() as pool:
        tasks = [
            loop.run_in_executor(
                pool,
                encrypt_data,
                data,
            )
            for data in data_items
        ]

        results = await asyncio.gather(*tasks)

    print(results)
```

`asyncio.gather()` waits for all process-pool tasks to finish.

The `*tasks` syntax unpacks the list into separate arguments.

---

# 10. Background Worker with Threading

Sometimes we want a background task that runs independently, such as:

* Logging system health
* Monitoring application status
* Sending heartbeat messages
* Running lightweight background checks

For this, a background thread can be useful.

Example:

```python id="p7eomp"
import threading
import time


def background_worker():
    while True:
        time.sleep(1)
        print("Logging system health")
```

Create and start the thread:

```python id="hxi2da"
thread = threading.Thread(
    target=background_worker,
    daemon=True,
)

thread.start()
```

---

# 11. What Is a Daemon Thread?

A daemon thread runs in the background.

```python id="b0ap2f"
daemon=True
```

means the thread will not prevent the program from exiting.

If only daemon threads are left, Python can stop the program.

Daemon threads are useful for background support tasks.

They are not ideal for critical tasks that must always finish.

---

# 12. Asyncio with Background Thread

```python id="hyqxhd"
import asyncio
import threading
import time


def background_worker():
    while True:
        time.sleep(1)
        print("Logging system health")


async def fetch_orders():
    await asyncio.sleep(3)
    print("Orders fetched")


thread = threading.Thread(
    target=background_worker,
    daemon=True,
)

thread.start()

asyncio.run(fetch_orders())
```

The background thread logs system health while the async function waits.

---

# 13. Why This Works

The background worker uses a separate thread.

The async function uses the event loop.

They can run side by side.

```text id="2b1g6w"
Thread:
    Logs system health every second

Asyncio:
    Waits asynchronously for order fetching
```

The thread does not block the async event loop.

The async task does not stop the background thread.

---

# 14. Practical Use Case

Imagine a chai delivery SaaS platform.

Asyncio can handle:

* Payment API calls
* Google Maps API calls
* Customer order requests
* Delivery status updates

Threads can handle:

* Background logging
* Health checks
* Lightweight monitoring

Processes can handle:

* Demand prediction
* Image processing
* CPU-heavy analytics
* Machine learning inference

All three can work together when used carefully.

---

# 15. Choosing the Right Tool

| Task                        | Suggested tool      |
| --------------------------- | ------------------- |
| API calls                   | Asyncio             |
| Database waits              | Asyncio or threads  |
| Blocking legacy SDK         | ThreadPoolExecutor  |
| CPU-heavy calculation       | ProcessPoolExecutor |
| Background logging          | Threading           |
| Heavy ML prediction         | Multiprocessing     |
| Web server request handling | Asyncio             |

---

# 16. Important Warnings

## Do Not Use Processes for Everything

Processes have overhead.

They require:

* Process startup
* Separate memory
* Data serialization
* Result transfer
* Main guard protection

Use processes mainly when the work is CPU-heavy enough to justify the cost.

## Do Not Block the Event Loop

Avoid this inside async functions:

```python id="wdpccc"
time.sleep(3)
```

Use this instead:

```python id="046hjx"
await asyncio.sleep(3)
```

Or move blocking work to a thread:

```python id="xf54a8"
await asyncio.to_thread(blocking_function)
```

## Process Functions Must Be Picklable

Functions used with `ProcessPoolExecutor` should usually be defined at the top level of the file.

Avoid using nested functions or lambdas for process-pool work.

---

# 17. Common Mistakes

## Missing Parentheses

Incorrect:

```python id="5glq2b"
with ProcessPoolExecutor as pool:
```

Correct:

```python id="a0lsc1"
with ProcessPoolExecutor() as pool:
```

## Missing Main Guard

Incorrect:

```python id="bk7b6i"
asyncio.run(main())
```

Better for multiprocessing:

```python id="s6bpyq"
if __name__ == "__main__":
    asyncio.run(main())
```

## Calling the Target Function Immediately

Incorrect:

```python id="v4odpa"
loop.run_in_executor(
    pool,
    encrypt_data("card-1234"),
)
```

Correct:

```python id="t3cuwc"
loop.run_in_executor(
    pool,
    encrypt_data,
    "card-1234",
)
```

---

# 18. Asyncio + Multiprocessing Flow

```text id="kwia7x"
Main process starts
        ↓
asyncio.run(main()) starts event loop
        ↓
main() creates process pool
        ↓
CPU-heavy work goes to child process
        ↓
Event loop awaits the result
        ↓
Child process returns result
        ↓
Async code continues
```

---

# 19. Asyncio + Threading Flow

```text id="slseto"
Main program starts
        ↓
Background daemon thread starts
        ↓
Thread logs health periodically
        ↓
Asyncio event loop runs async task
        ↓
Async task awaits non-blocking operation
        ↓
Background thread continues independently
        ↓
Async task completes
        ↓
Program exits
```

---

# Key Takeaways

* Asyncio can work with multiprocessing.
* Asyncio can also work with threading.
* Use `ProcessPoolExecutor` for CPU-heavy work.
* Use `ThreadPoolExecutor` or `asyncio.to_thread()` for blocking I/O work.
* Use `asyncio.get_running_loop()` to access the active event loop.
* Use `loop.run_in_executor()` to offload blocking or CPU-heavy work.
* Use the `__main__` guard when using multiprocessing.
* Use daemon threads for lightweight background tasks.
* Avoid blocking the event loop with `time.sleep()`.
* Asyncio, threading, and multiprocessing are different tools for different jobs.
