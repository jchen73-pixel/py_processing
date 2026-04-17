#            01234567890123456789012
hoursList = "SFTWONHURELELIVEGHTXENE"
hOne = [4, 5, 9]
hTwo = [2, 3, 4]
hThree = [2, 6, 8, 9, 11]
hFour = [1, 4, 7, 8]
hFive = [1, 13, 14, 15]
hSix = [0, 13, 19]
hSeven = [0, 9, 14, 20, 21]
hEight = [9, 13, 16, 17, 18]
hNine = [5, 13, 21, 22]
hTen = [18, 20, 21]
hEleven = [9, 10, 11, 14, 20, 21]
hTwelve = [2, 3, 11, 12, 14, 15]
hours = [hOne, hTwo, hThree, hFour, hFive, hSix, hSeven, hEight, hNine, hTen, hEleven, hTwelve]

#           012345678901
tensList = "FTWENHIFORTY"
ten = [1, 3, 4]
twenty = [1, 2, 3, 4, 10, 11]
thirty = [1, 5, 6, 9, 10, 11]
forty = [7, 8, 9, 10, 11]
fifty = [0, 6, 7, 10, 11]
tens = [ten, twenty, thirty, forty, fifty]

#           012345678901234567890
onesList = "OXSFTWONHUREIVGHTXENE"
one = [6, 7, 11]
two = [4, 5, 6]
three = [4, 8, 10, 11, 18]
four = [3, 6, 9, 10]
five = [3, 12, 13, 18]
six = [2, 12, 17]
seven = [2, 11, 13, 18, 19]
eight = [11, 12, 14, 15, 16]
nine = [7, 12, 19, 20]
ones = [one, two, three, four, five, six, seven, eight, nine]

#               0123456789012345678901234
specialsList = "NSTWHELFIFOURXEVENEGHTEEN"
eleven = [5, 6, 14, 15, 16, 17]
twelve = [2, 3, 5, 6, 15, 16]
thirteen = [2, 4, 8, 12, 21, 22, 23, 24]
fourteen = [9, 10, 11, 12, 21, 22, 23, 24]
fifteen = [7, 8, 9, 21, 22, 23, 24]
sixteen = [1, 8, 13, 21, 22, 23, 24]
seventeen = [1, 14, 15, 16, 17, 21, 22, 23, 24]
eighteen = [5, 8, 19, 20, 21, 22, 23, 24]
nineteen = [0, 8, 17, 18, 21, 22, 23, 24]
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
        hourNow = hours[11] # 12
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
                if tens_val == 0:
                    secOnes.append(0)

def draw_row(pattern, active, x, y):
    for i in range(len(pattern)):
        char = pattern[i]
        if i in active:
            fill(255, 170, 0)
        else:
            fill(45)
        text(char, x + (i * 25), y)

def displayTime():
    background(15)
    fill(255, 170, 0)
    text("I", 300, 50)
    text("T", 325, 50)
    text("I", 375, 50)
    text("S", 400, 50)
    draw_row(hoursList, hourNow, 75, 100)
    draw_row(tensList, minTens, 212.5, 150)
    draw_row(onesList, minSec, 100, 200)
    draw_row(specialsList, minTeens, 50, 250)
    fill(255, 170, 0)
    text("A", 325, 300)
    text("N", 350, 300)
    text("D", 375, 300)
    draw_row(tensList, secTens, 212.5, 350)
    draw_row(onesList, secOnes, 100, 400)
    draw_row(specialsList, secTeens, 50, 450)
    fill(255, 170, 0)
    text("S", 275, 500)
    text("E", 300, 500)
    text("C", 325, 500)
    text("O", 350, 500)
    text("N", 375, 500)
    text("D", 400, 500)
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