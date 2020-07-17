class Student:
    def __init__(self, name):
        self.name = name


class Graduate(Student):
    def __init__(self, name, graduation_date):
        super().__init__(name)
        self.graduation_date = graduation_date
