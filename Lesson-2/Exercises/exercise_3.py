class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, other):
        return self.age == other.age

    def __lt__(self, other):
        return self.age < other.age

    def __gt__(self, other):
        return self.age > other.age


if __name__ == '__main__':
    john = Student(name="John", age=21)
    bob = Student(name="Bob", age=32)
    alice = Student(name="Alice", age=21)

    print(john > bob)
    print(john < bob)
    print(john == alice)
