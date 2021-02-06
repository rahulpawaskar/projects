

import pro
import billing
j=pro.Product()
k=billing.Bill()
x=input("Press 1:To alter the stock list 2:To buy:")
if x=='1':
	y=input("Press 1:to add 2:to update price 3:to update quantity 4:display all the products 5:search 6:delete")
	if(y=='1'):
		j.add()
	elif y=='2':
		po=input("Enter the product:")
		pr=input("Enter the new price:")
		j.update_price(po,pr)
	elif y=='3':
		p=input("Enter the product:")
		q=input("Enter the quantity:")
		j.update_quantity(p,q)
	elif y=='4':
		j.display()
	elif y=='5':
		s=input("Enter the product to search:")
		j.search(s)
	else:
		k=input("Enter the key of product to be deleted:")
		j.delete(k)
else:
	op='y'
	i=0
	amt=0
	lines=[]
	line1=[]
	while op!='n':
		pd=input("Enter the product:")
		qn=input("Enter the quantity:")
		if k.buy(pd,qn)!=0:
			lines.append(pd)
			
			line1.append(qn)
			i=i+1
		amt=amt+(int(qn)*k.buy(pd,qn,True))
		op=input("Do you want to continue shopping:y or n?")
	if i!=0:
		print("BILL:")
		loop=0
		while loop<i:
			print(lines[loop],line1[loop],k.ret_price(lines[loop]))
			loop=loop+1		
		print("Total:",amt)

		
