# Python Threading Deep Dive

## Overview

Threading allows a Python program to run multiple tasks concurrently inside the same process.

This lesson covers:

* Process vs thread
* Creating threads
* Starting and joining threads
* Passing arguments to threads
* Using threads for I/O-bound work
* Why threads are not ideal for CPU-bound work
* Using locks to protect shared state

---

# 1. Process vs Thread

A **process** is an independent running program.

A **thread** is a smaller unit of execution inside a process.

```text id="61pq85"
Process
│
├── Thread 1
├── Thread 2
└── Thread 3
```

Each process has its own memory space.

Threads inside the same process share memory.

This makes threads lightweight, but it also means shared data must be handled carefully.

---

# 2. Creating a Thread

Python provides the built-in `threading` module.

```python id="ghj52x"
import threading
```

Create a thread using:

```python id="wccf17"
thread = threading.Thread(
    target=function_name
)
```

The `target` is the function that the thread will run.

Do not write:

```python id="ox7duo"
target=function_name()
```

That calls the function immediately.

Correct:

```python id="t3xus5"
target=function_name
```

---

# 3. Basic Thread Example

```python id="91x1y8"
import threading
import time


def boil_milk():
    print("Boiling milk...")
    time.sleep(2)
    print("Milk boiled")


def toast_bun():
    print("Toasting bun...")
    time.sleep(3)
    print("Done with bun toast")
```

Create two threads:

```python id="uxsabh"
thread_one = threading.Thread(
    target=boil_milk
)

thread_two = threading.Thread(
    target=toast_bun
)
```

Start them:

```python id="kewjc8"
thread_one.start()
thread_two.start()
```

Wait for them:

```python id="rv7f42"
thread_one.join()
thread_two.join()
```

---

# 4. start() and join()

## start()

`start()` begins the thread execution.

```python id="5lhn7u"
thread.start()
```

## join()

`join()` waits for the thread to finish.

```python id="3cgf9v"
thread.join()
```

Without `join()`, the main program may continue before the thread completes.

---

# 5. Measuring Time

```python id="bl42sz"
start = time.time()

thread_one.start()
thread_two.start()

thread_one.join()
thread_two.join()

end = time.time()

print(f"Finished in {end - start:.2f} seconds")
```

If one task takes 2 seconds and another takes 3 seconds, threaded execution may finish in around 3 seconds instead of 5 seconds.

This works well when tasks spend time waiting.

---

# 6. Passing Arguments to Threads

A thread target can accept arguments.

```python id="pl6h08"
def prepare_chai(chai_type, wait_time):
    print(f"{chai_type} chai brewing...")
    time.sleep(wait_time)
    print(f"{chai_type} chai is ready")
```

Pass arguments using `args`.

```python id="xil4jj"
thread = threading.Thread(
    target=prepare_chai,
    args=("Masala", 2)
)
```

`args` must be a tuple.

For one argument, use a trailing comma:

```python id="mjzmh1"
args=("Masala",)
```

---

# 7. Thread Example with Arguments

```python id="5d0v4u"
thread_one = threading.Thread(
    target=prepare_chai,
    args=("Masala", 2)
)

thread_two = threading.Thread(
    target=prepare_chai,
    args=("Ginger", 3)
)

thread_one.start()
thread_two.start()

thread_one.join()
thread_two.join()
```

Both tasks can progress during overlapping time.

---

# 8. Where Threads Are Useful

Threads are useful for **I/O-bound tasks**.

I/O-bound tasks spend time waiting for something outside the CPU.

Examples:

* Web requests
* API calls
* Database queries
* File reading
* File writing
* Network operations

While one thread waits, another thread can continue.

---

# 9. Where Threads Are Not Very Useful

Threads are usually not helpful for speeding up CPU-heavy Python code in CPython.

CPU-heavy tasks include:

* Large mathematical calculations
* Pure Python image processing
* Pure Python video processing
* Heavy loops
* Large data transformations

Because of the Global Interpreter Lock, or GIL, only one thread usually executes Python bytecode at a time inside one CPython process.

For CPU-bound work, multiprocessing is often a better choice.

---

# 10. Threaded Download Example

Downloading from the web is an I/O-bound operation.

One thread can wait for one URL while another thread requests another URL.

```python id="2sg6ba"
import threading
import urllib.request


def download_url(url):
    with urllib.request.urlopen(url, timeout=10) as response:
        data = response.read()

    print(f"Downloaded {len(data)} bytes from {url}")
```

Create one thread per URL:

```python id="sy1avh"
urls = [
    "https://httpbin.org/image/jpeg",
    "https://httpbin.org/image/png",
    "https://httpbin.org/image/svg",
]

threads = []

for url in urls:
    thread = threading.Thread(
        target=download_url,
        args=(url,)
    )

    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
```

This example reads response content and prints the size.

It does not need to save images to disk.

---

# 11. Thread Output Order

Thread output order is not guaranteed.

Example:

```text id="hbl5jm"
Starting download from URL 1
Starting download from URL 2
Finished download from URL 2
Finished download from URL 1
```

This is normal.

The operating system decides when each thread gets execution time.

---

# 12. Shared State

Threads in the same process share memory.

This means multiple threads can access the same variable.

```python id="c087vs"
counter = 0
```

If many threads update the same variable, the final result may become incorrect.

This is called a **race condition**.

---

# 13. Race Condition

A race condition occurs when the final result depends on timing.

This line looks simple:

```python id="e0qkng"
counter += 1
```

But internally it involves multiple steps:

1. Read the current value
2. Add one
3. Store the new value

If two threads do this at the same time, one update may overwrite the other.

---

# 14. Lock

Python provides `threading.Lock`.

```python id="siqfo9"
lock = threading.Lock()
```

A lock ensures that only one thread enters a protected section at a time.

```python id="1w60dw"
with lock:
    counter += 1
```

When one thread holds the lock, other threads must wait.

---

# 15. Thread-Safe Counter

```python id="wiocbx"
import threading


counter = 0
lock = threading.Lock()


def increment():
    global counter

    for _ in range(100_000):
        with lock:
            counter += 1
```

Create ten threads:

```python id="nr67vs"
threads = [
    threading.Thread(target=increment)
    for _ in range(10)
]
```

Start and join:

```python id="s2d6ao"
for thread in threads:
    thread.start()

for thread in threads:
    thread.join()

print(counter)
```

Expected result:

```text id="by0wsp"
1000000
```

---

# 16. Why Use with lock?

This is recommended:

```python id="5v4qk4"
with lock:
    counter += 1
```

It is safer than:

```python id="yj8qz9"
lock.acquire()
counter += 1
lock.release()
```

The `with` statement releases the lock even if an exception occurs inside the block.

---

# 17. Lock Trade-Off

Locks protect correctness, but they can reduce speed.

If all threads wait for the same lock, that part of the program becomes sequential.

Use locks only around the smallest required critical section.

Good:

```python id="dp945m"
with lock:
    counter += 1
```

Avoid locking large unrelated code blocks.

---

# 18. Threading Best Practices

Use threads when:

* The task is I/O-bound
* The task waits for external systems
* Shared data is limited
* You need lightweight concurrency

Be careful when:

* Multiple threads modify shared data
* Output order matters
* Exceptions happen inside threads
* Work is CPU-heavy
* Threads depend too much on each other

---

# 19. Threading vs Multiprocessing

| Threading                           | Multiprocessing                   |
| ----------------------------------- | --------------------------------- |
| Multiple threads inside one process | Multiple separate processes       |
| Shared memory                       | Separate memory                   |
| Lower overhead                      | Higher overhead                   |
| Good for I/O-bound tasks            | Good for CPU-bound tasks          |
| Affected by GIL for Python bytecode | Can use multiple CPU cores        |
| Needs locks for shared mutable data | Needs inter-process communication |

---

# Key Takeaways

* A process can contain multiple threads.
* Threads inside the same process share memory.
* Use `threading.Thread` to create a thread.
* Use `target` to specify the function.
* Use `args` to pass arguments.
* Use `start()` to begin execution.
* Use `join()` to wait for completion.
* Threads are useful for I/O-bound work.
* Threads are usually not ideal for CPU-bound pure Python work.
* Shared mutable data can cause race conditions.
* Use `threading.Lock()` to protect shared data.
* Keep locked sections small.
