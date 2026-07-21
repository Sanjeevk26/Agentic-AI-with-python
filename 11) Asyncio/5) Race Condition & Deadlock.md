# Python Profiling and Debugging Threads

## Overview

When working with threading, multiprocessing, and async code, debugging can become harder because tasks may run concurrently.

Common issues include:

* Slow functions
* Race conditions
* Deadlocks
* Blocking code
* Threads not finishing
* Shared data being modified incorrectly

There is no single tool that solves every concurrency problem. The most important thing is to write careful code and understand where shared state, locks, and blocking operations exist.

---

# 1. What Is Profiling?

Profiling means measuring how much time your program spends in different functions.

It helps answer questions like:

* Which function is slow?
* Where is most of the time being spent?
* Is the program CPU-heavy or I/O-heavy?
* Which part should be optimized first?

Profiling does not automatically fix the code. It only shows where time is being spent.

---

# 2. Using cProfile

Python provides a built-in profiler called `cProfile`.

Run a Python file with profiling:

```bash id="0swpjs"
python -m cProfile -s time script_name.py
```

Example:

```bash id="mc9ezq"
python -m cProfile -s time 08_daemon.py
```

Here:

```text id="inwrkj"
-m cProfile
```

runs the built-in profiler.

```text id="rp8n7s"
-s time
```

sorts the output by time spent.

---

# 3. cProfile Output

The output usually includes columns such as:

| Column                      | Meaning                                 |
| --------------------------- | --------------------------------------- |
| `ncalls`                    | Number of calls                         |
| `tottime`                   | Total time spent in the function itself |
| `percall`                   | Time per call                           |
| `cumtime`                   | Total time including sub-functions      |
| `filename:lineno(function)` | Function location                       |

The output can look complicated at first.

With practice, you mainly look for functions with high `tottime` or `cumtime`.

---

# 4. When Profiling Helps

Profiling is useful for:

* CPU-heavy functions
* Slow loops
* I/O-heavy functions
* Complex threaded programs
* Async programs with slow coroutines
* Multiprocessing programs with expensive tasks

Profiling tells you where to focus your optimization work.

---

# 5. Race Condition

A race condition happens when multiple threads access and modify shared data at the same time.

The final result depends on timing.

Example:

```python id="2kfss3"
chai_stock = 0


def restock_chai():
    global chai_stock

    for _ in range(100_000):
        chai_stock += 1
```

If two threads run this function together, the expected result is:

```text id="6803s3"
200000
```

But in real-world conditions, the result may become incorrect because both threads are modifying the same variable.

---

# 6. Why Race Conditions Are Dangerous

This line looks simple:

```python id="fu1gru"
chai_stock += 1
```

But internally, it involves multiple steps:

1. Read the current value
2. Add one
3. Store the new value

If two threads do this at the same time, one update may overwrite the other.

This can be dangerous in applications such as:

* Banking
* Stock trading
* Inventory systems
* Payment systems
* Booking systems
* Order processing systems

Even one incorrect update can create serious issues.

---

# 7. Race Conditions May Not Always Appear

Race conditions are tricky because they may not appear every time.

Sometimes code works perfectly on your local machine.

But under heavy load, production traffic, or different hardware, the issue may appear.

That is why code that modifies shared state should be protected even if the bug is not visible during testing.

---

# 8. Fixing Race Conditions with Lock

Python provides `threading.Lock`.

```python id="zifhl6"
lock = threading.Lock()
```

Use the lock when modifying shared data:

```python id="9ezo0c"
with lock:
    chai_stock += 1
```

This ensures only one thread modifies the shared value at a time.

---

# 9. Safe Counter Example

```python id="o660ee"
import threading


chai_stock = 0
stock_lock = threading.Lock()


def restock_chai():
    global chai_stock

    for _ in range(100_000):
        with stock_lock:
            chai_stock += 1
```

When multiple threads call this function, the shared counter is protected.

---

# 10. Deadlock

A deadlock happens when two or more threads wait forever for each other.

Example:

```text id="pjps94"
Thread 1 has Lock A and waits for Lock B
Thread 2 has Lock B and waits for Lock A
```

Both threads are stuck.

Neither can continue.

---

# 11. Deadlock Example

```python id="l8myuf"
lock_a = threading.Lock()
lock_b = threading.Lock()


def task_one():
    with lock_a:
        with lock_b:
            print("Task one completed")


def task_two():
    with lock_b:
        with lock_a:
            print("Task two completed")
```

This can create a deadlock because both tasks acquire locks in different orders.

---

# 12. Why Deadlocks Are Hard to Debug

Deadlocks may not always happen immediately.

They depend on timing.

The same program may work many times and then suddenly freeze.

Deadlocks are harder to find when:

* Locks are used across many files
* Different developers write different parts
* There are no logs
* The program has many threads
* Lock order is not documented

---

# 13. Avoiding Deadlocks

Common ways to avoid deadlocks:

* Always acquire locks in the same order
* Keep locked sections small
* Avoid nested locks when possible
* Use timeouts while acquiring locks
* Add logging around lock acquisition
* Review shared-state code carefully

Example rule:

```text id="l1n09v"
Always acquire Lock A before Lock B.
```

If every thread follows the same order, deadlocks are less likely.

---

# 14. Logging for Thread Debugging

Logging helps debug concurrent programs.

Instead of only using `print()`, use Python's `logging` module.

```python id="4392pb"
import logging
```

Logging can include:

* Thread name
* Time
* Message level
* File name
* Function name

This makes it easier to understand which thread did what.

---

# 15. Thread-Safe Logging

Python's standard `logging` module is thread-safe for normal use.

Example:

```python id="1cnlvw"
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(threadName)s] %(message)s",
)
```

This prints the thread name with each log message.

---

# 16. Debugging Thread Issues

When debugging thread problems, check:

* Which data is shared?
* Which functions modify shared data?
* Are locks used correctly?
* Are locks acquired in a consistent order?
* Are any threads running infinite loops?
* Are daemon threads stopping too early?
* Are non-daemon threads keeping the program alive?
* Is blocking code being used inside async code?

---

# 17. Helpful Third-Party Profiling Tools

Some external tools can help with profiling and visualization.

Examples include:

* `py-spy`
* `vprof`

These tools can provide better visual output than raw `cProfile`.

They can help show:

* Where time is spent
* Which functions are active
* Stack traces
* CPU usage patterns
* Performance bottlenecks

They are helpful, but they are not magic solutions. You still need to understand the code.

---

# 18. cProfile vs External Profilers

| Tool       | Use                        |
| ---------- | -------------------------- |
| `cProfile` | Built-in Python profiler   |
| `py-spy`   | External sampling profiler |
| `vprof`    | Visual profiling tool      |

Use `cProfile` first because it is built into Python.

Use external tools when you need better visualization or deeper runtime inspection.

---

# 19. Common Mistakes

## Assuming Local Success Means Safe Code

A race condition may not appear during local testing.

Still protect shared mutable state.

## Using Locks Without Planning

Locks can fix race conditions, but they can also create deadlocks.

Use them carefully.

## Holding Locks Too Long

Avoid doing slow work while holding a lock.

Bad:

```python id="bx37vk"
with lock:
    slow_network_call()
```

Better:

```python id="lf91tn"
result = slow_network_call()

with lock:
    shared_data.append(result)
```

## Acquiring Locks in Different Orders

This increases deadlock risk.

Keep lock ordering consistent.

---

# 20. Practical Rule

Use this approach:

```text id="5hvw09"
Shared data?
    ↓
Can multiple threads modify it?
    ↓
Use a lock
    ↓
Keep the lock section small
    ↓
Use consistent lock order
    ↓
Add logging
    ↓
Profile slow areas
```

---

# Key Takeaways

* Profiling shows where time is spent.
* `cProfile` is Python's built-in profiler.
* Use `python -m cProfile -s time file.py` to profile a script.
* Race conditions happen when threads modify shared data unsafely.
* Race conditions may not appear every time.
* Use `threading.Lock()` to protect shared state.
* Deadlocks happen when threads wait on each other forever.
* Avoid deadlocks by using consistent lock ordering.
* Logging helps understand threaded execution.
* Third-party tools like `py-spy` and `vprof` can help with profiling.
* There is no silver bullet for concurrency bugs.
* Careful code design is the best prevention.
