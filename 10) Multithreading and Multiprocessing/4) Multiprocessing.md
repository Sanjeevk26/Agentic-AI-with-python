# Python Multiprocessing: Processes, Queues, and Shared Values

## Overview

Multiprocessing allows Python programs to run tasks in separate processes.

This is useful when the task is CPU-heavy and pure Python threading does not provide much speed benefit due to the GIL.

This lesson covers:

* Why threads may not help CPU-heavy work
* How to convert thread-based code into process-based code
* Why multiprocessing needs the `__main__` guard
* How processes communicate using `Queue`
* How processes share simple values using `Value`
* How locks protect shared process data

---

# 1. Threads vs Processes

## Threads

Threads run inside the same process.

They share:

* Memory
* Global variables
* Objects
* File handles
* Process resources

This makes communication easy, but shared data must be protected carefully.

## Processes

Processes are separate running programs.

Each process usually has its own:

* Python interpreter
* Memory space
* Global variables
* GIL
* Process ID

Because memory is separate, processes do not automatically share data.

---

# 2. Why Threads May Not Help CPU-Heavy Work

Threads are useful for I/O-bound tasks such as:

* Web requests
* Database calls
* File reads
* File writes
* Waiting for APIs

But CPU-heavy tasks are different.

CPU-heavy tasks include:

* Large loops
* Mathematical calculations
* Image processing
* Video processing
* Data crunching

Example:

```python id="yy282c"
def cpu_heavy():
    total = 0

    for number in range(10**7):
        total += number * number

    return total
```

This task mostly uses the CPU.

In CPython, CPU-heavy Python code does not usually become faster with threads because of the Global Interpreter Lock.

---

# 3. CPU-Heavy Work with Threads

```python id="x0t8sh"
import threading
import time


def cpu_heavy():
    print("Crunching numbers...")

    total = 0

    for number in range(10**7):
        total += number * number

    print("Done crunching numbers")
```

Create two threads:

```python id="i7l7pf"
threads = [
    threading.Thread(target=cpu_heavy)
    for _ in range(2)
]
```

Start and join them:

```python id="41ryvb"
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
```

This creates two threads, but it does not guarantee faster CPU-bound execution.

---

# 4. CPU-Heavy Work with Processes

The same CPU-heavy task can be moved to separate processes.

```python id="3zwq76"
from multiprocessing import Process
import time


def cpu_heavy():
    print("Crunching numbers...")

    total = 0

    for number in range(10**7):
        total += number * number

    print("Done crunching numbers")
```

Create processes:

```python id="ud0bpb"
processes = [
    Process(target=cpu_heavy)
    for _ in range(2)
]
```

Start and join:

```python id="r59cm5"
for process in processes:
    process.start()

for process in processes:
    process.join()
```

Since each process has its own interpreter and GIL, multiple processes can run CPU-heavy Python work in parallel on multiple CPU cores.

---

# 5. The **main** Guard

Multiprocessing code should be protected using:

```python id="bypldq"
if __name__ == "__main__":
```

Example:

```python id="zajlcv"
from multiprocessing import Process


def cpu_heavy():
    print("Working")


if __name__ == "__main__":
    process = Process(target=cpu_heavy)

    process.start()
    process.join()
```

This is especially important on Windows and platforms that use the `spawn` start method.

Without the main guard, Python may raise an error such as:

```text id="1c0nwr"
An attempt has been made to start a new process
before the current process has finished its bootstrapping phase.
```

The main guard tells Python where the safe entry point of the program is.

---

# 6. Why Processes Need Communication Tools

Threads can share memory directly.

Processes do not share memory by default.

This means a normal global variable changed in one process is not automatically changed in another process.

Example:

```python id="m9vhg3"
counter = 0
```

If one child process updates this variable, the parent process does not automatically see that update.

To communicate between processes, Python provides tools such as:

* `Queue`
* `Pipe`
* `Value`
* `Array`
* Managers
* Shared memory

---

# 7. Queue

A `Queue` is used to pass data between processes.

It works like a safe communication channel.

One process can put data into the queue.

Another process can get data from the queue.

```python id="zeouu7"
from multiprocessing import Process, Queue
```

Create a queue:

```python id="az2ksd"
queue = Queue()
```

Put data into the queue:

```python id="he8tav"
queue.put("Masala chai is ready")
```

Get data from the queue:

```python id="b3h6qy"
message = queue.get()
```

---

# 8. Process with Queue Example

```python id="xa1zqk"
from multiprocessing import Process, Queue


def prepare_chai(queue):
    queue.put("Masala chai is ready")


if __name__ == "__main__":
    queue = Queue()

    process = Process(
        target=prepare_chai,
        args=(queue,)
    )

    process.start()
    process.join()

    print(queue.get())
```

Output:

```text id="0yh2lb"
Masala chai is ready
```

The child process cannot directly return a value to the parent like a normal function.

Instead, it places the result into the queue.

---

# 9. Why Queue Is Useful

A queue is useful when:

* Multiple processes produce results
* One parent process needs to collect results
* Tasks finish at different times
* Data must move safely between processes
* Work is divided among workers

Example:

```text id="mr2zqw"
Process 1 → Queue
Process 2 → Queue
Process 3 → Queue
Parent process reads from Queue
```

---

# 10. Sharing Simple Values with Value

For simple shared values, Python provides `multiprocessing.Value`.

```python id="tdcven"
from multiprocessing import Value
```

Create a shared integer:

```python id="ci8to6"
counter = Value("i", 0)
```

Here:

```text id="oxc4jd"
"i" means integer
0 is the initial value
```

Access the actual value using:

```python id="090akg"
counter.value
```

---

# 11. Value with Lock

`Value` comes with a lock by default.

You can safely update it using:

```python id="5x9sr2"
with counter.get_lock():
    counter.value += 1
```

The lock ensures only one process updates the shared value at a time.

---

# 12. Process with Shared Value Example

```python id="oeea6k"
from multiprocessing import Process, Value


def increment(counter):
    for _ in range(100_000):
        with counter.get_lock():
            counter.value += 1


if __name__ == "__main__":
    counter = Value("i", 0)

    processes = [
        Process(target=increment, args=(counter,))
        for _ in range(4)
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print(counter.value)
```

Expected output:

```text id="1jz8kk"
400000
```

Four processes each increment the value 100,000 times.

---

# 13. Queue vs Value

| Queue                               | Value                          |
| ----------------------------------- | ------------------------------ |
| Used to pass messages or results    | Used to share one simple value |
| Can hold many items                 | Holds one shared value         |
| Good for producer-consumer patterns | Good for counters and flags    |
| Uses `put()` and `get()`            | Uses `.value`                  |
| Useful for task results             | Useful for shared state        |

---

# 14. Locks in Multiprocessing

Locks are important when multiple processes update the same shared value.

Without a lock, two processes may read and update the value at the same time.

This can cause lost updates.

Safe:

```python id="qmn25w"
with counter.get_lock():
    counter.value += 1
```

Unsafe:

```python id="wr2z0h"
counter.value += 1
```

Even though the line looks simple, it involves reading, modifying, and writing.

---

# 15. Common Multiprocessing Flow

```text id="m5t5zz"
Define worker function
    ↓
Create Process objects
    ↓
Pass arguments using args
    ↓
Start all processes
    ↓
Join all processes
    ↓
Collect results
```

Example:

```python id="3o25il"
process = Process(
    target=worker_function,
    args=(value,)
)
```

As with threads, `args` must be a tuple.

For one argument:

```python id="rx70qj"
args=(queue,)
```

The comma is important.

---

# 16. When to Use Multiprocessing

Use multiprocessing for:

* CPU-heavy calculations
* Image processing
* Video processing
* Batch processing
* Large independent tasks
* Parallel data processing
* AI or ML preprocessing workloads

Multiprocessing works best when tasks are independent and do not need constant communication.

---

# 17. When Not to Use Multiprocessing

Avoid multiprocessing when:

* Tasks are very small
* Data transfer cost is high
* Processes need constant shared state
* The task is mainly I/O-bound
* Threading or `asyncio` is enough
* Startup overhead is larger than the task itself

Multiprocessing is powerful, but it has overhead.

---

# 18. Important Corrections

## Processes Do Not Share Normal Memory

A global variable is not automatically shared between processes.

Use tools such as:

```python id="mq930b"
Queue
Value
Array
Pipe
Manager
```

## Multiprocessing Does Not Remove the GIL

Each process has its own GIL.

Multiprocessing avoids one shared GIL by using separate interpreters.

## Queue Is Not Exactly a Normal List

A queue is a data structure for ordered communication.

In multiprocessing, it is process-safe and designed for inter-process communication.

---

# 19. Practical Example

Imagine processing many images.

Each image can be handled independently.

```text id="ryvlhk"
Process 1 → Image 1
Process 2 → Image 2
Process 3 → Image 3
Process 4 → Image 4
```

This is a good multiprocessing use case because each process can work independently.

The parent process can collect results afterward.

---

# Key Takeaways

* Multiprocessing creates separate processes.
* Each process has separate memory.
* Threads share memory; processes generally do not.
* CPU-heavy Python code is often better suited to multiprocessing than threading.
* Use `Process` to create a child process.
* Use `start()` to begin a process.
* Use `join()` to wait for a process to finish.
* Use the `if __name__ == "__main__":` guard.
* Use `Queue` to pass data between processes.
* Use `Value` to share simple values such as counters.
* Use `get_lock()` before updating a shared `Value`.
* Multiprocessing has overhead and should be used carefully.
