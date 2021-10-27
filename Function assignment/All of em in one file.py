#%%
#name the function "convert_to_days"
def convert_to_days():
    #input hours
    hours = int(input("Enter number of hours: "))
    #input minutes
    minutes = int(input("Enter number of minutes: "))
    #input seconds
    seconds = int(input("Enter number of seconds: "))
    def get_days():
        days = (hours/24) + ((minutes/60)/24) + ((((seconds/60)/60)/24))
        #round to 4 digits
        d = round(days,4)
        #return the value of the rounded days
        return d
    #store the value of d
    d = get_days()
    #print out the number of days
    print ("The number of days is: ", d)
#run the function
convert_to_days()
# %%
#declare a function "calc_weight_on_planet accepting 2 "
def calc_weight_on_planet(woe,sgop = 23.1):
    #earth gravity
    earthG = 9.8
    #find mass through w = m * g
    mass = woe / earthG
    #find the weight on the plannet
    w = mass * sgop
    #return the weight
    return w
calc_weight_on_planet(120,23.1)
# %%
#create a function called num_atoms
def num_atoms(aoe,atw=196.97):
    #Declare Avogaro number variable
    Avogadro = 6.022*10**23
    #calculate the result
    result = (aoe/atw)*Avogadro
    #return the result
    return result
num_atoms(10) #3.0573183733563486e+22
# %%
#create function cal_new_height
def calc_new_height():
    #input the current width
    current_width = eval(input("Enter the current width: "))
    #input the current height
    current_height = eval(input("Enter the current height: "))
    #input the desired width
    desired_width = eval(input("Enter the desired width: "))
    #find the aspect ratio of the picture
    aspect_ratio = current_height/current_width 
    #find the desired height by multiplying the ratio with the width
    desired_height = aspect_ratio*desired_width
    #print it out
    print("The corresponding height is", float(desired_height))
    #return the value
    return float(desired_height)
calc_new_height()
# %%
#Make the main convert_temp function
def convert_temp():
    #Take the user input for the temperature in Fahrenheit
    TempF = eval(input("Enter a temperature in Fahrenheit: "))
    #Print out The temperature in Fahrenheit
    print("The temperature in Fahrenheit is: ", TempF)
    #Make a helper function called convert_to_celsius
    def convert_to_celsius():
        #Use the equation to conver the temperature to celsius
        TempC = (5/9)*(TempF-32)
        #print out the temperature in celsius
        print("The temperature in Celsius is:", TempC)
        #return the temperature as a float
        return float(TempC)
    #Store the returned value in variable Tc
    Tc = convert_to_celsius()
    #Make a second helper function called convert_to_kelvin
    def convert_to_kelvin():
        #Use the formula to convert celsius to kelvin
        TempK = Tc + 273.15
        #print it out on the screen
        print("The temperature in Kelvin is: ", TempK)
        #return the value as a float
        return float(TempK)
    #store the returned value in variable Tk
    Tk = convert_to_kelvin()
#run the function
convert_temp()
# %%
