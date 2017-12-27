import turtle
import os

s = turtle.Screen()
s.register_shape('enemy.gif')
s.tracer(0, 0)
BULLET_SPEED = 10

t  = turtle.Turtle()
t.up()
t.sety(-280)
t.shapesize(4)
t.left(90)


e = turtle.Turtle()
e.up()
e.shapesize(4)
e.shape('enemy.gif')
e.color('red')
e.sety(250)

bullet = turtle.Turtle()
bullet.up()
bullet.left(90)
bullet.color('blue')
bullet.hideturtle()
# bullet.fired = False

def move_l():
    x = t.xcor()
    new_x = x - 20
    t.setx(new_x)


def move_r():
    x = t.xcor()
    new_x = x + 20
    t.setx(new_x)

def fire():
    # bullet.fired = True
    os.system('aplay LASER.WAV&')
    if bullet.isvisible():
        return
    print(bullet.pos())

    bullet.setpos(t.pos())
    bullet.showturtle()

s.listen()
s.onkeypress(move_r, 'Right')
s.onkeypress(move_l, 'Left')
s.onkeypress(fire, 'space')

enemy_move = 2
screen_border = 450


while True:
    # Move right
    x = e.xcor()
    new_x = x + enemy_move
    e.setx(new_x)

    if new_x > screen_border or new_x < -screen_border:
        enemy_move = enemy_move * -1
        y = e.ycor()
        new_y = y - 50
        e.sety(new_y)

    if bullet.isvisible():
        by = bullet.ycor()
        new_bullet_y = by + BULLET_SPEED
        dist = bullet.distance(e.pos())
        if dist < 50:
            e.hideturtle()
            bullet.hideturtle()
        if new_bullet_y > 300:
            bullet.hideturtle()

        bullet.sety(new_bullet_y)
        # print(new_bullet_y)
    s.update()

s.mainloop()