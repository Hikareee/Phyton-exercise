#Slope of a line 

#Algorithm

# input the x1 and x2 variables
# input the y1 and y2 variables
# afterwards calculate the slope using the equation 
# print it out. 

#input x1 and x2 
x1 = eval(input("input x1: "))
x2 = eval(input("input x2: "))
#input y1 and y2
y1 = eval(input("input y1: "))
y2 = eval(input("input y2: "))
#calculate slope
slope = (y2-y1)/(x2-x1)
#output 
print ("The slope for the line that connects two points", slope)