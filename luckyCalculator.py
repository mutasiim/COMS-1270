# Mohammad Mu Tasim Chowdhury                   09 - 22 - 2024
# Assignment #2

# A calculator having 7 basic operations, but with a special ability to generate a lucky number

print("Lucky Calculator!")

print(" ")

print("By: Mohammad Mu Tasim Chowdhury")
print("[COM S 1270 1]")

print(" ")

import random

print("What would you like to do:")

print(" ")

feature = input("[c]alculator, [l]ucky number, [q]uit: ")

if feature == "c":
    operation = input("Please Choose a Calculation [+], [-], [*], [/], [//], [%], [**]: ")

    if operation == "+":
        int1 = int(input("Please Enter An Integer: "))
        int2 = int(input("Please Enter An Integer: "))
        print("The result of your calculation was:", int1+int2)
    
    elif operation == "-":
        int1 = int(input("Please Enter An Integer: "))
        int2 = int(input("Please Enter An Integer: "))
        print("The result of your calculation was:", int1-int2)
    
    elif operation == "*":
        int1 = int(input("Please Enter An Integer: "))
        int2 = int(input("Please Enter An Integer: "))
        print("The result of your calculation was:", int1*int2)

    elif operation == "/":
        int1 = int(input("Please Enter An Integer: "))
        int2 = int(input("Please Enter An Integer: "))
        if (int2 == 0):
            print("ERROR: Dividing by zero is not allowed")
        
        else:
            print("The result of your calculation was:", int1/int2)

    elif operation == "//":
        int1 = int(input("Please Enter An Integer: "))
        int2 = int(input("Please Enter An Integer: "))
        if (int2 == 0):
            print("ERROR: Dividing by zero is not allowed")
        
        else:
            print("The result of your calculation was:", int1//int2)

    elif operation == "%":
        int1 = int(input("Please Enter An Integer: "))
        int2 = int(input("Please Enter An Integer: "))
        if (int2 == 0):
            print("ERROR: Dividing by zero is not allowed")
        
        else:
            print("The result of your calculation was:", int1%int2)
    
    elif operation == "**":
        int1 = int(input("Please Enter An Integer: "))
        int2 = int(input("Please Enter An Integer: "))
        print("The result of your calculation was:", int1**int2)
    
    else:
        print("ERROR: You must enter either \"+\", \"-\", \"*\", \"/\", \"//\", \"%\", or \"*\"")

elif feature == "l":
    startrand = int(input("Please Enter An Integer: "))
    endrand = int(input("Please Enter An Integer: "))
    randomnumber = random.randrange (startrand, endrand)
    print("Your lucky number is:", randomnumber)

elif feature == "q":
    print("Goodbye!")

else:
    print("ERROR: I did not understand your input... Please try again...")


