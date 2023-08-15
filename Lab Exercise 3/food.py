def menuFood():
	print("\n ~~~~~~~~~ MENU ~~~~~~~~~")


	kl = open("menu.txt","w")

	kl.write("\n\nNo  | Food					\t| Price		|")
	kl.write("\n1  | Burger Set					| RM11.00	|")
	kl.write("\n2  | Pizza Set					| RM11.00	|")
	kl.write("\n3  | Spaghetti Bolognese Set	| RM12.00	|")
	kl.write("\n4  | Spaghetti Agilo Set 		| RM13.00	|")

	kl.write("\n\nNo  | Beverages			  	\t| Price					|")
	kl.write("\n1  | Coca Cola					| 						|")
	kl.write("\n1  | Pepsi						| Included in the set	|")
	kl.write("\n1  | Fanta Strawberry			| 						|")
	kl.write("\n1  | Fanta Orange				| 						|")
	kl.close()

	kl = open("menu.txt","r")
	print(kl.read())