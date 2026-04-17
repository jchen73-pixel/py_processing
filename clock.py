masterList = "ONSTWHELFIFOURXEVENEGHTEENY" # this honestly took the most amount of time to create

one = [11, 18, 19]
two = [3, 4, 11]
three = [3, 5, 13, 15, 17]
four = [8, 11, 12, 13]
five = [8, 9, 16, 17]
six = [2, 9, 14]
seven = [2, 6, 16, 17, 18]
eight = [6, 9, 20, 21, 22]
nine = [1, 9, 18, 19]
ten = [3, 6, 18]
eleven = [6, 7, 15, 16, 17, 18]
twelve = [3, 4, 6, 7, 16, 17]
thirteen = [3, 5, 9, 13, 22, 23, 24, 25]
fourteen = [8, 11, 12, 13, 22, 23, 24, 25]
fifteen = [8, 9, 10, 22, 23, 24, 25]
sixteen = [2, 9, 14, 22, 23, 24, 25]
seventeen = [2, 6, 16, 17, 18, 22, 23, 24, 25]
eighteen = [6, 9, 20, 21, 22, 23, 24, 25]
nineteen = [1, 9, 18, 19, 22, 23, 24, 25]
twenty = [3, 4, 6, 18, 22, 26]
thirty = [3, 5, 9, 13, 22, 26]
forty = [8, 11, 13, 22, 26]
fifty = [8, 9, 10, 22, 26]

hours = [one, two, three, four, five, six, seven, eight, nine, ten, eleven, twelve]
tens = [ten, twenty, thirty, forty, fifty]
ones = [one, two, three, four, five, six, seven, eight, nine]
specials = [eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen]

hourNow = []
minTens = []
minSec = []
minTeens = []
secTens = []
secOnes = []
secTeens = []
isPM = False

def checkTime():
    global hourNow, minTens, minSec, minTeens, secTens, secOnes, secTeens, isPM
    isPM = False
    if hour() >= 12:
        isPM = True
    if hour() > 12:
        hourNow = hours[hour() - 13]
    elif hour() == 0:
        hourNow = hours[11]
    else:
        hourNow = hours[hour() - 1]
    
    minTens = []
    minSec = []
    minTeens = []
    if minute() > 0:
        if 11 <= minute() <= 19:
            minTeens = specials[minute() - 11]
        else:
            tens_val = int(minute() / 10)
            ones_val = minute() % 10
            if tens_val > 0:
                minTens = tens[tens_val - 1]
            if ones_val > 0:
                minSec = list(ones[ones_val - 1])
                if tens_val == 0:
                    minSec.append(0)

    secTens = []
    secOnes = []
    secTeens = []
    if second() > 0:
        if 11 <= second() <= 19:
            secTeens = specials[second() - 11]
        else:
            tens_val = int(second() / 10)
            ones_val = second() % 10
            if tens_val > 0:
                secTens = tens[tens_val - 1]
            if ones_val > 0:
                secOnes = list(ones[ones_val - 1])

def draw_row(pattern, active, x, y):
    for i in range(len(pattern)):
        char = pattern[i]
        if i in active:
            fill(255, 170, 0)
        else:
            fill(45)
        text(char, x + (i * 25), y)

def displayTime():
    global hourNow, minTens, minSec, minTeens, secTens, secOnes, secTeens, isPM
    background(15)
    fill(255, 170, 0)
    text("I", 300, 50)
    text("T", 325, 50)
    text("I", 375, 50)
    text("S", 400, 50)
    draw_row(masterList, hourNow, 25, 100)
    draw_row(masterList, minTens, 25, 150)
    draw_row(masterList, minSec, 25, 200)
    draw_row(masterList, minTeens, 25, 250)
    fill(255, 170, 0)
    text("A", 325, 300)
    text("N", 350, 300)
    text("D", 375, 300)
    draw_row(masterList, secTens, 25, 350)
    draw_row(masterList, secOnes, 25, 400)
    draw_row(masterList, secTeens, 25, 450)
    fill(255, 170, 0)
    text("S", 275, 500)
    text("E", 300, 500)
    text("C", 325, 500)
    text("O", 350, 500)
    text("N", 375, 500)
    text("D", 400, 500)
    if second() == 1:
        fill(45)
    text("S", 425, 500)
    if isPM:
        fill(255, 170, 0) 
        text("P", 325, 550)
        fill(45)
        text("A", 350, 550)
    else:
        fill(45)
        text("P", 325, 550)
        fill(255, 170, 0)
        text("A", 350, 550)
    fill(255, 170, 0)
    text("M", 375, 550)

def setup():
    size(700, 600) 
    text_size(26)
    text_align(CENTER, CENTER)

def draw():
    checkTime()
    displayTime()