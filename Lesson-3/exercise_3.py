class User:
    def __init__(self, full_name, age):
        self.full_name = full_name
        self.age = age

    def info(self):
        print(f'Name: {self.full_name}, Age: {self.age}')


class Teacher(User):
    def __init__(self, full_name, age, subject):
        super().__init__(full_name, age)
        self.subject = subject

    def teach(self):
        print(f"{self.full_name} is teaching {self.subject}")


class Mentor(Teacher):
    def __init__(self, full_name, age, subject, role):
        super().__init__(full_name, age, subject)
        self.role = role

    def mentor(self):
        print(f"{self.full_name} is mentoring students in {self.subject} as a {self.role}")


class Assistant(Teacher):
    def __init__(self, full_name, age, subject, assistant_role):
        super().__init__(full_name, age, subject)
        self.assistant_role = assistant_role

    def assist(self):
        print(f"{self.full_name} is assisting in {self.subject} as a {self.assistant_role}")


teacher1 = Teacher("John Doe", 30, "Mathematics")
teacher1.info()
teacher1.teach()

mentor1 = Mentor("Jane Smith", 35, "Science", "Senior Mentor")
mentor1.info()
mentor1.teach()
mentor1.mentor()

assistant1 = Assistant("Alice Johnson", 25, "Physics", "Teaching Assistant")
assistant1.info()
assistant1.teach()
assistant1.assist()
