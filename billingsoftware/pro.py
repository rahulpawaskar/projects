import csv
class Product:	
	def add(self):
		with open('E://Desktop/pro/billingsoftware/supermarket.csv','a',newline='') as csvfile:
			writer=csv.writer(csvfile)
			x=input("Enter the product:")
			y=input("Enter the price:")
			z=input("Enter the quantity:")
			lines=[x,y,z]
			writer.writerow(lines)
	def update_price(self,product,new_price):
		with open('E://Desktop/pro/billingsoftware/supermarket.csv') as csvfile:
			read=csv.reader(csvfile)
			lines=[l for l in read]
			for i in lines:
				for j in i:
					if(j==product):
						i[1]=new_price
		with open('E://Desktop/pro/billingsoftware/supermarket.csv','w',newline='') as csvfile:
			writer=csv.writer(csvfile)
			writer.writerows(lines)
	def update_quantity(self,product,new_quantity):
		with open('E://Desktop/pro/billingsoftware/supermarket.csv') as csvfile:
			read=csv.reader(csvfile)
			lines=[l for l in read]
			for i in lines:
				for j in i:
					if(j==product):
						i[2]=new_quantity
		with open('E://Desktop/pro/billingsoftware/supermarket.csv','a',newline='') as csvfile:
			writer=csv.writer(csvfile)
			writer.writerows(lines)
	def display(self):
		with open('E://Desktop/pro/billingsoftware/supermarket.csv') as csvfile:
			read=csv.DictReader(csvfile)
			for row in read:
				print(row['Product'])
	def search(self,product):
		with open('E://Desktop/pro/billingsoftware/supermarket.csv') as csvfile:
			read=csv.DictReader(csvfile)
			a=0
			for row in read:
				if(row['Product']==product):
					a=1
					print(row)
					break
			if(a!=1):
				print("Item not found")

			
	
