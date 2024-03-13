import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("Time elapsed: ", end_time - start_time)
        return result
    return wrapper

@timer
def my_function():
    time.sleep(2)

my_function()