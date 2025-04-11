#
# Trenton B. Davis
# 02/19/25
# Kilometer Converter Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

def KilometerConverter(kilometers):
    miles = float(kilometers) * 0.6214
    print("{:,.2f}".format(miles) + " this is how many miles are in " + "{:,.2f}".format(kilometers) + " kilometers.")

kilometerInput = int(input("what is the distance in kilometers? "))
KilometerConverter(kilometerInput)