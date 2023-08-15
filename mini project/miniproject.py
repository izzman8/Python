from tkinter import *
from tkinter import messagebox  
import mysql.connector

mydb = mysql.connector.connect(
	host="localhost",
	user="root",
	password="1234",
	database="bmi"
)
mycursor=mydb.cursor()
window=Tk()
window.geometry("300x300")
window.title("BMI CALCULATOR")
window['bg'] = "light blue"
frame = Frame()
frame.pack()

def centimeter(cm):
	cmeter = cm/100
	return(cmeter)

def gram(g):
	gram = g/1000
	return(gram)

def write(gram,cmeter):
	my = open("bmi.txt","a")
	my.write("\n\nYour height in Meter : " + str(cmeter))
	my.write("\nYour weight in KG : " + str(gram))
	my.close()

def output(gram,cmeter):
	my = open("bmi.txt","r")
	print(my.read())
	return()

my = open("bmi.txt","w")
my.write(" | bmi       \t|  status        |\n")
my.write(" | below 18.5\t|  underweight   |\n")
my.write(" | below 25.0\t|  normal weight |\n")
my.write(" | below 30.0\t|  over weight   |\n")
my.write(" | above 30.0\t|  obese         |")

my = open("bmi.txt","r")
print(my.read())

b=0
while(b == 0):
		try:
			cm =int(input("Enter your height in Centimeter : "))
			b+=1
		except:
			print("please enter numbers only")
			b = 0

while(b == 1):
		try:
			g =int(input("Enter your weight in Gram : "))
			b+=1
		except:
			print("please enter numbers only")
			b = 1

cmeter = centimeter(cm)
gram = gram(g)
write = write(gram,cmeter)
display = output(gram,cmeter)





class App():
		
	def window1(self):
		global weight, height, name
		Label(window, text="SYSTEM BMI CALCULATOR : ").pack(pady = 10)
		messagebox.showinfo("info", "Enter Name,Weight and Height")

		Label(window, text="Enter Name: ").pack()
		name = StringVar()
		Entry(window, textvariable = name).pack()

		Label(window, text="Weight in kg: ").pack()
		weight = DoubleVar()
		Entry(window, textvariable = weight).pack()

		Label(window, text = "Height in meter(float): ").pack(pady = 10)
		height = DoubleVar()
		Entry(window, textvariable = height).pack()

		Button(window, text = "Calculate: ", command = self.calculate, fg= "red").pack()
		Button(window, text = "Display: ", command = self.display, fg= "red").pack()


	def calculate(self):
		second = Tk()
		second.geometry("300x300")
		second.title("YOUR BMI")
		second['bg'] = "light blue"
		frame = Frame()
		frame.pack()

		name1 = StringVar()
		weight1 = DoubleVar()
		height1 = DoubleVar()
		BMI = DoubleVar()

		weight1 = weight.get()
		height1 = height.get()
		name1 = name.get()
		BMI = weight1 / (height1*height1)
		self.bmi_num = DoubleVar()
		self.bmi_text = StringVar()

		self.bmi_num= round(BMI,2)
		if (BMI < 18.5) : 
			self.bmi_text="You are underweight"
		elif (BMI >= 18.5 and BMI < 24.9): 
			self.bmi_text="You are normal"
		elif (BMI >= 24.9 and BMI < 30): 
			self.bmi_text="You are overweight"
		else:
			self.bmi_text="You are obese"

		Label(second, text = name1).pack(pady = 10)
		Label(second, text = self.bmi_text).pack(pady = 10)
		Label(second, text = self.bmi_num).pack(pady = 10)

		sql = "INSERT INTO acc (name, bmi_calc) VALUES (%s,%s)"
		val = (name1, BMI) 

		mycursor.execute(sql, val)

		mydb.commit()

		mycursor.execute("SELECT * FROM acc")
		myresult = mycursor.fetchall()

		Button(second, text = "Exit ", command = lambda: second.destroy(), fg= "red").pack()

	def display(self):
		mycursor.execute("SELECT * FROM acc")
		myresult = mycursor.fetchall()

		i=16
		for acc in myresult:
			for j in range(len(acc)):
				e = Entry(window,width=10,fg='black')
				e.pack(pady=i)
				e.insert(END,acc[j])
			i=i+1

app=App()
app.window1()
mainloop()