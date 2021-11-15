# workWithFiles1.py
# The purpose of this program is to show how to work with files in Python.
# Jeremy Hunton
# 9/27/21

from pathlib import Path
import os

#this function takes a file location and prints out the contents
def whatsInTheBox(fileLocation):
    # print out the info based upon the file location.
    print('The ' + fileLocation + ' folder contains the following: ' + str(os.listdir(fileLocation)))
# print the current directory
print(Path.cwd())

#this function takes a file location and prints out the contents with their size
def contentSize(fileLocation):
    # print out the file location
    print('The ' + fileLocation + ' folder contains the following:')
    # for each file within the fileLocation, display the contents and the size
    for fileName in os.listdir(fileLocation):
        print(fileName + ': ' + str(os.path.getsize(os.path.join(fileLocation, fileName))))

#change the current directory to CPT180Stuff folder
stuffDir = os.chdir('C:\cpt180Stuff')
# print the current directory
print(Path.cwd())

#try to make a "cellphones" file in the CPT180stuff folder
try:
    os.makedirs('C:\cpt180Stuff\\cellphones')
except OSError as e:
    print('Directory already created.')

#call whatsInTheBox to pint the folder contents
whatsInTheBox('C:\cpt180Stuff')
whatsInTheBox('C:\cpt180Stuff\cars')
whatsInTheBox('C:\cpt180Stuff\pets')
contentSize('C:\cpt180Stuff\pets\cats')
contentSize('C:\cpt180Stuff\pets\dogs')

# Question:
# What would be the result of the following code and what is the significance of the result:
# from pathlib import Path
# print(Path.home())

# Answer:
# The code would print the home for the user. If you have multiple users, it would be the
# file address of the user that is logged in.
