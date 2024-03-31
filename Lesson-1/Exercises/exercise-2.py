class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)


if __name__ == '__main__':
    queue = Queue()
    assert queue.size() == 0
    queue.enqueue(1)
    assert queue.size() == 1
    assert queue.dequeue() == 1
    assert queue.size() == 0
