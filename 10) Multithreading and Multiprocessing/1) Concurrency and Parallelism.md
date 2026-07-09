# Python Concurrency and Parallelism

## Overview

Concurrency and parallelism allow programs to make progress on multiple tasks.

They are related but not identical:

* **Concurrency** means managing multiple tasks during overlapping periods.
* **Parallelism** means executing multiple tasks at the same physical time.

Python commonly provides:

| Goal                      | Common tools                             |
| ------------------------- | ---------------------------------------- |
| Thread-based concurrency  | `threading`, `ThreadPoolExecutor`        |
| Asynchronous concurrency  | `asyncio`                                |
| Process-based parallelism | `multiprocessing`, `ProcessPoolExecutor` |

---

# 1. Concurrency

Concurrency means that multiple tasks make progress during the same period.

The tasks do not necessarily execute at the exact same instant.

A worker may switch between tasks whenever one task is waiting.

## Real-World Example

Imagine one chai-shop worker:

1. Takes an order
2. Waits for payment confirmation
3. Starts another order while waiting
4. Returns to the first order when confirmation arrives

The worker handles several tasks concurrently by switching between them.

## Simplified Timeline

```text
Time ──────────────────────────────>

Task A: Work ─ Wait ─ Work
Task B:      Work ─ Wait ─ Work
```

The tasks overlap, even though one worker may be managing them.

---

# 2. Parallelism

Parallelism means multiple tasks execute at the same time using separate computing resources.

## Real-World Example

Imagine three chai makers:

* Worker 1 prepares Masala Chai
* Worker 2 prepares Ginger Chai
* Worker 3 prepares Elaichi Chai

The three tasks can progress simultaneously.

## Simplified Timeline

```text
Time ──────────────────────────────>

Core 1: Task A ─────────────
Core 2: Task B ─────────────
Core 3: Task C ─────────────
```

Parallelism usually requires multiple CPU cores or processors.

---

# 3. Concurrency vs Parallelism

| Concurrency                        | Parallelism                           |
| ---------------------------------- | ------------------------------------- |
| Multiple tasks make progress       | Multiple tasks execute simultaneously |
| May use one or more CPU cores      | Usually uses multiple CPU cores       |
| Useful for waiting-heavy work      | Useful for calculation-heavy work     |
| Commonly uses threads or `asyncio` | Commonly uses processes               |
| Focuses on task coordination       | Focuses on simultaneous execution     |

Concurrency is about dealing with many tasks.

Parallelism is about performing many tasks at the same time.

---

# 4. I/O-Bound Tasks

An I/O-bound task spends much of its time waiting for external operations.

Examples include:

* Reading files
* Calling APIs
* Waiting for databases
* Downloading data
* Receiving network responses
* Waiting for user input

Threads and asynchronous programming are commonly suitable for I/O-bound work.

While one task waits, another task can make progress.

---

# 5. CPU-Bound Tasks

A CPU-bound task spends most of its time performing calculations.

Examples include:

* Image processing
* Video encoding
* Mathematical calculations
* Data compression
* Machine-learning computation
* Large data transformations

Process-based parallelism is commonly suitable for CPU-bound Python work.

Separate processes can execute Python code on separate CPU cores.

---

# 6. Python Threads and the GIL

In the standard CPython implementation, the Global Interpreter Lock, or GIL, normally allows only one thread at a time to execute Python bytecode within a process.

This means threads generally do not speed up pure Python CPU-bound calculations.

However, threads are still useful because:

* The GIL is released during many I/O operations
* One thread can run while another waits
* Many libraries release the GIL during native operations
* Threads share the same process memory

Therefore:

```text
I/O-bound work → threading can be useful
CPU-bound Python work → multiprocessing is often better
```

Threads may be scheduled by the operating system on different cores, but the GIL limits simultaneous execution of ordinary Python bytecode within one CPython process.

---

# 7. Creating a Thread

Python provides the built-in `threading` module.

```python
import threading
```

A thread can be created using:

```python
thread = threading.Thread(
    target=some_function
)
```

The `target` specifies the function that the thread should execute.

---

# 8. Starting a Thread

Creating a thread does not start it.

Use:

```python
thread.start()
```

Example:

```python
order_thread = threading.Thread(
    target=take_orders
)

order_thread.start()
```

Python begins executing the target function in the new thread.

---

# 9. Waiting with join()

Calling `start()` returns immediately after starting the thread.

Use `join()` when the main program must wait for the thread to finish.

```python
order_thread.join()
```

Example:

```python
order_thread.start()
brew_thread.start()

order_thread.join()
brew_thread.join()

print("All work completed")
```

The final message runs only after both threads finish.

---

# 10. Threading Example

```python
import threading
import time


def take_orders():
    for order_number in range(1, 4):
        print(f"Taking order {order_number}")
        time.sleep(2)


def brew_chai():
    for order_number in range(1, 4):
        print(f"Brewing chai {order_number}")
        time.sleep(3)
```

Create and run the threads:

```python
order_thread = threading.Thread(
    target=take_orders
)

brew_thread = threading.Thread(
    target=brew_chai
)

order_thread.start()
brew_thread.start()

order_thread.join()
brew_thread.join()
```

The output from the two threads may be interleaved.

The exact ordering is not guaranteed.

---

# 11. Why sleep() Is Used in Demonstrations

`time.sleep()` pauses the current thread.

```python
time.sleep(2)
```

It is commonly used in examples to simulate waiting for:

* A database
* A web service
* A file
* A network response
* Another external system

It does not perform actual work.

Because sleeping releases execution time, another thread can run during the waiting period.

---

# 12. Thread Arguments

Arguments can be passed to a thread's target function using `args`.

```python
def brew_chai(chai_name):
    print(f"Brewing {chai_name}")
```

Create the thread:

```python
thread = threading.Thread(
    target=brew_chai,
    args=("Masala Chai",),
)
```

The trailing comma is important because `args` expects a tuple.

---

# 13. Multiprocessing

The `multiprocessing` module creates separate processes.

```python
from multiprocessing import Process
```

Each process has:

* Its own Python interpreter
* Its own memory space
* Its own process ID
* The ability to run on a separate CPU core

This provides true parallel execution for CPU-bound Python code when sufficient cores are available.

---

# 14. Creating a Process

```python
process = Process(
    target=some_function
)
```

Start it:

```python
process.start()
```

Wait for it:

```python
process.join()
```

The interface is similar to the threading interface.

---

# 15. Passing Arguments to a Process

```python
def brew_chai(chai_name):
    print(f"Brewing {chai_name}")
```

Create a process:

```python
process = Process(
    target=brew_chai,
    args=("Masala Chai",),
)
```

As with threads, the `args` value must be a tuple.

---

# 16. The **main** Guard

Multiprocessing code should normally be protected using:

```python
if __name__ == "__main__":
```

Example:

```python
from multiprocessing import Process


def perform_task():
    print("Task running")


if __name__ == "__main__":
    process = Process(target=perform_task)

    process.start()
    process.join()
```

This is especially important on Windows and platforms that use the `spawn` process-start method.

Without the guard, child processes may repeatedly execute the module and create additional processes.

---

# 17. Multiprocessing Example

```python
from multiprocessing import Process
import time


def brew_chai(chai_name):
    print(f"Starting {chai_name}")
    time.sleep(3)
    print(f"Finished {chai_name}")


if __name__ == "__main__":
    processes = [
        Process(
            target=brew_chai,
            args=(f"Chai {number}",),
        )
        for number in range(1, 4)
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print("All chai prepared")
```

The processes may run simultaneously on different CPU cores.

The exact print order is not guaranteed.

---

# 18. Threads vs Processes

| Threads                                 | Processes                            |
| --------------------------------------- | ------------------------------------ |
| Share the same memory                   | Have separate memory                 |
| Lower creation overhead                 | Higher creation overhead             |
| Easier data sharing                     | Requires inter-process communication |
| Suitable for I/O-bound work             | Suitable for CPU-bound work          |
| A thread failure can affect the process | Process failures are more isolated   |
| Limited by the GIL for Python bytecode  | Can use multiple CPU cores           |

---

# 19. Sequential vs Concurrent Execution

## Sequential

```python
take_orders()
brew_chai()
```

The second function starts only after the first one finishes.

If the functions take six and nine seconds, total execution may be approximately fifteen seconds.

## Concurrent

```python
order_thread.start()
brew_thread.start()
```

The waiting periods can overlap.

Total time may be close to the duration of the slower task rather than the sum of both tasks.

Exact timing depends on the work, system, and scheduling.

---

# 20. Process Startup Overhead

Multiprocessing is not always faster.

Creating processes involves:

* Starting Python interpreters
* Allocating separate memory
* Serializing arguments
* Transferring data
* Coordinating results
* Combining partial outputs

For very small tasks, this overhead may be greater than the time saved through parallelism.

Use multiprocessing when the tasks are large enough to justify the additional cost.

---

# 21. Waiting for the Slowest Task

Suppose three processes are working:

```text
Process 1: 2 seconds
Process 2: 2 seconds
Process 3: 8 seconds
```

If all results are required, the program must wait for the slowest process.

Parallelism reduces total execution time only when the work can be divided effectively.

It does not remove:

* Coordination time
* Startup overhead
* Result-combination time
* Uneven workload problems

---

# 22. ThreadPoolExecutor

The `concurrent.futures` module provides a higher-level interface for working with threads.

```python
from concurrent.futures import ThreadPoolExecutor
```

Example:

```python
with ThreadPoolExecutor(max_workers=3) as executor:
    executor.submit(brew_chai, "Masala")
    executor.submit(brew_chai, "Ginger")
```

`ThreadPoolExecutor` manages the creation and reuse of worker threads.

It is often easier than manually managing many `Thread` objects.

---

# 23. ProcessPoolExecutor

For process-based parallelism:

```python
from concurrent.futures import ProcessPoolExecutor
```

Example:

```python
with ProcessPoolExecutor(max_workers=3) as executor:
    executor.submit(cpu_heavy_task, data)
```

`ProcessPoolExecutor` manages a pool of worker processes.

It is commonly used when:

* Several independent CPU-heavy tasks exist
* Results need to be collected
* Manual process management would be repetitive

---

# 24. asyncio

`asyncio` supports cooperative asynchronous concurrency.

It is especially useful for large numbers of I/O-bound tasks such as:

* API requests
* Network services
* WebSocket connections
* Database calls
* Async web applications

It commonly uses:

```python
async def
```

and:

```python
await
```

Unlike multiprocessing, `asyncio` does not normally create a separate process for every task.

---

# 25. Choosing the Right Approach

| Workload                       | Common choice         |
| ------------------------------ | --------------------- |
| Many network requests          | `asyncio` or threads  |
| File and database waiting      | Threads or async APIs |
| CPU-heavy pure Python work     | Multiprocessing       |
| A few background I/O tasks     | Threads               |
| Thousands of async connections | `asyncio`             |
| Independent calculations       | Process pool          |

The best choice depends on the type of work rather than the number of tasks alone.

---

# 26. Important Corrections

## Threads Do Not Always Mean One CPU Core

The operating system can schedule threads across different cores.

However, in standard CPython, the GIL usually prevents multiple threads in one process from executing Python bytecode simultaneously.

The practical conclusion remains:

```text
Use threads mainly for I/O-bound Python work.
```

## Multiprocessing Does Not Guarantee Faster Execution

Processes can use multiple CPU cores, but performance depends on:

* Available cores
* Workload size
* Process startup cost
* Data-transfer cost
* Work distribution
* Operating-system scheduling

## Output Order Is Not Guaranteed

Thread and process output may appear in different orders between executions.

Do not rely on print order to determine correct execution.

---

# Key Takeaways

* Concurrency and parallelism are related but different.
* Concurrency manages overlapping tasks.
* Parallelism executes tasks simultaneously.
* Threads are commonly used for I/O-bound concurrency.
* `asyncio` supports asynchronous I/O concurrency.
* Processes are commonly used for CPU-bound parallelism.
* `Thread.start()` and `Process.start()` begin execution.
* `join()` waits for a thread or process to finish.
* Thread outputs may be interleaved.
* Multiprocessing code should use the `__main__` guard.
* Threads share memory, while processes use separate memory.
* CPython's GIL limits CPU-bound Python thread parallelism.
* Multiprocessing has greater startup and communication overhead.
* Parallelism is not automatically better than concurrency.
