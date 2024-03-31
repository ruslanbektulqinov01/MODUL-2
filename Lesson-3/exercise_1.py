class Student:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    @classmethod
    def from_full_name(cls, full_name):
        first_name, last_name = full_name.split()
        return cls(first_name, last_name)


student = Student.from_full_name('John Doe')
print(student.first_name)
print(student.last_name)
