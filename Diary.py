import os.path
import json
from Student import Student
from Subject import Subject


class Diary(object):
    def __init__(self, students):
        super(Diary, self).__init__()
        self.students = students

    def print_list_of_students(self):
        counter = 1
        for student in self.students:
            print str(counter) + " - " + student.get_name_and_surname()
            counter += 1

    def get_list_of_students(self):
        return self.students


def show_menu():
    print "1 - Show list of students"
    print "2 - Add student"
    print "3 - End"


def student_menu():
    print "1 - Get total average score"
    print "2 - Get class average score"
    print "3 - Get total attendance"
    print "4 - Get name and surname"


def show_subjects():
    print "1 - python"
    print "2 - cpp"
    print "3 - java"
    print "4 - przyroda"


def sample_list():
    student1 = ["Artur", "Rog", {'python': [[3.5, 4, 5, 2], [1, 1, 1, 1, 1, 0, 0, 1]],
                                 'cpp': [[5, 4, 3, 4, 5, 3.5, 4.5], [1, 1, 1, 0, 0, 1, 0, 1]],
                                 'java': [[5, 4, 3, 4, 5, 3.5, 4.5, 4, 4, 4], [1, 1, 1, 0, 1, 0, 0, 0]],
                                 'przyroda': [[5, 4, 2, 2, 3.5, 4.5], [1, 1, 1, 1, 1, 1, 1, 1]]}]
    student2 = ["Adam", "Malysz", {'python': [[3.5, 3.5, 4, 3, 5], [1, 1, 1, 1, 1, 0, 0, 1]],
                                   'cpp': [[5, 4, 2, 3, 4, 5, 2, 3, 4.5], [1, 1, 1, 0, 0, 1, 0, 1]],
                                   'java': [[5, 4, 3, 4, 5, 3.5, 2, 2, 5, 3, 4.5], [1, 1, 1, 0, 1, 0, 0, 0]],
                                   'przyroda': [[2, 3, 4, 4.5, 5, 4.5, 3.5], [1, 1, 1, 1, 1, 1, 1, 1]]}]
    student3 = ["Jan", "Nowak", {'python': [[3, 2, 4.5, 3.5, 5], [1, 0, 1, 1, 1, 0, 1, 1]],
                                 'cpp': [[4.5, 4.5, 2, 3.5, 4, 5, 2, 3, 4.5], [0, 1, 0, 1, 1, 1, 1, 1]],
                                 'java': [[5, 3, 3, 3, 2, 3.5, 2, 2, 2, 3, 4.5], [1, 1, 1, 1, 1, 1, 0, 1]],
                                 'przyroda': [[2, 3.5, 4.5, 4.5, 5, 4.5, 3.5], [1, 1, 1, 1, 1, 1, 1, 1]]}]
    student4 = ["Jakub", "Skalak", {'python': [[3, 2, 3, 3.5, 4], [1, 1, 1, 1, 1, 0, 1, 1]],
                                    'cpp': [[4.5, 4, 4, 3.5, 4, 5, 2, 3, 2], [1, 1, 0, 1, 1, 1, 1, 1]],
                                    'java': [[5, 3, 5, 4, 3, 4.5, 2, 2, 2, 3, 4.5], [1, 1, 1, 1, 1, 1, 0, 1]],
                                    'przyroda': [[2, 3.5, 4.5, 4, 5, 4, 3.5], [1, 1, 1, 1, 1, 0, 1, 1]]}]

    return [student1, student2, student3, student4]


def make_new_student():
    new_name = raw_input("Name of new student:")
    new_surname = raw_input("Surname of new student:")
    new_python_grades = map(float, raw_input("Enter python grades: ").split())
    new_python_attendance = map(int, raw_input("Enter python attendance: ").split())
    new_cpp_grades = map(float, raw_input("Enter cpp grades: ").split())
    new_cpp_attendance = map(int, raw_input("Enter cpp attendance: ").split())
    new_java_grades = map(float, raw_input("Enter java grades: ").split())
    new_java_attendance = map(int, raw_input("Enter java attendance: ").split())
    new_przyroda_grades = map(float, raw_input("Enter przyroda grades: ").split())
    new_przyroda_attendance = map(int, raw_input("Enter przyroda attendance: ").split())

    return [new_name, new_surname,
            {"python": [new_python_grades, new_python_attendance], "cpp": [new_cpp_grades, new_cpp_attendance],
             "java": [new_java_grades, new_java_attendance],
             "przyroda": [new_przyroda_grades, new_przyroda_attendance]}]


if __name__ == '__main__':
    filename = "text.txt"
    students = list()
    if os.path.isfile(filename):
        students = json.load(open(filename, 'r'))
    else:
        students = sample_list()

    list_of_students = list()
    list_of_subjects = list()
    for student in students:
        for subject in student[2]:
            list_of_subjects.append(Subject(subject, student[2][subject][0], student[2][subject][1]))
        list_of_students.append(Student(student[0], student[1], list_of_subjects))
        list_of_subjects = list()

    diary = Diary(list_of_students)
    while True:
        show_menu()
        option = input()
        if option == 1:
            print "\tLIST OF STUDENTS:\t"
            diary.print_list_of_students()
            option = input("Choose a student: ")
            student_menu()
            option2 = input()
            if option2 == 1:
                average = diary.get_list_of_students()[option - 1].get_total_average_score()
                print "Total average score: ", average
            if option2 == 2:
                show_subjects()
                option3 = input("Choose a subject: ")
                diary.get_list_of_students()[option - 1].get_class_average_score(option3 - 1)
            #     print str(self.subjects[id].get_subject_name()) + " average score: "
            elif option2 == 3:
                att, tot = diary.get_list_of_students()[option - 1].get_total_attendance()
                print "Attendance: " + str(att) + " hours out of " + str(tot) + " total."
            elif option2 == 4:
                print "Name and surname of student: " + str(
                    diary.get_list_of_students()[option - 1].get_name_and_surname())
            print
        elif option == 2:
            # Zeby zobaczyc nowego studenta trzeba jeszcze raz odpalic program
            new_list = students[:]
            new_list.append(make_new_student())
            json.dump(new_list, open("text.txt", 'w'))

        elif option == 3:
            break
