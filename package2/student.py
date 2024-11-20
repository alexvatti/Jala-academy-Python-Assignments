class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def display_info(self):
        print(f"Student's Name: {self.name}, Grade: {self.grade}")