# Python GIL Demo
# Topics:
# 1. Global Interpreter Lock
# 2. CPU-bound threading
# 3. CPU-bound multiprocessing
# 4. start() and join()
# 5. __main__ guard
# 6. Race condition reminder
# -------------------------------------------------

import os
import threading
import time
from multiprocessing import Process


# Keep this number moderate so the file remains
# runnable on most systems. Increase it if you want
# the timing difference to be more visible.
COUNT_LIMIT = 30_000_000


# =================================================
# 1. CPU-Bound Work Function
# =================================================

def crunch_numbers(label: str) -> None:
    """
    Perform CPU-bound work by incrementing a local
    counter many times.

    The counter is local to this function call.
    It is not shared between threads or processes.
    """

    print(f"{label} started.")

    count = 0

    for _ in range(COUNT_LIMIT):
        count += 1

    print(f"{label} finished. Final count: {count}")


# =================================================
# 2. Sequential Demo
# =================================================

def run_sequential_demo() -> None:
    """
    Run two CPU-heavy tasks one after another.
    """

    print("\nSEQUENTIAL CPU WORK")
    print("-" * 50)

    start_time = time.perf_counter()

    crunch_numbers("Sequential Task 1")
    crunch_numbers("Sequential Task 2")

    elapsed_time = time.perf_counter() - start_time

    print(
        f"Sequential total time: "
        f"{elapsed_time:.2f} seconds"
    )


# =================================================
# 3. Threading Demo
# =================================================

def run_threading_demo() -> None:
    """
    Run two CPU-heavy tasks using threads.

    In CPython, the GIL usually prevents these two
    threads from executing Python bytecode in true
    parallel inside one process.
    """

    print("\nTHREADING CPU WORK")
    print("-" * 50)

    start_time = time.perf_counter()

    thread_one = threading.Thread(
        target=crunch_numbers,
        args=("Barista Thread 1",),
        name="Barista 1",
    )

    thread_two = threading.Thread(
        target=crunch_numbers,
        args=("Barista Thread 2",),
        name="Barista 2",
    )

    thread_one.start()
    thread_two.start()

    thread_one.join()
    thread_two.join()

    elapsed_time = time.perf_counter() - start_time

    print(
        f"Threading total time: "
        f"{elapsed_time:.2f} seconds"
    )


# =================================================
# 4. Multiprocessing Task
# =================================================

def crunch_numbers_process(label: str) -> None:
    """
    Perform CPU-heavy work in a separate process.

    Each process has its own Python interpreter,
    memory space, and GIL.
    """

    process_id = os.getpid()

    crunch_numbers(
        f"{label} in process {process_id}"
    )


# =================================================
# 5. Multiprocessing Demo
# =================================================

def run_multiprocessing_demo() -> None:
    """
    Run two CPU-heavy tasks using two processes.

    This can run in true parallel when multiple CPU
    cores are available.
    """

    print("\nMULTIPROCESSING CPU WORK")
    print("-" * 50)

    start_time = time.perf_counter()

    process_one = Process(
        target=crunch_numbers_process,
        args=("Process Task 1",),
    )

    process_two = Process(
        target=crunch_numbers_process,
        args=("Process Task 2",),
    )

    process_one.start()
    process_two.start()

    process_one.join()
    process_two.join()

    elapsed_time = time.perf_counter() - start_time

    print(
        f"Multiprocessing total time: "
        f"{elapsed_time:.2f} seconds"
    )


# =================================================
# 6. Threading Is Still Useful for I/O-Bound Work
# =================================================

def wait_for_chai(order_number: int) -> None:
    """
    Simulate waiting for an external operation.

    time.sleep() represents waiting for something
    outside Python, such as a file, database, or API.
    """

    print(f"Order {order_number}: waiting started.")
    time.sleep(2)
    print(f"Order {order_number}: waiting finished.")


def run_io_threading_demo() -> None:
    """
    Demonstrate that threads can help with waiting-heavy
    I/O-style work.
    """

    print("\nTHREADING I/O-STYLE WORK")
    print("-" * 50)

    start_time = time.perf_counter()

    threads = [
        threading.Thread(
            target=wait_for_chai,
            args=(order_number,),
        )
        for order_number in range(1, 4)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    elapsed_time = time.perf_counter() - start_time

    print(
        f"I/O-style threading total time: "
        f"{elapsed_time:.2f} seconds"
    )


# =================================================
# 7. Race Condition Reminder
# =================================================

shared_counter = 0
counter_lock = threading.Lock()


def unsafe_increment() -> None:
    """
    This intentionally updates shared state without
    a lock.

    The GIL does not guarantee that user-level shared
    data is logically safe in every threaded program.
    """

    global shared_counter

    for _ in range(100_000):
        shared_counter += 1


def safe_increment() -> None:
    """
    Update shared state using a lock.
    """

    global shared_counter

    for _ in range(100_000):
        with counter_lock:
            shared_counter += 1


def run_race_condition_reminder() -> None:
    """
    Demonstrate the correct pattern for protecting
    shared mutable state.

    Exact race behaviour may vary by Python version
    and machine, so the important takeaway is the
    locking pattern.
    """

    global shared_counter

    print("\nSHARED STATE AND LOCKS")
    print("-" * 50)

    shared_counter = 0

    unsafe_threads = [
        threading.Thread(target=unsafe_increment)
        for _ in range(2)
    ]

    for thread in unsafe_threads:
        thread.start()

    for thread in unsafe_threads:
        thread.join()

    print(
        "Counter after unsafe increments:",
        shared_counter,
    )

    shared_counter = 0

    safe_threads = [
        threading.Thread(target=safe_increment)
        for _ in range(2)
    ]

    for thread in safe_threads:
        thread.start()

    for thread in safe_threads:
        thread.join()

    print(
        "Counter after safe increments:",
        shared_counter,
    )


# =================================================
# 8. Main Function
# =================================================

def main() -> None:
    """
    Run all GIL-related demonstrations.
    """

    print("Main process ID:", os.getpid())
    print("CPU count:", os.cpu_count())

    run_sequential_demo()
    run_threading_demo()
    run_multiprocessing_demo()
    run_io_threading_demo()
    run_race_condition_reminder()


# =================================================
# 9. Main Guard
# =================================================

# The __main__ guard is required for multiprocessing,
# especially on Windows and spawn-based platforms.

if __name__ == "__main__":
    main()


# =================================================
# Notes
# =================================================

# GIL:
# Global Interpreter Lock.
#
#
# In CPython:
# Only one thread at a time executes Python bytecode
# inside a single Python process.
#
#
# Threading:
# Useful for I/O-bound tasks such as:
# - API calls
# - Database calls
# - File waiting
# - Network operations
#
#
# CPU-bound threading:
# Usually does not speed up pure Python calculations
# in CPython because of the GIL.
#
#
# Multiprocessing:
# Creates separate processes.
# Each process has:
# - Its own interpreter
# - Its own memory
# - Its own GIL
#
#
# Multiprocessing can provide true parallelism
# for CPU-bound Python work when multiple CPU cores
# are available.
#
#
# Important:
# Multiprocessing does not remove the GIL.
# It avoids one shared GIL by using separate processes.
#
#
# __main__ guard:
#
# if __name__ == "__main__":
#     main()
#
# Required for safe multiprocessing startup.
#
#
# Race conditions:
# The GIL protects CPython internals.
# It does not remove the need for locks when your
# program modifies shared mutable data.
#
#
# Lock example:
#
# with threading.Lock():
#     shared_value += 1
#
#
# Performance note:
# Timings vary by computer, operating system,
# Python version, and current CPU load.
