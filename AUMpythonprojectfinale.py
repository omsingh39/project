# -*- coding: utf-8 -*-
"""
Created on Sun Mar 27 12:38:22 2022

@author: Acer01
"""


import turtle as t
playerAscore=0
playerBscore=0
  
#creating a window and declaring a variable called window and calling the screen()
window=t.Screen()
window.title("The Passer Game")
window.bgcolor("green")
window.setup(width=1000,height=600)
window.tracer(0)
  
#Creating the left paddle
leftpaddle=t.Turtle()
leftpaddle.speed(6)
leftpaddle.shape("square")
leftpaddle.color("black")
leftpaddle.shapesize(stretch_wid=5,stretch_len=1)
leftpaddle.penup()
leftpaddle.goto(-350,0)
  
#Creating the right paddle
rightpaddle=t.Turtle()
rightpaddle.speed(6)
rightpaddle.shape("square")
rightpaddle.color("white")
rightpaddle.shapesize(stretch_wid=5,stretch_len=1)
rightpaddle.penup()
rightpaddle.goto(350,0)
  
#Code for creating the ball
ball=t.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(5,5)
ballxdirection=0.2
ballydirection=0.2
  
#Code for creating pen for scorecard update
pen=t.Turtle()
pen.speed(0)
pen.color("Blue")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("score",align="center",font=('Arial',24,'normal'))
  
#code for moving the leftpaddle
def leftpaddleup():
    y=leftpaddle.ycor()
    y=y+90
    
    leftpaddle.sety(y)
  
def leftpaddledown():
    y=leftpaddle.ycor()
    y=y-90
    leftpaddle.sety(y)
  
#code for moving the rightpaddle
def rightpaddleup():
    y=rightpaddle.ycor()
    y=y+90
    rightpaddle.sety(y)
   # if rightpaddle.ycor()>290:
        #y=y-90
  
def rightpaddledown():
    y=rightpaddle.ycor()
    y=y-90
    rightpaddle.sety(y)
    #if rightpaddle.ycor()>-290:
       # y=y+90
  
#Assign keys to play
window.listen()
window.onkeypress(leftpaddleup,'w')
window.onkeypress(leftpaddledown,'s')
window.onkeypress(rightpaddleup,'Up')
window.onkeypress(rightpaddledown,'Down')
  
while True:
    window.update()
  
    #moving the ball
    ball.setx(ball.xcor()+ballxdirection)
    ball.sety(ball.ycor()+ballydirection)
  
    #border set up
    if ball.ycor()>290:
        # ball.sety(290)
        ballydirection=ballydirection*-1
    if ball.ycor()<-290:
        # ball.sety(-290)
        ballydirection=ballydirection*-1
          
    if  ball.xcor() > 390:
        ball.goto(0,0)
        ballxdirection = ballxdirection * -1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(playerAscore,playerBscore),align="center",font=('Monaco',24,"normal"))
        playerAscore = playerAscore + 1
       
  
  
  
    if  ball.xcor() < -390: # Left width paddle Border
        ball.goto(0,0)
        ballxdirection = ballxdirection * -1
        playerBscore = playerBscore + 1
        pen.clear()
        pen.write("Player A: {}                    Player B: {} ".format(playerAscore,playerBscore),align="center",font=('Monaco',24,"normal"))
        
  
     # Handling the collisions with paddles.
  
    if(ball.xcor() > 340) and (ball.xcor() < 350) and (ball.ycor() < rightpaddle.ycor() + 50 and ball.ycor() > rightpaddle.ycor() - 50):
        #ball.setx(340)
        ballxdirection = ballxdirection * -1
     
  
    if(ball.xcor() < -340) and (ball.xcor() > -350) and (ball.ycor() < leftpaddle.ycor() + 50 and ball.ycor() > leftpaddle.ycor() - 50):
        #ball.setx(-340)
        ballxdirection = ballxdirection * -1
        