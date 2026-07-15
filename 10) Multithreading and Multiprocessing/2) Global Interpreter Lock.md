# Python GIL: Global Interpreter Lock

## Overview

The **GIL**, or **Global Interpreter Lock**, is a lock used in the standard CPython implementation of Python.

Its main job is to allow only one thread at a time to execute Python bytecode inside one Python process.

This affects how Python threads behave, especially for CPU-heavy tasks.

---

# 1. What Is the GIL?

GIL stands for:

```text id="58n3qy"
Global Interpreter Lock
```

It is a lock inside CPython that protects the interpreter's internal state.

In simple terms:

```text id="lixz46"
Only one thread can execute Python bytecode at a time in one CPython process.
```

This does not mean Python cannot use threads.

It means Python threads are limited when they are doing CPU-heavy Python work.

---

# 2. Why Does the GIL Exist?

CPython manages memory using reference counting.

Example:

```python id="iye6k3"
x = []
```

Internally, Python tracks how many references point to an object.

When several threads operate at the same time, CPython needs to protect internal memory-management operations.

The GIL simplifies this by ensuring that only one thread executes Python bytecode at a time.

---

# 3. Real-World Analogy

Imagine a chai shop with one billing counter.

There may be many workers, but only one worker can use the billing counter at a time.

```text id="q4uxpc"
Worker 1 → Counter
Worker 2 → Waits
Worker 3 → Waits
```

Once Worker 1 is done, another worker can use the counter.

The GIL works similarly for Python bytecode execution inside one CPython process.

---

# 4. GIL and Threads

Python threads are useful for I/O-bound tasks.

Examples:

* Waiting for a file
* Calling an API
* Waiting for a database
* Downloading data
* Reading from a network socket

While one thread waits, another thread can make progress.

However, for CPU-bound Python code, threads usually do not provide true parallel execution because of the GIL.

---

# 5. CPU-Bound Work

CPU-bound work means the program spends most of its time doing calculations.

Examples:

* Image processing
* Video processing
* Large loops
* Mathematical calculations
* Data compression
* Pure Python number crunching

Example:

```python id="ml88kh"
count = 0

for _ in range(50_000_000):
    count += 1
```

This kind of task keeps the CPU busy.

Threads usually do not speed this up in CPython because only one thread executes Python bytecode at a time.

---

# 6. Threading Example

```python id="9nvjlp"
import threading
import time


def brew_chai():
    print(
        f"{threading.current_thread().name} "
        f"started brewing..."
    )

    count = 0

    for _ in range(30_000_000):
        count += 1

    print(
        f"{threading.current_thread().name} "
        f"finished brewing."
    )
```

Create two threads:

```python id="d2tv7t"
thread_one = threading.Thread(
    target=brew_chai,
    name="Barista 1",
)

thread_two = threading.Thread(
    target=brew_chai,
    name="Barista 2",
)
```

Start and wait:

```python id="smod91"
thread_one.start()
thread_two.start()

thread_one.join()
thread_two.join()
```

Both threads exist, but for CPU-heavy Python bytecode, they do not truly execute in parallel inside the same CPython process.

---

# 7. Important Correction About Shared Variables

The GIL does not remove the need for thread-safety.

This operation:

```python id="zq0guw"
counter += 1
```

looks like one operation, but internally it involves multiple steps.

If multiple threads update shared data, race conditions can still occur.

Use synchronization tools such as:

```python id="myl184"
threading.Lock()
```

when multiple threads modify shared state.

The GIL protects CPython internals. It does not automatically make all user-level code logically safe.

---

# 8. Multiprocessing and the GIL

The `multiprocessing` module creates separate processes.

Each process has:

* Its own Python interpreter
* Its own memory space
* Its own GIL

Because each process has a separate GIL, multiple processes can execute Python bytecode truly in parallel on multiple CPU cores.

```python id="e971bg"
from multiprocessing import Process
```

Example:

```python id="0q91xk"
process_one = Process(target=crunch_numbers)
process_two = Process(target=crunch_numbers)

process_one.start()
process_two.start()

process_one.join()
process_two.join()
```

This is commonly better for CPU-bound pure Python work.

---

# 9. Multiprocessing Requires the **main** Guard

When using multiprocessing, especially on Windows, protect process-starting code with:

```python id="pebo3j"
if __name__ == "__main__":
```

Example:

```python id="s0qauc"
from multiprocessing import Process


def crunch_numbers():
    pass


if __name__ == "__main__":
    process = Process(target=crunch_numbers)

    process.start()
    process.join()
```

Without this guard, child processes may re-import the file and accidentally start new processes again.

This can cause errors related to bootstrapping or spawning.

---

# 10. Threading vs Multiprocessing

| Feature               | Threading           | Multiprocessing                                  |
| --------------------- | ------------------- | ------------------------------------------------ |
| Execution unit        | Thread              | Process                                          |
| Memory                | Shared memory       | Separate memory                                  |
| GIL                   | One GIL per process | One GIL per process                              |
| CPU-bound Python work | Usually not faster  | Can be faster                                    |
| I/O-bound work        | Often useful        | Usually heavier than needed                      |
| Startup cost          | Lower               | Higher                                           |
| Data sharing          | Easier              | Requires IPC, queues, pipes, shared memory, etc. |
| Best for              | Waiting-heavy tasks | CPU-heavy tasks                                  |

---

# 11. Why Multiprocessing Can Be Faster

In threading:

```text id="xvb0ui"
One Python process
One GIL
Multiple threads
Only one thread executes Python bytecode at a time
```

In multiprocessing:

```text id="evxspt"
Process 1 → Own Python interpreter → Own GIL
Process 2 → Own Python interpreter → Own GIL
Process 3 → Own Python interpreter → Own GIL
```

Separate processes can run on separate CPU cores.

This allows true parallelism for CPU-bound Python code.

---

# 12. Multiprocessing Is Not Always Better

Multiprocessing has costs:

* Starting processes takes time
* Each process has separate memory
* Data must be transferred between processes
* Results must be combined
* Debugging can be harder
* Shared state requires special handling

For small tasks, multiprocessing overhead may be greater than the benefit.

---

# 13. When Threads Are Still Useful

Threads are still useful for I/O-bound work.

Example:

```python id="6pqdbb"
time.sleep(2)
```

While one thread sleeps or waits for I/O, another thread can run.

Threads are commonly useful for:

* Web requests
* File operations
* Background monitoring
* Waiting for external services
* Lightweight concurrent tasks

---

# 14. When Processes Are Useful

Processes are commonly useful for CPU-heavy work.

Examples:

* Processing large files
* Image transformations
* Data analysis
* Heavy calculations
* Batch processing
* Running independent jobs in parallel

---

# 15. Important Notes

## The GIL Is CPython-Specific

Most people use CPython, the standard Python implementation.

Other Python implementations may behave differently.

## Some Libraries Release the GIL

Libraries written in C, C++, Rust, or Fortran may release the GIL during heavy computation.

Examples include parts of scientific and numerical libraries.

This means some threaded programs can still benefit from parallelism when heavy work is handled outside normal Python bytecode.

## Multiprocessing Does Not “Disable” the GIL

Multiprocessing does not remove the GIL.

Instead, it creates separate Python processes, and each process has its own GIL.

---

# 16. Common Error with Multiprocessing

If multiprocessing code is not protected with:

```python id="k6gsvk"
if __name__ == "__main__":
```

you may see an error similar to:

```text id="670hpw"
An attempt has been made to start a new process
before the current process has finished its bootstrapping phase.
```
Fix it by placing process creation and startup inside the main guard.

---

# 17. Choosing Between Threading and Multiprocessing

| Task type                      | Better choice                       |
| ------------------------------ | ----------------------------------- |
| Waiting for APIs               | Threading or asyncio                |
| Waiting for database calls     | Threading or asyncio                |
| Reading many files             | Threading can help                  |
| Heavy pure Python calculations | Multiprocessing                     |
| Image or video processing      | Multiprocessing or native libraries |
| Small quick tasks              | Sequential may be enough            |

---

# Key Takeaways

* GIL stands for Global Interpreter Lock.
* The GIL exists in CPython.
* It allows only one thread at a time to execute Python bytecode in one process.
* Threads are still useful for I/O-bound work.
* Threads usually do not speed up CPU-bound pure Python code.
* The GIL does not make all shared user data automatically safe.
* Use `threading.Lock()` for shared mutable state.
* Multiprocessing creates separate processes.
* Each process has its own interpreter, memory, and GIL.
* Multiprocessing can provide real parallelism for CPU-bound Python work.
* Multiprocessing requires the `if __name__ == "__main__":` guard.
* Multiprocessing has overhead and is not always the best choice.
