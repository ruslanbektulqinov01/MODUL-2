class Student:
    def __init__(self, first_name, last_name, age, grade):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.grade = grade

    def __str__(self):
        return f'{self.first_name}'

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def about(self):
        return f"{self.full_name} is student, age is {self.age}. Grade is {self.grade}."


student = Student("John", "Smith", 22, 2)

print(student.last_name)
