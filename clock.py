masterList = "ONSTWHELFIFOURXEVENEGHTEENY" # this honestly took the most amount of time to create
numbers = [
    [], # 0
    [11, 18, 19], # 1
    [3, 4, 11], # 2
    [3, 5, 13, 15, 17], # 3
    [8, 11, 12, 13], # 4
    [8, 9, 16, 17], # 5
    [2, 9, 14], # 6
    [2, 6, 16, 17, 18], # 7
    [6, 9, 20, 21, 22], # 8
    [1, 9, 18, 19], # 9
    [3, 6, 18], # 10
    [6, 7, 15, 16, 17, 18], # 11
    [3, 4, 6, 7, 16, 17], # 12
    [3, 5, 9, 13, 22, 23, 24, 25], # 13
    [8, 11, 12, 13, 22, 23, 24, 25], # 14
    [8, 9, 10, 22, 23, 24, 25], # 15
    [2, 9, 14, 22, 23, 24, 25], # 16
    [2, 6, 16, 17, 18, 22, 23, 24, 25], # 17
    [6, 9, 20, 21, 22, 23, 24, 25], # 18
    [1, 9, 18, 19, 22, 23, 24, 25], # 19
    [3, 4, 6, 18, 22, 26], # 20
    [3, 5, 9, 13, 22, 26], # 30
    [8, 11, 13, 22, 26], # 40
    [8, 9, 10, 22, 26] # 50
]

hourNow = []
minTens = []
minOnes = []
minTeens = []
secTens = []
secOnes = []
secTeens = []
isPM = False

def checkTime():
    global hourNow, minTens, minOnes, minTeens, secTens, secOnes, secTeens, isPM
    isPM = False
    if hour() >= 12:
        isPM = True
    if hour() > 12:
        hourNow = numbers[hour() - 12]
    elif hour() == 0:
        hourNow = numbers[12]
    else:
        hourNow = numbers[hour()]
    
    minTens = []
    minOnes = []
    minTeens = []
    if minute() > 0:
        if 11 <= minute() <= 19:
            minTeens = numbers[minute()]
        else:
            tens = int(minute() / 10)
            ones = minute() % 10
            if tens == 1:
                minTens = numbers[10]
            elif tens > 1:
                minTens = numbers[18 + tens]
            if ones > 0:
                minOnes = list(numbers[ones])
                if tens == 0:
                    minOnes.append(0)

    secTens = []
    secOnes = []
    secTeens = []
    if second() > 0:
        if 11 <= second() <= 19:
            secTeens = numbers[second()]
        else:
            tens = int(second() / 10)
            ones = second() % 10
            if tens == 1:
                secTens = numbers[10]
            elif tens > 1:
                secTens = numbers[18 + tens]
            if ones > 0:
                secOnes = list(numbers[ones])

def draw_row(active, x, y):
    for i in range(len(masterList)):
        char = masterList[i]
        if i in active:
            fill(255, 170, 0)
        else:
            fill(45)
        text(char, x + (i * 25), y)

def displayTime():
    global hourNow, minTens, minOnes, minTeens, secTens, secOnes, secTeens, isPM
    background(15)
    fill(255, 170, 0)
    text("A", 325, 300)
    text("N", 350, 300)
    text("D", 375, 300)
    text("M", 375, 500)
    if isPM:
        fill(255, 170, 0) 
        text("P", 325, 500)
        fill(45)
        text("A", 350, 500)
    else:
        fill(45)
        text("P", 325, 500)
        fill(255, 170, 0)
        text("A", 350, 500)
    draw_row(hourNow, 25, 100)
    draw_row(minTens, 25, 150)
    draw_row(minOnes, 25, 200)
    draw_row(minTeens, 25, 250)
    draw_row(secTens, 25, 350)
    draw_row(secOnes, 25, 400)
    draw_row(secTeens, 25, 450)

def setup():
    size(700, 600) 
    text_size(26)
    text_align(CENTER, CENTER)

def draw():
    checkTime()
    displayTime()