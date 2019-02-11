"""
Brent Fanning random turtle mov
"""

import turtle
import random

import unittest

import pdb

from dir2rando.randTurt import RandT1

import randTurt


ob1 = randTurt.RandT1()
func1 = ob1.turtlesetup()

count1=0
while(count1 < 10):
    ob1.moveturtle( func1[0], func1[1] )
    count1 = count1 + 1
