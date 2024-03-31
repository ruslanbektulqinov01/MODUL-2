from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    first_name: str
    last_name: str
    age: int

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def greet(self, user_name):
        print(f"{self.first_name}: Hi, {user_name.first_name}!")


john = User("John", "Smith", 21)
bob = User("Bob", "Joe", 32)

john.greet(bob)
bob.greet(john)

# class Stack:
#     def __init__(self):
#         self.items = []
#
#     def push(self, item):
#         self.items.append(item)
#
#     def pop(self):
#         return self.items.pop()
#
#     def top(self):
#         return self.items[-1]
#
#     def size(self):
#         return len(self.items)
#
#     def empty(self):
#         return self.size() == 0
#
#
# def test_stack():
#     stack = Stack()
#     assert stack.size() == 0
#     assert stack.empty() == True
#
#     stack.push(1)
#     assert stack.size() == 1
#     assert stack.empty() == False
#     assert stack.top() == 1
#
#     stack.push(2)
#
#     assert stack.size() == 2
#     assert stack.empty() == False
#     assert stack.top() == 2
#
#     assert stack.pop() == 2
#
#     assert stack.size() == 1
#     assert stack.empty() == False
#     assert stack.top() == 1
#
#     assert stack.pop() == 1
#     assert stack.size() == 0
#     assert stack.empty() == True
#
#
# if __name__ == '__main__':
#     test_stack()
