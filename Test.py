import unittest
from diary import Diary


class TestDiary(unittest.TestCase):
    def __init__(self, init_test):
        super(TestDiary, self).__init__(init_test)

    def setUp(self):
        self.students = {}
        self.student = None
        self.name = 'test_firstname'
        self.surname = 'test_secondname'
        # (self, name, surname, classes, attendance):
        self.diary = Diary(self.name, self.surname)
        pass

    def tearDown(self):
        self.diary = None

    def test_get_total_average_score_method(self):
        pass

    def test_get_average_score_class_method(self):
        pass

    def test_get_name_and_surname_method(self):
        pass

    def test_get_total_attendance_method(self):
        pass


def test():
    suite = unittest.TestSuite()
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(TestDiaty))
    unittest.TextTestRunner(verbosity=2).run(suite)
