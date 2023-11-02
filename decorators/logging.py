def function_trace(func):

    def wrapper(*args, **kwargs):
        print("Entering", func.__name__)
        result = func(*args, **kwargs)
        print("Exited", func.__name__)
        return result

    return wrapper

@function_trace
def greetings(name):
    print("Executing in greetings function")
    return f"Hello, {name}!"

print(greetings("Ian"))
