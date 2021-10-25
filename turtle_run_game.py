import turtle as t
import random
import time

score = 0           # 점수를 저장하는 변수
playing = False     # 현재 게임 플레이 중인지 확인하는 변수
boost = False
tspeed = 1

t.title("Turtle Run")   # 내가 조종하는 터틀
t.setup(1800, 1000)
t.bgcolor("orange")
t.shape("turtle")   # 거북이 모양의 커서를 사용합니다.
t.speed(0)          # 거북이 속도를 가장 빠르게로 지정합니다
t.up()
t.color("white")

te = t.Turtle()     # 악당 거북이(빨간색) te
te.shape("turtle")
te.color("red")
te.speed(0)
te.up()
te.goto(0, 200)

ts = t.Turtle()     # 먹이(초록색 동그라미)  ts
ts.shape("circle")
ts.color("green")
ts.speed(0)
ts.up()
ts.goto(0, -200)

ta = t.Turtle()               # boost
ta.shape("triangle")
ta.color("blue")
ta.speed(0)
ta.up()
ta.goto(0, 50)

tb = t.Turtle()              # shield
tb.shape("square")
tb.color("yellow")
tb.speed(0)
tb.up()
tb.goto(0, 80)

def turn_right():                # 오른쪽으로 방향을 바꿉니다.
    t.setheading(0)

def turn_up():                   # 위로 방향을 바꿉니다.
    t.setheading(90)

def turn_left():                 # 왼쪽으로 방향을 바꿉니다.
    t.setheading(180)

def turn_down():                 # 아래로 방향을 바꿉니다.
    t.setheading(270)

def message(m1, m2, m3):                    # 메시지를 화면에 표시하는 함수
    t.clear()
    t.goto(0, 100)
    t.write(m1, False, "center", ("", 30))
    t.goto(0, -100)
    t.write(m2, False, "center", ("", 25))
    t.goto(0, -135)
    t.write(m3, False, "center", ("", 15))
    t.home()

def push_A():
    t.write("You can use boost", font=("", 50))
    t.forward(100)

def die():
    global playing
    text = "Score : " + str(score)
    message("Game Over", text, "you bad")
    playing = False
    score = 0

def start():                    # 게임을 시작하는 함수
    global playing
    if playing == False:
        playing = True
        t.clear()               # 메시지를 지웁니다
        play()

def speeditem():
    global tspeed, canitem
    if tspeed > 10:
        canitem = 55
    if tspeed > 20:
        canitem = 60
    if tspeed > 25:
        canitem = 65
    if tspeed > 30:
        canitem = 70
    if tspeed > 40:
        canitem = 80
    if tspeed > 60:
        canitem = 110
    if tspeed > 70:
        canitem = 130
    if tspeed > 80:
        canitem = 150

def play():                     # 게임을 실제로 플레이하는 함수
    canitem = 30
    global boost
    global score
    global playing
    global tspeed
    for i in range(tspeed):
        t.forward(4)
        speeditem()
        
    if random.randint(1, 50) == 5:       # 1~50 사이에서 뽑은 수가 5이면(2% 확률)
        ang = te.towards(t.pos())
        te.setheading(ang)              # 악당 거북이가 주인공 거북이를 바라보게 합니다.
    speed = score - 4

    for x in range(speed):
        if random.randint(1, 50) == 3:       # 1~50 사이에서 뽑은 수가 3이면(2% 확률)
            ang = te.towards(t.pos())
            te.setheading(ang)              # 악당 거북이가 주인공 거북이를 바라보게 합니다.
        te.forward(3)

    if t.distance(ts) < canitem:             # 주인공과 먹이의 거리가 12보다 작으면(가깝게 있으면)
        score = score + 10        # 점수를 올립니다.
        t.write("Score : " + str(score), font=("", 20))                  # 점수를 화면에 표시합니다.
        star_x = random.randint(-400, 400)
        star_y = random.randint(-230, 230)
        ts.goto(star_x, star_y)         # 먹이를 다른 곳으로 옮깁니다.

    if t.distance(ta) < canitem:             # 주인공과 레벨의 거리가 12보다 작으면(가깝게 있으면)
            tspeed = tspeed + 3
            t.write("turtle speed : " + str(tspeed))                  # 스피드를 화면에 표시합니다.
            star2_x = random.randint(-400, 400)
            star2_y = random.randint(-230, 230)
            ta.goto(star2_x, star2_y)         # 레벨을 다른 곳으

    if t.distance(tb) < canitem:             # 주인공과 레벨의 거리가 12보다 작으면(가깝게 있으면)
            if boost == True:
                t.write('you have boost')
            if boost == False:
                boost = True
                star3_x = random.randint(-700, 700)
                star3_y = random.randint(-400, 400)
                tb.goto(star3_x, star3_y)

    if t.distance(te) < canitem:             # 주인공과 악당의 거리가 12보다 작으면 게임을 종료합니다.
        if boost == True:
            score += 5
            t.write("Score : " + str(score), font=("", 20))  
            star_x = random.randint(-1500,1500)
            star_y = random.randint(-1500,1500)
            te.goto(star_x, star_y)         # 먹이를 다른 곳으로 옮깁니다.
            boost = False
        else:
            text = "Score : " + str(score)
            message("Game Over", text, "you bad")
            playing = False
            score = 0

    if playing:
        t.ontimer(play, 200)            # 게임 플레이 중이면 0.1초 후 play 함수를 실행합니다.

          


          

t.onkeypress(turn_right, "Right")  
t.onkeypress(turn_up, "Up")
t.onkeypress(turn_left, "Left")
t.onkeypress(turn_down, "Down")
t.onkeypress(start, "space")
t.listen()
message("Turtle Run", "[Space]", "SM University")




