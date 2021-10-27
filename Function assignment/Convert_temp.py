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