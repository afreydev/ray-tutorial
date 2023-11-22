import ray
import time

@ray.remote
def main_function():
    print("Main function is going to sleep")
    time.sleep(30)
    print("I'm ready")
    result = ray.get(second_function.remote())
    return result

@ray.remote
def second_function():
    print("Second function is going to sleep")
    time.sleep(30)
    print("Second function is ready")
    return "second result"

# Automatically connect to the running Ray cluster.
ray.init()
print(ray.get(main_function.remote()))
