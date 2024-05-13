#importing random
import random

#Difficulty selection
avdif = ['easy', 'medium', 'hard']
cdif = input("Choose difficulty: ")
cdif = cdif.lower()
while cdif not in avdif:
    print("Choose only 'easy', 'medium', 'hard'")
    cdif = input("Choose difficulty: ").lower()
    if cdif in avdif:
        break

#Variable declaration
usdchr = []
rndchr = ''
tble = []
cmpttble = ''
tble2 = ''
unusble = []
cntprsnt = ''
mvs = 0

#creating a list of charecters in random order
if cdif == 'easy':
    el = [chr(i) for i in range(65, 65+8)]
    for j in range(4):
        row = []
        for i in range(4):
            rndchr = random.choice(el)
            while usdchr.count(rndchr) > 1:
                rndchr = random.choice(el)
            usdchr.append(rndchr)
            row.append(rndchr)
        tble.extend(row)
    rl = 4

elif cdif == 'medium':
    el = [chr(i) for i in range(65, 65+18)]
    for j in range(6):
        row = []
        for i in range(6):
            rndchr = random.choice(el)
            while usdchr.count(rndchr) > 1:  
                rndchr = random.choice(el)
            usdchr.append(rndchr)
            tble.append(rndchr)
    rl = 6

else:
    el = [chr(int(i)) for i in range(64, 64+32)]
    for j in range(8):
        row = []
        for i in range(8):
            rndchr = random.choice(el)
            while usdchr.count(rndchr) > 1:
                rndchr = random.choice(el)
            usdchr.append(rndchr)
            row.append(rndchr)
        tble.extend(row)
    rl = 8

#creating a table with respect to the chosen difficulty
tblefmt = '    '
for i in range(1, rl + 1):
    tblefmt += str(i) + '     '

tblefmt += '\n ' + ' _____' * rl + '\n'
for i in range(rl):
    tblefmt += chr(65 + i) + '| {}   ' * (rl) + '|'
    tblefmt += '\n ' + '|_____' * (rl) + '|'
    tblefmt += '\n'

vsbllst = [' '] * rl ** 2

#loop that runs till the board is completed
while True:
    #getting input from user about which tile to uncover
    print("\nFor eg: you can use A1 to uncover the tile in first row first column...")
    opn = input("Enter the tile to uncover: ")
    while len(opn) != 2:
        print("Invalid input.\n")
        opn = input("Enter the tile to uncover: ")

    if opn[0].isnumeric():
        rw = int(opn[0])
        cmn = ord(opn[1].upper())

    else:
        rw = int(opn[1])
        cmn = ord(opn[0].upper())

    nm = rw + (cmn - 65) * rl - 1
    if nm > rl ** 2:
        print("Invalid input.\n")
        continue

    #checking if tile is already completed
    if nm in unusble:
        print("This tile is completed\n")
        continue
    
    #fetching the charecters in the tile selected
    if mvs % 2 == 0:
        vsbllst[nm] = tble[nm]
        exec('cmpttble = tblefmt.format(' + str(vsbllst)[1:-1] + ')')
        cntprsnt = tble[nm]
        nm2 = nm

    else:
        if nm == nm2:
            print("Invalid input\n")
            continue

        vsbllst[nm] = tble[nm]

        #checking if a tile was completed
        if tble[nm] == cntprsnt:
            print("You guessed/found it!\n")
            unusble.extend([nm, nm2])
            vsbllst[nm] = '✓'
            vsbllst[nm2] = '✓'
        exec('cmpttble = tblefmt.format(' + str(vsbllst)[1:-1] + ')')
        print(cmpttble)
        for i in range(len(vsbllst)):
            if vsbllst[i] != '✓':
                vsbllst[i] = ' ' 
        exec('cmpttble = tblefmt.format(' + str(vsbllst)[1:-1] + ')')

        #Ensure that user does not see the previously opened tiles
        cwkencwkj = input("Press ENTER to continue: ")
        print('\n' * 200)

    #display the table
    print(cmpttble)
    
    #incrementing moves after every iteration
    mvs += 1 

    #checking if the table is completed
    if vsbllst.count("✓") == rl ** 2:
        break

#displaying number of moves taken to complete and a completion message
print("Good Job!!")
print("You finished the board in", mvs, 'moves!')