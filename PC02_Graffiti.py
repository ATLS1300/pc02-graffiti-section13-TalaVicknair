#!/usr/bin/env python
# coding: utf-8

'''
Turtle starter code
ATLS 1300
Author: Dr. Z
Author: Tala Vicknair
May 29, 2020
'''

import turtle #import the library of commands that you'd like to use

turtle.colormode(255)

# Create a panel to draw on. 
panel = turtle.Screen()
w = 750 # width of panel
h = 750 # height of panel
panel.setup(width=w, height=h) #600 x 600 is a decent size to work on. 
#You can experiment by making it the size of your screen or super tiny!

# Create a colorful background and add Bezos image to it
image = "Bezos.gif"
panel.bgcolor("lightsteelblue1")
panel.bgpic(image)

#=======Add your code here======
beardTopLeft = (5,25)
beardTopRight = (35,30)
beardBot = (25,-5)

leftEarLeft = (-90,150)
leftEarTop = (-85,210)
leftEarRight = (-50,175)
leftEarIn = (-75,160)

rightEarLeft = (20,210)
rightEarTop = (80,220)
rightEarBot = (50,170)
rightEarIn = (40,180)

whiskerLeftTopIn = (-35,85)
whiskerLeftTopOut = (-70,90)
whiskerLeftMidIn = (-35,75)
whiskerLeftMidOut = (-75,75)
whiskerLeftBotIn = (-35,65)
whiskerLeftBotOut = (-70,60)

whiskerRightTopIn = (50,85)
whiskerRightTopOut = (80,90)
whiskerRightMidIn = (50,75)
whiskerRightMidOut = (90,75)
whiskerRightBotIn = (50,65)
whiskerRightBotOut = (80,60)

tailLengthBot = (-280,-247)
tailLengthTop = (-280,-50)

tailEndLeft = (-295,-65)
tailEndTop = (-280,-5)
tailEndRight = (-260,-65)

nose = (20,75)
finger = (115,-93)
text = (162,-175)

beamLeft = (200,-247)
beamSpikeLeft = (225,-200)
beamSpikeMidLeft = (275,-245)
beamSpikeMid = (285,-185)
beamSpikeRight = (350,-185)

turtle.up()
turtle.pensize(1)
turtle.fillcolor("red")
turtle.goto(beardTopLeft)
turtle.begin_fill()
turtle.down()
turtle.goto(beardTopRight)
turtle.goto(beardBot)
turtle.goto(beardTopLeft)
turtle.end_fill()
turtle.up()

turtle.goto(leftEarLeft)
turtle.pensize(3)
turtle.fillcolor("gray30")
turtle.begin_fill()
turtle.down()
turtle.goto(leftEarTop)
turtle.goto(leftEarRight)
turtle.goto(leftEarLeft)
turtle.end_fill()
turtle.fillcolor("red")
turtle.begin_fill()
turtle.goto(leftEarTop)
turtle.goto(leftEarIn)
turtle.goto(leftEarLeft)
turtle.end_fill()
turtle.up()

turtle.goto(rightEarLeft)
turtle.fillcolor("grey10")
turtle.down()
turtle.begin_fill()
turtle.goto(rightEarTop)
turtle.goto(rightEarBot)
turtle.goto(rightEarLeft)
turtle.end_fill()
turtle.up()
turtle.fillcolor("red4")
turtle.goto(rightEarBot)
turtle.down()
turtle.begin_fill()
turtle.goto(rightEarTop)
turtle.goto(rightEarIn)
turtle.goto(rightEarBot)
turtle.end_fill()
turtle.up()

turtle.goto(whiskerRightTopIn)
turtle.down()
turtle.goto(whiskerRightTopOut)
turtle.up()
turtle.goto(whiskerRightMidIn)
turtle.down()
turtle.goto(whiskerRightMidOut)
turtle.up()
turtle.goto(whiskerRightBotIn)
turtle.down()
turtle.goto(whiskerRightBotOut)
turtle.up()
turtle.goto(whiskerLeftTopIn)
turtle.down()
turtle.goto(whiskerLeftTopOut)
turtle.up()
turtle.goto(whiskerLeftMidIn)
turtle.down()
turtle.goto(whiskerLeftMidOut)
turtle.up()
turtle.goto(whiskerLeftBotIn)
turtle.down()
turtle.goto(whiskerLeftBotOut)
turtle.up()

turtle.goto(nose)
turtle.fillcolor("red")
turtle.down()
turtle.begin_fill()
turtle.circle(15)
turtle.end_fill()
turtle.up()

turtle.goto(tailLengthBot)
turtle.down()
turtle.goto(tailLengthTop)
turtle.begin_fill()
turtle.goto(tailEndLeft)
turtle.goto(tailEndTop)
turtle.goto(tailEndRight)
turtle.goto(tailLengthTop)
turtle.end_fill()
turtle.up()

turtle.goto(finger)
turtle.pensize(2)
turtle.down()
turtle.goto(beamLeft)
turtle.goto(beamSpikeLeft)
turtle.goto(beamSpikeMidLeft)
turtle.goto(beamSpikeMid)
turtle.goto(beamSpikeRight)
turtle.goto(finger)
turtle.up()

turtle.goto(text)
turtle.write("Pee In Bottles Ray",True,font = ("Impact",12,"normal"))

#=======Clean up code (do not change)======
# this code ensures that your script runs correctly each time.
turtle.done()
