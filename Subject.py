class Subject(object):
    def __init__(self, subject_name, grades, attendance):
        super(Subject, self).__init__()
        self.subject_name = subject_name
        self.grades = grades
        self.attendance = attendance

    def get_average_score(self):
        return reduce(lambda x, y: x + y, self.grades) / len(self.grades)

    def get_attendance(self):
        return sum(self.attendance), len(self.attendance)

    def get_subject_name(self):
        return self.subject_name
