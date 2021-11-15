# printRandomNumbers.py
# The purpose of this program is to print a random number set within the user's requirements
# Jeremy Hunton
# 8/24/2021

import random

# request how many random numbers are required, and the limit of the numbers
print('How many random numbers do you want to print?')
count = int(input())

print('What is the lower limit of the random numbers?')
lowerLim = int(input())

print('What is the upper limit of the random numbers?')
upperLim = int(input())

# print out the list of random numbers
for i in range(count):
    print(random.randint(lowerLim, upperLim), end = ', ')

#Q:
#When importing a module into a Python program, what is the difference between using
#the import statement and using the from statement? Which is normally preferred? Why?

#A:
#When using the import statement, you need to reference the module name when calling a function from that module.
#When using the from import method, you do not need to reference the module name. In the import statement above for the
#random module, when calling the randint function, the random module is referenced. If I used a from import statement, I
#would be able to use randint by itself in place of random.randint. While using a from import statement saves text space,
#it is better to use the import statement for clarity. Using an import statement will show you which functions are coming
#from which modules and helps you keep track of your code better, especially when you need to debug.
