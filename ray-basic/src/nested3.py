import ray
import time

@ray.remote
def test_function():
    return "test result"

@ray.remote
def calling_test():
    return ray.get([test_function.remote() for _ in range(5)])

ray.init()
print(ray.get(calling_test.remote()))
