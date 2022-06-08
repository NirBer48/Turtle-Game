import turtle
import time
import random

t = 0 #arrows timing
d = 0 #arrows timing
b = 2.5 #arrows speed
l = 1 #level
f = 0 #lucky arrow timing
s = 0 #score
luck = False #checking for lucky arrow
god = False #god level eZ 
Game_Over = False #game status

#game window
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Little turtle")
wn.setup(width=1200, height=700)
wn.tracer(0)

#turtle (player)
tr = turtle.Turtle()
tr.speed(0)
tr.shape("turtle")
tr.color("green")
tr.penup()
tr.left(90)
tr.goto(0, -300)
tr.shapesize(stretch_wid=2.5, stretch_len=2.5) #50 pixels by 50 pixels

#pen1 (countdown)
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, -50)

#pen 2 (level)
pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color("white")
pen2.penup()
pen2.hideturtle()
pen2.goto(440, 280)

#pen 3 (abilitys)
pen3 = turtle.Turtle()
pen3.speed(0)
pen3.color("white")
pen3.penup()
pen3.hideturtle()
pen3.goto(400, 240)

#pen 4 (score - final)
pen4 = turtle.Turtle()
pen4.speed(0)
pen4.color("blue")
pen4.penup()
pen4.hideturtle()
pen4.goto(0, -200)

#pen 5 (score - updated)
pen5 = turtle.Turtle()
pen5.speed(0)
pen5.color("white")
pen5.penup()
pen5.hideturtle()
pen5.goto(500, -300)

#arrows
arr1 = turtle.Turtle()
arr1.speed(0)
arr1.shape("classic")
arr1.color("red")
arr1.penup()
arr1.shapesize(stretch_wid=3, stretch_len=7)
arr1.right(90)
arr1.goto(0, 350)
arr1.dy = -0.7 # speed of arrows
arr1.dx = 0.4 # speed of arrows (boss)

arr2 = turtle.Turtle()
arr2.speed(0)
arr2.shape("classic")
arr2.color("red")
arr2.penup()
arr2.shapesize(stretch_wid=3, stretch_len=7)
arr2.right(90)
arr2.goto(0, 350)

arr3 = turtle.Turtle()
arr3.speed(0)
arr3.shape("classic")
arr3.color("red")
arr3.penup()
arr3.shapesize(stretch_wid=3, stretch_len=7)
arr3.right(90)
arr3.goto(0, 350)

arr4 = turtle.Turtle()
arr4.speed(0)
arr4.shape("classic")
arr4.color("red")
arr4.penup()
arr4.shapesize(stretch_wid=3, stretch_len=7)
arr4.right(90)
arr4.goto(0, 350)

arr5 = turtle.Turtle()
arr5.speed(0)
arr5.shape("classic")
arr5.color("red")
arr5.penup()
arr5.shapesize(stretch_wid=3, stretch_len=7)
arr5.right(90)
arr5.goto(0, 350)

arr6 = turtle.Turtle()
arr6.speed(0)
arr6.shape("classic")
arr6.color("red")
arr6.penup()
arr6.shapesize(stretch_wid=3, stretch_len=7)
arr6.right(90)
arr6.goto(0, 350)

arr7 = turtle.Turtle()
arr7.speed(0)
arr7.shape("classic")
arr7.color("red")
arr7.penup()
arr7.shapesize(stretch_wid=3, stretch_len=7)
arr7.right(90)
arr7.goto(0, 350)

arr8 = turtle.Turtle()
arr8.speed(0)
arr8.shape("classic")
arr8.color("red")
arr8.penup()
arr8.shapesize(stretch_wid=3, stretch_len=7)
arr8.right(90)
arr8.goto(0, 350)

arr9 = turtle.Turtle()
arr9.speed(0)
arr9.shape("classic")
arr9.color("red")
arr9.penup()
arr9.shapesize(stretch_wid=3, stretch_len=7)
arr9.right(90)
arr9.goto(0, 350)

arr10 = turtle.Turtle()
arr10.speed(0)
arr10.shape("classic")
arr10.color("red")
arr10.penup()
arr10.shapesize(stretch_wid=3, stretch_len=7)
arr10.right(90)
arr10.goto(0, 350)

arr11 = turtle.Turtle()
arr11.speed(0)
arr11.shape("classic")
arr11.color("red")
arr11.penup()
arr11.shapesize(stretch_wid=3, stretch_len=7)
arr11.right(90)
arr11.goto(0, 350)

arr12 = turtle.Turtle()
arr12.speed(0)
arr12.shape("classic")
arr12.color("red")
arr12.penup()
arr12.shapesize(stretch_wid=3, stretch_len=7)
arr12.right(90)
arr12.goto(0, 350)

arr13 = turtle.Turtle()
arr13.speed(0)
arr13.shape("classic")
arr13.color("red")
arr13.penup()
arr13.shapesize(stretch_wid=3, stretch_len=7)
arr13.right(90)
arr13.goto(0, 350)

arr14 = turtle.Turtle()
arr14.speed(0)
arr14.shape("classic")
arr14.color("red")
arr14.penup()
arr14.shapesize(stretch_wid=3, stretch_len=7)
arr14.right(90)
arr14.goto(0, 350)

arr15 = turtle.Turtle()
arr15.speed(0)
arr15.shape("classic")
arr15.color("red")
arr15.penup()
arr15.shapesize(stretch_wid=3, stretch_len=7)
arr15.right(90)
arr15.goto(0, 350)

#specials
lucky = turtle.Turtle()
lucky.speed(0)
lucky.shape("classic")
lucky.color("gold")
lucky.penup()
lucky.shapesize(stretch_wid=3, stretch_len=7)
lucky.right(90)
lucky.dy = -0.4
lucky.goto(0, 10000000)

#movment
def move_left():
    x = tr.xcor()
    x -= 20
    tr.setx(x)
    tr.right(90)

def move_right():
    x = tr.xcor()
    x += 20
    tr.setx(x)
    tr.right(90)

def move_up():
    y = tr.ycor()
    y += 20
    tr.sety(y)
    tr.right(90)
    
def move_down():
    y = tr.ycor()
    y -= 20
    tr.sety(y)
    tr.right(90)

def move_left_s():
    x = tr.xcor()
    x -= 40
    tr.setx(x)

def move_right_s():
    x = tr.xcor()
    x += 40
    tr.setx(x)

def move_up_s():
    y = tr.ycor()
    y += 40
    tr.sety(y)
    
def move_down_s():
    y = tr.ycor()
    y -= 40
    tr.sety(y)

wn.listen()
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

for i in range (3):
    pen.write(3-i, align = "center", font = ("Courier", 100, "normal"))
    pen.clear()
    time.sleep(1)

pen2.write("Level:{}".format(l) , align = "center", font = ("Courier", 40, "normal"))
pen5.write("Score:{}".format(s) , align = "center", font = ("Courier", 20, "normal"))

#main game loop
while not Game_Over:
    wn.update()
    arr1.sety(arr1.ycor() + arr1.dy)
    arr2.sety(arr2.ycor() + arr1.dy)
    arr3.sety(arr3.ycor() + arr1.dy)
    arr4.sety(arr4.ycor() + arr1.dy)
    arr5.sety(arr5.ycor() + arr1.dy)
    arr6.sety(arr6.ycor() + arr1.dy)
    arr7.sety(arr7.ycor() + arr1.dy)
    arr8.sety(arr8.ycor() + arr1.dy)
    arr9.sety(arr9.ycor() + arr1.dy)
    arr10.sety(arr10.ycor() + arr1.dy)
    arr11.sety(arr11.ycor() + arr1.dy)
    arr12.sety(arr12.ycor() + arr1.dy)
    arr13.sety(arr13.ycor() + arr1.dy)
    arr14.sety(arr14.ycor() + arr1.dy)
    arr15.sety(arr15.ycor() + arr1.dy)
    lucky.sety(lucky.ycor() + lucky.dy)

    t+= 1

    if  god == True:
        arr1.setx(arr1.xcor() + arr1.dx)
        arr2.setx(arr2.xcor() + arr1.dx)
        arr3.setx(arr3.xcor() + arr1.dx)
        arr4.setx(arr4.xcor() + arr1.dx)
        arr5.setx(arr5.xcor() + arr1.dx)
        arr6.setx(arr6.xcor() + arr1.dx)
        arr7.setx(arr7.xcor() + arr1.dx)
        arr8.setx(arr8.xcor() + arr1.dx)
        arr9.setx(arr9.xcor() + arr1.dx)
        arr10.setx(arr10.xcor() + arr1.dx)
        arr11.setx(arr11.xcor() + arr1.dx)
        arr12.setx(arr12.xcor() + arr1.dx)
        arr13.setx(arr13.xcor() + arr1.dx)
        arr14.setx(arr14.xcor() + arr1.dx)
        arr15.setx(arr15.xcor() + arr1.dx)

        if t%(100*b) == 0 and d == 0:
            arr1.goto(random.randint(-600, 540), 350)

        if t%(100*b) == 0 and d == 1:
            arr2.goto(-600, random.randint(-320, 350))

        if t%(100*b) == 0 and d == 2:
            arr3.goto(random.randint(-600, 540), 350)

        if t%(100*b) == 0 and d == 3:
            arr4.goto(-600, random.randint(-320, 350))

        if t%(100*b) == 0 and d == 4: 
            arr5.goto(random.randint(-600, 540), 350) 

        if t%(100*b) == 0 and d == 5: 
            arr6.goto(-600, random.randint(-320, 350))

        if t%(100*b) == 0 and d == 6: 
            arr7.goto(random.randint(-600, 540), 350)

        if t%(100*b) == 0 and d == 7: 
            arr8.goto(-600, random.randint(-320, 350))

        if t%(100*b) == 0 and d == 8: 
            arr9.goto(random.randint(-600, 540), 350)

        if t%(100*b) == 0 and d == 9: 
            arr10.goto(-600, random.randint(-320, 350))

        if t%(100*b) == 0 and d == 10: 
            arr11.goto(random.randint(-600, 540), 350)

        if t%(100*b) == 0 and d == 11: 
            arr12.goto(-600, random.randint(-320, 350))

        if t%(100*b) == 0 and d == 12: 
            arr13.goto(random.randint(-600, 540), 350)

        if t%(100*b) == 0 and d == 13: 
            arr14.goto(-600, random.randint(-320, 350))

        if t%(100*b) == 0 and d == 14: 
            arr15.goto(random.randint(-600, 540), 350)
            d = -1
        if t%(100*b) == 0:
            d += 1
            
    if tr.xcor() >= 550:
        tr.setx(550)

    if tr.xcor() <= -575:
        tr.setx(-575)

    if tr.ycor() >= 325:
        tr.sety(325)

    if tr.ycor() <= -310:
        tr.sety(-310)

    if arr1.ycor() < -380 or arr1.ycor() < -380 or arr2.ycor() < -380 or arr3.ycor() < -380 or arr4.ycor() < -380 or arr5.ycor() < -380 or arr6.ycor() < -380 or arr7.ycor() < -380 or arr8.ycor() < -380 or arr9.ycor() < -380 or arr10.ycor() < -380 or arr11.ycor() < -380 or arr12.ycor() < -380 or arr13.ycor() < -380 or arr14.ycor() < -380 or arr15.ycor() < -380:
        s += 1
        pen5.clear()
        pen5.write("Score:{}".format(s) , align = "center", font = ("Courier", 20, "normal"))
    if god == False:
        if t%(100*b) == 0 and d == 0:
            arr1.goto(random.randint(-580, 580), 350)

        if t%(100*b) == 0 and d == 1:
            arr2.goto(random.randint(-580, 580), 350)

        if t%(100*b) == 0 and d == 2:
            arr3.goto(random.randint(-580, 580), 350)

        if t%(100*b) == 0 and d == 3:
            arr4.goto(random.randint(-580, 580), 350)

        if t%(100*b) == 0 and d == 4: 
            arr5.goto(random.randint(-580, 580), 350) 

        if t%(100*b) == 0 and d == 5: 
            arr6.goto(random.randint(-580, 580), 350)

        if t%(100*b) == 0 and d == 6: 
            arr7.goto(random.randint(-580, 580), 350)

        if t%(100*b) == 0 and d == 7: 
            arr8.goto(random.randint(-580, 580), 350)

        if t%(100*b) == 0 and d == 8: 
            arr9.goto(random.randint(-580, 580), 350)

        if t%(100*b) == 0 and d == 9: 
            arr10.goto(random.randint(-580, 580), 350)

        if t%(100*b) == 0 and d == 10: 
            arr11.goto(random.randint(-580, 580), 350)

        if t%(100*b) == 0 and d == 11: 
            arr12.goto(random.randint(-580, 580), 350)

        if t%(100*b) == 0 and d == 12: 
            arr13.goto(random.randint(-580, 580), 350)

        if t%(100*b) == 0 and d == 13: 
            arr14.goto(random.randint(-580, 580), 350)

        if t%(100*b) == 0 and d == 14: 
            arr15.goto(random.randint(-580, 580), 350)
            d = -1
        if t%(100*b) == 0:
            d += 1

    if t%(3000*b) == 0 and luck == False and lucky.ycor() > 400:
        lucky.goto(random.randint(-580, 580), 350)

    if luck == True:
        f+=1

    if t%6000 == 0 and b>=1:
        b-=0.5
        l+=1
        arr1.dy -= 0.15
        pen2.clear()
        pen2.write("Level:{}".format(l) , align = "center", font = ("Courier", 40, "normal"))

    if (tr.ycor() - 25 < arr1.ycor()+70 and tr.ycor() + 25 > arr1.ycor()) and (tr.xcor() - 25 < arr1.xcor()+25 and tr.xcor() + 25 > arr1.xcor()-25):
        Game_Over = True
    if (tr.ycor() - 25 < arr2.ycor()+70 and tr.ycor() + 25 > arr2.ycor()) and (tr.xcor() - 25 < arr2.xcor()+25 and tr.xcor() + 25 > arr2.xcor()-25):
        Game_Over = True
    if (tr.ycor() - 25 < arr3.ycor()+70 and tr.ycor() + 25 > arr3.ycor()) and (tr.xcor() - 25 < arr3.xcor()+25 and tr.xcor() + 25 > arr3.xcor()-25):
        Game_Over = True      
    if (tr.ycor() - 25 < arr4.ycor()+70 and tr.ycor() + 25 > arr4.ycor()) and (tr.xcor() - 25 < arr4.xcor()+25 and tr.xcor() + 25 > arr4.xcor()-25):
        Game_Over = True
    if (tr.ycor() - 25 < arr5.ycor()+70 and tr.ycor() + 25 > arr5.ycor()) and (tr.xcor() - 25 < arr5.xcor()+25 and tr.xcor() + 25 > arr5.xcor()-25):
        Game_Over = True
    if (tr.ycor() - 25 < arr6.ycor()+70 and tr.ycor() + 25 > arr6.ycor()) and (tr.xcor() - 25 < arr6.xcor()+25 and tr.xcor() + 25 > arr6.xcor()-25):
        Game_Over = True
    if (tr.ycor() - 25 < arr7.ycor()+70 and tr.ycor() + 25 > arr7.ycor()) and (tr.xcor() - 25 < arr7.xcor()+25 and tr.xcor() + 25 > arr7.xcor()-25):
        Game_Over = True
    if (tr.ycor() - 25 < arr8.ycor()+70 and tr.ycor() + 25 > arr8.ycor()) and (tr.xcor() - 25 < arr8.xcor()+25 and tr.xcor() + 25 > arr8.xcor()-25):
        Game_Over = True
    if (tr.ycor() - 25 < arr9.ycor()+70 and tr.ycor() + 25 > arr9.ycor()) and (tr.xcor() - 25 < arr9.xcor()+25 and tr.xcor() + 25 > arr9.xcor()-25):
        Game_Over = True
    if (tr.ycor() - 25 < arr10.ycor()+70 and tr.ycor() + 25 > arr10.ycor()) and (tr.xcor() - 25 < arr10.xcor()+25 and tr.xcor() + 25 > arr10.xcor()-25):
        Game_Over = True
    if (tr.ycor() - 25 < arr11.ycor()+70 and tr.ycor() + 25 > arr11.ycor()) and (tr.xcor() - 25 < arr11.xcor()+25 and tr.xcor() + 25 > arr11.xcor()-25):
        Game_Over = True
    if (tr.ycor() - 25 < arr12.ycor()+70 and tr.ycor() + 25 > arr12.ycor()) and (tr.xcor() - 25 < arr12.xcor()+25 and tr.xcor() + 25 > arr12.xcor()-25):
        Game_Over = True
    if (tr.ycor() - 25 < arr13.ycor()+70 and tr.ycor() + 25 > arr13.ycor()) and (tr.xcor() - 25 < arr13.xcor()+25 and tr.xcor() + 25 > arr13.xcor()-25):
        Game_Over = True
    if (tr.ycor() - 25 < arr14.ycor()+70 and tr.ycor() + 25 > arr14.ycor()) and (tr.xcor() - 25 < arr14.xcor()+25 and tr.xcor() + 25 > arr14.xcor()-25):
        Game_Over = True
    if (tr.ycor() - 25 < arr15.ycor()+70 and tr.ycor() + 25 > arr15.ycor()) and (tr.xcor() - 25 < arr15.xcor()+25 and tr.xcor() + 25 > arr15.xcor()-25):
        Game_Over = True
    if (tr.ycor() - 25 < lucky.ycor()+70 and tr.ycor() + 25 > lucky.ycor()) and (tr.xcor() - 25 < lucky.xcor()+25 and tr.xcor() + 25 > lucky.xcor()-25):
        wn.onkeypress(move_up_s, "Up")
        wn.onkeypress(move_down_s, "Down")
        wn.onkeypress(move_left_s, "Left")
        wn.onkeypress(move_right_s, "Right")
        lucky.goto(0, 1000000)
        luck = True
        f = 0
        s += 20
        pen5.clear()
        pen5.write("Score:{}".format(s) , align = "center", font = ("Courier", 20, "normal"))
        pen3.write("Abilities: Speed", align = "center", font = ("Courier", 15, "normal"))
    if (f == 2600):
        wn.onkeypress(move_up, "Up")
        wn.onkeypress(move_down, "Down")
        wn.onkeypress(move_left, "Left")
        wn.onkeypress(move_right, "Right")
        pen3.clear()
        luck = False
        f = 0
    if arr1.ycor() < -380:
        arr1.goto(0, 1000000)
    if arr2.ycor() < -380:
        arr2.goto(0, 1000000)
    if arr3.ycor() < -380:
        arr3.goto(0, 1000000)
    if arr4.ycor() < -380:
        arr4.goto(0, 1000000)
    if arr5.ycor() < -380:
        arr5.goto(0, 1000000)
    if arr6.ycor() < -380:
        arr6.goto(0, 1000000)
    if arr7.ycor() < -380:
        arr7.goto(0, 1000000)
    if arr8.ycor() < -380:
        arr8.goto(0, 1000000)
    if arr9.ycor() < -380:
        arr9.goto(0, 1000000)
    if arr10.ycor() < -380:
        arr10.goto(0, 1000000)
    if arr11.ycor() < -380:
        arr11.goto(0, 1000000)
    if arr12.ycor() < -380:
        arr12.goto(0, 1000000)
    if arr13.ycor() < -380:
        arr13.goto(0, 1000000)
    if arr14.ycor() < -380:
        arr14.goto(0, 1000000)
    if arr15.ycor() < -380:
        arr15.goto(0, 1000000)
    if t%30000 == 0 and god != True:
        god = True
        pen2.clear()
        pen2.write("Level:God" , align = "center", font = ("Courier", 40, "normal"))
        arr1.left(30)
        arr2.left(30)
        arr3.left(30)
        arr4.left(30)
        arr5.left(30)
        arr6.left(30)
        arr7.left(30)
        arr8.left(30)
        arr9.left(30)
        arr10.left(30)
        arr11.left(30)
        arr12.left(30)
        arr13.left(30)
        arr14.left(30)
        arr15.left(30)
        arr1.goto(0, 1000000)
        arr2.goto(0, 1000000)
        arr3.goto(0, 1000000)
        arr4.goto(0, 1000000)
        arr5.goto(0, 1000000)
        arr6.goto(0, 1000000)
        arr7.goto(0, 1000000)
        arr8.goto(0, 1000000)
        arr9.goto(0, 1000000)
        arr10.goto(0, 1000000)
        arr11.goto(0, 1000000)
        arr12.goto(0, 1000000)
        arr13.goto(0, 1000000)
        arr14.goto(0, 1000000)
        arr15.goto(0, 1000000)
        arr1.dy = -1.7
        arr1.dx = 0.7

pen5.clear()
pen2.clear()
pen.write("Game Over", align = "center", font = ("Courier", 100, "normal"))
pen4.write("Your score:{}".format(s), align = "center", font = ("Courier", 60, "normal"))
time.sleep(2)
