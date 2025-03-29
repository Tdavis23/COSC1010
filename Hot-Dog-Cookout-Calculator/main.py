#
# Trenton B. Davis
# 03/28/2025
# Hot Dog Cookout Calculator Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

def HotDogCookoutCalculator():
    #define global CONSTANTS
    HOTDOGS_PER_PACKAGE = 10 
    BUNS_PER_PACKAGE = 8

    #inputs 
    attendees = int(input("How Many People are going? "))
    hotDogsPerPerson = int(input("How many hot dogs will each person recieve? "))

    #calculate hotDogs and Buns needed
    totalHotDogsNeeded = attendees * hotDogsPerPerson

    hotDogPackagesNeeded = (totalHotDogsNeeded + HOTDOGS_PER_PACKAGE -1 ) // HOTDOGS_PER_PACKAGE

    totalBunsNeeded = attendees

    bunPackagesNeeded = (totalBunsNeeded + BUNS_PER_PACKAGE -1 ) // BUNS_PER_PACKAGE

    #calculate leftover buns and hotDogs
    leftoverHotDogs = hotDogPackagesNeeded * HOTDOGS_PER_PACKAGE - totalHotDogsNeeded
    leftoverBuns = bunPackagesNeeded * BUNS_PER_PACKAGE - totalBunsNeeded

    #print the information
    print(f"\nMinimum number of packages of hot dogs required: {hotDogPackagesNeeded}")
    print(f"Minimum number of packages of hot dog buns required: {bunPackagesNeeded}")
    print(f"Number of hot dogs that will be left over: {leftoverHotDogs}")
    print(f"Number of hot dog buns that will be left over: {leftoverBuns}")

#run the function
HotDogCookoutCalculator()