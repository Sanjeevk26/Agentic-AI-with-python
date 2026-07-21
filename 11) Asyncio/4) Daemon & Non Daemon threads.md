# Python Daemon and Non-Daemon Threads

## Overview

In Python, threads can be of two main types:

* Daemon threads
* Non-daemon threads

The main difference is how they behave when the main program finishes.

A **daemon thread** runs in the background and automatically stops when the main program exits.

A **non-daemon thread** keeps running even after the main program finishes, until the thread itself completes.

---

# 1. What Is a Daemon Thread?

A daemon thread is a background thread.

It is usually used for non-critical background work.

Examples:

* Logging
* Monitoring
* Health checks
* Background cleanup
* Periodic status checks

Daemon threads automatically stop when the main program exits.

---

# 2. Daemon Thread Analogy

Imagine a chai shop.

The main worker takes orders and serves customers.

A background helper checks the tea temperature every few seconds.

If the shop closes, the helper also stops automatically.

That helper is like a daemon thread.

---

# 3. Creating a Daemon Thread

```python id="wr5you"
import threading


thread = threading.Thread(
    target=some_function,
    daemon=True,
)
```

The important part is:

```python id="7nbmo2"
daemon=True
```

This marks the thread as a daemon thread.

---

# 4. Daemon Thread Example

```python id="ate6ds"
import threading
import time


def monitor_tea_temperature():
    while True:
        print("Monitoring tea temperature...")
        time.sleep(2)


thread = threading.Thread(
    target=monitor_tea_temperature,
    daemon=True,
)

thread.start()

print("Main program done")
```

Output may look like:

```text id="rjg8wi"
Monitoring tea temperature...
Main program done
```

After the main program exits, the daemon thread is stopped automatically.

---

# 5. What Is a Non-Daemon Thread?

A non-daemon thread is a normal thread.

By default, threads are non-daemon.

This means the program will wait for them to finish before fully exiting.

```python id="oc4yyv"
thread = threading.Thread(
    target=some_function
)
```

This is non-daemon by default.

It is the same as:

```python id="xxsoua"
thread = threading.Thread(
    target=some_function,
    daemon=False,
)
```

---

# 6. Non-Daemon Thread Example

```python id="6k2b2s"
import threading
import time


def monitor_tea_temperature():
    while True:
        print("Monitoring tea temperature...")
        time.sleep(2)


thread = threading.Thread(
    target=monitor_tea_temperature
)

thread.start()

print("Main program done")
```

In this example, the thread keeps running.

Even though the main program prints `"Main program done"`, the program does not fully exit because the non-daemon thread is still active.

---

# 7. Key Difference

| Daemon Thread                               | Non-Daemon Thread         |
| ------------------------------------------- | ------------------------- |
| Runs in the background                      | Runs as a normal thread   |
| Stops automatically when main program exits | Keeps program alive       |
| Good for non-critical tasks                 | Good for important tasks  |
| May be killed before completing work        | Gets time to finish       |
| `daemon=True`                               | `daemon=False` by default |

---

# 8. When to Use Daemon Threads

Use daemon threads for tasks that are helpful but not critical.

Examples:

* Periodic logging
* Monitoring temperature
* Printing heartbeat messages
* Background status checks
* Cache cleanup
* Non-critical telemetry

Daemon threads are useful when the program should not wait for the background task.

---

# 9. When Not to Use Daemon Threads

Avoid daemon threads for important work.

Do not use daemon threads for:

* Saving important files
* Writing financial records
* Completing payments
* Updating databases
* Sending critical reports
* Tasks that must finish safely

A daemon thread can be stopped suddenly when the main program exits.

---

# 10. Using join() with Threads

`join()` tells the main program to wait for a thread.

```python id="1sb825"
thread.join()
```

For a non-daemon thread that runs forever, `join()` will also wait forever.

Example:

```python id="duhiul"
thread.start()
thread.join()
```

If the thread has an infinite loop, the program will not move forward.

---

# 11. Stopping a Thread Gracefully

Python does not provide a safe direct way to forcefully kill a thread.

A better approach is to use a shared flag or `threading.Event`.

Example:

```python id="hd7sau"
stop_event = threading.Event()
```

The thread checks whether it should stop:

```python id="20ybp2"
while not stop_event.is_set():
    print("Monitoring...")
```

The main program can stop it:

```python id="b8xnuk"
stop_event.set()
```

---

# 12. Graceful Non-Daemon Thread Example

```python id="eyxsff"
import threading
import time


def monitor_tea_temperature(stop_event):
    while not stop_event.is_set():
        print("Monitoring tea temperature...")
        time.sleep(1)

    print("Monitoring stopped")


stop_event = threading.Event()

thread = threading.Thread(
    target=monitor_tea_temperature,
    args=(stop_event,),
)

thread.start()

time.sleep(5)

stop_event.set()
thread.join()

print("Main program done")
```

This is safer than running an infinite non-daemon thread forever.

---

# 13. Important Notes

## Default Thread Type

By default, Python threads are non-daemon.

```python id="mru1hs"
thread = threading.Thread(target=worker)
```

This thread will keep the program alive.

## Daemon Must Be Set Before start()

This is correct:

```python id="j7kshc"
thread.daemon = True
thread.start()
```

This is also correct:

```python id="buc7q7"
thread = threading.Thread(
    target=worker,
    daemon=True,
)
thread.start()
```

This is incorrect:

```python id="hj493g"
thread.start()
thread.daemon = True
```

You must set daemon status before starting the thread.

---

# 14. Simple Rule

Use this rule:

```text id="ysuok8"
Important task → non-daemon thread
Background helper task → daemon thread
```

Daemon threads are convenient, but they should not be used for work that must complete.

---

# Key Takeaways

* Daemon threads run in the background.
* Daemon threads stop automatically when the main program exits.
* Non-daemon threads keep the program alive.
* Python threads are non-daemon by default.
* Use daemon threads for non-critical background work.
* Use non-daemon threads for important work that must finish.
* Set `daemon=True` before calling `start()`.
* Use `threading.Event` to stop long-running threads gracefully.
* Avoid daemon threads for saving files, writing databases, or payment-related work.
