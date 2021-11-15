# Vampire.py
# This program uses if/then statements to determine if the user name is Alice, and how old they are
# Jeremy Hunton
# 8/24/2021

# request user's name and age
print('What is your name?')
userName = input()
print('What is your age?')
age = int(input())

# if then statement checking if the use is Alice, and their age
if userName == 'Alice':
    print('Hi, Alice.')
elif age < 12:
    print('You are not Alice, kiddo.')
elif age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif age > 100:
    print('You are not Alice, grannie.')
else:
    print('You are not Alice.')

#Q: Fix the code below:
# if car = 'Ford'
#   print(You have a Ford)
#else car == 'Chevrolet':
# print('You have a Chevrolet')

# Fixed Code
#if car == 'Ford':
#    print('You have a Ford')
#elif car == 'Chevrolet':
#    print('You have a Chevrolet')

#an else statement could also be used without the car == 'Chevrolet' condition.
