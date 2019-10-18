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
p_pick_m = 0
p_pick_lr = ''
p_pick_rot = 0

while(count1 < 5):
	# def turtPmove(self,wn,jimmy, p_move_pick, p_pick_left_right, p_rot_pick):

	p_reply = input('Select travel DISTANCE: ')
	p_pick_m = int(p_reply)

	p_reply = input('Choose direction to travel-- LEFT or RIGHT: ')
	p_pick_lr = str(p_reply)

	p_reply = input('Enter a value between 0 and 360 degrees to indicate how far left or right you want to go: ')
	p_pick_rot = int(p_reply)

	ob1.turtPmove( func1[0], func1[1], p_pick_m, p_pick_lr, p_pick_rot)
	count1 = count1 + 1



