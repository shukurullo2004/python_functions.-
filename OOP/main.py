class Talaba:
    """More info about student"""

    def __init__(self, name, surname, No):
        self.name = name
        self.surname = surname
        self.No = No
        self.students = []

    def get_name(self):
        return self.name

    def get_no(self):
        return self.No

    def get_surname(self):
        return self.surname

    def add_students(self, student):
        self.students.append(student)

    # def __str__(self):
    #     student_info = f"Name: {self.name}\nSurname: {self.surname}\nNo: {self.No}"
    #     return student_info


student = Talaba('Azamat', 'Isoqulov', '21')
student.add_students('Shamsqamar')
print(student.get_surname())
