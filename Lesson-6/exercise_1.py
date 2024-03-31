# def wrap(char):
#     def wrapper(func):
#         def inner():
#             print(char * 12)
#             func()
#             print(char * 12)
#         return inner
#     return wrapper
#
#
# @wrap("%")
# @wrap("*")
# def hello():
#     print("Hello World!")
#
#
# hello()
from datetime import datetime


def log(char):
    def decorator(func):
        def inner():
            print(f"- called function: hello at {char}")
            func()
            print(f"- finished function: hello at {char}")

        return inner

    return decorator


time = datetime.now().strftime("%X")


@log(time)
def hello():
    print("hello")


hello()
