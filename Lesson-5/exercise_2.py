def float_range(start, stop, step):
    while start < stop:
        yield start
        start += step


for i in float_range(1, 5, 0.5):
    print(i)

