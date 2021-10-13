#Wind chill temperature calculator

#Algorithm 

#Declare the maximum and minimum temperature.
#Use an input and while loop to let the user input temperature from the range provided.
#if the input is valid we break the loop if it is invalid we let the users re-enter a valid temperature.
#Let the users input the wind speed and use a while loop to validate the input.
#if it is valid we break the loop if it isn't we let the users re-enter the wind speed.
#calculate the wind chill temperature using the formula.

#minimal and maximum temperature
min = -58
max = 41
#Temperature input
while True:
 temp = eval(input("Please enter a temperature between -58 degrees Fahrenheit and 41 degrees Fahrenheit: "))
 if max >= temp >= min:
     break
 else:
     print ("Temperature must be between -58F and 41F.")
     continue
     
#Input Wind speed
while True:
  wind = eval(input("Please enter wind speeds greater than or equal to 2mph: "))
  if wind >= 2:
      break
  else: 
      print ("Speed must be greater than or equal to ")
      continue
      
  
#Calculate the wind chill index
v = wind**0.16
tav = temp*v
#final result
result = 35.74 + (0.6215*temp) - (35.75*v) + (0.4275*tav)
resultf = "{:.2f}".format(result)
print (resultf)