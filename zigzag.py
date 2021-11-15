# zigzag
# the purpose of this program is to create a zigzag animation until the user stops it with Ctrl + C.
# Jeremy Hunton
# 9/10/2021

import time, sys

# request user input for the number of astrisks
print('How many astrisks do you want to display?')
print('Choose between 5 and 25.')
userInput = input()
validateInput = False
#try to convert astrix to number
while validateInput == False:
    #handle input exception
    try: # Validate that the input is a number
        numAstrix = int(userInput)
        # make sure the input is correct with while loop
        while numAstrix < 5 or numAstrix > 25: # Validate that the number is within the correct range
            print('This is not the correct range! Please enter a number between 5 and 25')
            print('between 5 and 25')
            # re-display input
            print('How many astrisks do you want to display?')
            print('Choose between 5 and 25.')
            numAstrix = int(input())
        validateInput = True
    except ValueError: #Handle the input not being a number.
        print('That is not a number! Please enter a number and try again.')
        print('How many astrisks do you want to display?')
        print('Choose between 5 and 25.')
        userInput = input()

# start the zigzag program
indent = 0 # How many spaces to indent
indentIncreasing = True # Whether the indentation is increasing or not.

try:
    while True: # The main program loop.
        print(' ' * indent, end = '')
        # for loop assigning the astrisk length to the numAstrix input
        for x in range(0, numAstrix):

            if x < numAstrix - 1: # if the range is not the last astrisk, no space
                print('*', end = '')
            else: # else last astrisk so add a space
                print('*')

        time.sleep(0.1) # Pause for 1/10 of a second

        if indentIncreasing:
            # Increase the number of spaces:
            indent = indent + 1
            if indent == 20:
                # Change direction
                # add extra space before STOP so it lines up with the lines and looks pretty (adjusted for the length of STOP! (5 chars))
                totalSpace = numAstrix + 15
                for x in range(0, totalSpace):
                    if x < totalSpace - 1: # if the range is not the last, no space
                        print(' ', end = '')
                    else: # else the last space
                        print(' STOP!')
                indentIncreasing = False
        else:
            #Decrease the number of spaces:
            indent = indent -1
            if indent == 0:
                # Change direction
                print('START!')
                indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()

# Question: What would the output be for the following code?
# season = 'Winter'
# def out1():
#   season = 'Summer'
#   print(season)
# def out2():
#   print(season)
# def out3():
#   global season
#   season = 'Summer'
#   print(season)
# def out4():
#   print(season)
# out1()
# out2()
# out3()
# out4()

# Answer: the output would be -
# Summer
# Winter
# Summer
# Summer

