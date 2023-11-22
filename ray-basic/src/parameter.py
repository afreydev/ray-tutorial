import ray

@ray.remote
def first_name():
    return "Lucas"

@ray.remote
def last_name():
    return "Fernandez"

@ray.remote
def complete_name(name, lastname):
    return f"{name} {lastname}"


first_name_ref = first_name.remote()
last_name_ref = last_name.remote()


# You can pass an object ref as an argument to another Ray task.
complete_name_result = complete_name.remote(first_name_ref, last_name_ref)
assert ray.get(complete_name_result) == "Lucas Fernandez"