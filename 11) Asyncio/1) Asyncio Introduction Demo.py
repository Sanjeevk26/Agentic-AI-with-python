# Python Asyncio Basics
# Topics:
# 1. async def
# 2. await
# 3. asyncio.run()
# 4. asyncio.sleep()
# 5. asyncio.gather()
# 6. Blocking vs non-blocking code
# 7. Optional aiohttp example
# -------------------------------------------------

import asyncio
import time


# =================================================
# 1. First Coroutine
# =================================================

async def brew_chai() -> None:
    """
    A coroutine is a special function that can pause
    and resume.

    async def creates a coroutine function.
    """

    print("Brewing chai...")

    # Non-blocking wait.
    await asyncio.sleep(2)

    print("Chai is ready")


def run_first_coroutine_demo() -> None:
    """
    Run one coroutine using asyncio.run().
    """

    print("\nFIRST COROUTINE")
    print("-" * 50)

    asyncio.run(brew_chai())


# =================================================
# 2. Multiple Coroutines with gather()
# =================================================

async def brew_named_chai(chai_name: str) -> None:
    """
    Brew one named chai using a non-blocking wait.
    """

    print(f"Brewing {chai_name}...")

    await asyncio.sleep(2)

    print(f"{chai_name} is ready")


async def run_multiple_brews() -> None:
    """
    Run multiple coroutines concurrently.
    """

    await asyncio.gather(
        brew_named_chai("Masala Chai"),
        brew_named_chai("Green Chai"),
        brew_named_chai("Ginger Chai"),
    )


def run_gather_demo() -> None:
    """
    Demonstrate asyncio.gather().
    """

    print("\nMULTIPLE COROUTINES WITH gather()")
    print("-" * 50)

    start_time = time.perf_counter()

    asyncio.run(run_multiple_brews())

    elapsed = time.perf_counter() - start_time

    print(
        f"Total time with async sleep: "
        f"{elapsed:.2f} seconds"
    )


# =================================================
# 3. Blocking Sleep Inside async def
# =================================================

async def blocking_brew(chai_name: str) -> None:
    """
    This is intentionally bad async code.

    time.sleep() blocks the whole thread and prevents
    other coroutines from running during the sleep.
    """

    print(f"Blocking brew started: {chai_name}")

    time.sleep(2)

    print(f"Blocking brew finished: {chai_name}")


async def run_blocking_brews() -> None:
    """
    Run blocking operations using gather().

    Because time.sleep() blocks, these tasks behave
    mostly sequentially.
    """

    await asyncio.gather(
        blocking_brew("Masala Chai"),
        blocking_brew("Green Chai"),
        blocking_brew("Ginger Chai"),
    )


def run_blocking_demo() -> None:
    """
    Compare blocking sleep against async sleep.
    """

    print("\nBLOCKING time.sleep() INSIDE async def")
    print("-" * 50)

    start_time = time.perf_counter()

    asyncio.run(run_blocking_brews())

    elapsed = time.perf_counter() - start_time

    print(
        f"Total time with blocking sleep: "
        f"{elapsed:.2f} seconds"
    )


# =================================================
# 4. Non-Blocking Sleep with Task List
# =================================================

async def non_blocking_brew(
    chai_name: str,
    delay: float,
) -> str:
    """
    Return a result after a non-blocking delay.
    """

    print(f"Started {chai_name}")

    await asyncio.sleep(delay)

    print(f"Finished {chai_name}")

    return f"{chai_name} ready"


async def run_task_list_demo() -> None:
    """
    Build a list of coroutine objects and unpack them
    into asyncio.gather().
    """

    chai_orders = [
        ("Masala Chai", 2),
        ("Ginger Chai", 3),
        ("Elaichi Chai", 1),
    ]

    tasks = [
        non_blocking_brew(chai_name, delay)
        for chai_name, delay in chai_orders
    ]

    # *tasks unpacks the list into separate arguments.
    results = await asyncio.gather(*tasks)

    print("Results:")
    for result in results:
        print(result)


def run_unpacking_demo() -> None:
    """
    Demonstrate *tasks with asyncio.gather().
    """

    print("\nTASK LIST AND *tasks UNPACKING")
    print("-" * 50)

    start_time = time.perf_counter()

    asyncio.run(run_task_list_demo())

    elapsed = time.perf_counter() - start_time

    print(
        f"Total time with task list: "
        f"{elapsed:.2f} seconds"
    )


# =================================================
# 5. Event Loop-Friendly Workflow
# =================================================

async def fetch_from_database(order_id: int) -> dict:
    """
    Simulate a non-blocking database call.
    """

    print(f"Order {order_id}: fetching from database")

    await asyncio.sleep(1)

    return {
        "order_id": order_id,
        "chai": "Masala Chai",
        "status": "ready",
    }


async def handle_order(order_id: int) -> None:
    """
    Simulate handling one web request.
    """

    order = await fetch_from_database(order_id)

    print(
        f"Order {order['order_id']}: "
        f"{order['chai']} is {order['status']}"
    )


async def run_order_handler_demo() -> None:
    """
    Run several request handlers concurrently.
    """

    await asyncio.gather(
        handle_order(101),
        handle_order(102),
        handle_order(103),
    )


def run_web_style_demo() -> None:
    """
    Demonstrate async style used in web frameworks.
    """

    print("\nWEB-STYLE ASYNC WORKFLOW")
    print("-" * 50)

    start_time = time.perf_counter()

    asyncio.run(run_order_handler_demo())

    elapsed = time.perf_counter() - start_time

    print(
        f"Web-style workflow completed in "
        f"{elapsed:.2f} seconds"
    )


# =================================================
# 6. Optional aiohttp Demo
# =================================================

async def fetch_url_with_aiohttp(
    session,
    url: str,
) -> int:
    """
    Fetch a URL using aiohttp.

    aiohttp is a third-party package:
    pip install aiohttp
    """

    async with session.get(url) as response:
        await response.text()

        print(
            f"Fetched {url} "
            f"with status {response.status}"
        )

        return response.status


async def run_aiohttp_requests() -> None:
    """
    Run multiple async HTTP requests concurrently.
    """

    import aiohttp

    urls = [
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/2",
        "https://httpbin.org/delay/2",
    ]

    async with aiohttp.ClientSession() as session:
        tasks = [
            fetch_url_with_aiohttp(session, url)
            for url in urls
        ]

        statuses = await asyncio.gather(*tasks)

    print("Statuses:", statuses)


def run_optional_aiohttp_demo() -> None:
    """
    Run the aiohttp demo only if aiohttp is installed.

    This keeps the file runnable even without
    third-party dependencies.
    """

    print("\nOPTIONAL aiohttp HTTP REQUESTS")
    print("-" * 50)

    try:
        import aiohttp  # noqa: F401
    except ImportError:
        print(
            "aiohttp is not installed. "
            "Install it with: pip install aiohttp"
        )
        return

    start_time = time.perf_counter()

    asyncio.run(run_aiohttp_requests())

    elapsed = time.perf_counter() - start_time

    print(
        f"aiohttp requests completed in "
        f"{elapsed:.2f} seconds"
    )


# =================================================
# 7. Main Program
# =================================================

def main() -> None:
    """
    Run all asyncio demonstrations.
    """

    print("Python Asyncio Basics")
    print("=" * 50)

    run_first_coroutine_demo()
    run_gather_demo()
    run_blocking_demo()
    run_unpacking_demo()
    run_web_style_demo()
    run_optional_aiohttp_demo()


if __name__ == "__main__":
    main()


# =================================================
# Notes
# =================================================

# async def:
# Defines a coroutine function.
#
#
# Coroutine:
# A special function that can pause and resume.
#
#
# await:
# Pauses the current coroutine until the awaited
# operation completes.
#
#
# Important:
# await can only be used inside async def.
#
#
# asyncio.run():
# Starts an event loop and runs one coroutine.
#
#
# asyncio.sleep():
# A non-blocking sleep. Other coroutines can run
# while one coroutine is waiting.
#
#
# time.sleep():
# A blocking sleep. It blocks the current thread.
#
#
# asyncio.gather():
# Runs multiple awaitables concurrently and waits
# for all of them.
#
#
# *tasks:
# Unpacks a list of coroutines/tasks into separate
# arguments for gather().
#
#
# async with:
# Used for asynchronous context managers, such as
# aiohttp.ClientSession().
#
#
# Asyncio is best for:
# - API calls
# - Network requests
# - Database waits
# - File or external I/O
# - Web server request handling
#
#
# Asyncio is not mainly for:
# - CPU-heavy calculation
# - Image/video processing in pure Python
# - Large mathematical loops
#
# For CPU-heavy work, use multiprocessing or
# ProcessPoolExecutor.
