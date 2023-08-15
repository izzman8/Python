from tkinter import *

window = Tk()
window.title("Check Status")

class app():


	def calc(self):

		if(age.get()>=18 and age.get()<120):
			status = "Eligable To Vote"
			Label(window,text="Name:").grid(row=3,column=0)
			Label(window,text=name.get()).grid(row=3,column=1)

			Label(window,text="Age:").grid(row=4,column=0)
			Label(window,text=age.get()).grid(row=4,column=1)

			Label(window,text="Status:").grid(row=5,column=0)
			Label(window,text=status).grid(row=5,column=1)

		elif(age.get()>=0 and age.get()<18):
			status = "Not Eligable To Vote"
			Label(window,text="Name:").grid(row=3,column=0)
			Label(window,text=name.get()).grid(row=3,column=1)

			Label(window,text="Age:").grid(row=4,column=0)
			Label(window,text=age.get()).grid(row=4,column=1)

			Label(window,text="Status:").grid(row=5,column=0)
			Label(window,text=status).grid(row=5,column=1)

		elif(age.get()<0):
			status = "Not valid"
			Label(window,text="Name:").grid(row=3,column=0)
			Label(window,text=name.get()).grid(row=3,column=1)

			Label(window,text="Age:").grid(row=4,column=0)
			Label(window,text=age.get()).grid(row=4,column=1)

			Label(window,text="Status:").grid(row=5,column=0)
			Label(window,text=status).grid(row=5,column=1)

		else:
			status = "Invalid"
			Label(window,text="Name:").grid(row=3,column=0)
			Label(window,text=name.get()).grid(row=3,column=1)

			Label(window,text="Age:").grid(row=4,column=0)
			Label(window,text=age.get()).grid(row=4,column=1)

			Label(window,text="Status:").grid(row=5,column=0)
			Label(window,text=status).grid(row=5,column=1)

	def window1(self):
		global name,age
		Label(window,text="Name:").grid(row=0,column=0)
		name=StringVar()
		Entry(window,textvariable=name).grid(row=0,column=1)

		Label(window,text="Age:").grid(row=1,column=0)
		age=IntVar()
		Entry(window,textvariable=age).grid(row=1,column=1)

		Button(window,text="Submit",command=self.calc).grid(row=2,column=1)

obj=app()
obj.window1()
mainloop()