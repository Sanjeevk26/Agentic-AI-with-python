# Python Multiprocessing
# Topics:
# 1. CPU-heavy work with threads
# 2. CPU-heavy work with processes
# 3. __main__ guard
# 4. multiprocessing.Queue
# 5. multiprocessing.Value
# 6. Shared counter with process-safe lock
# -------------------------------------------------

import os
import threading
import time
from multiprocessing import Process, Queue, Value


# Keep this moderate so the file runs on most systems.
# Increase this number if you want stronger timing differences.
CPU_LIMIT = 10**7


# =================================================
# 1. CPU-Heavy Function
# =================================================

def cpu_heavy(task_name: str) -> int:
    """
    Simulate CPU-heavy work.

    This is calculation-heavy, not waiting-heavy.
    """

    print(f"{task_name}: crunching numbers...")

    total = 0

    for number in range(CPU_LIMIT):
        total += number * number

    print(f"{task_name}: done")

    return total


# =================================================
# 2. CPU-Heavy Work with Threads
# =================================================

def run_thread_cpu_demo() -> None:
    """
    Run CPU-heavy work using threads.

    In CPython, this usually does not speed up
    pure Python CPU-heavy work because of the GIL.
    """

    print("\nCPU-HEAVY WORK WITH THREADS")
    print("-" * 50)

    start_time = time.time()

    threads = [
        threading.Thread(
            target=cpu_heavy,
            args=(f"Thread {index}",),
        )
        for index in range(1, 3)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()

    print(
        f"Threading time taken: "
        f"{end_time - start_time:.2f} seconds"
    )


# =================================================
# 3. CPU-Heavy Work with Processes
# =================================================

def run_process_cpu_demo() -> None:
    """
    Run CPU-heavy work using separate processes.

    Each process has its own Python interpreter,
    memory space, and GIL.
    """

    print("\nCPU-HEAVY WORK WITH PROCESSES")
    print("-" * 50)

    start_time = time.time()

    processes = [
        Process(
            target=cpu_heavy,
            args=(f"Process {index}",),
        )
        for index in range(1, 3)
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    end_time = time.time()

    print(
        f"Multiprocessing time taken: "
        f"{end_time - start_time:.2f} seconds"
    )


# =================================================
# 4. Queue Example
# =================================================

def prepare_chai(queue: Queue) -> None:
    """
    Put a result into a multiprocessing queue.

    A child process cannot directly return a value
    to the parent like a normal function, so it can
    place the result into a queue.
    """

    process_id = os.getpid()

    message = (
        f"Masala chai is ready "
        f"from process {process_id}"
    )

    queue.put(message)


def run_queue_demo() -> None:
    """
    Pass a Queue to a process and read the result
    back in the parent process.
    """

    print("\nQUEUE DEMO")
    print("-" * 50)

    queue = Queue()

    process = Process(
        target=prepare_chai,
        args=(queue,),
    )

    process.start()
    process.join()

    result = queue.get()

    print("Received from queue:")
    print(result)


# =================================================
# 5. Queue with Multiple Processes
# =================================================

def prepare_named_chai(
    queue: Queue,
    chai_name: str,
) -> None:
    """
    Put a named chai result into the queue.
    """

    process_id = os.getpid()

    queue.put(
        f"{chai_name} ready from process {process_id}"
    )


def run_multi_queue_demo() -> None:
    """
    Start multiple processes and collect all results
    from a shared queue.
    """

    print("\nMULTI-PROCESS QUEUE DEMO")
    print("-" * 50)

    queue = Queue()

    chai_names = [
        "Masala Chai",
        "Ginger Chai",
        "Elaichi Chai",
    ]

    processes = [
        Process(
            target=prepare_named_chai,
            args=(queue, chai_name),
        )
        for chai_name in chai_names
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print("Results from queue:")

    while not queue.empty():
        print(queue.get())


# =================================================
# 6. Shared Value Example
# =================================================

def increment_counter(counter: Value) -> None:
    """
    Increment a shared counter safely.

    counter.get_lock() gives access to the lock
    associated with the shared Value.
    """

    for _ in range(100_000):
        with counter.get_lock():
            counter.value += 1


def run_shared_value_demo() -> None:
    """
    Share a simple integer counter between processes.
    """

    print("\nSHARED VALUE DEMO")
    print("-" * 50)

    counter = Value("i", 0)

    processes = [
        Process(
            target=increment_counter,
            args=(counter,),
        )
        for _ in range(4)
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print("Expected counter:", 400_000)
    print("Final counter:", counter.value)


# =================================================
# 7. Unsafe Shared Value Example
# =================================================

def unsafe_increment_counter(counter: Value) -> None:
    """
    Increment a shared counter without using a lock.

    This is intentionally unsafe and should not be
    used for shared state updates.
    """

    for _ in range(100_000):
        counter.value += 1


def run_unsafe_shared_value_demo() -> None:
    """
    Demonstrate the unsafe pattern.

    The result may or may not appear wrong depending
    on timing and machine behavior, but the pattern
    is not reliable.
    """

    print("\nUNSAFE SHARED VALUE DEMO")
    print("-" * 50)

    counter = Value("i", 0)

    processes = [
        Process(
            target=unsafe_increment_counter,
            args=(counter,),
        )
        for _ in range(4)
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    print("Expected counter:", 400_000)
    print("Unsafe final counter:", counter.value)
    print(
        "Use counter.get_lock() when multiple "
        "processes update the same Value."
    )


# =================================================
# 8. Main Program
# =================================================

def main() -> None:
    """
    Run all multiprocessing examples.
    """

    print("Python Multiprocessing Demo")
    print("=" * 50)
    print("Main process ID:", os.getpid())

    run_thread_cpu_demo()
    run_process_cpu_demo()
    run_queue_demo()
    run_multi_queue_demo()
    run_shared_value_demo()
    run_unsafe_shared_value_demo()


# Multiprocessing code should be protected by
# the main guard, especially on Windows.
if __name__ == "__main__":
    main()


# =================================================
# Notes
# =================================================

# Thread:
# A lightweight execution unit inside one process.
#
#
# Process:
# A separate running program with its own memory.
#
#
# CPU-heavy work:
# Often better suited to multiprocessing than
# threading in CPython.
#
#
# Create a process:
#
# process = Process(
#     target=function_name,
#     args=("value",)
# )
#
#
# Start a process:
#
# process.start()
#
#
# Wait for a process:
#
# process.join()
#
#
# Main guard:
#
# if __name__ == "__main__":
#     main()
#
#
# Queue:
# Used to pass data between processes.
#
# queue.put(value)
# queue.get()
#
#
# Value:
# Used to share a simple value between processes.
#
# counter = Value("i", 0)
# counter.value
#
#
# Lock with Value:
#
# with counter.get_lock():
#     counter.value += 1
#
#
# Important:
# Normal global variables are not automatically
# shared between processes.
#
#
# Multiprocessing is useful for:
# - CPU-heavy work
# - Image processing
# - Batch processing
# - Independent parallel jobs
#
#
# Multiprocessing may not be ideal for:
# - Very small tasks
# - I/O-heavy tasks
# - Tasks that constantly share data
# - Work where process startup overhead is too high
