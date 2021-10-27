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
#store the value in a variable "result"
result = calc_weight_on_planet(120,23.1)
#print it out
print(result)