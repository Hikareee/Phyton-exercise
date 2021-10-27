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
