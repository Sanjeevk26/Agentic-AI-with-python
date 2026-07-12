# Python Threading Deep Dive
# Topics:
# 1. Basic threads
# 2. start() and join()
# 3. Passing arguments to threads
# 4. Threaded downloads
# 5. Shared state
# 6. threading.Lock
# -------------------------------------------------

import threading
import time
import urllib.error
import urllib.request


# =================================================
# 1. Basic Thread Functions
# =================================================

def boil_milk() -> None:
    """
    Simulate boiling milk.
    """

    print("Boiling milk...")
    time.sleep(2)
    print("Milk boiled")


def toast_bun() -> None:
    """
    Simulate toasting a bun.
    """

    print("Toasting bun...")
    time.sleep(3)
    print("Done with bun toast")


# =================================================
# 2. Sequential Breakfast Demo
# =================================================

def run_sequential_breakfast() -> None:
    """
    Run two tasks one after another.
    """

    print("\nSEQUENTIAL BREAKFAST")
    print("-" * 50)

    start_time = time.time()

    boil_milk()
    toast_bun()

    end_time = time.time()

    print(
        f"Breakfast ready in "
        f"{end_time - start_time:.2f} seconds"
    )


# =================================================
# 3. Threaded Breakfast Demo
# =================================================

def run_threaded_breakfast() -> None:
    """
    Run two waiting-heavy tasks using threads.
    """

    print("\nTHREADED BREAKFAST")
    print("-" * 50)

    start_time = time.time()

    thread_one = threading.Thread(
        target=boil_milk,
        name="MilkThread",
    )

    thread_two = threading.Thread(
        target=toast_bun,
        name="BunThread",
    )

    thread_one.start()
    thread_two.start()

    thread_one.join()
    thread_two.join()

    end_time = time.time()

    print(
        f"Breakfast ready in "
        f"{end_time - start_time:.2f} seconds"
    )


# =================================================
# 4. Passing Arguments to Threads
# =================================================

def prepare_chai(
    chai_type: str,
    wait_time: float,
) -> None:
    """
    Prepare a specific chai type.
    """

    thread_name = threading.current_thread().name

    print(
        f"[{thread_name}] "
        f"{chai_type} chai brewing..."
    )

    time.sleep(wait_time)

    print(
        f"[{thread_name}] "
        f"{chai_type} chai is ready"
    )


def run_thread_arguments_demo() -> None:
    """
    Pass arguments to thread target functions.
    """

    print("\nTHREAD ARGUMENTS")
    print("-" * 50)

    thread_one = threading.Thread(
        target=prepare_chai,
        args=("Masala", 2),
        name="MasalaThread",
    )

    thread_two = threading.Thread(
        target=prepare_chai,
        args=("Ginger", 3),
        name="GingerThread",
    )

    thread_one.start()
    thread_two.start()

    thread_one.join()
    thread_two.join()

    print("Both chai orders are ready.")


# =================================================
# 5. Threaded Download Function
# =================================================

def download_url(url: str) -> None:
    """
    Download data from a URL and print the byte size.

    This uses urllib from the Python standard library,
    so no third-party package is required.
    """

    thread_name = threading.current_thread().name

    print(f"[{thread_name}] Starting download from {url}")

    try:
        with urllib.request.urlopen(
            url,
            timeout=10,
        ) as response:
            data = response.read()

    except urllib.error.URLError as error:
        print(
            f"[{thread_name}] Download failed "
            f"from {url}: {error}"
        )
        return

    print(
        f"[{thread_name}] Finished download from "
        f"{url}. Size: {len(data)} bytes"
    )


def run_threaded_download_demo() -> None:
    """
    Download multiple URLs concurrently using threads.
    """

    print("\nTHREADED DOWNLOADS")
    print("-" * 50)

    urls = [
        "https://httpbin.org/image/jpeg",
        "https://httpbin.org/image/png",
        "https://httpbin.org/image/svg",
    ]

    threads: list[threading.Thread] = []

    start_time = time.time()

    for index, url in enumerate(urls, start=1):
        thread = threading.Thread(
            target=download_url,
            args=(url,),
            name=f"DownloadThread-{index}",
        )

        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()

    print(
        f"All downloads completed in "
        f"{end_time - start_time:.2f} seconds"
    )


# =================================================
# 6. Shared State with Lock
# =================================================

counter = 0
counter_lock = threading.Lock()


def increment_counter() -> None:
    """
    Increment a shared counter safely.

    The lock ensures only one thread modifies the
    counter at a time.
    """

    global counter

    for _ in range(100_000):
        with counter_lock:
            counter += 1


def run_lock_demo() -> None:
    """
    Demonstrate protecting shared data with a lock.
    """

    global counter

    print("\nTHREAD LOCK DEMO")
    print("-" * 50)

    counter = 0

    threads = [
        threading.Thread(
            target=increment_counter,
            name=f"CounterThread-{index}",
        )
        for index in range(1, 11)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Expected counter:", 1_000_000)
    print("Final counter:", counter)


# =================================================
# 7. Unsafe Counter Demo
# =================================================

unsafe_counter = 0


def unsafe_increment_counter() -> None:
    """
    Increment shared state without a lock.

    This is not recommended for shared mutable data.
    """

    global unsafe_counter

    for _ in range(100_000):
        unsafe_counter += 1


def run_unsafe_counter_demo() -> None:
    """
    Show the unsafe pattern.

    On some Python versions and machines, this may
    still appear correct. That does not make the
    pattern safe for real threaded programs.
    """

    global unsafe_counter

    print("\nUNSAFE COUNTER DEMO")
    print("-" * 50)

    unsafe_counter = 0

    threads = [
        threading.Thread(
            target=unsafe_increment_counter,
            name=f"UnsafeThread-{index}",
        )
        for index in range(1, 11)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    print("Expected counter:", 1_000_000)
    print("Unsafe final counter:", unsafe_counter)
    print(
        "Note: This may look correct sometimes, "
        "but shared mutable state should still be "
        "protected with a lock."
    )


# =================================================
# 8. Main Program
# =================================================

def main() -> None:
    """
    Run all threading demonstrations.
    """

    print("Python Threading Deep Dive")
    print("=" * 50)

    run_sequential_breakfast()
    run_threaded_breakfast()
    run_thread_arguments_demo()
    run_threaded_download_demo()
    run_lock_demo()
    run_unsafe_counter_demo()


if __name__ == "__main__":
    main()


# =================================================
# Notes
# =================================================

# Thread:
# A lightweight execution unit inside a process.
#
#
# Process:
# An independent running program with its own memory.
#
#
# Create a thread:
#
# thread = threading.Thread(
#     target=function_name
# )
#
#
# Start a thread:
#
# thread.start()
#
#
# Wait for a thread:
#
# thread.join()
#
#
# Pass arguments:
#
# thread = threading.Thread(
#     target=function_name,
#     args=("value",)
# )
#
#
# Important:
# args must be a tuple.
#
# For one argument:
#
# args=("value",)
#
#
# I/O-bound tasks:
# Threads are useful when tasks spend time waiting.
#
# Examples:
# - Web requests
# - File reading
# - File writing
# - Database calls
# - Network calls
#
#
# CPU-bound tasks:
# Threads usually do not speed up pure Python
# CPU-heavy work in CPython because of the GIL.
#
#
# Lock:
#
# lock = threading.Lock()
#
# with lock:
#     shared_value += 1
#
#
# Race condition:
# A bug caused when multiple threads access shared
# mutable data and the result depends on timing.
#
#
# Best practice:
# Use locks for shared mutable data and keep locked
# sections small.
