import functools


def event(func):
    @functools.wraps(func)
    def wrapper():
        print("Hey")
        func()
        print("Hey")

    return wrapper

@event
def hello():
    print("Hello events!")

hello()
