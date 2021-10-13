#Perimeter of a triangle

#Perimeter of a triangle 

#Algorithm

#Input lengths 1, 2, 3
#declaring the pairs of the sum of the two lengths and declaring that the third length cannot be bigger than the second length.
#using if statemets to make sure that the sum of the two lengths is larger than the remaining length.
#when conditions are met the perimeter should be calculated and printed out.
#when the conditions are not met an error message would appear.

#LENGTHS
l1 = eval(input("input length 1: "))
l2 = eval(input("input length 2: "))
l3 = eval(input("input length 3: "))
#using if statements to makes sure the sum of every pair of two lengths is greater than the remaining edge.
p1 = l1+l2 > l3
p2 = l1+l3 > l2
p3 = l2+l3 > l1

if p1 and p2 and p3:
    perimeter = l1+l2+l3
    print("The perimeter is",perimeter)
else:
    print("Perimeter cannot be calculated: the input is invalid.") 