#
# Trenton B. Davis
# Date
# Lottery Number Generator Programming Project
# COSC 1010
#
import random 

def numberGenerator():

    # call var
    numberList = []

    #define lottery numbers
    for index in range(7):
        numberList.append(random.randint(0,9))
    
    #print lottery numbers
    print("did you get the winning ticket?")
    for index in range(len(numberList)):
        print(numberList[index], end="" )

        
numberGenerator()
# Use comments liberally throughout the program. 