# workWithFiles2.py
# The purpose of this program is to demonstrate MORE file handling with Python.
# Jeremy Hunton
# 9/27/21

from pathlib import Path
import os

# declare the path for cats and dogs
pDogsText = 'C:\cpt180Stuff\pets\dogs\dognames.txt'
pCatsText = 'C:\cpt180Stuff\pets\cats\catnames.txt'
pCats= Path(pCatsText)
pDogs = Path(pDogsText)
# make sure catnames.txt and dognames.txt exist in the paths
if(pCats.is_file() and pDogs.is_file()):
    # true so follow the rest of the steps

    # open the dognames.txt in read mode
    dogsFile = open(pDogsText, 'r')
    dogContent = dogsFile.read()
    print(dogContent)
    # close the file
    dogsFile.close()

    # open the catnames.txt in read mode
    catsFile = open(pCatsText, 'r')
    catContent = catsFile.read()
    print(catContent)
    # close the file
    catsFile.close()

    # open the catnames.txt in append mode
    catsFile = open(pCatsText, 'a')
    # write two names to the cats file
    catsFile.write('Smittyworbenyagermanjensen\n')
    catsFile.write('Simba\n')
    # close the file
    catsFile.close()

    # open the cats file in read
    catsFile = open(pCatsText, 'r')
    catContent = catsFile.read()
    print(catContent)
    catsFile.close()

# else false so show error
else:
    print('Unable to access one or more files')

#Question:
# What is the difference between the read() and readlines() methods?

#Answer:
# The readlines() method will read the file and break each line into a separate string and display it as a list,
# while read() will display the file as a single large string value.
