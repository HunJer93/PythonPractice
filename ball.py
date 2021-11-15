# ball
# the ball program requests the user's inputs describing a ball and displays the proper output
# Jeremy Hunton
# 8/23/2021

#request the name
print('What is your name?')
userName = input()

#request the color of the ball
print('What is the color of the ball?')
ballColor = input()

#request the radius of the ball (in inches)
print('What is the radius of the ball (in inches)?')
radius = input()

#declare pi
pi = 3.1416

#calculate the volume of the ball
volume = 4/3 * pi * float(radius)**3

#print the output. Display the volume rounded to 2 decimal places
print('Hello ' + userName + ', the ball is ' + ballColor + ' and has a volume of ' + str(round(volume, 2)) + ' cubic inches.')

# The values obtained from the input method arrive as string data types and not integers or floats. In order
# to use the input in a mathematical formula, you need convert the input to a float or an integer. If you do not,
# you will receive an error.


