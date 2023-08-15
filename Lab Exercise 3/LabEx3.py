import food

my = open("order.txt","w")

print("\nWelcome To FastFood Restaurant")

print("\nYour must enter your detail to continue ")

name =str(input("\nPlease enter your name : "))
ic =int(input("Please enter your ic number: "))
address =str(input("Please enter your address: "))
number =int(input("please enter your phone number: "))
email =str(input("Please enter your email: "))

my.write("\nCustomer Detail")
my.write("\n\nName :" + str(name))
my.write("\nIC Number :" + str(ic))
my.write("\nAddress :" + str(address))
my.write("\nPhone Number :" + str(number))
my.write("\nEmail :" + str(email))
my.close()

food.menuFood()

a = 0
total = 0
b = 0

my = open("order.txt","a")
my.write("\n\nNo  | Food 	\t\t\t\t| Beverage	\t | Total Set \t | Total Price \t |")

while a < 10:

	print("\nPlease choose the set you want? \n")

	while(b == 0):
		try:
			id =int(input("Food id =  "))
			b+=1
		except:
			print("enter [1] for Burger Set, [2] for Pizza set, [3] for Spaghetti Bolognese set and [4] for Spaghetti Agilo set")
			b = 0

	bev =int(input("Beverage id = "))
	much =int(input("How many set do you want? : "))

	
	if (id == 1):
		try:
			my = open("order.txt","a")
			totalset = 11 * much
			total = total + totalset
			if (bev == 1):
				my.write("\n" + str(id) + "\t| " + "Burger Set" + "\t\t  | " + "Coca Cola" + "\t  |" + str(much) + "\t\t  | RM " + str(totalset) + "\t\t  |")
			elif (bev == 2):
				my.write("\n" + str(id) + "\t| " + "Burger Set" + "\t\t  | " + "Pepsi" + "\t  |" + str(much) + "\t\t  | RM " + str(totalset) + "\t\t  |")
			elif (bev == 3):
				my.write("\n" + str(id) + "\t| " + "Burger Set" + "\t\t  | " + "Fanta Strawberry" + "\t  |" + str(much) + "\t\t  | RM " + str(totalset) + "\t\t  |")
			elif (bev == 4):
				my.write("\n" + str(id) + "\t| " + "Burger Set" + "\t\t  | " + "Fanta Orange" + "\t  |" + str(much) + "\t\t  | RM " + str(totalset) + "\t\tt  |")
		except:
			my.close()

	elif (id == 2):
		try:
			my = open("order.txt","a")
			totalset = 11 * much
			total = total + totalset
			if (bev == 1):
				my.write("\n" + str(id) + "\t| " + "Pizza Set" + "\t\t  | " + "Coca Cola" + "\t  |" + str(much) + "\t\t  | RM " + str(totalset) + "\t\t  |")
			elif (bev == 2):
				my.write("\n" + str(id) + "\t| " + "Pizza Set" + "\t\t  | " + "Pepsi" + "\t  |" + str(much) + "\t\t  | RM " + str(totalset) + "\t\t  |")
			elif (bev == 3):
				my.write("\n" + str(id) + "\t| " + "Pizza Set" + "\t\t  | " + "Fanta Strawberry" + "\t  |" + str(much) + "\t\t  | RM " + str(totalset) + "\t\t  |")
			elif (bev == 4):
				my.write("\n" + str(id) + "\t| " + "Pizza Set" + "\t\t  | " + "Fanta Orange" + "\t  |" + str(much) + "\t\t  | RM " + str(totalset) + "\t\t  |")
		except:
			my.close()

	elif (id == 3):
		try:
			my = open("order.txt","a")
			totalset = 12 * much
			total = total + totalset			
			if (bev == 1):
				my.write("\n" + str(id) + "\t| " + "Spaghetti Bolognese Set" + "\t  | " + "Coca Cola" + "\t  |" + str(much) + "\t\t  | RM " + str(totalset) + "\t\t  |")
			elif (bev == 2):
				my.write("\n" + str(id) + "\t| " + "Spaghetti Bolognese Set" + "\t  | " + "Pepsi" + "\t  |" + str(much) + "\t\t  | RM " + str(totalset) + "\t\t  |")
			elif (bev == 3):
				my.write("\n" + str(id) + "\t| " + "Spaghetti Bolognese Set" + "\t  | " + "Fanta Strawberry" + "\t  |" + str(much) + "\t\t  | RM " + str(totalset) + "\t\t  |")
			elif (bev == 4):
				my.write("\n" + str(id) + "\t| " + "Spaghetti Bolognese Set" + "\t  | " + "Fanta Orange" + "\t  |" + str(much) + "\t\t  | RM " + str(totalset) + "\t\t  |")
		except:
			my.close()

	elif (id == 4):
		try:
			my = open("order.txt","a")
			totalset = 13 * much
			total = total + totalset
			if (bev == 1):
				my.write("\n" + str(id) + "\t| " + "Spaghetti Aglio Set" + "\t\t  | " + "Coca Cola" + "\t  |" + str(much) + "\t\t  | RM " + str(totalset) + "\t\t  |")
			elif (bev == 2):
				my.write("\n" + str(id) + "\t| " + "Spaghetti Aglio Set" + "\t\t  | " + "Pepsi" + "\t  |" + str(much) + "\t\t  | RM " + str(totalset) + "\t\t  |")
			elif (bev == 3):
				my.write("\n" + str(id) + "\t| " + "Spaghetti Aglio Set" + "\t\t  | " + "Fanta Strawberry" + "\t  |" + str(much) + "\t\t  | RM " + str(totalset) + "\t\t  |")
			elif (bev == 4):
				my.write("\n" + str(id) + "\t| " + "Spaghetti Aglio Set" + "\t\t  | " + "Fanta Orange" + "\t  |" + str(much) + "\t\t  | RM " + str(totalset) + "\t\t  |")
		except:
			my.close()

	done =int(input("Finish Order? 1=[NO] or 2=[YES] : "))

	if (done == 1):
		a += 1

	elif (done == 2):

		total = total + 4
		my = open("order.txt", "a")
		my.write("\n\n Total Price with delivery  = RM " + str(total))
		my.close()

		my = open("order.txt","r")
		print(my.read())

		a = 10