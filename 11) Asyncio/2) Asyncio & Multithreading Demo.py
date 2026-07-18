# Python Asyncio with Multithreading
# Topics:
# 1. Blocking functions
# 2. ThreadPoolExecutor
# 3. asyncio.get_running_loop()
# 4. loop.run_in_executor()
# 5. asyncio.gather()
# 6. asyncio.to_thread()
# -------------------------------------------------

import asyncio
import time
from concurrent.futures import ThreadPoolExecutor


# =================================================
# 1. Blocking Function
# =================================================

def check_stock(item: str) -> str:
    """
    Simulate a blocking stock check.

    This could represent a blocking database query,
    a legacy API call, or a slow synchronous SDK.
    """

    print(f"Checking {item} in store...")

    # This blocks the thread where it runs.
    time.sleep(3)

    return f"{item} stock: 42"


# =================================================
# 2. Bad Example: Blocking the Event Loop
# =================================================

async def bad_async_stock_check() -> None:
    """
    This is intentionally bad async code.

    The function is async, but it directly calls
    a blocking function. This blocks the event loop.
    """

    print("\nBAD ASYNC EXAMPLE")
    print("-" * 50)

    start_time = time.perf_counter()

    result = check_stock("Masala Chai")

    elapsed = time.perf_counter() - start_time

    print(result)
    print(f"Completed in {elapsed:.2f} seconds")


# =================================================
# 3. Good Example: run_in_executor()
# =================================================

async def stock_check_with_executor() -> None:
    """
    Run a blocking function in a separate thread
    using ThreadPoolExecutor.
    """

    print("\nrun_in_executor() EXAMPLE")
    print("-" * 50)

    start_time = time.perf_counter()

    loop = asyncio.get_running_loop()

    with ThreadPoolExecutor() as pool:
        result = await loop.run_in_executor(
            pool,
            check_stock,
            "Masala Chai",
        )

    elapsed = time.perf_counter() - start_time

    print(result)
    print(f"Completed in {elapsed:.2f} seconds")


# =================================================
# 4. Multiple Blocking Calls with ThreadPoolExecutor
# =================================================

async def multiple_stock_checks_with_executor() -> None:
    """
    Run several blocking calls concurrently using
    a thread pool executor.
    """

    print("\nMULTIPLE STOCK CHECKS WITH EXECUTOR")
    print("-" * 50)

    start_time = time.perf_counter()

    loop = asyncio.get_running_loop()

    items = [
        "Masala Chai",
        "Ginger Chai",
        "Elaichi Chai",
    ]

    with ThreadPoolExecutor(max_workers=3) as pool:
        tasks = [
            loop.run_in_executor(
                pool,
                check_stock,
                item,
            )
            for item in items
        ]

        results = await asyncio.gather(*tasks)

    elapsed = time.perf_counter() - start_time

    for result in results:
        print(result)

    print(f"Completed in {elapsed:.2f} seconds")


# =================================================
# 5. Using Default Executor
# =================================================

async def stock_check_with_default_executor() -> None:
    """
    Pass None as the executor to use asyncio's
    default thread pool executor.
    """

    print("\nDEFAULT EXECUTOR EXAMPLE")
    print("-" * 50)

    loop = asyncio.get_running_loop()

    result = await loop.run_in_executor(
        None,
        check_stock,
        "Green Chai",
    )

    print(result)


# =================================================
# 6. Simpler Alternative: asyncio.to_thread()
# =================================================

async def stock_check_with_to_thread() -> None:
    """
    Run a blocking function in a thread using
    asyncio.to_thread().

    This is simpler than run_in_executor() for
    common use cases.
    """

    print("\nasyncio.to_thread() EXAMPLE")
    print("-" * 50)

    start_time = time.perf_counter()

    result = await asyncio.to_thread(
        check_stock,
        "Tulsi Chai",
    )

    elapsed = time.perf_counter() - start_time

    print(result)
    print(f"Completed in {elapsed:.2f} seconds")


# =================================================
# 7. Multiple Calls with asyncio.to_thread()
# =================================================

async def multiple_stock_checks_with_to_thread() -> None:
    """
    Run multiple blocking functions concurrently
    using asyncio.to_thread().
    """

    print("\nMULTIPLE STOCK CHECKS WITH to_thread()")
    print("-" * 50)

    start_time = time.perf_counter()

    items = [
        "Kesar Chai",
        "Lemon Chai",
        "Cardamom Chai",
    ]

    tasks = [
        asyncio.to_thread(
            check_stock,
            item,
        )
        for item in items
    ]

    results = await asyncio.gather(*tasks)

    elapsed = time.perf_counter() - start_time

    for result in results:
        print(result)

    print(f"Completed in {elapsed:.2f} seconds")


# =================================================
# 8. Async Work Alongside Thread Work
# =================================================

async def async_timer(name: str, seconds: int) -> None:
    """
    A normal async task using non-blocking sleep.
    """

    print(f"{name} started")
    await asyncio.sleep(seconds)
    print(f"{name} finished")


async def mixed_async_and_thread_work() -> None:
    """
    Run async tasks and threaded blocking tasks
    together.
    """

    print("\nMIXED ASYNC AND THREAD WORK")
    print("-" * 50)

    start_time = time.perf_counter()

    tasks = [
        async_timer("Async timer 1", 2),
        async_timer("Async timer 2", 3),
        asyncio.to_thread(
            check_stock,
            "Rose Chai",
        ),
        asyncio.to_thread(
            check_stock,
            "Mint Chai",
        ),
    ]

    results = await asyncio.gather(*tasks)

    elapsed = time.perf_counter() - start_time

    print("Mixed results:")
    for result in results:
        if result is not None:
            print(result)

    print(f"Completed in {elapsed:.2f} seconds")


# =================================================
# 9. Main Coroutine
# =================================================

async def main() -> None:
    """
    Run all demonstrations.
    """

    print("Python Asyncio with Multithreading")
    print("=" * 50)

    await bad_async_stock_check()
    await stock_check_with_executor()
    await multiple_stock_checks_with_executor()
    await stock_check_with_default_executor()
    await stock_check_with_to_thread()
    await multiple_stock_checks_with_to_thread()
    await mixed_async_and_thread_work()


# =================================================
# 10. Program Entry Point
# =================================================

if __name__ == "__main__":
    asyncio.run(main())


# =================================================
# Notes
# =================================================

# Asyncio:
# Useful for non-blocking I/O and cooperative
# concurrency.
#
#
# Threading:
# Useful for blocking I/O functions that are not
# written using async/await.
#
#
# ThreadPoolExecutor:
#
# from concurrent.futures import ThreadPoolExecutor
#
# with ThreadPoolExecutor() as pool:
#     ...
#
#
# get_running_loop():
#
# loop = asyncio.get_running_loop()
#
# Gets the currently running event loop.
#
#
# run_in_executor():
#
# result = await loop.run_in_executor(
#     pool,
#     blocking_function,
#     arg1,
#     arg2,
# )
#
#
# Important:
# Pass the function and arguments separately.
#
# Correct:
#
# loop.run_in_executor(pool, check_stock, "Masala")
#
# Incorrect:
#
# loop.run_in_executor(pool, check_stock("Masala"))
#
#
# asyncio.to_thread():
#
# result = await asyncio.to_thread(
#     blocking_function,
#     arg1,
#     arg2,
# )
#
# This is a simpler way to run blocking functions
# in a separate thread.
#
#
# Use this pattern when:
# - You have async code
# - You must call blocking synchronous functions
# - The blocking work is mostly I/O-bound
#
#
# For CPU-heavy pure Python work:
# Prefer multiprocessing or ProcessPoolExecutor.
