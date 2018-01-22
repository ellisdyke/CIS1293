from random import *

randNum = randint(1,10)

print('''\nCOMPUTER IS THINKING OF A NUMBER BETWEEN 1 AND 10.\n\n''')

while True:
    
    g = input('ENTER YOUR GUESS NOW: ')
    try:
        g = int(g)
    except ValueError:
        print('INVALID INPUT: PLEASE ENTER AN INTEGER BETWEEN 1 AND 10')

    if (g == randNum):
        print('Y O U  W I N')
        break
    if (g != randNum):
        print('G A M E  O V E R\n\nCORRECT ANSWER WAS: ',randNum)
        break
