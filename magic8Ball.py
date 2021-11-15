# magic8Ball
# The purpose of this program is to create a magic 8 ball simulation
# Jeremy Hunton
# 9/10/2021

import random

# request user name
print('What is your name?')
userName = input()

# request yes or no question
print('What is your yes/no question?')
question = input()


def getAnswer(answerNumber):
    if answerNumber == 1:
        return 'It is certain'
    elif answerNumber == 2:
        return 'It is decidedly so'
    elif answerNumber == 3:
        return 'Yes'
    elif answerNumber == 4:
        return 'Reply hazy try again'
    elif answerNumber == 5:
        return 'Ask again later'
    elif answerNumber == 6:
        return 'Concentrate and ask again'
    elif answerNumber == 7:
        return 'My reply is no'
    elif answerNumber == 8:
        return 'Outlook not so good'
    elif answerNumber == 9:
        return 'Very doubtful'
    elif answerNumber == 10:
        return 'Not a Chance!'

r = random.randint(1,10)
fortune = getAnswer(r)

# print output
print(userName + ', ' + fortune)

#Question: What are Pythons two levels of scope? Explain each one.
#Answer: The levels of scope in Python are local scope and global scope. Local scope is when you declare variables inside of a
# function and those variables cannot be used outside of that function. Global scope is when you declare variables at the top
# of your program that ALL functions in your program inherit. Global variables are useful for constants or variables that change
# throughout your program, but having all of your variables in a program is messy and bad practice.
