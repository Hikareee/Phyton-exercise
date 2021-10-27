#create a function called num_atoms
def num_atoms(aoe,atw=196.97):
    #Declare Avogaro number variable
    Avogadro = 6.022*10**23
    #calculate the result
    result = (aoe/atw)*Avogadro
    #return the result
    return result
num_atoms(10) #3.0573183733563486e+22
num_atoms(10, 12.001)#5.017915173735522e+23
num_atoms(10, 1.008)#5.97420634920635e+24