#Software sales 

#Algorithm

#Declare a constant price variable .
#Let the user input the quantity of the product.
#Use if statemets to identify the discountr amount. 
#calculate the discounted price.
#print it out to the screen.

#Price of the product 
price = 100 
#user input 
quantity = eval(input("Input the amound of packages you want to order: "))
#discounts 
if (19>=quantity>=10):
   discount = 10
elif (49>=quantity>=20):
   discount = 20
elif (99>=quantity>=50):
   discount = 30
elif (quantity>=100):
   discount = 40
else:
   discount = 0
#sub total
sub = price * quantity
#if statements 
if (19>=quantity>=10):
   price = sub - (100*(discount/100))
elif (49>=quantity>=20):
   price = sub - (100*(discount/100))
elif (99>=quantity>=50):
   price = sub - (100*(discount/100))
elif (quantity>=100):
   price = sub - (100*(discount/100))
else:
   price = sub - 0
#discounted price
discounted = price - sub
#print
print ("Packages ordered: ", quantity, end="\n")
print ("Discount Amount @", discount,"%",": $",discounted ,end="\n" )
print ("price = $",price)
