def readtxt():
	my = open("age.txt","w")
	my.write(" | type \t|  status    |\n")
	my.write(" |   1  \t|  Student   |\n")
	my.write(" |   2  \t|  Staff     |\n")
	my.write(" |   3  \t|  Teacher   |\n")
	my = open("age.txt","r")
	return(my)

def age(birth,current):
	age = current - birth
	return(age)

def writetxt(age):
	my = open("age.txt","w")
	my.write("\n\nName : " + str(name))
	my.write("\nType : " + str(types))
	my.write("\nCurrent year : " + str(current))
	my.write("\nYour age : " + str(age))
	my.close()
	my1 = open("age.txt","a")
	if(age>0 and age<=12):
		my1.write("\nYou are kid")
	elif(age>13 and age<=22):
		my1.write("\nYou are teenager")
	elif(age>22):
		my1.write("\nYou are adult")
	else:
		print("\nWrong input for age")

def outputtxt(age):
	my = open("age.txt","r")
	print(my.read())
	return()

def writedoc(age):
	my = open("age.doc","w")
	my.write("\n\nName : " + str(name))
	my.write("\nType : " + str(types))
	my.write("\nCurrent year : " + str(current))
	my.write("\nYour age : " + str(age))
	my.close()
	my1 = open("age.doc","a")
	if(age>0 and age<=17):
		my1.write("\nYou are too young,can't be a staff")
	elif(age>17 and age<=60):
		my1.write("\nYou are staff")
	elif(age>60):
		my1.write("\nYou are retired")
	else:
		print("\nWrong input for age")

def outputdoc(age):
	my = open("age.doc","r")
	print(my.read())
	return()

def writexls(age):
	my = open("age.xls","w")
	my.write("\n\nName : " + str(name))
	my.write("\nType : " + str(types))
	my.write("\nCurrent year : " + str(current))
	my.write("\nYour age : " + str(age))
	my.close()
	my1 = open("age.xls","a")
	if(age>0 and age<=17):
		my1.write("\nYou are too young,can't be a Teacher")
	elif(age>17 and age<=60):
		my1.write("\nYou are Teacher")
	elif(age>60):
		my1.write("\nYou are retired")
	else:
		print("\nWrong input for age")

def outputxls(age):
	my = open("age.xls","r")
	print(my.read())
	return()

my = readtxt()
print(my.read())

b=0
name=str(input("Enter your name : "))
types=str(input("Enter your type : "))

while(b == 0):
		try:
			current =int(input("Enter current year : "))
			b+=1
		except:
			print("please enter numbers only")
			b = 0

while(b == 1):
		try:
			birth =int(input("Enter your birth year : "))
			b+=1
		except:
			print("please enter numbers only")
			b = 1

age = age(birth,current)


if(types == '1'):
	types="Student"
	write = writetxt(age)
	display = outputtxt(age)

elif(types == '2'):
	types="Staff"
	write = writedoc(age)
	display = outputdoc(age)

elif(types == '3'):
	types="Teacher"
	write = writexls(age)
	display = outputxls(age)

else:
	print("wrong input for type")