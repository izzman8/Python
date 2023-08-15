from tkinter import *

class app():

	def __init__(self,ids,name,salary):
		self.ids=ids
		self.name=name
		self.salary=salary

	def writetxt(self):
		my = open("myFile1220","w")
		my.write("\n\nYour Staff ID is = "+ str(self.ids))
		my.write("\nYour Name is = "+ str(self.name))
		my.write("\nYour Salary in month is = "+ str(self.salary))

	def outputtxt(self):
		my = open("myFile1220","r")
		print(my.read())
b=0
while(b == 0):
	try:
		ids = int(input("Your Staff Id : "))
		b=1
	except:
		print("ID must be numbers")
		b=0

name = str(input("Your Name : "))

while(b==1):
	try:	
		salary = int(input("Your Salary in Month : "))
		b=2
	except:
		print("Salary must be numbers")
		b=1

obj=app(ids,name,salary)
obj.writetxt()
obj.outputtxt()
