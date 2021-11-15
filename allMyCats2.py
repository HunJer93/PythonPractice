# allMycats2.py
# The purpose of this program is to create a list with the names of cats
# Jeremy Hunton
# 9/20/2021

# create a list for the cat names
catNames = []
while True:
    print('Enter the name of cat ' + str(len(catNames) + 1) + ' (Or enter nothing to stop.):')
    name = input()
    if name == '':
        break
    catNames = catNames + [name] # list concatenation

# print the list of names sorted in alphabetical order
catNames.sort(key=str.lower)
print('The cat names are:')
for name in catNames:
    print(' ' + name)

# Question
# What are the data types and values of myColor, yourColors, thoseColors, and allColors?
# colors =['green','red','blue','purple','yellow','orange']
# myColor = colors[-1]
# yourColors = colors[2:4]
# thoseColors = colors[-3:]
# allColors = len(colors)

# Answers:
# myColor is a string set to 'orange'
# yourColors is a List set to ['blue','purple']
# thoseColors is a List set to ['purple','yellow','orange']
# allColors is a int set to 6
