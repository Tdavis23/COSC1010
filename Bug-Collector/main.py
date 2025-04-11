#
# Trenton Davis
# 04/10/25
# Bug Collector Programming Project
# COSC 1010
#
def bugTally():

# Initialize variables for bugs and total number of bugs collected.
    accumatedBugs = 0 

# Get number of bugs collected each day using a for loop.
    for day in range(7):
        print("ive caught " + str(accumatedBugs) + " bugs")
        bugsCaught = int(input(f"how many bugs did you catch on day {day+1}: "))
        accumatedBugs += bugsCaught
bugTally()

# Display the total number of bugs collected.
