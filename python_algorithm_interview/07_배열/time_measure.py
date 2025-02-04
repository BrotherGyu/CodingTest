import time

def measure_execution_time(func, *args, **kwargs):
    """
    Measures the execution time of a given function in milliseconds.
    
    Parameters:
    - func: The function to be executed.
    - *args: Positional arguments for the function.
    - **kwargs: Keyword arguments for the function.
    
    Returns:
    - result: The output of the function.
    - execution_time_ms: The execution time in milliseconds.
    """
    start_time = time.time()
    result = func(*args, **kwargs)
    end_time = time.time()
    execution_time_ms = (end_time - start_time) * 1000  # Convert to milliseconds
    return result, execution_time_ms