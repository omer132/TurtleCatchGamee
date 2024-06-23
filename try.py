import turtle 
import random

# data
turtl=[]
gridSize=10
x_coor=[20  ,10 ,0 ,-10 ,-20]
y_coor=[10, 0, -10, -20]
FONT = ('Arial', 30, 'normal')
score=0
game=False

# screen setting
screen=turtle.Screen()
screen.bgcolor("sky blue")

# turtle setting
def turt(x,y):
    turt=turtle.Turtle()
    def handle_click(x,y):
        global score
        score += +1
        score_turtle.clear()
        score_turtle.write("Score: {}".format(score), move=False, align="center", font=FONT)
        
    turt.onclick(handle_click)
    turt.color("dark green")
    turt.shape("turtle")
    turt.penup()
    turt.shapesize(2,2)
    turt.goto(x*gridSize,y*gridSize)
    turtl.append(turt)

# turtle booster
def booster():
    for y in x_coor:
        for x in y_coor:
            turt(y,x)

# secret
def hideturtle():
    for t in turtl:
        t.hideturtle()

def showturtle():
    if not game:
        hideturtle()
        random.choice(turtl).showturtle()
        screen.ontimer(showturtle,500)

score_turtle=turtle.Turtle()

def setup_score_turtle():
    score_turtle.hideturtle()
    score_turtle.color("blue")
    score_turtle.penup()

    top_height = screen.window_height() / 2  # positive height/2 is the top of the screen
    y = top_height - top_height / 10  # decreasing a bit so text will be visible
    score_turtle.setposition(0, y)
    score_turtle.write(arg='Score: 0', move=False, align='center', font=FONT)

times=turtle.Turtle()

def tim(time):
    global game
    top_height = screen.window_height() / 2
    y = top_height - top_height / 10
    times.hideturtle()
    times.penup()
    times.setposition(0, y - 30)
    times.clear()

    if time>0:
        times.clear()
        times.write("Time: {}".format(time),move=False,align="center",font=FONT)
        screen.ontimer(lambda: tim(time-1),1000)

    else:
        game=True
        times.clear()
        hideturtle()
        times.write("Game Over!",align="center",font=FONT)

def game_start():
    global game
    game=False
    turtle.tracer(0)
    turt(5,5)
    booster()
    hideturtle()
    showturtle()
    setup_score_turtle()
    turtle.tracer(1)
    screen.ontimer( lambda: tim(10),10)

game_start()
turtle.mainloop()