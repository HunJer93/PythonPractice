#This program says hello and asks for my name.

print('Hello, world!')
print('What is your name?')     #ask for their name
myName = input()
print('It is good to meet you, ' + myName)
print('The length of your name is: ')
print(len(myName))
print('What is your age?')      #ask for their age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')

#To dissect the line str(int(myAge) + 1), I will start inside and work outside.
#myAge is calling the variable myAge that was assigned to the user input. Since the
#user input was never given a value int(myAge) converts the input to an integer value
#and then adds 1 to it with int(myAge) + 1. This whole value is then converted into a
#string data type with the str data assignment so that it can be printed to the
#program output with the print() function used later on.
