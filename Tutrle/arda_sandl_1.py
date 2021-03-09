import turtle as tr
from random import randrange

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
        t2.write(sy, True, align="center", font=("Helvetica", 8, "normal"))
        t2.forward(-100)

    t2.right(90)
    t2.forward(100)
    t2.left(90)
    t2.forward(100)
    
    for i in range(6, 11):
        sy = str(i)
        t2.write(sy, True, align="center", font=("Helvetica", 8, "normal"))
        t2.forward(100)

    t2.right(90)
    t2.forward(100)
    t2.right(90)
    t2.forward(95)

    for i in range(11, 16):
        sy = str(i)
        t2.write(sy, True, align="center", font=("Helvetica", 8, "normal"))
        t2.forward(100)

    t2.left(90)
    t2.forward(100)
    t2.left(90)
    t2.forward(120)
    
    for i in range(16, 21):
        sy = str(i)
        t2.write(sy, True, align="center", font=("Helvetica", 8, "normal"))
        t2.forward(100)

    t2.right(90)
    t2.forward(100)
    t2.right(90)
    t2.forward(90)
    
    for i in range(21, 26):
        sy = str(i)
        t2.write(sy, True, align="center", font=("Arial", 8, "normal"))
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


    # Added two other character selection

    animal1 = str(input("Which character do you want for first player? {Monkey, Cow, Bull or Lion} (answer as monkey, cow, bull, lion)"))
    
    
    tr.addshape( animal1 +".gif")
    t0.shape(animal1 +".gif")
    t0.right(90)
    t0.forward(230)
    t0.right(90)
    t0.forward(180)

    
    animal2 = str(input("Which character do you want for second player? {Monkey, Cow, Bull or Lion} (answer as monkey, cow, bull, lion)"))

    tr.addshape(animal2 +".gif")
    tc.shape(animal2 +".gif")
    tc.right(90)
    tc.forward(270)
    tc.right(90)
    tc.forward(180)
    
    animal1 = animal1.capitalize()
    animal2 = animal2.capitalize()
    
    pos1=0
    pos2=0

    while pos1 < 25 and pos2 < 25:
        
        input("Press Enter to roll dice for player 1!")
        pos1r = (randrange(1,6))
        print("You roll" + " " + str(pos1r))
        pos1 = pos1 + pos1r 
        print(animal1 + " is at position " + str(pos1))

        if pos1 == 5:
            pos1 = 15
            print(animal1 + " used the ladder")
        if pos1 == 8:
            print("Uh oh, " + animal2 + " fell down the snake! xO" )
            pos1 = 3
        if pos1 == 9:
            print(animal1 + " used the ladder")
            pos1 = 12
        if pos1 == 18:
            print(animal1 + " used the ladder")
            pos1 = 23
        if pos1 == 20:
            print("Uh oh, " + animal2 + " fell down the snake! xO" )
            pos1 = 1
        if pos1 == 24:
            print("Uh oh, " + animal2 + " fell down the snake! xO" )
            pos1 = 14

        input("Press Enter to roll dice for player 2!")
        pos2r = (randrange(1,6))
        print("You roll" +  " " + str(pos2r))
        pos2 = pos2 + pos2r
        print(animal2 + " is at position " + str(pos2))

        if pos2 == 5:
            print(animal2 + " used the ladder")
            pos2 = 15
        if pos2 == 8:
            print("Uh oh, " + animal2 + " fell down the snake! xO" )
            pos2 = 3
        if pos2 == 9:
            print(animal2 + " used the ladder")
            pos2 = 12
        if pos2 == 18:
            print(animal2 + " used the ladder")
            pos2 = 23
        if pos2 == 20:
            print("Uh oh, " + animal2 + " fell down the snake! xO" )
            pos2 = 1
        if pos2 == 24:
            print("Uh oh, " + animal2 + " fell down the snake! xO" )
            pos2 = 14
       
        
 #   def roll():
        


 #   def moveplayer(player, current_pos):
  #      snake_squares = {16: 4, 33: 20, 48: 24, 62: 56, 78: 69, 94: 16}
   #     ladder_squares = {3: 12, 7: 23, 20: 56, 47: 53, 60: 72, 80: 94}
    #tr.addshape("bull.gif")
   # tr.shape("bull.gif")
  #  tr.penup()
 #   tr.goto(-300,-270)
    


main()
