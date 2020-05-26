

class Students:
	rollno = 0 
	def __init__(self,rollno,name,math,sci,social,eng,lang):
		self.name = name
		self.rollno = 0
		self.math = math
		self.sci = sci 
		self.social = social
		self.eng = eng
		self.lang = lang

	def accept(self,name,rollno,math,sci,social,eng,lang,dict1['ENTRIES']):
		self.name = input('Enter name of Student: ')
		self.rollno += 1
		self.math = int(input('Enter the marks scored by the Student in Mathematics: '))
		self.sci = int(input('Enter the marks scored by the Student in Science: '))
		self.social = int(input('Enter the marks scored by the Student in Social Science: '))
		self.eng = int(input('Enter the marks scored by the Student in English: '))
		self.lang = int(input('Enter the marks scored by the Student in language: '))

		dict1['ENTRIES'].append({'NAME: ':self.name,'ROLL NUMBER: ':self.rollno,'MATHEMATICS: ':self.math,'SCIENCE: ':self.sci,'SOCIAL SCIENCE: ':self.social,'ENGLISH: ':self.english,'LANGUAGE: ':self.lang})

	def display(self,dict1):
		print(dict1)







		