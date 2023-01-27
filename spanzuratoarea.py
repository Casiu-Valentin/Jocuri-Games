# Realizat de /Produced by Casiu George Valentin
"""
Jocul spanzuratoarea
The Hangman game
Realizat cu tarile UE/Made with EU countries
"""

def desen(g): #procedura de desenare a spanzuratorii si personajului/the procedure for drawing the hangman and the character
    a=turtle.Turtle()
    a.ht()
    a.pensize(5)
    a.color("red")
    if g==0:
        a.pensize(3)
        a.pencolor("black")
        a.pu()
        a.goto(100,-100)
        a.pd()
        a.fd(100)
        a.lt(120)
        a.fd(100)
        a.lt(120)
        a.fd(100)
        a.goto(150,-100)
        a.goto(150,200)
        a.goto(0,200)
        a.goto(0,150)
    elif g==1:
        a.pu()
        a.goto(0,100)
        a.pd()
        a.circle(25)
        a.pu()
        a.goto(-10,130)
        a.pd()
        a.circle(5)
        a.pu()
        a.goto(10,130)
        a.pd()
        a.circle(5)
        a.pu()
        a.goto(0, 128)
        a.pd()
        a.rt(90)
        a.fd(5)
        a.lt(90)
        a.fd(3)
        a.pu()
        a.goto(-10, 115)
        a.pd()
        a.fd(20)
    elif g==2:
        a.pu()
        a.goto(0, 100)
        a.pd()
        a.right(90)
        a.fd(100)
    elif g==3:
        a.rt(55)
        a.fd(70)
    elif g == 4:
        a.rt(125)
        a.fd(70)
    elif g==5:
        a.goto(0,70)
        a.rt(55)
        a.fd(50)
    elif g==6:
        a.goto(0, 70)
        a.rt(125)
        a.fd(50)
    else:
        a.left(70)
        a.fd(50)

def afis(a,b,c,d): #procedura de afisare a unui text(c) in mod grafic in diverse pozitii(a,b) si intermitent rosu-galben
    turtle.pu() #procedure to display a text(c) graphically in various position(a,b) and flashing red-yellow
    turtle.goto(a,b)
    turtle.pd()
    for i in range(d):
        if i % 2 == 0:
            turtle.color("yellow")
        else:
            turtle.color("red")
        time.sleep(0.1)
        turtle.write(c, move=False, align="center", font=('Arial', 18, 'normal'))

#Programul principal/The main program
import random
import turtle
import time
tari = ['AUSTRIA', 'BELGIA', 'BULGARIA','CIPRU', 'CEHIA', 'CROATIA', 'DANEMARCA', 'ESTONIA',
 'FINLANDA', 'FRANTA', 'GERMANIA', 'GRECIA', 'UNGARIA','IRLANDA', 'ITALIA', 'LETONIA','LITUANIA',
 'LUXEMBURG', 'MALTA', 'OLANDA', 'POLONIA','PORTUGALIA','ROMANIA', 'SLOVACIA', 'SLOVENIA', 'SPANIA', 'SUEDIA']
turtle.setup (width=500, height=500, startx=1028, starty=0)
tara = random.choice(tari)
print(tara)
rasp = '-' * len(tara)
print('SPANZURATOAREA')
print('Ghiceste tara din UE!')
print(rasp)
turtle.pu()
turtle.goto(0,210)
turtle.pd()
turtle.write("SPANZURATOAREA",align="center",font=('Arial', 18, 'normal'))
turtle.ht()
g = 0
desen(g)
while g<6:
    c = input('Introduceti litera: ')
    c = c.upper()
    if c not in tara:
        g = g + 1
        desen(g)
        if g==6:
            print('Ai pierdut! Tara era', tara)
            afis(0,0,"ESTI SPANZURAT!!!",50)
            afis(0, -220, "TARA ESTE " + tara + "!!!", 26)
            break
        else:
            print('Fara',c,'- mai ai',str(6-g),'incercari!')
            continue
    else:#daca exista litera
        rasp_temp = list(rasp)
        rasp = ""
        for x in range(len(rasp_temp)):
            if c == tara[x]:
                rasp_temp[x] = c
            rasp += rasp_temp[x]
        print(rasp)
        if rasp.find('-') == -1:#verific daca cuvantul este complet
            print('Felicitari!')
            afis(0,-180, "FELICITARI!!!", 26)
            afis(0,-220,"TARA ESTE "+tara+"!!!", 50 )
            break
