import turtle

window=turtle.Screen()
window.bgcolor('black')
window.setup(width=1366,height=768)
window.title("Pac-Man Made by Marc")
window.tracer(0)

char=turtle.Turtle()
char.speed(0)
char.goto(600,-50)
char.shape('circle')
char.color('yellow')
char.penup()

char2=turtle.Turtle()
char2.speed(0)
char2.goto(char.xcor() -7 ,char.ycor()-2)
char2.shape('triangle')
char2.color('black')
char2.shapesize(stretch_len=0.5,stretch_wid=0.5)
char2.penup()

mouth=turtle.Turtle()
mouth.speed(0)
mouth.goto(char.xcor() -3 ,char.ycor() +5)
mouth.shape('circle')
mouth.color('black')
mouth.shapesize(stretch_len=0.3,stretch_wid=0.3)

score=0
score1=turtle.Turtle()
score1.speed(0)
score1.color('white')
score1.hideturtle()
score1.penup()
score1.goto(0,350)
score1.write("Score = 0",align='center',font=('Arial',18,'normal'))

lose=turtle.Turtle()
lose.speed(0)
lose.color('red')
lose.penup()
lose.goto(0,0)
lose.hideturtle()
#lose.write("You Lost",align='center',font=('Arial',24,'normal'))

win_msg=turtle.Turtle()
win_msg.speed(0)
win_msg.color('green')
win_msg.penup()
win_msg.goto(0,0)
win_msg.hideturtle()

eatable1=turtle.Turtle()
eatable1.speed(0)
eatable1.shape('circle')
eatable1.color('cyan')
eatable1.penup()
eatable1.goto(520,-50)
eatable1.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable2=turtle.Turtle()
eatable2.speed(0)
eatable2.shape('circle')
eatable2.color('cyan')
eatable2.penup()
eatable2.goto(420,-50)
eatable2.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable3=turtle.Turtle()
eatable3.speed(0)
eatable3.shape('circle')
eatable3.color('cyan')
eatable3.penup()
eatable3.goto(320,-50)
eatable3.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable4=turtle.Turtle()
eatable4.speed(0)
eatable4.shape('circle')
eatable4.color('cyan')
eatable4.penup()
eatable4.goto(220,-50)
eatable4.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable5=turtle.Turtle()
eatable5.speed(0)
eatable5.shape('circle')
eatable5.color('cyan')
eatable5.penup()
eatable5.goto(120,-50)
eatable5.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable6=turtle.Turtle()
eatable6.speed(0)
eatable6.shape('circle')
eatable6.color('cyan')
eatable6.penup()
eatable6.goto(20,-50)
eatable6.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable7=turtle.Turtle()
eatable7.speed(0)
eatable7.shape('circle')
eatable7.color('cyan')
eatable7.penup()
eatable7.goto(20,50)
eatable7.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable8=turtle.Turtle()
eatable8.speed(0)
eatable8.shape('circle')
eatable8.color('cyan')
eatable8.penup()
eatable8.goto(-120,50)
eatable8.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable9=turtle.Turtle()
eatable9.speed(0)
eatable9.shape('circle')
eatable9.color('cyan')
eatable9.penup()
eatable9.goto(-220,50)
eatable9.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable10=turtle.Turtle()
eatable10.speed(0)
eatable10.shape('circle')
eatable10.color('cyan')
eatable10.penup()
eatable10.goto(-320,50)
eatable10.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable11=turtle.Turtle()
eatable11.speed(0)
eatable11.shape('circle')
eatable11.color('cyan')
eatable11.penup()
eatable11.goto(-420,50)
eatable11.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable12=turtle.Turtle()
eatable12.speed(0)
eatable12.shape('circle')
eatable12.color('cyan')
eatable12.penup()
eatable12.goto(-520,50)
eatable12.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable13=turtle.Turtle()
eatable13.speed(0)
eatable13.shape('circle')
eatable13.color('cyan')
eatable13.penup()
eatable13.goto(-620,50)
eatable13.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable14=turtle.Turtle()
eatable14.speed(0)
eatable14.shape('circle')
eatable14.color('cyan')
eatable14.penup()
eatable14.goto(120,50)
eatable14.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable15=turtle.Turtle()
eatable15.speed(0)
eatable15.shape('circle')
eatable15.color('cyan')
eatable15.penup()
eatable15.goto(220,50)
eatable15.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable16=turtle.Turtle()
eatable16.speed(0)
eatable16.shape('circle')
eatable16.color('cyan')
eatable16.penup()
eatable16.goto(320,50)
eatable16.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable17=turtle.Turtle()
eatable17.speed(0)
eatable17.shape('circle')
eatable17.color('cyan')
eatable17.penup()
eatable17.goto(420,50)
eatable17.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable18=turtle.Turtle()
eatable18.speed(0)
eatable18.shape('circle')
eatable18.color('cyan')
eatable18.penup()
eatable18.goto(520,50)
eatable18.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable19=turtle.Turtle()
eatable19.speed(0)
eatable19.shape('circle')
eatable19.color('cyan')
eatable19.penup()
eatable19.goto(620,50)
eatable19.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable20=turtle.Turtle()
eatable20.speed(0)
eatable20.shape('circle')
eatable20.color('cyan')
eatable20.penup()
eatable20.goto(20,150)
eatable20.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable21=turtle.Turtle()
eatable21.speed(0)
eatable21.shape('circle')
eatable21.color('cyan')
eatable21.penup()
eatable21.goto(-120,150)
eatable21.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable22=turtle.Turtle()
eatable22.speed(0)
eatable22.shape('circle')
eatable22.color('cyan')
eatable22.penup()
eatable22.goto(-220,150)
eatable22.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable23=turtle.Turtle()
eatable23.speed(0)
eatable23.shape('circle')
eatable23.color('cyan')
eatable23.penup()
eatable23.goto(-320,150)
eatable23.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable24=turtle.Turtle()
eatable24.speed(0)
eatable24.shape('circle')
eatable24.color('cyan')
eatable24.penup()
eatable24.goto(-420,150)
eatable24.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable25=turtle.Turtle()
eatable25.speed(0)
eatable25.shape('circle')
eatable25.color('cyan')
eatable25.penup()
eatable25.goto(-520,150)
eatable25.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable26=turtle.Turtle()
eatable26.speed(0)
eatable26.shape('circle')
eatable26.color('cyan')
eatable26.penup()
eatable26.goto(-620,150)
eatable26.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable27=turtle.Turtle()
eatable27.speed(0)
eatable27.shape('circle')
eatable27.color('cyan')
eatable27.penup()
eatable27.goto(20,250)
eatable27.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable28=turtle.Turtle()
eatable28.speed(0)
eatable28.shape('circle')
eatable28.color('cyan')
eatable28.penup()
eatable28.goto(120,250)
eatable28.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable29=turtle.Turtle()
eatable29.speed(0)
eatable29.shape('circle')
eatable29.color('cyan')
eatable29.penup()
eatable29.goto(220,250)
eatable29.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable30=turtle.Turtle()
eatable30.speed(0)
eatable30.shape('circle')
eatable30.color('cyan')
eatable30.penup()
eatable30.goto(320,250)
eatable30.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable31=turtle.Turtle()
eatable31.speed(0)
eatable31.shape('circle')
eatable31.color('cyan')
eatable31.penup()
eatable31.goto(420,250)
eatable31.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable32=turtle.Turtle()
eatable32.speed(0)
eatable32.shape('circle')
eatable32.color('cyan')
eatable32.penup()
eatable32.goto(520,250)
eatable32.shapesize(stretch_len=0.7,stretch_wid=0.7)

eatable33=turtle.Turtle()
eatable33.speed(0)
eatable33.shape('circle')
eatable33.color('cyan')
eatable33.penup()
eatable33.goto(620,250)
eatable33.shapesize(stretch_len=0.7,stretch_wid=0.7)

barrier1_normal=turtle.Turtle()
barrier1_normal.speed(0)
barrier1_normal.shape('square')
barrier1_normal.color('magenta')
barrier1_normal.penup()
barrier1_normal.goto(400,-20)
barrier1_normal.shapesize(stretch_len=35,stretch_wid=0.3)

barrier2_normal=turtle.Turtle()
barrier2_normal.speed(0)
barrier2_normal.shape('square')
barrier2_normal.color('magenta')
barrier2_normal.penup()
barrier2_normal.goto(400,-75)
barrier2_normal.shapesize(stretch_len=41,stretch_wid=0.3)

barrier1=turtle.Turtle()
barrier1.speed(0)
barrier1.shape('square')
barrier1.color('magenta')
barrier1.right(90)
barrier1.penup()
barrier1.goto(50,2)
barrier1.shapesize(stretch_len=2.5,stretch_wid=0.3)

barrier2=turtle.Turtle()
barrier2.speed(0)
barrier2.shape('square')
barrier2.color('magenta')
barrier2.right(90)
barrier2.penup()
barrier2.goto(-5,-20)
barrier2.shapesize(stretch_len=5,stretch_wid=0.3)

barrier3_normal=turtle.Turtle()
barrier3_normal.speed(0)
barrier3_normal.shape('square')
barrier3_normal.color('magenta')
barrier3_normal.penup()
barrier3_normal.goto(357,25)
barrier3_normal.shapesize(stretch_len=31,stretch_wid=0.3)

barrier3=turtle.Turtle()
barrier3.speed(0)
barrier3.shape('square')
barrier3.color('magenta')
barrier3.penup()
barrier3.right(90)
barrier3.goto(665,50)
barrier3.shapesize(stretch_len=3,stretch_wid=0.3)

barrier4_normal=turtle.Turtle()
barrier4_normal.speed(0)
barrier4_normal.shape('square')
barrier4_normal.color('magenta')
barrier4_normal.penup()
barrier4_normal.goto(357,79)
barrier4_normal.shapesize(stretch_len=31,stretch_wid=0.3)

barrier5_normal=turtle.Turtle()
barrier5_normal.speed(0)
barrier5_normal.shape('square')
barrier5_normal.color('magenta')
barrier5_normal.penup()
barrier5_normal.goto(357,220)
barrier5_normal.shapesize(stretch_len=31,stretch_wid=0.3)

barrier4=turtle.Turtle()
barrier4.speed(0)
barrier4.shape('square')
barrier4.color('magenta')
barrier4.right(90)
barrier4.penup()
barrier4.goto(50,150)
barrier4.shapesize(stretch_len=7,stretch_wid=0.3)

barrier6_normal=turtle.Turtle()
barrier6_normal.speed(0)
barrier6_normal.shape('square')
barrier6_normal.color('magenta')
barrier6_normal.penup()
barrier6_normal.goto(328,290)
barrier6_normal.shapesize(stretch_len=33.9,stretch_wid=0.3)

barrier7_normal=turtle.Turtle()
barrier7_normal.speed(0)
barrier7_normal.shape('square')
barrier7_normal.color('magenta')
barrier7_normal.penup()
barrier7_normal.goto(-340,25)
barrier7_normal.shapesize(stretch_len=33,stretch_wid=0.3)

barrier5=turtle.Turtle()
barrier5.speed(0)
barrier5.shape('square')
barrier5.color('magenta')
barrier5.penup()
barrier5.right(90)
barrier5.goto(-665,55)
barrier5.shapesize(stretch_len=2.5,stretch_wid=0.3)

barrier8_normal=turtle.Turtle()
barrier8_normal.speed(0)
barrier8_normal.shape('square')
barrier8_normal.color('magenta')
barrier8_normal.penup()
barrier8_normal.goto(-340,80)
barrier8_normal.shapesize(stretch_len=33,stretch_wid=0.3)

barrier6=turtle.Turtle()
barrier6.speed(0)
barrier6.shape('square')
barrier6.color('magenta')
barrier6.right(90)
barrier6.penup()
barrier6.goto(-10,103)
barrier6.shapesize(stretch_len=2.7,stretch_wid=0.3)

barrier9_normal=turtle.Turtle()
barrier9_normal.speed(0)
barrier9_normal.shape('square')
barrier9_normal.color('magenta')
barrier9_normal.penup()
barrier9_normal.goto(-340,125)
barrier9_normal.shapesize(stretch_len=33,stretch_wid=0.3)

barrier10_normal=turtle.Turtle()
barrier10_normal.speed(0)
barrier10_normal.shape('square')
barrier10_normal.color('magenta')
barrier10_normal.penup()
barrier10_normal.goto(-340,180)
barrier10_normal.shapesize(stretch_len=33,stretch_wid=0.3)

barrier7=turtle.Turtle()
barrier7.speed(0)
barrier7.shape('square')
barrier7.color('magenta')
barrier7.right(90)
barrier7.penup()
barrier7.goto(-665,155)
barrier7.shapesize(stretch_len=2.5,stretch_wid=0.3)

barrier8=turtle.Turtle()
barrier8.speed(0)
barrier8.shape('square')
barrier8.color('magenta')
barrier8.right(90)
barrier8.penup()
barrier8.goto(-10,235)
barrier8.shapesize(stretch_len=5.6,stretch_wid=0.3)

barrier9=turtle.Turtle()
barrier9.speed(0)
barrier9.shape('square')
barrier9.color('magenta')
barrier9.right(90)
barrier9.penup()
barrier9.goto(665,255)
barrier9.shapesize(stretch_len=3.5,stretch_wid=0.3)

barrier10=turtle.Turtle()
barrier10.speed(0)
barrier10.shape('square')
barrier10.color('magenta')
barrier10.right(90)
barrier10.penup()
barrier10.goto(670,-50)
barrier10.shapesize(stretch_len=2.7,stretch_wid=0.3)

enemy1=turtle.Turtle()
enemy1.speed(0)
enemy1.shape('circle')
enemy1.color('red')
#enemy1.hideturtle()
enemy1.penup()
enemy1.goto(20,50)
enemy1.dx=1.5
enemy2=turtle.Turtle()
enemy2.speed(0)
enemy2.shape('circle')
enemy2.color('red')
#enemy1.hideturtle()
enemy2.penup()
enemy2.goto(320,250)
enemy2.dx=1.5

def move_left():
    char.clear()
    char.backward(5)
    char2.clear()
    char2.backward(5)
    mouth.clear()
    mouth.backward(5)
    
def move_right():
    char.clear()
    char.forward(5)
    char2.clear()
    char2.forward(5)
    mouth.clear()
    mouth.forward(5)
def move_up():
    char.clear()
    char.sety(char.ycor()+5)
    char2.clear()
    char2.sety(char2.ycor()+5)
    mouth.clear()
    mouth.sety(mouth.ycor()+5)
def move_down():
    char.clear()
    char.sety(char.ycor()-5)
    char2.clear()
    char2.sety(char2.ycor()-5)
    mouth.clear()
    mouth.sety(mouth.ycor()-5)
def close_button():
    turtle.bye()
def fast_left():
    char.clear()
    char.forward(100)
    char2.clear()
    char2.forward(100)
    mouth.clear()
    mouth.forward(100)
def fast_right():
    char.clear()
    char.backward(100)
    char2.clear()
    char2.backward(100)
    mouth.clear()
    mouth.backward(100)
def enemy1_left():
    enemy1.clear()
    enemy1.forward(10)
def enemy1_right():
    enemy1.clear()
    enemy1.backward(10)

window.listen()
window.onkeypress(move_left,"Left")
window.onkeypress(move_right,"Right")
window.onkeypress(move_up,"Up")
window.onkeypress(move_down,"Down")
window.onkeypress(fast_left,"D")
window.onkeypress(fast_right,"A")

while True:
    window.update()
    
    enemy1.setx(enemy1.xcor() + enemy1.dx)
    if enemy1.xcor() == 200:
        enemy1.clear()
        enemy1.dx *= -1
    if enemy1.xcor() <= -200:
        enemy1.clear()
        enemy1.dx *= -1
    
    enemy2.setx(enemy2.xcor() + enemy2.dx)
    if enemy2.xcor() == 500:
        enemy2.clear()
        enemy2.dx *= -1
    if enemy2.xcor() == 20:
        enemy2.clear()
        enemy2.dx *= -1
    
    
    if ((enemy1.xcor() == char.xcor()) or (enemy1.xcor() +10 == char.xcor())) and ((enemy1.ycor() == char.ycor()) or (enemy1.ycor() + 10 == char.ycor() + 10)):
        lose.write("You Lost Press R to Close",align='center',font=("Arial 50"))
        window.onkeypress(exit,"Down")
        window.onkeypress(exit,"Right")
        window.onkeypress(exit,"Left")
        window.onkeypress(exit,"Up")
        window.onkeypress(close_button,"r")
    
    if ((enemy2.xcor() == char.xcor()) or (enemy2.xcor() +10 == char.xcor())) and ((enemy2.ycor() == char.ycor()) or (enemy2.ycor() + 10 == char.ycor() + 10)):
        lose.write("You Lost Press R to Close",align='center',font=("Arial 50"))
        window.onkeypress(exit,"Down")
        window.onkeypress(exit,"Right")
        window.onkeypress(exit,"Left")
        window.onkeypress(exit,"Up")
        window.onkeypress(close_button,"r")
    
    
    if score >= 33:
        win_msg.write("You Won Press R to close",align='center',font=("Arial",50))
        window.onkeypress(exit,"Down")
        window.onkeypress(exit,"Right")
        window.onkeypress(exit,"Left")
        window.onkeypress(exit,"Up")
        window.onkeypress(close_button,"r")
    
    if (char.xcor() <= barrier1_normal.xcor() + 350) and (char.xcor() >= barrier1_normal.xcor() - 350) and (char.ycor() == barrier1_normal.ycor()):
        lose.write("You Lost Press R to Close",align='center',font=("Arial 50"))
        window.onkeypress(exit,"Down")
        window.onkeypress(exit,"Right")
        window.onkeypress(exit,"Left")
        window.onkeypress(exit,"Up")
        window.onkeypress(close_button,"r")
    if (char.xcor() <= barrier2_normal.xcor() + 410) and (char.xcor() >= barrier2_normal.xcor() - 410) and (char.ycor() == barrier2_normal.ycor()):
        lose.write("You Lost Press R to Close",align='center',font=("Arial 50"))
        window.onkeypress(exit,"Down")
        window.onkeypress(exit,"Right")
        window.onkeypress(exit,"Left")
        window.onkeypress(exit,"Up")
        window.onkeypress(close_button,"r")
    if (char.xcor() <= barrier3_normal.xcor() + 310) and (char.xcor() >= barrier3_normal.xcor() - 310) and (char.ycor() == barrier3_normal.ycor()):
        lose.write("You Lost Press R to Close",align='center',font=("Arial 50"))
        window.onkeypress(exit,"Down")
        window.onkeypress(exit,"Right")
        window.onkeypress(exit,"Left")
        window.onkeypress(exit,"Up")
        window.onkeypress(close_button,"r")
    if (char.xcor() <= barrier4_normal.xcor() + 310) and (char.xcor() >= barrier4_normal.xcor() - 310) and (char.ycor() == barrier4_normal.ycor()):
        lose.write("You Lost Press R to Close",align='center',font=("Arial 50"))
        window.onkeypress(exit,"Down")
        window.onkeypress(exit,"Right")
        window.onkeypress(exit,"Left")
        window.onkeypress(exit,"Up")
        window.onkeypress(close_button,"r")
    if (char.xcor() <= barrier5_normal.xcor() + 310) and (char.xcor() >= barrier5_normal.xcor() - 310) and (char.ycor() == barrier5_normal.ycor()):
        lose.write("You Lost Press R to Close",align='center',font=("Arial 50"))
        window.onkeypress(exit,"Down")
        window.onkeypress(exit,"Right")
        window.onkeypress(exit,"Left")
        window.onkeypress(exit,"Up")
        window.onkeypress(close_button,"r")
    if (char.xcor() <= barrier6_normal.xcor() + 339) and (char.xcor() >= barrier6_normal.xcor() - 339) and (char.ycor() == barrier6_normal.ycor()):
        lose.write("You Lost Press R to Close",align='center',font=("Arial 50"))
        window.onkeypress(exit,"Down")
        window.onkeypress(exit,"Right")
        window.onkeypress(exit,"Left")
        window.onkeypress(exit,"Up")
        window.onkeypress(close_button,"r")
    if (char.xcor() <= barrier7_normal.xcor() + 330) and (char.xcor() >= barrier7_normal.xcor() - 330) and (char.ycor() == barrier7_normal.ycor()):
        lose.write("You Lost Press R to Close",align='center',font=("Arial 50"))
        window.onkeypress(exit,"Down")
        window.onkeypress(exit,"Right")
        window.onkeypress(exit,"Left")
        window.onkeypress(exit,"Up")
        window.onkeypress(close_button,"r")
    if (char.xcor() <= barrier8_normal.xcor() + 330) and (char.xcor() >= barrier8_normal.xcor() - 330) and (char.ycor() == barrier8_normal.ycor()):
        lose.write("You Lost Press R to Close",align='center',font=("Arial 50"))
        window.onkeypress(exit,"Down")
        window.onkeypress(exit,"Right")
        window.onkeypress(exit,"Left")
        window.onkeypress(exit,"Up")
        window.onkeypress(close_button,"r")
    if (char.xcor() <= barrier9_normal.xcor() + 330) and (char.xcor() >= barrier9_normal.xcor() - 330) and (char.ycor() == barrier9_normal.ycor()):
        lose.write("You Lost Press R to Close",align='center',font=("Arial 50"))
        window.onkeypress(exit,"Down")
        window.onkeypress(exit,"Right")
        window.onkeypress(exit,"Left")
        window.onkeypress(exit,"Up")
        window.onkeypress(close_button,"r")
    if (char.xcor() <= barrier10_normal.xcor() + 330) and (char.xcor() >= barrier10_normal.xcor() - 330) and (char.ycor() == barrier10_normal.ycor()):
        lose.write("You Lost Press R to Close",align='center',font=("Arial 50"))
        window.onkeypress(exit,"Down")
        window.onkeypress(exit,"Right")
        window.onkeypress(exit,"Left")
        window.onkeypress(exit,"Up")
        window.onkeypress(close_button,"r")
        
    if (char.xcor() == barrier1.xcor())  and (char.ycor() <= barrier1.ycor()  +25 ) and (char.ycor() >= barrier1.ycor() - 25):
        lose.write("You Lost Press R to Close",align='center',font=("Arial 50"))
        window.onkeypress(exit,"Down")
        window.onkeypress(exit,"Right")
        window.onkeypress(exit,"Left")
        window.onkeypress(exit,"Up")
        window.onkeypress(close_button,"r")
    if (char.xcor() == barrier2.xcor())  and (char.ycor() <= barrier2.ycor()  +50 ) and (char.ycor() >= barrier2.ycor() - 50):
        lose.write("You Lost Press R to Close",align='center',font=("Arial 50"))
        window.onkeypress(exit,"Down")
        window.onkeypress(exit,"Right")
        window.onkeypress(exit,"Left")
        window.onkeypress(exit,"Up")
        window.onkeypress(close_button,"r")
    if (char.xcor() == barrier3.xcor())  and (char.ycor() <= barrier3.ycor()  +30 ) and (char.ycor() >= barrier3.ycor() - 30):
        lose.write("You Lost Press R to Close",align='center',font=("Arial 50"))
        window.onkeypress(exit,"Down")
        window.onkeypress(exit,"Right")
        window.onkeypress(exit,"Left")
        window.onkeypress(exit,"Up")
        window.onkeypress(close_button,"r")
    if (char.xcor() == barrier4.xcor())  and (char.ycor() <= barrier4.ycor()  +70 ) and (char.ycor() >= barrier4.ycor() - 70):
        lose.write("You Lost Press R to Close",align='center',font=("Arial 50"))
        window.onkeypress(exit,"Down")
        window.onkeypress(exit,"Right")
        window.onkeypress(exit,"Left")
        window.onkeypress(exit,"Up")
        window.onkeypress(close_button,"r")
    if (char.xcor() == barrier5.xcor())  and (char.ycor() <= barrier5.ycor()  +25 ) and (char.ycor() >= barrier5.ycor() - 25):
        lose.write("You Lost Press R to Close",align='center',font=("Arial 50"))
        window.onkeypress(exit,"Down")
        window.onkeypress(exit,"Right")
        window.onkeypress(exit,"Left")
        window.onkeypress(exit,"Up")
        window.onkeypress(close_button,"r")
    if (char.xcor() == barrier6.xcor())  and (char.ycor() <= barrier6.ycor()  +27 ) and (char.ycor() >= barrier6.ycor() - 27):
        lose.write("You Lost Press R to Close",align='center',font=("Arial 50"))
        window.onkeypress(exit,"Down")
        window.onkeypress(exit,"Right")
        window.onkeypress(exit,"Left")
        window.onkeypress(exit,"Up")
        window.onkeypress(close_button,"r")
    if (char.xcor() == barrier7.xcor())  and (char.ycor() <= barrier7.ycor()  +25 ) and (char.ycor() >= barrier7.ycor() - 25):
        lose.write("You Lost Press R to Close",align='center',font=("Arial 50"))
        window.onkeypress(exit,"Down")
        window.onkeypress(exit,"Right")
        window.onkeypress(exit,"Left")
        window.onkeypress(exit,"Up")
        window.onkeypress(close_button,"r")
    if (char.xcor() == barrier8.xcor())  and (char.ycor() <= barrier8.ycor()  +56 ) and (char.ycor() >= barrier8.ycor() - 56):
        lose.write("You Lost Press R to Close",align='center',font=("Arial 50"))
        window.onkeypress(exit,"Down")
        window.onkeypress(exit,"Right")
        window.onkeypress(exit,"Left")
        window.onkeypress(exit,"Up")
        window.onkeypress(close_button,"r")
    if (char.xcor() == barrier9.xcor())  and (char.ycor() <= barrier9.ycor()  +35 ) and (char.ycor() >= barrier9.ycor() - 35):
        lose.write("You Lost Press R to Close",align='center',font=("Arial 50"))
        window.onkeypress(exit,"Down")
        window.onkeypress(exit,"Right")
        window.onkeypress(exit,"Left")
        window.onkeypress(exit,"Up")
        window.onkeypress(close_button,"r")
    if (char.xcor() == barrier10.xcor())  and (char.ycor() <= barrier10.ycor()  +27 ) and (char.ycor() >= barrier10.ycor() - 27):
        lose.write("You Lost Press R to Close",align='center',font=("Arial 50"))
        window.onkeypress(exit,"Down")
        window.onkeypress(exit,"Right")
        window.onkeypress(exit,"Left")
        window.onkeypress(exit,"Up")
        window.onkeypress(close_button,"r")
    
    
    if (eatable1.xcor() == char.xcor()) and (eatable1.ycor() == char.ycor()):
        eatable1.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable1.goto(999,-9950)
    if (eatable2.xcor() == char.xcor()) and (eatable2.ycor() == char.ycor()):
        eatable2.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable2.goto(9999,-59990)
    if (eatable3.xcor() == char.xcor()) and (eatable3.ycor() == char.ycor()):
        eatable3.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable3.goto(9999999,-999999)
    if (eatable4.xcor() == char.xcor()) and (eatable4.ycor() == char.ycor()):
        eatable4.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable4.goto(999,9999)
    if (eatable5.xcor() == char.xcor()) and (eatable5.ycor() == char.ycor()):
        eatable5.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable5.goto(9999,9999)
    if  (eatable6.xcor() == char.xcor()) and (eatable6.ycor() == char.ycor()):
        eatable6.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable6.goto(666666,99999)
    if (eatable7.xcor() == char.xcor()) and (eatable7.ycor() == char.ycor()):
        eatable7.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable7.goto(9999,9999)
    if (eatable8.ycor() == char.ycor()) and (eatable8.xcor() == char.xcor()):
        eatable8.clear()
        score1.clear()
        score += 1                     #8
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable8.goto(999999,-9999999)
    if (eatable9.ycor() == char.ycor()) and (eatable9.xcor() >= char.xcor()):
        eatable9.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable9.goto(-9999,9999)
    if (eatable10.ycor() == char.ycor()) and (eatable10.xcor() >= char.xcor()):
        eatable10.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable10.goto(-9999,9999)
    if (eatable11.ycor() == char.ycor()) and (eatable11.xcor() >= char.xcor()):
        eatable11.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable11.goto(-9999,9999)
    if (eatable12.ycor() == char.ycor()) and (eatable12.xcor() >= char.xcor()):
        eatable12.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable12.goto(-9999,9999)
    if (eatable13.ycor() == char.ycor()) and (eatable13.xcor() >= char.xcor()):
        eatable13.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable13.goto(-9999,9999)
    if (eatable14.ycor() == char.ycor()) and (eatable14.xcor() == char.xcor()):
        eatable14.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable14.goto(999999,-9999999)
    if (eatable15.ycor() == char.ycor()) and (eatable15.xcor() == char.xcor()):
        eatable15.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable15.goto(-9999,9999)
    if (eatable16.ycor() == char.ycor()) and (eatable16.xcor() == char.xcor()):
        eatable16.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable16.goto(-9999,9999)
    if (eatable17.ycor() == char.ycor()) and (eatable17.xcor() == char.xcor()):
        eatable17.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable17.goto(-9999,9999)
    if (eatable18.ycor() == char.ycor()) and (eatable18.xcor() == char.xcor()):
        eatable18.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable18.goto(-9999,9999)
    if (eatable19.ycor() == char.ycor()) and (eatable19.xcor() == char.xcor()):
        eatable19.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable19.goto(-9999,9999)
    if (eatable20.ycor() == char.ycor()) and (eatable20.xcor() == char.xcor()):
        eatable20.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable20.goto(-9999,9999)
    if (eatable21.ycor() == char.ycor()) and (eatable21.xcor() == char.xcor()):
        eatable21.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable21.goto(-9999,9999)
    if (eatable22.ycor() == char.ycor()) and (eatable22.xcor() == char.xcor()):
        eatable22.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable22.goto(-9999,9999)
    if (eatable23.ycor() == char.ycor()) and (eatable23.xcor() == char.xcor()):
        eatable23.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable23.goto(-9999,9999)
    if (eatable24.ycor() == char.ycor()) and (eatable24.xcor() == char.xcor()):
        eatable24.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable24.goto(-9999,9999)
    if (eatable25.ycor() == char.ycor()) and (eatable25.xcor() == char.xcor()):
        eatable25.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable25.goto(-9999,9999)
    if (eatable26.ycor() == char.ycor()) and (eatable26.xcor() == char.xcor()):
        eatable26.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable26.goto(-9999,9999)
    if (eatable27.ycor() == char.ycor()) and (eatable27.xcor() == char.xcor()):
        eatable27.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable27.goto(-9999,9999)
    if (eatable28.ycor() == char.ycor()) and (eatable28.xcor() == char.xcor()):
        eatable28.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable28.goto(-9999,9999)
    if (eatable29.ycor() == char.ycor()) and (eatable29.xcor() == char.xcor()):
        eatable29.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable29.goto(-9999,9999)
    if (eatable30.ycor() == char.ycor()) and (eatable30.xcor() == char.xcor()):
        eatable30.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable30.goto(-9999,9999)
    if (eatable31.ycor() == char.ycor()) and (eatable31.xcor() == char.xcor()):
        eatable31.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable31.goto(-9999,9999)
    if (eatable32.ycor() == char.ycor()) and (eatable32.xcor() == char.xcor()):
        eatable32.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable32.goto(-9999,9999)
    if (eatable33.ycor() == char.ycor()) and (eatable33.xcor() == char.xcor()):
        eatable33.clear()
        score1.clear()
        score += 1
        score1.write(f'Score={score}',align='center',font=('Arial',18,'normal'))
        eatable33.goto(-9999,9999)
