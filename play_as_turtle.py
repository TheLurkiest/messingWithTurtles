"""
Brent Fanning random turtle mov
"""

import turtle
import random
import unittest
import pdb

import playerTurt
from playerTurt import MeTurt


p_reply=''
p_reply = input('Enter the COLOR you want your turtle to be: ')

ob1 = playerTurt.MeTurt()
func1 = ob1.turtlesetup( str(p_reply) )

count1=0
while(count1 < 5):
	ob1.moveturtle( func1[0], func1[1] )
	count1 = count1 + 1


