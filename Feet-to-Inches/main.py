#
# Trenton Davis
# 04/10/25
# Feet to Inches Programming Project
# COSC 1010
#
# Use comments liberally throughout the program.
def FeetToInches(feet):
    inches = float(feet) * 12
    print(str(inches) + " this is how many inches are in " + feet + " feet")

inputFeet = input("how many feet are there? ")
FeetToInches(inputFeet)