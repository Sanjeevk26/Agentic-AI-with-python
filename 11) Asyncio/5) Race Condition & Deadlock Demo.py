# Python Thread Profiling and Debugging
# Topics:
# 1. Profiling with cProfile
# 2. Race condition example
# 3. Fixing race condition with Lock
# 4. Deadlock example
# 5. Avoiding deadlock with consistent lock order
# 6. Thread-aware logging
# -------------------------------------------------

import logging
import threading
import time


# =================================================
# 1. Logging Setup
# =================================================

logging.basicConfig(
    level=logging.INFO,
    format=(
        "%(asctime)s "
        "[%(threadName)s] "
        "%(message)s"
    ),
    datefmt="%H:%M:%S",
)


# =================================================
# 2. Profiling Target Function
# =================================================

def slow_chai_preparation() -> None:
    """
    A simple function that can be profiled.

    To profile this file, run:

    python -m cProfile -s time python_thread_profiling_debugging.py
    """

    logging.info("Starting slow chai preparation")

    boil_water()
    grind_spices()
    brew_chai()

    logging.info("Finished slow chai preparation")


def boil_water() -> None:
    """
    Simulate waiting for water to boil.
    """

    time.sleep(0.5)


def grind_spices() -> None:
    """
    Simulate CPU-style work.
    """

    total = 0

    for number in range(500_000):
        total += number * number

    logging.info("Spice grinding total: %s", total)


def brew_chai() -> None:
    """
    Simulate brewing time.
    """

    time.sleep(0.5)


# =================================================
# 3. Race Condition Example
# =================================================

unsafe_chai_stock = 0


def unsafe_restock_chai() -> None:
    """
    Update shared state without a lock.

    This is intentionally unsafe.

    Race conditions may not appear every time,
    especially on small local examples.
    """

    global unsafe_chai_stock

    for _ in range(100_000):
        current_stock = unsafe_chai_stock

        # Encourage thread switching so the race
        # condition is easier to observe.
        time.sleep(0)

        unsafe_chai_stock = current_stock + 1


def run_race_condition_demo() -> None:
    """
    Demonstrate unsafe shared-state modification.
    """

    global unsafe_chai_stock

    logging.info("RACE CONDITION DEMO")
    logging.info("-" * 50)

    unsafe_chai_stock = 0

    threads = [
        threading.Thread(
            target=unsafe_restock_chai,
            name=f"UnsafeRestocker-{index}",
        )
        for index in range(1, 3)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    logging.info("Expected stock: 200000")
    logging.info("Actual stock:   %s", unsafe_chai_stock)
    logging.info(
        "The result may be lower because updates "
        "can overwrite each other."
    )


# =================================================
# 4. Safe Race Condition Fix with Lock
# =================================================

safe_chai_stock = 0
stock_lock = threading.Lock()


def safe_restock_chai() -> None:
    """
    Update shared state safely using a lock.
    """

    global safe_chai_stock

    for _ in range(100_000):
        with stock_lock:
            safe_chai_stock += 1


def run_safe_lock_demo() -> None:
    """
    Demonstrate safe shared-state modification.
    """

    global safe_chai_stock

    logging.info("SAFE LOCK DEMO")
    logging.info("-" * 50)

    safe_chai_stock = 0

    threads = [
        threading.Thread(
            target=safe_restock_chai,
            name=f"SafeRestocker-{index}",
        )
        for index in range(1, 3)
    ]

    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()

    logging.info("Expected stock: 200000")
    logging.info("Actual stock:   %s", safe_chai_stock)


# =================================================
# 5. Deadlock Example
# =================================================

lock_a = threading.Lock()
lock_b = threading.Lock()


def deadlock_task_one() -> None:
    """
    Acquire Lock A, then try to acquire Lock B.
    """

    logging.info("Task one trying to acquire Lock A")

    with lock_a:
        logging.info("Task one acquired Lock A")
        time.sleep(0.2)

        logging.info("Task one trying to acquire Lock B")

        with lock_b:
            logging.info("Task one acquired Lock B")


def deadlock_task_two() -> None:
    """
    Acquire Lock B, then try to acquire Lock A.

    This reverse order can cause deadlock.
    """

    logging.info("Task two trying to acquire Lock B")

    with lock_b:
        logging.info("Task two acquired Lock B")
        time.sleep(0.2)

        logging.info("Task two trying to acquire Lock A")

        with lock_a:
            logging.info("Task two acquired Lock A")


def run_deadlock_demo() -> None:
    """
    Demonstrate a deadlock pattern safely.

    The threads are daemon threads and join uses a
    timeout so this demo does not freeze forever.
    """

    logging.info("DEADLOCK DEMO")
    logging.info("-" * 50)

    thread_one = threading.Thread(
        target=deadlock_task_one,
        name="DeadlockTaskOne",
        daemon=True,
    )

    thread_two = threading.Thread(
        target=deadlock_task_two,
        name="DeadlockTaskTwo",
        daemon=True,
    )

    thread_one.start()
    thread_two.start()

    thread_one.join(timeout=2)
    thread_two.join(timeout=2)

    if thread_one.is_alive() or thread_two.is_alive():
        logging.info(
            "Deadlock detected: one or both threads "
            "are still waiting."
        )
    else:
        logging.info("No deadlock happened this time.")


# =================================================
# 6. Avoiding Deadlock with Consistent Lock Order
# =================================================

def safe_task_one() -> None:
    """
    Acquire locks in a consistent order:
    Lock A first, then Lock B.
    """

    logging.info("Safe task one trying Lock A")

    with lock_a:
        logging.info("Safe task one acquired Lock A")
        time.sleep(0.1)

        logging.info("Safe task one trying Lock B")

        with lock_b:
            logging.info("Safe task one acquired Lock B")


def safe_task_two() -> None:
    """
    Also acquire locks in the same order:
    Lock A first, then Lock B.
    """

    logging.info("Safe task two trying Lock A")

    with lock_a:
        logging.info("Safe task two acquired Lock A")
        time.sleep(0.1)

        logging.info("Safe task two trying Lock B")

        with lock_b:
            logging.info("Safe task two acquired Lock B")


def run_deadlock_fix_demo() -> None:
    """
    Demonstrate avoiding deadlock by using the same
    lock order in every thread.
    """

    logging.info("DEADLOCK FIX DEMO")
    logging.info("-" * 50)

    thread_one = threading.Thread(
        target=safe_task_one,
        name="SafeTaskOne",
    )

    thread_two = threading.Thread(
        target=safe_task_two,
        name="SafeTaskTwo",
    )

    thread_one.start()
    thread_two.start()

    thread_one.join()
    thread_two.join()

    logging.info("Both safe tasks completed.")


# =================================================
# 7. Lock Timeout Example
# =================================================

def task_with_lock_timeout() -> None:
    """
    Use lock.acquire(timeout=...) to avoid waiting
    forever for a lock.
    """

    logging.info("Trying to acquire Lock A with timeout")

    acquired = lock_a.acquire(timeout=1)

    if not acquired:
        logging.info("Could not acquire Lock A in time")
        return

    try:
        logging.info("Acquired Lock A safely")
        time.sleep(0.2)

    finally:
        lock_a.release()
        logging.info("Released Lock A")


def run_lock_timeout_demo() -> None:
    """
    Demonstrate lock acquisition with timeout.
    """

    logging.info("LOCK TIMEOUT DEMO")
    logging.info("-" * 50)

    thread = threading.Thread(
        target=task_with_lock_timeout,
        name="TimeoutWorker",
    )

    thread.start()
    thread.join()


# =================================================
# 8. Main Program
# =================================================

def main() -> None:
    """
    Run all profiling and debugging demonstrations.
    """

    logging.info("Python Thread Profiling and Debugging")
    logging.info("=" * 50)

    slow_chai_preparation()
    run_race_condition_demo()
    run_safe_lock_demo()
    run_deadlock_demo()
    run_deadlock_fix_demo()
    run_lock_timeout_demo()

    logging.info("Program completed.")


if __name__ == "__main__":
    main()


# =================================================
# Profiling Commands
# =================================================

# Run this file normally:
#
# python python_thread_profiling_debugging.py
#
#
# Run with built-in cProfile:
#
# python -m cProfile -s time python_thread_profiling_debugging.py
#
#
# Meaning:
#
# -m cProfile
# Runs Python's built-in profiler.
#
#
# -s time
# Sorts profiling output by time spent.
#
#
# Useful cProfile columns:
#
# ncalls:
# Number of calls.
#
# tottime:
# Total time spent in the function itself.
#
# percall:
# Time per call.
#
# cumtime:
# Total cumulative time, including sub-functions.
#
#
# =================================================
# Notes
# =================================================

# Profiling:
# Measures where your program spends time.
#
#
# Race condition:
# Happens when multiple threads modify shared data
# and the final result depends on timing.
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
# Deadlock:
# Happens when threads wait forever for locks held
# by each other.
#
#
# Avoid deadlock by:
# - Acquiring locks in the same order
# - Keeping locked sections small
# - Avoiding nested locks when possible
# - Using timeout where useful
# - Adding thread-aware logging
#
#
# Thread-aware logging:
#
# logging.basicConfig(
#     format="%(asctime)s [%(threadName)s] %(message)s"
# )
#
#
# External profiling tools:
# - py-spy
# - vprof
#
#
# Important:
# There is no silver bullet for concurrency bugs.
# Careful design, locking discipline, logging, and
# profiling are all required.
