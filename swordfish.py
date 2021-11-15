# swordfish.py
# The purpose of this program is to create a simple password login for the users Joe and Natalie with the password swordfish.
# Jeremy Hunton
# 8/24/2021

#while loop for the proper password
while True:
    print('Who are you?')
    name = input()
    if name != 'Joe' and name != 'Natalie':
        continue #if the name is not Joe or Natalie, skip the below code

    #if the name is Joe, greet Joe
    if name == 'Joe':
        print('Hello, Joe! What is the password? (It is a fish.)')
    #else the name is Natalie, so greet Natalie
    else:
        print('Hello, Natalie! What is the password? (It is a fish.)')
    #request the password from the user
    password = input()
    #if the password is swordfish, break the while loop to allow access
    if password == 'swordfish':
        break
    else:
        print('Sorry, wrong password')
print('Access granted!')

#for loop printing out the alphabet
for i in range(65, 91):
    print(chr(i), end = '')

#Q:
#Explain the difference between a continue statement and a break statement when used within a while loop.

#A:
#A continue statement allows you to start a while loop over from the beginning. A break
#statement is used to break out of the while loop and continue on in the program.
