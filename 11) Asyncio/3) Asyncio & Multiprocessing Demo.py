```python id="gbi2d9"
# python_asyncio_with_multiprocessing.py

# -------------------------------------------------
# Python Asyncio with Multiprocessing and Threads
# Topics:
# 1. ProcessPoolExecutor
# 2. asyncio.get_running_loop()
# 3. loop.run_in_executor()
# 4. asyncio.gather()
# 5. Background daemon thread
# 6. Async task running alongside a thread
# -------------------------------------------------

import asyncio
import hashlib
import threading
import time
from concurrent.futures import ProcessPoolExecutor


# =================================================
# 1. CPU-Heavy Function
# =================================================

def encrypt_data(data: str) -> str:
    """
    Simulate CPU-heavy encryption work.

    This function is intentionally synchronous.
    It is designed to run inside a separate process.
    """

    encoded_data = data.encode("utf-8")

    digest = encoded_data

    # Repeat hashing to simulate CPU-heavy work.
    for _ in range(500_000):
        digest = hashlib.sha256(digest).digest()

    return (
        f"encrypted({data}) = "
        f"{digest.hex()[:32]}..."
    )


# =================================================
# 2. Single ProcessPoolExecutor Task
# =================================================

async def run_single_process_task() -> None:
    """
    Offload one CPU-heavy function to a process pool.
    """

    print("\nSINGLE PROCESS TASK")
    print("-" * 50)

    start_time = time.perf_counter()

    loop = asyncio.get_running_loop()

    with ProcessPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool,
            encrypt_data,
            "credit-card-1234",
        )

    elapsed = time.perf_counter() - start_time

    print(result)
    print(f"Completed in {elapsed:.2f} seconds")


# =================================================
# 3. Multiple ProcessPoolExecutor Tasks
# =================================================

async def run_multiple_process_tasks() -> None:
    """
    Offload multiple CPU-heavy functions to a process
    pool and collect results using asyncio.gather().
    """

    print("\nMULTIPLE PROCESS TASKS")
    print("-" * 50)

    start_time = time.perf_counter()

    data_items = [
        "credit-card-1111",
        "credit-card-2222",
        "credit-card-3333",
    ]

    loop = asyncio.get_running_loop()

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

    elapsed = time.perf_counter() - start_time

    for result in results:
        print(result)

    print(f"Completed in {elapsed:.2f} seconds")


# =================================================
# 4. Background Thread Worker
# =================================================

def background_health_logger() -> None:
    """
    Run lightweight background logging in a daemon
    thread.

    This simulates a health logger that periodically
    reports application status.
    """

    while True:
        time.sleep(1)
        print("[background thread] System health OK")


# =================================================
# 5. Async Order Fetching
# =================================================

async def fetch_orders() -> None:
    """
    Simulate async order fetching.

    asyncio.sleep() is non-blocking, so the event loop
    can remain responsive while waiting.
    """

    print("\nASYNC ORDER FETCH")
    print("-" * 50)

    print("Fetching orders...")

    await asyncio.sleep(3)

    print("Orders fetched")


async def run_background_thread_demo() -> None:
    """
    Start a daemon thread and run async work while the
    thread keeps logging in the background.
    """

    print("\nBACKGROUND THREAD WITH ASYNCIO")
    print("-" * 50)

    thread = threading.Thread(
        target=background_health_logger,
        daemon=True,
        name="HealthLogger",
    )

    thread.start()

    await fetch_orders()

    print(
        "Async task completed. "
        "Daemon thread will stop when program exits."
    )


# =================================================
# 6. Combined Async, Thread, and Process Demo
# =================================================

async def call_payment_gateway(order_id: int) -> str:
    """
    Simulate an async payment API call.
    """

    print(f"Order {order_id}: calling payment API")

    await asyncio.sleep(2)

    return f"Order {order_id}: payment confirmed"


async def run_full_combined_demo() -> None:
    """
    Run async I/O work and CPU-heavy process work
    together.
    """

    print("\nCOMBINED ASYNC + PROCESS WORK")
    print("-" * 50)

    start_time = time.perf_counter()

    loop = asyncio.get_running_loop()

    with ProcessPoolExecutor() as pool:
        tasks = [
            call_payment_gateway(101),
            call_payment_gateway(102),
            loop.run_in_executor(
                pool,
                encrypt_data,
                "customer-sensitive-data-101",
            ),
            loop.run_in_executor(
                pool,
                encrypt_data,
                "customer-sensitive-data-102",
            ),
        ]

        results = await asyncio.gather(*tasks)

    elapsed = time.perf_counter() - start_time

    print("Results:")
    for result in results:
        print(result)

    print(f"Completed in {elapsed:.2f} seconds")


# =================================================
# 7. Main Coroutine
# =================================================

async def main() -> None:
    """
    Run all demonstrations.
    """

    print("Python Asyncio with Multiprocessing")
    print("=" * 50)

    await run_single_process_task()
    await run_multiple_process_tasks()
    await run_background_thread_demo()
    await run_full_combined_demo()


# =================================================
# 8. Program Entry Point
# =================================================

# The __main__ guard is required for multiprocessing,
# especially on Windows and spawn-based platforms.

if __name__ == "__main__":
    asyncio.run(main())


# =================================================
# Notes
# =================================================

# Asyncio:
# Handles asynchronous I/O and cooperative
# concurrency.
#
#
# ProcessPoolExecutor:
# Runs CPU-heavy functions in separate processes.
#
#
# Threading:
# Can run lightweight background work, such as
# health logging or monitoring.
#
#
# get_running_loop():
#
# loop = asyncio.get_running_loop()
#
#
# run_in_executor():
#
# result = await loop.run_in_executor(
#     pool,
#     function_name,
#     argument,
# )
#
#
# Important:
# Pass the function and arguments separately.
#
# Correct:
#
# loop.run_in_executor(pool, encrypt_data, data)
#
# Incorrect:
#
# loop.run_in_executor(pool, encrypt_data(data))
#
#
# ProcessPoolExecutor context manager:
#
# with ProcessPoolExecutor() as pool:
#     ...
#
# Parentheses are required.
#
#
# Main guard:
#
# if __name__ == "__main__":
#     asyncio.run(main())
#
# Required for safe multiprocessing.
#
#
# Daemon thread:
#
# threading.Thread(
#     target=worker,
#     daemon=True,
# )
#
# A daemon thread runs in the background and does
# not prevent the program from exiting.
#
#
# Use ProcessPoolExecutor for:
# - CPU-heavy work
# - Encryption
# - Image processing
# - Data crunching
# - ML-style prediction workloads
#
#
# Use asyncio for:
# - API calls
# - Database waits
# - Network requests
# - Async web apps
#
#
# Use threading for:
# - Background logging
# - Health checks
# - Blocking I/O helpers
```
