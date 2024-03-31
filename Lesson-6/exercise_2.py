# from contextlib import contextmanager
# from datetime import datetime
# time = datetime.now().strftime("%X")
#
#
# @contextmanager
# def log():
#     try:
#         yield print(f"- context manager opened at {time}")
#     finally:
#         print(f"- context manager closed at {time}")
#
#
# with log():
#     print("hello")

for i in range(1, 10, 2):
    print(i-0.5)
    print(i)



# Output:
# - context manager opened at 8:43:35
# hello
# - context manager closed at 8:43:36