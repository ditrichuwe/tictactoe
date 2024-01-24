area = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"] ]

def showField():
    for i in range(len(area)):
        print(area [i])

while True:
    showField()

    row=int(input("Type in the number of the row you wanna make your move"))
    column=int(input("Type in the number of the column you wanna make your move"))

    area[row][column] = "0"
