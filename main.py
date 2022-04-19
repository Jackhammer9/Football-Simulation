#imports
import turtle
import random
import time
from FunctionInvoker import FunctionInvoker

#A class to check for tackling after n seconds without halting the execution of programme
class TackleClock:
    def __init__(self ,tackler,times):
        self.StartTime = time.time()
        self.tackler = tackler
        self.time = times
    def TackleStatus(self):
        self.Current = time.time() - self.StartTime
        if self.Current >= self.time:
            return True
    def GetTackler(self):
        return self.tackler

#window configuration
win = turtle.Screen()
win.bgcolor('dark green')
win.title('FIFA: Primitive Age')
win.tracer(0)
w,h=1366,704

#map design
boundary = turtle.Turtle()
boundary.color('white')
boundary.speed(0)
boundary.pensize(5)
boundary.sety(-95/100*h/2)
boundary.sety(95/100*h/2)
boundary.setx(-95/100*w/2)
boundary.setx(95/100*w/2)
boundary.sety(-95/100*h/2)
boundary.setx(-95/100*w/2)
boundary.sety(95/100*h/2)
boundary.pu()
boundary.goto(0,-30)
boundary.pd()
boundary.circle(30)
boundary.pu()
boundary.goto(-95/100*w/2 , 3/10*h/2)
boundary.pd()
boundary.setx(-8/10*w/2)
boundary.color('green')
boundary.sety(-3/10*h/2)
boundary.color('white')
boundary.setx(-95/100*w/2)
boundary.pu()
boundary.goto(95/100*w/2 , 3/10*h/2)
boundary.pd()
boundary.setx(8/10*w/2)
boundary.color('green')
boundary.sety(-3/10*h/2)
boundary.color('white')
boundary.setx(95/100*w/2)
boundary.hideturtle()
boundary.pu()

#goal pen
goalpen = turtle.Turtle()
goalpen.ht()
goalpen.penup()
goalpen.color('white')

def GoalPrinter():
    goalpen.write('GOAL!', move=False, align="center", font=("Deja Vu Sans Mono", 135, "normal"))

def GoalCleaner():
    goalpen.clear()

#goal counter 
rcounter = turtle.Turtle()
rcounter.ht()
rcounter.penup()
rcounter.color('#eb4034')
rcounter.goto(50/100*w/2 , -200)
rcounter.write(f'0', move=False, align="center", font=("Deja Vu Sans Mono", 240, "normal"))

bcounter = turtle.Turtle()
bcounter.ht()
bcounter.penup()
bcounter.color('#3e65f0')
bcounter.goto(-50/100*w/2 , -200)
bcounter.write(f'0', move=False, align="center", font=("Deja Vu Sans Mono", 240, "normal"))

#initlising blue team
blueTeam = [turtle.Turtle() for i in range(11)]
blueGoalie = blueTeam[10]
for player in blueTeam:
    player.penup()
    player.speed(0)
    player.color('dark blue')
    player.shape('circle')
    player.turtlesize(1)
    player.goto(random.randint(-500 , -25) , random.randint(-320,320))
blueGoalie.goto(-85/100*w/2 , 0)

#distributing players in defenders , mid and forward
bdefenders , bmid , bforward = [] , [] , []
for i in range(0,4):
    blueTeam[i].goto(random.randint(-200 , -25) , random.randint(-320,320))
    bforward.append(blueTeam[i])

for i in range(4,7):
    blueTeam[i].goto(random.randint(-300 , -200) , random.randint(-320,320))
    bmid.append(blueTeam[i])

for i in range(7,10):
    blueTeam[i].goto(random.randint(-500 , -300) , random.randint(-320,320))
    bdefenders.append(blueTeam[i])

# initalising red team
redTeam = [turtle.Turtle() for i in range(11)]
redGoalie = redTeam[10]
for player in redTeam:
    player.penup()
    player.speed(0)
    player.color('dark red')
    player.shape('circle')
    player.turtlesize(1)
    player.goto(random.randint(25,500) , random.randint(-320,320))

# dividing red team into defenders , mid , forward
rdefenders , rmid , rforward = [] , [] , []
for i in range(0,4):
    redTeam[i].goto(random.randint(25 , 200) , random.randint(-320,320))
    rforward.append(redTeam[i])

for i in range(4,7):
    redTeam[i].goto(random.randint(200 , 300) , random.randint(-320,320))
    rmid.append(redTeam[i])

for i in range(7,10):
    redTeam[i].goto(random.randint(300 , 500) , random.randint(-320,320))
    rdefenders.append(redTeam[i])

# ball configurations
ball = turtle.Turtle()
ball.color('orange')
ball.pu()
ball.shape("circle")
ball.turtlesize(0.7)
taken = True
owner = None
team = 0
holder = player

# inital main player
player = blueTeam[0]
player.color('light blue')
player.goto(0,0)
started = False

# player movement functions
def up():
    if started:
        player.seth(90)
        player.fd(2)

def down():
    if started:
        player.seth(270)
        player.fd(2)

def left():
    if started:
        player.seth(180)
        player.fd(2)

def right():
    if started:
        player.seth(0)
        player.fd(2)

def nw():
    if started:
        player.seth(120)
        player.fd(2)

def ne():
    if started:
        player.seth(60)
        player.fd(2)

def sw():
    if started:
        player.seth(225)
        player.fd(2)

def se():
    if started:
        player.seth(315)
        player.fd(2)

# pass, shooting ball function
shot = False
def Shot(x,y,Special=False,Redshot = False):
    global started
    global team
    if not started:
        started = True
    global taken
    if taken and (team == 0 or Special or Redshot):
        global shot
        global player
        shot = True
        taken = False
        ball.speed(2)
        ball.seth(ball.towards(x,y))
        win.tracer(1)
        owner = player
        run = True
        if Special:
            time.sleep(3)
        ball.fd(26)
        while ball.distance(x , y) > 2 and run:
            ball.fd(4)
            if ball.xcor() > 60/100*w/2:
                while redGoalie.xcor() >= 78/100*w/2:
                    redGoalie.seth(redGoalie.towards(ball.pos()))
                    redGoalie.fd(2)
                    break
                while redGoalie.ycor() != ball.ycor():
                    if ball.ycor() > redGoalie.ycor() and redGoalie.ycor() < 93:
                        redGoalie.seth(90)
                        redGoalie.fd(2)
                        break
                    elif ball.ycor() < redGoalie.ycor() and redGoalie.ycor() > -93:
                        redGoalie.seth(270)
                        redGoalie.fd(2)
                        break
                    else:
                        break
            for players in blueTeam:
                if ball.distance(players.xcor() , players.ycor()) < 25 and not taken:
                    taken = True
                    global holder
                    if team == 0:
                        player.color('dark blue')
                    else:
                        holder.color('dark red')
                        player.color('dark blue')
                    player = players
                    holder = player
                    player.color('light blue')
                    team = 0
            for players in redTeam:
                if ball.distance(players.xcor() , players.ycor()) < 25 and not taken:
                    taken = True
                    if team == 0:
                        player.color('light blue')
                    else:
                        holder.color('dark red')
                    holder = players
                    team = 1
            if owner == player:
                pass
            else:
                run = False
        shot = False
        win.tracer(0)

# tackle enemy player when they have the ball
def Tackle():
    global team
    if team == 1 and ball.distance(player.xcor() , player.ycor()) < 25:
        global taken
        global holder
        taken = False
        holder = player
        team = 0

# switch player amongst team
SwitchPosition = 0
def Switch():
    global player
    global blueTeam
    global SwitchPosition
    if SwitchPosition >= 11:
        SwitchPosition = 0
    global team
    if team == 1 or taken == False:
        player.color('dark blue')
        player = blueTeam[SwitchPosition]
        player.color('light blue')
        SwitchPosition += 1

#key bindings
win.listen()
win.onkeypress(up , 'w')
win.onkeypress(down , 's')
win.onkeypress(left , 'a')
win.onkeypress(right , 'd')
win.onkeypress(nw , 'q')
win.onkeypress(ne , 'e')
win.onkeypress(sw , 'z')
win.onkeypress(se , 'x')
win.onkeypress(Tackle , 't')
win.onkeypress(Switch , 'space')
win.onscreenclick(Shot)

#game variables
EnemyTackle = False
Tackler = None
once = True #93 , 119
OutOnce = True
redGoalie.goto(85/100*w/2 , 0)
holder = player
IsPassing = True
redGoals , blueGoals = 0 , 0

#main loop
while True: 
    #check if ball goes out of bounds
    if ball.xcor() >= 95/100*w/2 or ball.xcor() <= -95/100*w/2 or ball.ycor() >= 95/100*h/2 or ball.ycor() <= -95/100*h/2:
        if OutOnce:
            team = 1
            ThrowPlayer = random.choice(redTeam)
            ThrowPlayer.setpos(ball.pos())
            holder = ThrowPlayer
            taken = True
            OutOnce = False
            PassReciever = None
            while PassReciever == None:
                choice = random.choice(redTeam)
                if choice !=holder:
                    PassReciever = choice
            Shot(PassReciever.xcor() , PassReciever.ycor() , Special=True)
    # restrict player's movement out of boundary
    for players in blueTeam:
        if players.ycor() > 95/100*h/2:
            players.setpos(player.xcor() , 95/100*h/2)
        elif players.ycor() < -95/100*h/2:
            players.setpos(player.xcor() , -90/100*h/2)
        if players.xcor() > 95/100*w/2:
            players.setpos(95/100*w/2 , player.ycor())
        elif players.xcor() < -95/100*w/2:
            players.setpos(-95/100*w/2 , player.ycor())

        # restricting movement around goal posts
        if players.xcor() <= -8/10*w/2 and players.ycor() >= 93 and players.ycor() < 100:
            players.setpos(players.xcor() , 93)
        elif players.xcor() <= -8/10*w/2 and players.ycor() <= 119 and players.ycor() > 100:
            players.setpos(players.xcor() , 119)
        if players.xcor() <= -8/10*w/2 and players.ycor() <= -93 and players.ycor() > -100:
            players.setpos(players.xcor() , -93)
        elif players.xcor() <= -8/10*w/2 and players.ycor() >= -119 and players.ycor() < -100:
            players.setpos(players.xcor() , -119)

        if players.xcor() >= 8/10*w/2 and players.ycor() >= 93 and players.ycor() < 100:
            players.setpos(players.xcor() , 93)
        elif players.xcor() >= 8/10*w/2 and players.ycor() <= 119 and players.ycor() > 100:
            players.setpos(players.xcor() , 119)
        if players.xcor() >= 8/10*w/2 and players.ycor() <= -93 and players.ycor() > -100:
            players.setpos(players.xcor() , -93)
        elif players.xcor() >= 8/10*w/2 and players.ycor() >= -119 and players.ycor() < -100:
            players.setpos(players.xcor() , -119)
    if started:
        #checking for goals
        if ball.ycor() > -93 and ball.ycor() < 93 and ball.xcor() > -95/100*w/2 and ball.xcor() < -80/100*w/2:
            GoalPrinter()
            taken = False
            holder = player
            team = 0
            ball.setpos(0,0)
            random.choice(bforward).goto(0,0)
            time.sleep(3)
            GoalCleaner()
            redGoals += 1
            rcounter.clear()
            rcounter.write(f'{redGoals}', move=False, align="center", font=("Deja Vu Sans Mono", 240, "normal"))

        if ball.ycor() > -93 and ball.ycor() < 93 and ball.xcor() < 95/100*w/2 and ball.xcor() > 80/100*w/2:
            GoalPrinter()
            taken = False
            holder = player
            team = 0
            ball.setpos(0,0)
            random.choice(bforward).goto(0,0)
            time.sleep(3)
            GoalCleaner()
            blueGoals += 1
            bcounter.clear()
            bcounter.write(f'{blueGoals}', move=False, align="center", font=("Deja Vu Sans Mono", 240, "normal"))

        if redGoals == 3:
            rcounter.clear()
            rcounter.write(f'Red Wins!', move=False, align="center", font=("Deja Vu Sans Mono", 40, "normal"))
            time.sleep(5)
            break

        elif blueGoals == 3:
            bcounter.clear()
            bcounter.write(f'Blue Wins!', move=False, align="center", font=("Deja Vu Sans Mono", 40, "normal"))
            time.sleep(5)
            break

        #blue team AI
        ForwardIterator = 1
        for fd in bforward:
            if fd != player and ball.distance(fd.pos()) < 475 and fd.xcor() < 65/100*w/2:
                fd.seth(random.randint(-90,90))
                fd.fd(2)
            if fd!=player and ball.xcor() < -250:
                fd.seth(fd.towards(random.randint(-350,-250) , ForwardIterator*75))
                fd.fd(2)
            if ForwardIterator > 0:
                ForwardIterator += 1
            else:
                ForwardIterator -= 1
            ForwardIterator *= -1
        
        IsEnemeyAhead = False
        Intruders = []
        if ball.xcor() < -25/100*w/2 and team == 1:
            IsEnemeyAhead = True
        for players in redTeam:
            if players.xcor() < -25/100*w/2:
                Intruders.append(players)
        Longest = 1000
        Intercepter = None
        if IsEnemeyAhead:
            for players in bmid:
                if players.distance(ball.pos()) < Longest:
                    Longest = players.distance(ball.pos())
                    Intercepter = players
            Intercepter.seth(Intercepter.towards(ball.pos()))
            while Intercepter.distance(ball.pos()) > 0:
                Intercepter.fd(2)
                break
        z = 1
        for mid in bmid:
            if mid != Intercepter and len(Intruders) > 0 and mid !=player:
                mid.seth(mid.towards(-300 , z*50))
                mid.fd(1.5)
                z -= 2
            elif mid != player:
                mid.seth(mid.towards(-150 , z*50))
                mid.fd(1.5)
                z -= 2
        y = 3
        for defender in bdefenders:
            if defender != player and ball.xcor() < -40/100*w/2 and team == 1:
                defender.seth(defender.towards(-400 , y*50))
                defender.fd(1.5)
                y -= 2
            elif defender != player:
                defender.seth(defender.towards(defender.xcor() , random.randint(-450 , 450)))
                defender.fd(2)

        if ball.xcor() < -60/100*w/2 and blueGoalie != player:
            while blueGoalie.xcor() <= -70/100*w/2:
                blueGoalie.seth(blueGoalie.towards(ball.pos()))
                blueGoalie.fd(2)
                break
            while blueGoalie.ycor() != ball.ycor():
                if ball.ycor() > blueGoalie.ycor() and blueGoalie.ycor() < 93:
                    blueGoalie.seth(90)
                    blueGoalie.fd(2)
                    break
                elif ball.ycor() < blueGoalie.ycor() and blueGoalie.ycor() > -93:
                    blueGoalie.seth(270)
                    blueGoalie.fd(2)
                    break
                else:
                    break

        # red team AI
        IsEnemeyAhead = False
        Intruders = []
        if ball.xcor() > 25/100*w/2 and team == 0:
            IsEnemeyAhead = True
        for players in redTeam:
            if players.xcor() > 25/100*w/2:
                Intruders.append(players)
        Longest = 1000
        Intercepter = None
        if IsEnemeyAhead:
            for players in rmid:
                if players.distance(ball.pos()) < Longest:
                    Longest = players.distance(ball.pos())
                    Intercepter = players
            Intercepter.seth(Intercepter.towards(ball.pos()))
            while Intercepter.distance(ball.pos()) > 0:
                Intercepter.fd(2)
                break
        
        z = 1
        for mid in rmid:
            if mid != Intercepter and len(Intruders) > 0:
                mid.seth(mid.towards(300 , z*50))
                mid.fd(1.5)
                z -= 2
            elif mid != player:
                mid.seth(mid.towards(150 , z*50))
                mid.fd(1.5)
                z -= 2

        if ball.xcor() > 60/100*w/2:
            while redGoalie.xcor() >= 78/100*w/2:
                redGoalie.seth(redGoalie.towards(ball.pos()))
                redGoalie.fd(2)
                break
            while redGoalie.ycor() != ball.ycor():
                if ball.ycor() > redGoalie.ycor() and redGoalie.ycor() < 93:
                    redGoalie.seth(90)
                    redGoalie.fd(2)
                    break
                elif ball.ycor() < redGoalie.ycor() and redGoalie.ycor() > -93:
                    redGoalie.seth(270)
                    redGoalie.fd(2)
                    break
                else:
                    break

        for defender in rdefenders:
            if ball.xcor() > 40/100*w/2 and team == 0:
                defender.seth(defender.towards(400 , y*50))
                defender.fd(1.5)
                y -= 2
            else:
                defender.seth(defender.towards(defender.xcor() , random.randint(-450 , 450)))
                defender.fd(2)

        if team == 1 and holder not in rforward and holder != None:
            if IsPassing:
                IsPassing = False
                Invoker = FunctionInvoker(lambda: Shot(PassReciever.xcor() , PassReciever.ycor() ,  Redshot = True) , 2)
            longest = 1000
            PassReciever = None
            for forward in rforward:
                if holder.distance(forward.pos()) < longest and holder != None:
                    longest = holder.distance(forward.pos())
                    PassReciever = forward
            if Invoker != None:
                Invoker.Invoke()
                if Invoker.ExecutionStatus == 1:
                    IsPassing = True

        if team == 1 and holder in rforward:
            if holder.distance(-85/100*w/2 , 0) > 250:
                holder.seth(random.randint(90 , 270))
                holder.fd(2)
            else:
                Shot(-90/100*w/2,random.randint(-93,93) , Redshot=True)

            
        ForwardIterator = 1
        for fd in rforward:
            if fd != holder and ball.distance(fd.pos()) < 475 and fd.xcor() > -65/100*w/2 and team == 1:
                fd.seth(fd.towards(-85/100*w/2,random.randint(-150,150)))
                fd.fd(2)
            if fd!=holder and ball.xcor() > 250 and team == 0:
                fd.seth(fd.towards(random.randint(250 , 350) , ForwardIterator*75))
                fd.fd(2)
            if ForwardIterator > 0:
                ForwardIterator += 1
            else:
                ForwardIterator -= 1
                ForwardIterator *= -1               

    if Tackler != None:
        #mechanism for enemy team tackling our player
        if Tackler.distance(player.pos()) > 25:
            TackleCl = None
            EnemyTackle = False
            once = True
            Tackler = None
    if EnemyTackle:
        if TackleCl.TackleStatus() == True:
            once = True
            EnemyTackle = False
            team = 1
            holder = Tackler
    if team == 0:
        for players in redTeam:
            if players.distance(player.xcor() , player.ycor()) < 25 and once:
                once = False
                EnemyTackle = True
                Tackler = players
                TackleCl = TackleClock(Tackler , 2)
    # changing ball holder and player
    if taken and not shot:
        ball.goto(holder.pos())
    for players in blueTeam:
        if ball.distance(players.xcor() , players.ycor()) < 25 and not taken:
            taken = True
            if team == 0:
                player.color('dark blue')
            else:
                holder.color('dark red')
            holder = players
            player = players
            player.color('light blue')
            team = 0
    for players in redTeam:
        if ball.distance(players.xcor() , players.ycor()) < 25 and not taken:
            taken = True
            if team == 0:
                player.color('light blue')
            else:
                holder.color('dark red')
            team = 1
            holder = players
    win.update()