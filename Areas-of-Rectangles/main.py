#
# Trenton B. Davis
# 02/26/25
# Areas of Rectangles Programming Project
# COSC 1010
#
# Local variables
lengthA = 0
widthA = 0
areaA = 0

lengthB = 0
widthB = 0
areaB = 0

# Get length A
lengthA = int(input("Enter the length of the first rectangle: "))

# Get width A
widthA = int(input("Enter the width of the first rectangle: "))

# Get length B
lengthB = int(input("Enter the length of the second rectangle: "))

# Get width B
widthB = int(input("Enter the width of the second rectangle: "))

print("\n ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ \n")

# Calculate area A
areaA = lengthA * widthA
print("First Rectangle")
print("Length: " + str(lengthA))
print("Width: " + str(widthA))
print("Area: " + str(areaA))

print("\n - - - - - - - - - - -  \n")

# Calculate area B
areaB = lengthB * widthB 
print("Second Rectangle")
print("Length: " + str(lengthB))
print("Width: " + str(widthB))
print("Area: " + str(areaB))

print("\n ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ \n")

# Print area comparison using if-elif-else statements

if areaA > areaB:
    print("the first rectangle is bigger")
elif areaB > areaA:
    print("the second rectangle is bigger")
else:
    print("the rectangles are the same size")

print("\n ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ \n")
