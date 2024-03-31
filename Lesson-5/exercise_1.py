from itertools import count


# def infinite_loop():
#     for i in count():
#         print(i)


def cheksiz_loop():
    i = 0
    while True:
        yield i
        i += 1


# infinite_loop()
iterator = iter(cheksiz_loop())
for num in iterator:
    print(num)
