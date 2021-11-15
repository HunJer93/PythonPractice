# collatzSeq
# The purpose of this program is to create a Collatz sequence.
# Jeremy Hunton
# 9/10/2021

import sys

# create even function
def collatz(number):
    # use modulo 2 on the number to see if it is even or odd
    modNum = number % 2
    if modNum == 0: #if the number is even, divide the number by 2
        modNum = number / 2
    else: # else the number is odd, so multiply by 3 and add 1
        modNum = (number * 3) + 1
        # print the number
    print(modNum)
    # return the new number
    return modNum


# request user input
print('Please enter a whole number greater than 0')
userInput= input()
validateInput = False

# validate user input to be 1) an integer and 2) greater than 0
while validateInput == False:
    # handle input exception
    try:
        # convert the input to a number
        number = int(userInput)
        # make sure the number is larger than 0 and vaildate
        while(number < 0):
            # print error and re-request input
            print('This is not correct! Please enter a number larger than 0')
            userInput= input()
            number = int(userInput)
        #validate the input
        validateInput = True
    except ValueError : # handle inproper data type
        print('Error! This is not a proper data type. Please try again')
        print('Please enter a whole number greater than 0')
        userInput= input()

# call the collatz function until the output is 1
while(number > 1):
        # call the collatz function and assign number to the value returned
        number = collatz(number)
# print that the code has end
print('This is the end of the Collatz function. Goodbye!')
sys.exit()

# Question: What is the difference between these two snippets of code:

#CODE 1:
# try:
#   print(invoice1())
#   print(invoice2())
# except:
#   print('Error in Processing')

#CODE 2:
# try:
#   print(invoice1())
# except:
#   print('Error in Processing')
# try:
#   print(invoice2())
# except:
#   print('Error in Processing')

#Answer:
# The difference between the 2 code examples is that the first example checks both print functions at the same time and prints
# one error if either of them have an issue. The 2nd example checks each print function at a time. If both invoices had an issue,
# there would be two error messages in the 2nd example, while there would only be 1 in the first example. The 2nd example would also allow
# one invoice to print if the format was correct and the other was incorrect, while the first option wouldn't print either if one is wrong.
