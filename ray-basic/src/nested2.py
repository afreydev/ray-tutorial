import ray
import time

@ray.remote
def test_function():
    return "test result"

@ray.remote
def calling_test():
    return [test_function.remote() for _ in range(5)]

# Automatically connect to the running Ray cluster.
ray.init()
references = ray.get(calling_test.remote())

print(references)
for ref in references:
    print(ray.get(ref))
