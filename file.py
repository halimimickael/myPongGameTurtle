import time
import turtle
import turtle as t

global speed
global mode_chosen
global not_started
global pending
global player_right
global player_left


# Score variables
player_a_score = 0
player_b_score = 0

COLOR_PADDLE_RIGHT = "#00FF00"
COLOR_PADDLE_LEFT = "#FA58F4"

ball_colors = ["#FFFF00", "#FF0000", "#00FF00", "#0000FF"]  # Ajout de couleurs ici

# Variable pour suivre l'indice de la couleur actuelle
current_ball_color_index = 0


# flags
game_over = False
pending = False
right_win = True

win = t.Screen()  # creating a window
win.title("Ping-Pong Game")  # Giving name to the game.
win.bgcolor('black')  # providing color to the HomeScreen
win.setup(width=800, height=600)  # Size of the game panel
win.tracer(0)  # which speed up's the game.
win.setup(1.0, 1.0)
turtle.bgpic("background.gif")


# Choosing a mode
pen1 = t.Turtle()
pen1.speed(0)
pen1.color('#FF8000')
pen1.penup()
pen1.hideturtle()
pen1.goto(0, 0)
pen1.write("choose your mode:\n\n\n solo \n\n versus", align="center", font=('Monaco', 30, "normal"))


# choose a mode by click
def set_click_pos(x, y):
    global mode_chosen
    global speed
    global not_started
    if not mode_chosen:
        if -185.0 < x < -80.0 and 90.0 < y < 130.0:
            # solo
            mode_chosen = 1
        elif -185.0 < x < -35.0 and 8.0 < y < 40.0:
            # double
            mode_chosen = 2
    else:
        if -260.0 < x < -151.0 and 164.0 < y < 205.0:
            # easy
            speed = 0.5
            not_started = False

        elif -260.0 < x < -96.0 and 132.0 > y > 83.0:
            # medium
            speed = 0.75
            not_started = False

        elif -260.0 < x < -147.0 and 5.0 < y < 48.0:
            # hard
            speed = 1
            not_started = False


turtle.onscreenclick(set_click_pos)
mode_chosen = 0

# wait for the choice of the mode, the mode_chosen flag stays false until the user doesn't click on a mode
while not mode_chosen:
    win.update()

pen1.clear()
pen1.write("Choose your difficulty :\n\n easy \n\n medium \n\n hard", align="center", font=('Monaco', 30, "normal"))
not_started = True

# wait for the choice of the speed, the not_started flag stays true until the user doesn't click on a difficulty
while not_started:
    win.update()

pen1.clear()

# border of game
border_pen = t.Turtle()
border_pen.color('#FF8000')
border_pen.penup()
border_pen.goto(-400, 300)
border_pen.pendown()
border_pen.pensize(3)

for _ in range(2):
    border_pen.forward(800)
    border_pen.right(90)
    border_pen.forward(600)
    border_pen.right(90)


border_pen.hideturtle() #supp la fleche

# Creating left paddle for the game
paddle_left = t.Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.color(COLOR_PADDLE_LEFT)
paddle_left.shapesize(stretch_wid=10, stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350, 0)

# Creating a right paddle for the game
paddle_right = t.Turtle()
paddle_right.speed(0)
paddle_right.shape('square')
paddle_right.shapesize(stretch_wid=10, stretch_len=1)
paddle_right.color(COLOR_PADDLE_RIGHT)
paddle_right.penup()
paddle_right.goto(350, 0)

# Creating a pong ball for the game
ball = t.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('#FFFF00')
ball.penup()
ball.goto(0, 0)


# scores
pen = t.Turtle()
pen.speed(0)
pen.color('#FF8000')
pen.penup()
pen.hideturtle()
pen.goto(0, 310)
pen.color(COLOR_PADDLE_LEFT)
pen.write("Player A: 0  ", align="right", font=('Monaco', 24, "bold"))
pen.color(COLOR_PADDLE_RIGHT)
pen.write("Player B: 0  ", align="left", font=('Monaco', 24, "bold"))


# Moving the left Paddle using the keyboard
def paddle_left_up():
    global paused
    if not paused and mode_chosen == 2:
        y = paddle_left.ycor()
        y = y + 30
        if y < 200:
            paddle_left.sety(y)
        else:
            paddle_left.sety(197)


# Moving the left paddle down
def paddle_left_down():
    global paused
    if not paused and mode_chosen == 2:
        y = paddle_left.ycor()
        y = y - 30
        if y > -200:
            paddle_left.sety(y)
        else:
            paddle_left.sety(-197)


# Moving the right paddle up
def paddle_right_up():
    global paused
    if not paused:
        y = paddle_right.ycor()
        y = y + 30
        if y < 200:
            paddle_right.sety(y)
        else:
            paddle_right.sety(197)


# Moving right paddle down
def paddle_right_down():
    global paused
    if not paused:
        y = paddle_right.ycor()
        y = y - 30
        if y > -200:
            paddle_right.sety(y)
        else:
            paddle_right.sety(-197)


def count_down():
    for i in range(3, 0, -1):
        show_counter(i)
        time.sleep(1)
    show_counter("GO!")
    time.sleep(1)
    counter.clear()


# Keyboard binding
# the 3 "unpause" functions are to turn to false the pending flag after checking if the right key is pressed
def unpause():
    global pending
    pending = False
    win.update()


def unpause_right():
    global right_win
    if not right_win:
        unpause()


def unpause_left():
    global right_win
    if right_win and mode_chosen == 2:
        unpause()


def reset_game():
    global player_a_score, player_b_score, player_left, player_right, paused, game_over
    if not game_over and paused:
        paddle_right.goto(350, 0)
        paddle_left.goto(-350, 0)
        ball.goto(0,0)
        player_a_score = 0
        player_b_score = 0
        ball.goto(0, 0)
        paused = False
        pen.clear()
        pen.color(COLOR_PADDLE_RIGHT)
        pen.write("Player A: 0  ",
                  align="left", font=('Monaco', 24, "bold"))
        pen.color(COLOR_PADDLE_LEFT)
        pen.write("Player B: 0  ",
                  align="right", font=('Monaco', 24, "bold"))
        pause_txt.clear()
        count_down()
        game_over = False  # Réinitialisez game_over à False


def pause():
    global paused
    if not game_over:
        paused = not paused
        if paused:
            pause_txt.write("     Pause\n\n'r' to restart", align="center", font=("Monaco", 50, "normal"))
        else:
            pause_txt.clear()


win.listen()
win.onkeypress(paddle_left_up, "a")
win.onkeypress(paddle_left_down, "q")
win.onkeypress(paddle_right_up, "Up")
win.onkeypress(paddle_right_down, "Down")
win.onkeypress(unpause_right, "Left")
win.onkeypress(unpause_left, "d")
win.onkeypress(reset_game, "r")
win.onkeypress(pause, "space")

# Main Game Loop

counter = t.Turtle()
counter.speed(1)
counter.color("pink")
counter.penup()
counter.hideturtle()
counter.goto(0, 100)


def show_counter(i):
    counter.clear()
    counter.write(i, align="center", font=("Monaco", 50, "normal"))


win.update()
# Compte à rebours : 3, 2, 1
count_down()

global paused
paused = False
pause_txt = t.Turtle()
pause_txt.speed(1)
pause_txt.color("pink")
pause_txt.penup()
pause_txt.hideturtle()
pause_txt.goto(0, 100)

# versus
ball_dx = speed
ball_dy = speed
while True:

    if paused:
        win.update()
        continue
    else:
        pause_txt.clear()
    if pending:
        win.update()
        if right_win:
            ball.goto(paddle_left.xcor() + 22, paddle_left.ycor())
            win.update()
            if mode_chosen == 1:
                for i in range(150):
                    time.sleep(0.01)
                    win.update()
                pending = False
        else:
            ball.goto(paddle_right.xcor() - 22, paddle_right.ycor())
            win.update()
        continue

    win.update()  # This methods is mandatory to run any game

    # Boucle pour changer la couleur de la balle à chaque itération
    current_ball_color = ball_colors[current_ball_color_index]
    ball.color(current_ball_color)

    # Incrémentation de l'indice de couleur
    current_ball_color_index = (current_ball_color_index + 1) % len(ball_colors)


    # Moving the ball
    ball.setx(ball.xcor() + ball_dx)
    ball.sety(ball.ycor() + ball_dy)

    # setting up the border

    if ball.ycor() > 290:  # Right top paddle Border
        ball.sety(290)
        ball_dy = ball_dy * -1

    if ball.ycor() < -290:  # Left top paddle Border
        ball.sety(-290)
        ball_dy = ball_dy * -1

    if ball.xcor() > 390:  # right width paddle Border
        ball.goto(paddle_right.position())
        pending = True
        right_win = False
        ball_dx = ball_dx * -1
        player_a_score = player_a_score + 1
        pen.clear()
        pen.color(COLOR_PADDLE_LEFT)
        pen.write("Player A: {}  ".format(player_a_score),
                  align="right", font=('Monaco', 24, "bold"))
        pen.color(COLOR_PADDLE_RIGHT)
        pen.write("Player B: {}  ".format(player_b_score),
                  align="left", font=('Monaco', 24, "bold"))

        if player_a_score == 5:
            pen.clear()
            pen.goto(0, 0)  # Ajustez la coordonnée verticale pour placer le texte au-dessus du terrain
            pen.color(COLOR_PADDLE_LEFT)
            pen.write("Player A wins!", align="center", font=('Monaco', 32, "bold"))
            game_over = True
            win.update()
            t.done()

    if (ball.xcor()) < -390:  # Left width paddle Border
        ball.goto(paddle_left.position())
        pending = True
        right_win = True
        ball_dx = ball_dx * -1
        player_b_score = player_b_score + 1
        pen.clear()
        pen.color(COLOR_PADDLE_LEFT)
        pen.write("Player A: {}  ".format(player_a_score),
                  align="right", font=('Monaco', 24, "bold"))
        pen.color(COLOR_PADDLE_RIGHT)
        pen.write("Player B: {}  ".format(player_b_score),
                  align="left", font=('Monaco', 24, "bold"))

    if player_b_score == 5:
        pen.clear()
        pen.goto(0, 0)  # Ajustez la coordonnée verticale pour placer le texte au-dessus du terrain
        pen.color(COLOR_PADDLE_RIGHT)
        pen.write("Player B wins!", align="center", font=('Monaco', 32, "bold"))
        game_over = True
        win.update()
        t.done()

    # Handling the collisions with paddles.

    if (ball.xcor() > 340) and (ball.xcor() < 350) and (
            paddle_right.ycor() + 100 > ball.ycor() > paddle_right.ycor() - 100):
        ball.setx(340)
        ball_dx = ball_dx * -1

    if (ball.xcor() < -340) and (ball.xcor() > -350) and (
            paddle_left.ycor() + 100 > ball.ycor() > paddle_left.ycor() - 100):
        ball.setx(-340)
        ball_dx = ball_dx * -1

    # single player mode so that the left paddle moves depending on the difficulty that the user chooses
    if mode_chosen == 1 and ball.ycor() != paddle_left.ycor() and speed == 0.5:
        direction = ball.ycor() - paddle_left.ycor()
        direction /= abs(direction)
        paddle_left.sety(paddle_left.ycor() + (0.3 * direction))

    if mode_chosen == 1 and ball.ycor() != paddle_left.ycor() and speed == 0.75:
        direction = ball.ycor() - paddle_left.ycor()
        direction /= abs(direction)
        paddle_left.sety(paddle_left.ycor() + (0.5 * direction))

    if mode_chosen == 1 and ball.ycor() != paddle_left.ycor() and speed == 1:
        direction = ball.ycor() - paddle_left.ycor()
        direction /= abs(direction)
        paddle_left.sety(paddle_left.ycor() + (0.7 * direction))

t.done()
