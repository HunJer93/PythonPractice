# myFavoriteCars.py
# The purpose of this program is to use tuples to display the year, make, and model of cars
# Jeremy Hunton
# 9/20/2021

car1 = (1965, 'Pontiac', 'GTO', 'blue')
car2 = (1969, 'Plymouth','Roadrunner', 'yellow')
car3 = (2002, 'Chevrolet', 'Z-28 Camaro', 'black')

carList = [car1, car2, car3]

for car in carList:
    print(str(car[0]), car[3], car[1], car[2])

#Question:
# Both strings and tuples are considered immutable. What does immutable mean? What are two
# advantages of using a tuple rather than a list?

#Answer:
# Immutable means that the value of the data/object cannot be changed in the computer memory once created (only overwritten).
# One advantage of using a tuple over a list is that a tuple is immutable and cannot be changed while a
# list is mutable and can be changed. Another advantage is that because tuples are immutable, Python optimizes
# tuples compared to lists making them slightly faster than code using lists.
