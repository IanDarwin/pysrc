def function_trace(func):

    def wrapper(*args, **kwargs):
        print("Entering", func.__name__)
        result = func(*args, **kwargs)
        print("Exiting", func.__name__)
        return result

    return wrapper

@function_trace
def greetings(name):
    return f"Hello, {name}!"

greetings("Ian")
