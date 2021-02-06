import csv
class Bill:
        def check_product(self,product):
                with open('supermarket.csv') as csvfile:
                        reader=csv.DictReader(csvfile)
                        a=0
                        for row in reader:
                                if(row['Product']==product):
                                        a=1
                                        break
                        if a==1:
                                return True
                        else:
                                print("Item not found")
                                return False
        def check_quantity(self,product,quantity):
                with open('supermarket.csv') as csvfile:
                        reader=csv.DictReader(csvfile)
                        a=0
                        for row in reader:
                                if(row['Product']==product):
                                        z=row['Quantity']
                                        a=1
                                        break
                        if a==1:
                                if (z>=quantity)or(int(z)>=int(quantity)):
                                        return True
                                else:
                                        print("Item out of stock")
                                        print(int(z),"stocks available")
                                        return False
                        else:
                                return False
        def ret_price(self,product):
                with open('supermarket.csv') as csvfile:
                        reader=csv.DictReader(csvfile)
                        for row in reader:
                                if row['Product']==product:
                                        return row['Price']
                                        break
        def red_quantity(self,product,quantity):
                with open('supermarket.csv') as csvfile:
                        reader=csv.reader(csvfile)
                        lines=[l for l in reader]
                        for i in range(len(lines)):
                                if(lines[i][0]==product):
                                        lines[i][2]=int(lines[i][2])-int(quantity)
                with open('supermarket.csv','w',newline='') as csvfile:
                        writer=csv.writer(csvfile)
                        writer.writerows(lines)
                        
        def buy(self,product,quantity,pa=False):
                b=self.check_product(product)
                if b==True:
                        a=self.check_quantity(product,quantity)
                        if(a==True):
                                k=self.ret_price(product)
                                if (pa==True):
                                        self.red_quantity(product,quantity)
                                return int(k)
                        else:
                                return 0
                else:
                        return 0
