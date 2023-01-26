# Realizat de /Produced by Casiu George Valentin
"""

"""
tari = ['AUSTRIA', 'BELGIA', 'BULGARIA','CIPRU', 'CEHIA', 'CROATIA', 'DANEMARCA', 'ESTONIA',
 'FINLANDA', 'FRANTA', 'GERMANIA', 'GRECIA', 'UNGARIA','IRLANDA', 'ITALIA', 'LETONIA','LITUANIA',
 'LUXEMBURG', 'MALTA', 'OLANDA', 'POLONIA','PORTUGALIA','ROMANIA', 'SLOVACIA', 'SLOVENIA', 'SPANIA', 'SUEDIA']
import random
import turtle
import time

def desen(g):
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

#Programul principal/The main program
turtle.setup (width=500, height=500, startx=1028, starty=0)
tara = random.choice(tari)
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
            turtle.pu()
            turtle.goto(0,0)
            turtle.pd()
            for i in range(50):
                if i%2==0:
                    turtle.color("yellow")
                else:
                    turtle.color("red")
                time.sleep(0.1)
                turtle.write("ESTI SPANZURAT!!!", align="center", font=('Arial', 18, 'normal'))
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
            break
input()
