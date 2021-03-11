import turtle as tr
from random import randrange
import time

#tbg = turtle.Screen()
#tbg.bgcolor("black")
#tbg.title("Arda's Snake & Ladder")


def main():
    tr.setup(800,800,0 ,0)              # Main setup, window etc. is being setup alongside turtles
    tr.title("Arda's Snake & Ladder")

    t1 = tr.Turtle()
    t2 = tr.Turtle()

    t1.fillcolor("red")
    t2.fillcolor("blue")
    t1.pendown()
    t2.pendown()


    t1.speed(10)            # Drawing begins :3
    t2.speed(10)
    
    t1.forward(300)
    t1.right(90)
    t1.forward(300)
    t1.right(90)
    t1.forward(100)
    t1.right(90)
    t1.forward(500)

    for i in range(2):
        
        t1.left(90)
        t1.forward(100)
        t1.left(90)
        t1.forward(500)
        t1.right(90)
        t1.forward(100)
        t1.right(90)
        t1.forward(500)


    t2.forward(300)
    t2.left(90)
    t2.forward(200)
    t2.left(90)
    t2.forward(500)
    t2.left(90)
    t2.forward(100)
    t2.left(90)
    t2.forward(500)

    for i in range(2):
        
        t2.right(90)
        t2.forward(100)
        t2.right(90)
        t2.forward(500)
        t2.left(90)
        t2.forward(100)
        t2.left(90)
        t2.forward(500)
    
    t2.penup()
    t1.penup()
    
    t2.left(90)
    t2.forward(70)
    t2.left(90)
    t2.forward(470)


    # Adding numbers, on each line they are done in a 5 times loop with helvetica font style

    t2.pencolor("red")

    for i in range(1, 6):
        sy = str(i)
        t2.write(sy, True, align="center", font=("Calibri", 8, "normal"))
        t2.forward(-100)

    t2.right(90)
    t2.forward(100)
    t2.left(90)
    t2.forward(100)
    
    for i in range(6, 11):
        sy = str(i)
        t2.write(sy, True, align="center", font=("Calibri", 8, "normal"))
        t2.forward(100)

    t2.right(90)
    t2.forward(100)
    t2.right(90)
    t2.forward(95)

    for i in range(11, 16):
        sy = str(i)
        t2.write(sy, True, align="center", font=("Calibri", 8, "normal"))
        t2.forward(100)

    t2.left(90)
    t2.forward(100)
    t2.left(90)
    t2.forward(120)
    
    for i in range(16, 21):
        sy = str(i)
        t2.write(sy, True, align="center", font=("Calibri", 8, "normal"))
        t2.forward(100)

    t2.right(90)
    t2.forward(100)
    t2.right(90)
    t2.forward(90)
    
    for i in range(21, 26):
        sy = str(i)
        t2.write(sy, True, align="center", font=("Calibri", 8, "normal"))
        t2.forward(100)



    #Now our objects will be created as turtles.
    # each will use a single object to 

    
    tl1 = tr.Turtle()
    tl1.penup()
    tr.addshape("ladder1.gif")
    tl1.shape("ladder1.gif")
    tl1.left(90)
    tl1.forward(90)
    tl1.left(-90)
    tl1.forward(30)

    tl2 = tr.Turtle()
    tl2.penup()
    tr.addshape("ladder2.gif")
    tl2.shape("ladder2.gif")
    tl2.forward(-90)
    tl2.left(-90)
    tl2.forward(100)

    tl3 = tr.Turtle()
    tl3.penup()
    tr.addshape("ladders.gif")
    tl3.shape("ladders.gif")
    tl3.right(90)
    tl3.forward(170)
    tl3.left(90)
    tl3.forward(260)

    tl4 = tr.Turtle()
    tl4.penup()
    tr.addshape("snake3.gif")
    tl4.shape("snake3.gif")
    tl4.forward(-190)
    tl4.left(-90)
    tl4.forward(120)

    tl5 = tr.Turtle()
    tl5.penup()
    tr.addshape("snake2.gif")
    tl5.shape("snake2.gif")
    tl5.forward(50)
    tl5.left(-90)
    tl5.forward(200)

    tl6 = tr.Turtle()
    tl6.penup()
    tr.addshape("snake.gif")
    tl6.shape("snake.gif")
    tl6.forward(130)
    tl6.left(90)
    tl6.forward(40)


    
    t0 = tr.Turtle()
    tc = tr.Turtle()
    t0.penup()
    tc.penup()

    t2.ht()

    tr.addshape("at.gif")
    t1.shape("at.gif")
    t1.forward(100)


    uh = tr.Turtle()
    tr.addshape("at2.gif")
    uh.shape("at2.gif")
    uh.penup()
    uh.forward(200)
    uh.left(90)
    uh.forward(240)



    # Board coordinates set

    Xtab = [-150, -50, 50, 150, 250,
            250, 150, 50, -50, -150,
            -150, -50, 50, 150, 250,
            250, 150, 50, -50, -150,
            -150, -50, 50, 150, 250,
            250,250,250,250,250,250,
            250,250,250,250,250,250,
            250,]
    
    Ytab = [-250, -250, -250, -250, -250,
            -150, -150, -150, -150, -150,
            -50, -50, -50, -50, -50,
            50, 50, 50, 50, 50,
            150, 150, 150, 150, 150
            ,150, 150, 150, 150, 150
            ,150, 150, 150, 150, 150]
    
    def gameplay():

        # Added two other character selection, Monkey and Lion respectively!

        animal1 = str(input("Which character do you want for first player? {Monkey, Cow, Bull, Camel or Lion}"))
        animal1 = animal1.lower()
    
        tr.addshape(animal1 +".gif")
        t0.shape(animal1 +".gif")
        t0.goto(-140, -250)
    

    
        animal2 = str(input("Which character do you want for second player? {Monkey, Cow, Bull, Camel or Lion}"))
        animal2 = animal2.lower()

        tr.addshape(animal2 +".gif")
        tc.shape(animal2 +".gif")
        tc.goto(-170, -250)
    
        animal1 = animal1.capitalize()
        animal2 = animal2.capitalize()
    
        pos1=0
        pos2=0

        zar = tr.Turtle()
        zar.penup()
        zar.forward(-300)

        for i in range(1, 7):
            tr.addshape(str(i) + ".gif") # Dice is being set here

        winner = tr.Turtle()            # Winning prompt is set here
        tr.addshape("win.gif")
        winner.shape("win.gif")
        winner.ht()
    
        while pos1 < 25 and pos2 < 25:
        
            input("Press Enter to roll dice for player 1!")
            pos1r = (randrange(1,6))
            zar.shape(str(pos1r)+".gif")
            print("You roll" + " " + str(pos1r))
            pos1 = pos1 + pos1r 
        
           # print(t0.pos())


            yuru = pos1r
            yu1 = pos1 - pos1r
            for i in range(yuru): 
                t0.setpos(Xtab[yu1 + i], Ytab[yu1 + i])
                time.sleep(0.4)
            
            if pos1 == 5:                               #Ladders and Snakes are here, transportation according to array
                pos1 = 15
                print(animal1 + " used the ladder")
                t0.setpos(Xtab[pos1-1],Ytab[pos1-1])
            if pos1 == 8:
                print("Uh oh, " + animal2 + " fell down the snake! xO" )
                pos1 = 3
                t0.setpos(Xtab[pos1-1],Ytab[pos1-1])
            if pos1 == 9:
                print(animal1 + " used the ladder")
                pos1 = 12
                t0.setpos(Xtab[pos1-1],Ytab[pos1-1])
            if pos1 == 18:
                print(animal1 + " used the ladder")
                pos1 = 23
                t0.setpos(Xtab[pos1-1],Ytab[pos1-1])
            if pos1 == 20:
                print("Uh oh, " + animal2 + " fell down the snake! xO" )
                pos1 = 1
                t0.setpos(Xtab[pos1-1],Ytab[pos1-1])
            if pos1 == 24:
                print("Uh oh, " + animal2 + " fell down the snake! xO" )
                pos1 = 14
                t0.setpos(Xtab[pos1-1],Ytab[pos1-1])

            print(animal1 + " is at position " + str(pos1))

            input("Press Enter to roll dice for player 2!")
            pos2r = (randrange(1,6))
            zar.shape(str(pos2r)+".gif")
            print("You roll" +  " " + str(pos2r))
            pos2 = pos2 + pos2r
        
        
            #print(tc.pos())
            yuru2 = pos2r
            yu2 = pos2 - pos2r 
            for i in range(yuru2): 
                tc.setpos(Xtab[yu2 + i], Ytab[yu2 + i])
                time.sleep(0.4)


            if pos2 == 5:
                print(animal2 + " used the ladder")
                pos2 = 15
                tc.setpos(Xtab[pos2-1],Ytab[pos2-1])
            if pos2 == 8:
                print("Uh oh, " + animal2 + " fell down the snake! xO" )
                pos2 = 3
                tc.setpos(Xtab[pos2-1],Ytab[pos2-1])
            if pos2 == 9:
                print(animal2 + " used the ladder")
                pos2 = 12
                tc.setpos(Xtab[pos2-1],Ytab[pos2-1])
            if pos2 == 18:
                print(animal2 + " used the ladder")
                pos2 = 23
                tc.setpos(Xtab[pos2-1],Ytab[pos2-1])
            if pos2 == 20:
                print("Uh oh, " + animal2 + " fell down the snake! xO" )
                pos2 = 1
                tc.setpos(Xtab[pos2-1],Ytab[pos2-1])
            if pos2 == 24:
                print("Uh oh, " + animal2 + " fell down the snake! xO" )
                pos2 = 14
                tc.setpos(Xtab[pos2-1],Ytab[pos2-1])

            print(animal2 + " is at position " + str(pos2))

            if pos1 > 24 or pos2 > 24:
                winner.st()
                ceap = str(input("Wanna play again? y or n"))
                ceap = ceap.capitalize()
                if  ceap == "Y":
                    winner.ht()
                    gameplay()
                if ceap == "N":
                    exit()
    gameplay()
            

main()

