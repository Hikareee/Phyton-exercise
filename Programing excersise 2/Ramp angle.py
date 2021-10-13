#Ramp angle 

#Algorithm

#Input the mass of the object. 
#Input the force needed for the object 
#make a constant variable for gravity.
#find the sin theta using force/(m*g).
#use the asin and degrees function to get the angle.
#format the angle to one decimal place.
#print it on the screen.

import math
#input mass 
mass = eval(input("input the mass here: "))
#input force
force = eval(input("input the force here: "))
#declare gravity 
g = 9.8
#weight
weight = mass*g
#angle of the ramp 
theta = (force/weight)

angle = math.asin(theta)
angele = math.degrees(angle)
fangele = "{:.1f}".format(angele)

print ("The angle of the ramp is:", fangele)