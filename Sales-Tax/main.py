#
# Trenton B. Davis 
# 02/07/2025 
# Sales Tax Programming Project
# COSC 2409 DNT
#

# Variable declarations
purchase = 0.0
stateSalesTax = 0.0
countySalesTax = 0.0
totalSalesTax = 0.0
saleTotal = 0.0

# Constants for the state and county tax rates
STATE_SALE_TAX = float(0.05)
COUNTY_SALE_TAX = float(0.025)

# Get the amount of the purchase.
purchase = float(input("Enter the total price: "))

# Calculate the state sales tax.

stateSalesTax = float(purchase * STATE_SALE_TAX)
# Calculate the county sales tax.
countySalesTax = float(purchase * COUNTY_SALE_TAX)

# Calculate the total tax.
totalSalesTax = float(stateSalesTax + countySalesTax)

# Calculate the total of the sale.
saleTotal = float(purchase + totalSalesTax)

# Print information about the sale.
print("The original price of the item was: $" + "{:,.2f}".format(purchase))
print("The state sales tax is  " + "{:,.2f}".format(stateSalesTax))
print("The county sales tax is " + "{:,.2f}".format(countySalesTax))
print("resulting in a total tax of " + "{:,.2f}".format(totalSalesTax))
print("The total price of the sale was: $" +  "{:,.2f}".format(saleTotal) + " tax included")