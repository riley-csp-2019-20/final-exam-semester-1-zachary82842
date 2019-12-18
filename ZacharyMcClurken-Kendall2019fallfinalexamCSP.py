#2019-20 Fall Computer Science Principles Final Exam

#Ms. Haubold


#Name
#Zachary McClurken-Kendall
#Date
#12/18/19


#### INSTRUCTIONS ####
#Create an etch a sketch turtle game
#The turtle should move with the arrow keys (up, down, left and right), and draw
#Space should clear the screen
#o and p should make the pen size bigger and smaller
#u should pick the pen up or put the pen down
#All code must be commented
#BONUS
#Add a feature to change colors
#

#import required libraries
import turtle as trtl
import random

#create turtle
sketcher = trtl.Turtle()


#movement functions
def sketcher_up(): # make the up function
    sketcher.setheading(90)
    sketcher.forward(10)

def sketcher_down(): # make the down function
    sketcher.setheading(270)
    sketcher.forward(10)

def sketcher_right(): # make the right function
    sketcher.setheading(0)
    sketcher.forward(10)

def sketcher_left(): # make the left fuction
    sketcher.setheading(180)
    sketcher.forward(10)

#color/drawing functions

# Make a variable for pensize
ps = 1

# Make a color list to choose from
c_list = ["blue","green","purple","orange","yellow","black"]

def pen_bigger(): # make the pensize bigger fucntion
    sketcher.pensize(ps + 2)

def pen_smaller(): # make the pensize smaller function
    sketcher.pensize(ps - 1)

def clear_screen(): # make the clear function+
    sketcher.clear()

def penup_pendown(): # make the penup and down function
    if sketcher.isdown():
        sketcher.penup()
    else:
        sketcher.pendown()
      

def sketcher_color(): # make the turtle and the pen change its color to blue # This is the Extra part
    sketcher.pencolor(random.choice(c_list))
    sketcher.color(random.choice(c_list))


#create screen
wn = trtl.Screen()
#bind to keypresses
wn.onkeypress(sketcher_up, "Up")
wn.onkeypress(sketcher_down, "Down")
wn.onkeypress(sketcher_right, "Right")
wn.onkeypress(sketcher_left, "Left")
wn.onkeypress(pen_bigger, "p")
wn.onkeypress(pen_smaller, "o")
wn.onkeypress(clear_screen, "space")
wn.onkeypress(penup_pendown, "u")
wn.onkeypress(sketcher_color, "c")

#listen
wn.listen()

#mainloop
wn.mainloop()