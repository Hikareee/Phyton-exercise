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
c = calc_new_height()
print(c)