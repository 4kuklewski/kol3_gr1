# ArturRog

import unittest
from Diary import Diary
from Student import Student
from Subject import Subject


class TestDiaryProperData(unittest.TestCase):
    def __init__(self, init_test):
        super(TestDiaryProperData, self).__init__(init_test)

    def setUp(self):
        tmp_tuple1, tmp_tuple2 = TestDataInit.students_data_factory()
        self.test_list = [tmp_tuple1[0], tmp_tuple2[0]]
        self.diary = Diary(self.test_list)

    def tearDown(self):
        self.test_list = None
        self.diary = None

    def test_get_list_of_students_method(self):
        self.assertEqual(self.diary.get_list_of_students(), self.test_list)


class TestStudentProperData(unittest.TestCase):
    def __init__(self, init_test):
        super(TestStudentProperData, self).__init__(init_test)

    def setUp(self):
        test_data = TestDataInit.students_data_factory()[0]
        student, self.proper_student_output = test_data
        self.courses = TestDataInit.courses_data_factory()
        subjects = list()
        for key in student[2]:
            grades = student[2][key][0]
            attendances = student[2][key][1]
            subjects.append(Subject(key, grades, attendances))
        self.testing_student = Student(student[0], student[1], subjects)

    def tearDown(self):
        self.proper_student_output = None
        self.testing_student = None
        self.courses = None

    def test_get_total_average_score_method(self):
        testing = self.testing_student
        proper = self.proper_student_output['average']
        index = 0
        for course in self.courses:
            testing_value = float(testing.get_class_average_score(index))
            proper_value = proper[course]
            self.assertEqual(testing_value, proper_value)
            index += 1

    def test_get_class_average_score_method(self):
        testing_value = self.testing_student.get_total_average_score()
        proper_value = self.proper_student_output['average']['total']
        print proper_value, testing_value
        self.assertEqual(testing_value, proper_value)

    def test_get_name_and_surname_method(self):
        testing = self.testing_student.get_name_and_surname().split(' ')
        proper = (self.proper_student_output['name'], self.proper_student_output['surname'])
        testing_name, proper_name = testing[0], proper[0]
        self.assertEqual(testing_name, proper_name)
        testing_surname, proper_surname = testing[1], proper[1]
        self.assertEqual(testing_surname, proper_surname)

    def test_get_total_attendance_method(self):
        testing_value = self.testing_student.get_total_attendance()
        proper_value = self.proper_student_output['attendance']['total']
        self.assertEqual(testing_value, proper_value)


class TestStudentWrongData(unittest.TestCase):
    def __init__(self, init_test):
        super(TestStudentWrongData, self).__init__(init_test)

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_wrong_subject_list(self):
        testing_values = (list(), None)
        for testing_value in testing_values:
            testing_student = Student('name', 'surname', testing_value)
            testing_student.get_total_average_score()
            testing_student.get_class_average_score(0)
            testing_student.get_total_attendance()
            testing_student.get_name_and_surname()

    def test_wrong_names_subject_list(self):
        subject = TestDataInit.subject_data_factory()
        testing_values = (
            (None, None),
            ('name_ok', None),
            ('name_ok', 10)
        )
        for testing_value in testing_values:
            name, surname = testing_value
            testing_student = Student(name, surname, [subject])
            testing_student.get_name_and_surname()


class TestSubjectProperData(unittest.TestCase):
    def __init__(self, init_test):
        super(TestSubjectProperData, self).__init__(init_test)

    def setUp(self):
        name = 'python'
        scores = [5, 4, 3, 4, 5, 3.5, 2, 2, 5, 3, 4.5]
        attendances = [1, 1, 1, 0, 1, 0, 0, 0]

        self.proper_subject_output = (name, (4, 8), sum(scores) / len(scores))
        self.testing_subject = Subject(name, scores, attendances)

    def tearDown(self):
        self.proper_subject_output = None
        self.testing_subject = None

    def test_get_average_score_method(self):
        testing_value = self.testing_subject.get_average_score()
        proper_value = self.proper_subject_output[2]
        self.assertEqual(testing_value, proper_value)

    def test_get_attendance_method(self):
        testing_value = self.testing_subject.get_attendance()
        proper_value = self.proper_subject_output[1]
        self.assertEqual(testing_value, proper_value)

    def test_get_subject_name_method(self):
        testing_value = self.testing_subject.get_subject_name()
        proper_value = self.proper_subject_output[0]
        self.assertEqual(testing_value, proper_value)


class TestSubjectWrongData(unittest.TestCase):
    def __init__(self, init_test):
        super(TestSubjectWrongData, self).__init__(init_test)
        self.proper_scores = [2, 3, 4, 5, 3]
        self.proper_attendances = [1, 0, 1, 0, 1, 1, 1]
        self.proper_name = 'python'
        self.not_greater_msg = ' not greater than or equal to '

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_empty_attendance_list(self):
        subject = Subject(self.proper_name, self.proper_scores, list())
        testing_tuple = subject.get_attendance()
        proper_tuple = (0, 0)
        self.assertEqual(testing_tuple, proper_tuple)

    def test_negative_attendance_list(self):
        testing_list = [-1, 0, -1, 0, -20, 3]
        subject = Subject(self.proper_name, self.proper_scores, testing_list)
        present, total = subject.get_attendance()
        msg = '0' + self.not_greater_msg + str(present) + ' for ' + str(testing_list)
        self.assertGreaterEqual(present, 0, msg)

    def test_bigger_then_1_attendance_list(self):
        testing_list = [0, 0, 1, 10, 2, 3]
        subject = Subject(self.proper_name, self.proper_scores, testing_list)
        present, total = subject.get_attendance()
        msg = str(total) + self.not_greater_msg + str(present) + ' for ' + str(testing_list)
        self.assertGreaterEqual(total, present, msg)

    def test_empty_scores_list(self):
        subject = Subject(self.proper_name, list(), self.proper_attendances)
        subject.get_average_score()


class TestDataInit(object):
    @staticmethod
    def courses_data_factory():
        return ['python', 'cpp', 'java']

    @staticmethod
    def subject_data_factory():
        name = 'python'
        scores = [5, 4, 3, 4, 5, 3.5, 2, 2, 5, 3, 4.5]
        attendances = [1, 1, 1, 0, 1, 0, 0, 0]
        return Subject(name, scores, attendances)

    @staticmethod
    def students_data_factory():
        courses = TestDataInit.courses_data_factory()

        # STUDENT 1
        student_init_1, student_out_data_1 = TestDataInit.student_data_factory(
            ('Artur', 'Rog'),
            courses,
            ([3.5, 4, 5, 2], [5, 4, 3, 4, 5, 3.5, 4.5], [5, 4, 3, 4, 5, 3.5, 4.5, 4, 4, 4]),
            ([1, 1, 1, 1, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 0, 0])
        )

        # STUDENT 2
        student_init_2, student_out_data_2 = TestDataInit.student_data_factory(
            ('Adam', 'Malysz'),
            courses,
            ([3.5, 3.5, 4, 3, 5], [5, 4, 2, 3, 4, 5, 2, 3, 4.5], [5, 4, 3, 4, 5, 3.5, 2, 2, 5, 3, 4.5]),
            ([1, 1, 1, 1, 1, 0, 0, 1], [1, 1, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 1, 0, 0, 0])
        )

        return (student_init_1, student_out_data_1), (student_init_2, student_out_data_2)

    @staticmethod
    def student_data_factory(names, courses, scores, attendances):
        name, surname = names
        c = courses
        python_scores, cpp_scores, java_scores = scores
        python_attendance, cpp_attendance, java_attendance = attendances

        student_out_data = dict()
        name = student_out_data['name'] = name
        surname = student_out_data['surname'] = surname
        python_attendance_tuple = len([i for i in python_attendance if i == 1]), len(python_attendance)
        cpp_attendance_tuple = len([i for i in cpp_attendance if i == 1]), len(cpp_attendance)
        java_attendance_tuple = len([i for i in java_attendance if i == 1]), len(java_attendance)
        student_out_data['attendance'] = {
            'total': (python_attendance_tuple[0] + cpp_attendance_tuple[0] + java_attendance_tuple[0],
                      python_attendance_tuple[1] + cpp_attendance_tuple[1] + java_attendance_tuple[1]),
            c[0]: python_attendance_tuple,
            c[1]: cpp_attendance_tuple,
            c[2]: java_attendance_tuple
        }
        total_average = list()
        total_average.extend(python_scores)
        total_average.extend(cpp_scores)
        total_average.extend(java_scores)
        student_out_data['average'] = {
            'total': sum(total_average) / len(total_average),
            c[0]: sum(python_scores) / len(python_scores),
            c[1]: sum(cpp_scores) / len(cpp_scores),
            c[2]: sum(java_scores) / len(java_scores)
        }
        student_init = [name, surname, {c[0]: [python_scores, python_attendance],
                                             c[1]: [cpp_scores, cpp_attendance],
                                             c[2]: [java_scores, java_attendance]}]
        return student_init, student_out_data


def test():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSubjectProperData))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestStudentProperData))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestDiaryProperData))

    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestSubjectWrongData))
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestStudentWrongData))
    unittest.TextTestRunner(verbosity=2).run(suite)

if __name__ == '__main__':
    test()
