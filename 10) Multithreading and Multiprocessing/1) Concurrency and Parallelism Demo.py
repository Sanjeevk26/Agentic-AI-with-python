# Python Concurrency and Parallelism
# Topics:
# 1. Sequential execution
# 2. Thread-based concurrency
# 3. Process-based parallelism
# 4. start() and join()
# 5. Thread and process arguments
# 6. Measuring execution time
# -------------------------------------------------

import os
import threading
import time
from multiprocessing import Process


# =================================================
# 1. Threading Tasks
# =================================================

def take_orders() -> None:
    """
    Simulate an I/O-bound order-taking operation.
    """

    for order_number in range(1, 4):
        print(
            f"[{threading.current_thread().name}] "
            f"Taking order {order_number}"
        )

        # Simulates waiting for input, payment,
        # a database, or another external operation.
        time.sleep(1)


def brew_orders() -> None:
    """
    Simulate an I/O-bound brewing operation.
    """

    for order_number in range(1, 4):
        print(
            f"[{threading.current_thread().name}] "
            f"Brewing chai for order {order_number}"
        )

        time.sleep(1.5)


# =================================================
# 2. Sequential Execution
# =================================================

def run_sequential_demo() -> None:
    """
    Run both tasks one after another.
    """

    print("\nSEQUENTIAL EXECUTION")
    print("-" * 50)

    start_time = time.perf_counter()

    take_orders()
    brew_orders()

    elapsed_time = time.perf_counter() - start_time

    print(
        f"Sequential execution completed in "
        f"{elapsed_time:.2f} seconds."
    )


# =================================================
# 3. Thread-Based Concurrency
# =================================================

def run_threading_demo() -> None:
    """
    Run the two waiting-heavy tasks concurrently.
    """

    print("\nTHREAD-BASED CONCURRENCY")
    print("-" * 50)

    start_time = time.perf_counter()

    order_thread = threading.Thread(
        target=take_orders,
        name="OrderThread",
    )

    brew_thread = threading.Thread(
        target=brew_orders,
        name="BrewThread",
    )

    # Starting a thread schedules its target function.
    order_thread.start()
    brew_thread.start()

    # Wait for both threads before continuing.
    order_thread.join()
    brew_thread.join()

    elapsed_time = time.perf_counter() - start_time

    print(
        f"Threading execution completed in "
        f"{elapsed_time:.2f} seconds."
    )

    print("All orders taken and chai brewed.")


# =================================================
# 4. Thread Function with Arguments
# =================================================

def prepare_named_chai(
    chai_name: str,
    waiting_time: float,
) -> None:
    """
    Prepare one named chai inside a thread.
    """

    print(
        f"[{threading.current_thread().name}] "
        f"Starting {chai_name}"
    )

    time.sleep(waiting_time)

    print(
        f"[{threading.current_thread().name}] "
        f"Finished {chai_name}"
    )


def run_thread_arguments_demo() -> None:
    """
    Pass positional arguments to thread targets.
    """

    print("\nTHREAD ARGUMENTS")
    print("-" * 50)

    chai_names = [
        "Masala Chai",
        "Ginger Chai",
        "Elaichi Chai",
    ]

    threads: list[threading.Thread] = []

    for chai_name in chai_names:
        thread = threading.Thread(
            target=prepare_named_chai,
            args=(chai_name, 1),
            name=f"{chai_name} Thread",
        )

        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print("All thread-based chai tasks completed.")


# =================================================
# 5. Multiprocessing Task
# =================================================

def brew_chai_process(
    chai_name: str,
    waiting_time: float,
) -> None:
    """
    Execute one chai task in a separate process.

    The process ID demonstrates that each task
    runs in a separate operating-system process.
    """

    process_id = os.getpid()

    print(
        f"[Process {process_id}] "
        f"Starting {chai_name}",
        flush=True,
    )

    time.sleep(waiting_time)

    print(
        f"[Process {process_id}] "
        f"Finished {chai_name}",
        flush=True,
    )


# =================================================
# 6. Process-Based Parallelism
# =================================================

def run_multiprocessing_demo() -> None:
    """
    Start several separate worker processes.
    """

    print("\nPROCESS-BASED EXECUTION")
    print("-" * 50)

    start_time = time.perf_counter()

    chai_names = [
        "Masala Chai",
        "Ginger Chai",
        "Elaichi Chai",
    ]

    processes: list[Process] = []

    for chai_name in chai_names:
        process = Process(
            target=brew_chai_process,
            args=(chai_name, 2),
        )

        processes.append(process)

    # Start all processes before waiting.
    for process in processes:
        process.start()

    # Wait until every process finishes.
    for process in processes:
        process.join()

    elapsed_time = time.perf_counter() - start_time

    print(
        f"Process execution completed in "
        f"{elapsed_time:.2f} seconds."
    )

    print("All process-based chai tasks completed.")


# =================================================
# 7. CPU-Bound Demonstration Function
# =================================================

def count_calculations(limit: int) -> int:
    """
    Perform a simple CPU-heavy calculation.

    A real application may instead process images,
    compress data, or perform mathematical analysis.
    """

    total = 0

    for number in range(limit):
        total += number * number

    return total


def run_cpu_process(
    worker_name: str,
    limit: int,
) -> None:
    """
    Run a calculation inside a separate process.
    """

    process_id = os.getpid()

    print(
        f"[Process {process_id}] "
        f"{worker_name} started",
        flush=True,
    )

    result = count_calculations(limit)

    print(
        f"[Process {process_id}] "
        f"{worker_name} completed. "
        f"Result: {result}",
        flush=True,
    )


def run_cpu_parallel_demo() -> None:
    """
    Demonstrate processes with CPU-bound work.

    The workload is intentionally moderate so the
    example remains practical on most computers.
    """

    print("\nCPU-BOUND PROCESS DEMO")
    print("-" * 50)

    start_time = time.perf_counter()

    processes = [
        Process(
            target=run_cpu_process,
            args=(f"Worker {number}", 2_000_000),
        )
        for number in range(1, 4)
    ]

    for process in processes:
        process.start()

    for process in processes:
        process.join()

    elapsed_time = time.perf_counter() - start_time

    print(
        f"CPU process demo completed in "
        f"{elapsed_time:.2f} seconds."
    )


# =================================================
# 8. Main Program
# =================================================

def main() -> None:
    """
    Run every concurrency and parallelism example.
    """

    print("Main process ID:", os.getpid())
    print("Available CPU count:", os.cpu_count())

    run_sequential_demo()
    run_threading_demo()
    run_thread_arguments_demo()
    run_multiprocessing_demo()
    run_cpu_parallel_demo()


# The main guard is essential for multiprocessing,
# especially on Windows and spawn-based platforms.
if __name__ == "__main__":
    main()


# =================================================
# Notes
# =================================================

# Concurrency:
# Multiple tasks make progress during overlapping
# periods of time.
#
#
# Parallelism:
# Multiple tasks physically execute at the same time,
# usually on different CPU cores.
#
#
# threading.Thread:
# Commonly useful for I/O-bound operations.
#
#
# multiprocessing.Process:
# Commonly useful for CPU-bound operations.
#
#
# start():
# Begins execution of a thread or process.
#
#
# join():
# Blocks until the selected thread or process ends.
#
#
# time.sleep():
# Simulates waiting. It does not perform CPU work.
#
#
# Thread target:
#
# thread = threading.Thread(
#     target=function_name
# )
#
#
# Thread arguments:
#
# thread = threading.Thread(
#     target=function_name,
#     args=("value",)
# )
#
#
# Process target:
#
# process = Process(
#     target=function_name,
#     args=("value",)
# )
#
#
# Important:
# Do not write target=function_name().
#
# That would call the function immediately and pass
# its returned value as the target.
#
#
# Correct:
#
# target=function_name
#
#
# CPython and the GIL:
# Threads are effective for waiting-heavy I/O work,
# but ordinary CPU-bound Python bytecode generally
# does not execute in parallel across threads within
# one CPython process.
#
#
# Multiprocessing:
# Separate processes can use separate CPU cores, but
# process creation and data transfer add overhead.
#
#
# Output order:
# Thread and process scheduling is nondeterministic.
# The print order may change between executions.
