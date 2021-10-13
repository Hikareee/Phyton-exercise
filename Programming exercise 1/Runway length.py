#Algorithm

# input the speed
# input the acceleration 
# calculate the minimum runway length through the equation (v^2/2a)
# print out the minimum length needed for the runway

#input speed and acceleration
v = eval(input("Input speed (m/s) here: "))
a = eval(input("input acceleration (m/s2) here: "))
#calculate runway length
length = (v**2)/(2*a) 
#print out length
print ("The minimum runway length needed for this airplane", length, "meters")