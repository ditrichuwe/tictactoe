area = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"] ]
turn=1

def chooseSign():
    if turn%2==0:
        sign="x"
    else:
        sign="0"
    return sign

def showField():
    for i in range(len(area)):
        print(area [i])

def checkWin():
     if area[1][0]=="x" and area[1][1]=="x" and area[1][2]=="x":
        print("x has won")
        return True
     
     if area[2][0]=="x" and area[2][1]=="x" and area[2][2]=="x":
        print("x has won")
        return True
     
     if area[0][0]=="x" and area[0][1]=="x" and area[0][2]=="x":
        print("x has won")
        return True
     
     if area[0][0]=="x" and area[1][0]=="x" and area[2][0]=="x":
        print("x has won")
        return True
     
     if area[0][1]=="x" and area[1][1]=="x" and area[2][1]=="x":
        print("x has won")
        return True
     
     if area[0][2]=="x" and area[1][2]=="x" and area[2][2]=="x":
        print("x has won")
        return True
     
     if area[0][0]=="x" and area[1][1]=="x" and area[2][2]=="x":
        print("x has won")
        return True
     
     if area[2][0]=="x" and area[1][1]=="x" and area[0][2]=="x":
        print("x has won")
        return True

     if area[1][0]=="0" and area[1][1]=="0" and area[1][2]=="0":
         print("0 has won")
         return True
     
     if area[2][0]=="0" and area[2][1]=="0" and area[2][2]=="0":
        print("0 has won")
        return True
     
     if area[0][0]=="0" and area[0][1]=="0" and area[0][2]=="0":
        print("0 has won")
        return True
     
     if area[0][0]=="0" and area[1][0]=="0" and area[2][0]=="0":
        print("0 has won")
        return True
     
     if area[0][1]=="0" and area[1][1]=="0" and area[2][1]=="0":
        print("0 has won")
        return True
     
     if area[0][2]=="0" and area[1][2]=="0" and area[2][2]=="0":
        print("0 has won")
        return True
     
     if area[0][0]=="0" and area[1][1]=="0" and area[2][2]=="0":
        print("0 has won")
        return True
     
     if area[2][0]=="0" and area[1][1]=="0" and area[0][2]=="0":
        print("0 has won")
        return True

while True:
    showField()

    row=int(input("Type in the number of the row you wanna make your move"))
    column=int(input("Type in the number of the column you wanna make your move"))

    area[row][column] =chooseSign()

    turn=turn+1
    if checkWin()==True:
        break


