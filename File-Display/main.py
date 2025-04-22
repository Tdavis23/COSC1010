#
# Trenton B. Davis
# 04/22/25
# File Display Programming Project
# COSC 1010
#
# Use comments liberally throughout the program. 

filePath = 'File-Display/numbers.txt'

def listFile():
    try:
        with open(filePath, 'r') as file:
            #read and display the file contents
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print('File does not exist')


#call function
listFile()
