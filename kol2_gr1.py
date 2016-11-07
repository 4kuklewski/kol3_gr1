#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.


import diary 


class Diary_App(object):


	def __init__(self):
		super(Diary_App, self).__init__()
		self.students = {}
		self.choice = None
		self.student = None


	def start(self):
		print "Pick a student\n"
		self.list_of_students()
		print ""
		while True:
			self.choice = raw_input()

			if int(self.choice) >= 0 and int(self.choice) < len(self.students):
				condition2 = True
				while condition2:
					self.student = diary.Diary(self.students[int(self.choice)][0],self.students[int(self.choice)][1],self.students[int(self.choice)][2],self.students[int(self.choice)][3])
					print "Current student: {}".format(self.student.get_name_and_surname())
					print "1 - Total Average Score"
					print "2 - Average Score For Class..."
					print "3 - Total Attendance"
					print "4 - Back to list of students"
					condition2 = int(raw_input())

					if condition2 > 4 or condition2 < 1:
						condition2 = False
					elif condition2 == 1:
						print "Total Average Score: ", self.student.get_total_average_score()
					elif condition2 == 2:
						print "1 - python"
						print "2 - cpp"
						print "3 - java"
						print "4 - przyroda"
					elif condition2 == 3:
						

			elif self.choice =='e':
				print "Goodbye!"
				break
			else:
				print "No such index in database."
				pass

			

	def list_of_students(self):
		file = open('student_list.txt', 'r')
		words = []
		for line in file:
			for word in line.split(' '):
				words.append(word)

		for iter in range(0,len(words),4):
			self.students[iter/4] = [words[iter],words[iter+1],words[iter+2],words[iter+3]]

		for key in self.students:
			print "Student {}: {} {} ".format(key,self.students[key][0],self.students[key][1])


if __name__ == '__main__':

	app = Diary_App()
	app.start()
	# my_diary = diary.Diary()
	# print "Welcome to {}'s diary.".format(my_diary.get_name_and_surname())
	# print "Total average score", my_diary.get_total_average_score()
	# print "Total average in python", my_diary.get_average_score_class("python")
	# print "Attendance {} out of {} total.".format(my_diary.get_total_attendance()[0], my_diary.get_total_attendance()[1])

		
	