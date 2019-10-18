"""
Brent Fanning random turtle creation
"""

# we'll need to import random and turtle from another python file
# and then create this object from WITHIN the other file
# ...and create a screen using wn = turtle.Screen()

import turtle
import random

class MeTurt(object):
	""" has methods that do turtle stuff """

	def __init__(self):
		pass

	def turtlesetup(self, p_color_pick):

		jimmy = turtle.Turtle()
		o = turtle.Turtle()
		wn = turtle.Screen()

		wn.bgcolor("blue")		# set the window background color

		jimmy.shape('turtle')

		if (p_color_pick != "red" and p_color_pick != "orange" and p_color_pick != "green" and p_color_pick != "blue" and p_color_pick != "lightgreen" and p_color_pick != "hotpink"):
			randomColor = random.randint(1,99)
			if(randomColor < 25):
				jimmy.color("lightgreen")
			if(randomColor < 50):
				jimmy.color("hotpink")
			if(randomColor < 75):
				jimmy.color("orange")
			else:
				jimmy.color("red")
		else:
			jimmy.color(str(p_color_pick))

		jimmy.pensize(3)
		jimmy.forward(2)

		starttx = random.randrange(-50,50)
		startty = random.randrange(-50,50)

		jimmy.penup()
		jimmy.setpos(starttx,startty)
		jimmy.pendown()

		return(wn,jimmy)


	def moveturtle(self,wn,jimmy):
		#while isInScreen(wn, jimmy):
		angle = random.randrange(1, 361)
		jimmy.right(angle)
		jimmy.forward(50)

	def turtFuncUturn(self, jimmy):
		"""
		do a u turn with this method
		"""
		# assuming we're starting facing east
		# go forward a short distance
		# ...then turn left 90 degrees
		# ...then go straight a short distance

		jimmy.forward((random.randint(25,100)))#25-100

		# ...then turn
		jimmy.left(90)
		jimmy.forward((random.randint(25,100)))

		# ...and turn again
		jimmy.left(90)
		jimmy.forward((random.randint(25,100)))
#=============================================================================

	# after entering:
	# import randTurt
	# ...into idle you can create a turtle object and then make it move randomly
	# in the following way:
	# enter the following line of code to start the program:
	# ...after making sure to enter this: ob1 = randTurt.RandT1()
	# ...then enter this one line:
	# y = ob1.turtlesetup()
	# ...or something like this: func = ob1.turtlesetup()

	# ...followed by something like this:
	# ob1.moveturtle( func[0], func[1] )
	# ...and boom!  The turtle moves!!! yay!
