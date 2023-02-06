import turtle

window = turtle.Screen()
window.title("Pong'by Audrey G")

window.bgcolor("deep pink")
window.setup(width=1000, height=600)
window.tracer(0)

#score
score_a = 0
score_b = 0


#Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("cyan")
paddle_a.shapesize(stretch_wid=7, stretch_len=2)
paddle_a.penup()
paddle_a.goto(-400, 0)

#Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("cyan")
paddle_b.shapesize(stretch_wid=7, stretch_len=2)
paddle_b.penup()
paddle_b.goto(400, 0)

#ball 
ball = turtle.Turtle()
ball.speed(40)
ball.shape("turtle")
ball.color("black")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = -5
#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("White")
pen.penup()
pen.hideturtle() 
pen.goto(0, 260)
pen.write(" Player A: 0 Player B: 0", align="center", font=("Comic Sans MS", 24, "normal"))



#function
def paddle_a_up():
  y = paddle_a.ycor()
  y += 20
  paddle_a.sety(y)
def paddle_a_down():
  y = paddle_a.ycor()
  y -= 20
  paddle_a.sety(y)
def paddle_b_up():
  y = paddle_b.ycor()
  y += 20
  paddle_b.sety(y) 
def paddle_b_down():
  y = paddle_b.ycor()
  y -= 20
  paddle_b.sety(y)
  
  
#Keyboard Binding
  window.listen()
  window.onkeypress(paddle_a_up, "e")
  window.onkeypress(paddle_a_down, "x")
  window.onkeypress(paddle_b_up, "Up")
  window.onkeypress(paddle_b_down, "Down")
  
  
#Main game loop
while True:
  window.update()
#MHit the ball
  ball.setx(ball.xcor() +ball.dx)
  ball.sety(ball.ycor() +ball.dy)

  
#border checking
  if ball.ycor() > 280:
    ball.sety(280)
    ball.dy *= -1
  if ball.ycor() < -280:
    ball.sety(-280)
    ball.dy *= -1
    
  if ball.xcor() > 500:
    ball.goto(0, 0)
    score_a *= 1
    ball.dx += -1
    pen.clear()
    my_text = " Welcome to Audrey's Arcade"
    print(format(my_text, '^50'))
    pen.write(" Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Comic Sans MS", 24, "normal"))
  if ball.xcor() < -500:
    ball.goto(0, 0)
    ball.dx *= -1
    score_b += 1
    pen.clear()
    pen.write(" Player A: {} Player B: {}".format(score_a, score_b), align="center", font=("Comic Sans MS", 24, "normal"))
  
#paddle and ball collision
  if ball.xcor() > 360 and ball.xcor() < 370 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
      ball.dx *= -1 
      ball.setx(360)
  if ball.xcor() > -360 and ball.xcor() > -370 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
      ball.dx *= -1 
      ball.setx(-360)
      
    
    
        
        
    
