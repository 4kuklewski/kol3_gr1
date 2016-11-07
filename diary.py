

class Diary(object):

	def __init__(self, name, surname, classes, attendance):
		super(Diary, self).__init__()
		self.classes_and_notes = classes
		self.total_attendance = attendance
		self.name = name
		self.surname = surname


	def get_total_average_score(self):
		avg = 0.
		number_of_notes = 0
		for key in self.classes_and_notes:
			avg += sum(self.classes_and_notes[key])
			number_of_notes += len(key)
		return avg/number_of_notes

	def get_average_score_class(self, class_name):
		avg = 0
		for val in self.classes_and_notes[class_name]:
			avg+=val

		return avg/len(self.classes_and_notes[class_name])

	def get_name_and_surname(self):
		return self.name + " " + self.surname

	def get_total_attendance(self):
		return (sum([sum(self.total_attendance[key]) for key in self.total_attendance]), sum([len(self.total_attendance[key]) for key in self.total_attendance]))





		

