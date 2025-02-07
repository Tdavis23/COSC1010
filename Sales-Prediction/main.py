#
# Trenton B. Davis 
# 02/06/2005
# Sales Prediction Programming Project
# COSC 1010
#

# Variables to hold the sales total and the profit
salesTotal = float(input("Enter how much you made from the sale: "))
# Get the amount of projected sales.

# Calculate the projected profit.
predictedProfit = salesTotal * 0.23
# Print the projected profit.
print("The profit off the sale was $", "{:,.2f}".format(predictedProfit))