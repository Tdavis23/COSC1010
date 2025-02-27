#
# Trenton B. Davis
# 02/16/25
# Budget Analysis Programming Project
# COSC 1010
#

#variables declared
budget = 0.0
expense = 0.0 
totalExpense = 0.0 
conditional = True 
conditionalInput = "NO"

#input for the budget
budget = float(input("\n\nEnter your budget: "))
print("Your budget is $" + "{:,.2f}".format(budget))
print("\n ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ \n")

# conditional loop 
while conditional == True:
    print("Budget: $" + "{:,.2f}".format(budget))
    print("Expenses: $" +  "{:,.2f}".format(totalExpense))
    expense = float(input("\nEnter next Expense: $"))
    totalExpense = float(totalExpense + expense)
    conditionalInput = str(input("Is this your final expense(YES : NO)? \n"))
    
    print("\n ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ \n")
    if conditionalInput.upper() == "YES":
        conditional = False
        break

# compare budget and expense
print("This was your budget: $" + "{:,.2f}".format(budget))
print("These were your expenses: $" + "{:,.2f}".format(totalExpense))
if budget >= totalExpense:
    remainder = budget - totalExpense 

    print("\n\nExpenses were within budget")
    print("This is how much you have left: $" + "{:,.2f}".format(remainder))
elif totalExpense > budget:
    debt = totalExpense - budget 

    print("\n\nExpenses were over budget")
    print("This is how much over budget you are: $" + "{:,.2f}".format(debt))
print("\n ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ \n")

#close session
print('\nSession Over\n')

# Use comments liberally throughout the program.