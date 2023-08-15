from abc import ABC
class membership(ABC):
	def calculate_netprice(self):
		pass

class platinum(membership):
	def calculate_netprice(self,price):
		self.price = price
		disc = price * 30 / 100
		total = price - disc
		return total

	def annual_reward(self,price):
		return price * 10 / 100

class silver(membership):
	def calculate_netprice(self,price):
		disc = price * 10 / 100
		total = price - disc
		return total

	def calculate_point(self,price):
		return price / 5

price = 0

membership_type = str(input("what is the membership type? \n1 platinum\n2 silver \n: "))
price=int(input("Enter Price : RM "))

if (membership_type=="platinum"):
	platinum = platinum()
	calculate_price = platinum.calculate_netprice(price)
	print("total price is = RM",calculate_price)
	print("get RM",platinum.annual_reward(price),"cashback")

elif (membership_type=="silver"):
	silver=silver()
	calculate_price = silver.calculate_netprice(price)
	print("total price is = RM",calculate_price)
	print("get",silver.calculate_point(price),"point")

else:
	print("Wrong membership Input")
	quit()
