import psutil
import os
from functools import wraps
from time import perf_counter


def measure_ram(func):
    """
    A decorator that measures the RAM usage of a function in MB.
    Requires psutil library: pip install psutil
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Get the current process
        process = psutil.Process(os.getpid())

        # Get memory info before execution
        mem_before = process.memory_info().rss / 1024 / 1024  # Convert to MB

        # Execute the function
        start_time = perf_counter()
        result = func(*args, **kwargs)
        end_time = perf_counter()

        # Get memory info after execution
        mem_after = process.memory_info().rss / 1024 / 1024  # Convert to MB

        # Calculate memory used
        mem_used = mem_after - mem_before

        print(f"Function '{func.__name__}':")
        print(f"  RAM Used: {mem_used:.2f} MB")
        print(f"  Execution Time: {end_time - start_time:.4f} seconds")

        return result

    return wrapper


# Example usage:
@measure_ram
def create_large_list(n):
    """Creates a list of n integers"""
    return [i for i in range(n)]


@measure_ram
def memory_intensive_operation():
    """Creates and manipulates large data structures"""
    data = [x * x for x in range(1000000)]
    return sum(data)


# Test the decorator
if __name__ == "__main__":
    # Test with different sizes
    result1 = create_large_list(1000000)
    result2 = memory_intensive_operation()