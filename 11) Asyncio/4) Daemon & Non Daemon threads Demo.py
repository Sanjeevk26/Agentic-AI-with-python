# Python Daemon and Non-Daemon Threads
# Topics:
# 1. Daemon threads
# 2. Non-daemon threads
# 3. Background monitoring
# 4. join()
# 5. Graceful stopping with threading.Event
# -------------------------------------------------

import threading
import time


# =================================================
# 1. Daemon Thread Example
# =================================================

def monitor_tea_temperature() -> None:
    """
    Simulate background monitoring.

    This function runs forever, so it is suitable
    for demonstrating a daemon thread.
    """

    while True:
        print("Monitoring tea temperature...")
        time.sleep(2)


def run_daemon_thread_demo() -> None:
    """
    Start a daemon thread.

    A daemon thread automatically stops when the
    main program exits.
    """

    print("\nDAEMON THREAD DEMO")
    print("-" * 50)

    thread = threading.Thread(
        target=monitor_tea_temperature,
        daemon=True,
        name="TeaTemperatureDaemon",
    )

    thread.start()

    time.sleep(1)

    print("Main program done for daemon demo.")
    print(
        "The daemon thread will stop automatically "
        "when the program exits."
    )


# =================================================
# 2. Non-Daemon Thread Example with Limited Loop
# =================================================

def monitor_temperature_limited() -> None:
    """
    Simulate a non-daemon task that eventually ends.

    This avoids creating an infinite program while
    still showing how non-daemon threads work.
    """

    for reading_number in range(1, 4):
        print(
            f"Non-daemon monitor reading "
            f"{reading_number}..."
        )
        time.sleep(1)

    print("Non-daemon monitor finished.")


def run_non_daemon_thread_demo() -> None:
    """
    Start a normal non-daemon thread.

    Python waits for non-daemon threads to finish
    before the program fully exits.
    """

    print("\nNON-DAEMON THREAD DEMO")
    print("-" * 50)

    thread = threading.Thread(
        target=monitor_temperature_limited,
        name="TeaTemperatureWorker",
    )

    thread.start()

    print("Main work is done, but thread is still running.")

    thread.join()

    print("Non-daemon thread completed.")


# =================================================
# 3. Daemon Flag Check
# =================================================

def run_daemon_flag_check() -> None:
    """
    Show daemon status of different threads.
    """

    print("\nDAEMON FLAG CHECK")
    print("-" * 50)

    daemon_thread = threading.Thread(
        target=monitor_temperature_limited,
        daemon=True,
        name="DaemonThread",
    )

    normal_thread = threading.Thread(
        target=monitor_temperature_limited,
        name="NormalThread",
    )

    print(
        f"{daemon_thread.name} daemon status:",
        daemon_thread.daemon,
    )

    print(
        f"{normal_thread.name} daemon status:",
        normal_thread.daemon,
    )


# =================================================
# 4. Graceful Stop Using threading.Event
# =================================================

def monitor_with_stop_event(
    stop_event: threading.Event,
) -> None:
    """
    Monitor repeatedly until stop_event is set.
    """

    while not stop_event.is_set():
        print("Gracefully monitoring tea temperature...")
        time.sleep(1)

    print("Monitoring stopped gracefully.")


def run_graceful_stop_demo() -> None:
    """
    Use threading.Event to stop a thread safely.
    """

    print("\nGRACEFUL STOP DEMO")
    print("-" * 50)

    stop_event = threading.Event()

    thread = threading.Thread(
        target=monitor_with_stop_event,
        args=(stop_event,),
        name="GracefulMonitor",
    )

    thread.start()

    time.sleep(4)

    print("Requesting monitor to stop...")
    stop_event.set()

    thread.join()

    print("Main program continued after graceful stop.")


# =================================================
# 5. Main Program
# =================================================

def main() -> None:
    """
    Run all daemon and non-daemon demonstrations.
    """

    print("Python Daemon and Non-Daemon Threads")
    print("=" * 50)

    run_daemon_flag_check()
    run_non_daemon_thread_demo()
    run_graceful_stop_demo()
    run_daemon_thread_demo()

    print("\nEnd of main program.")


if __name__ == "__main__":
    main()


# =================================================
# Notes
# =================================================

# Daemon thread:
# A background thread that automatically stops
# when the main program exits.
#
#
# Create daemon thread:
#
# thread = threading.Thread(
#     target=worker_function,
#     daemon=True,
# )
#
#
# Non-daemon thread:
# A normal thread that keeps the program alive
# until it finishes.
#
#
# By default:
# Python threads are non-daemon.
#
#
# daemon=True:
# Useful for non-critical background tasks.
#
#
# daemon=False:
# Useful for important tasks that should finish.
#
#
# Set daemon before start():
#
# thread.daemon = True
# thread.start()
#
#
# Do not set daemon after start():
#
# thread.start()
# thread.daemon = True
#
# This raises RuntimeError.
#
#
# join():
# Waits for a thread to finish.
#
#
# threading.Event:
# Useful for asking a thread to stop gracefully.
#
#
# Good daemon-thread examples:
# - Background logging
# - Monitoring
# - Health checks
# - Heartbeat messages
#
#
# Bad daemon-thread examples:
# - Saving important files
# - Database writes
# - Payment processing
# - Critical business operations
