#Tip Calculator 

#Algorithm
#Let the user input the sub total of the bil 
#Calculate the tip amount by calculating 25% of the subtotal 
#add tip and the subtotal to come up with the full total price

#input subtotal 
sub = eval(input("enter the sub total here: $"))
subf = "{:.2f}".format(sub)
#calculate tip amount
tip = sub*(25/100)
tipf =  "{:.2f}".format(tip)
#calculate the total
total = tip + sub
#turn the float to 2 decimal format
total = "{:.2f}".format(total)
#print out all 
everything = (f'Subtotal: ${subf} \n Tip: ${tipf} \n Total: ${total}')
print (everything)


