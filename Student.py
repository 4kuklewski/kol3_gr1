class Student(object):

    def __init__(self, name, surname, subjects):
        super(Student, self).__init__()
        self.name = name
        self.surname = surname
        self.subjects = subjects

    def get_total_average_score(self):
        return sum([subject.get_average_score() for subject in self.subjects] ) /len(self.subjects)

    def get_class_average_score(self, id):
        return self.subjects[id].get_average_score()

    def get_name_and_surname(self):
        return str(self.name) + " " + str(self.surname)

    def get_total_attendance(self):
        all_subjects = [subject.get_attendance() for subject in self.subjects]
        att, tot = self.calc_attendance(reduce(lambda x, y: x + y, all_subjects))
        return att, tot

    def calc_attendance(self, tuple):
        att = tot = 0
        for i in range(len(tuple) / 2):
            att += tuple[i * 2]
            tot += tuple[i * 2 + 1]
        return (att, tot)
