matrix=[]
for i in range(3): #row
    myList=[]
    for y in range(3):
        myList.append(" ")
    matrix.append(myList)
        
print(matrix)

for i in matrix :
    for y in i:
        print(f"[{y}]",end= " ")
    print()
while True:

    row=int(input("Satır 1-3 : ")) -1 #indexten dolayı -1
    column=int(input("Sütun 1-3 : ")) -1 #indexten dolayı -1
    symbol=input("X mi O mu ? ").lower()
    if 0<=row<=2 and 0<=column<=2:

        if symbol != "x" and symbol!= "o":
            print("Please enter just X or O")
            continue
        else:
            if matrix[row][column] != " ":
                print("Bu index dolu başka bir yer seç! ")
                continue
            matrix[row][column]=symbol
            for satir in matrix:
                for cell in satir:
                    print(f"[{cell}]",end= " ")
                print()
            if matrix[row][0] == symbol and  matrix[row][1]==symbol and  matrix[row][2]==symbol:
                print(f"{symbol} kazandı")
                break
            
            elif matrix[0][column] == symbol and  matrix[1][column]==symbol and  matrix[2][column]==symbol:
                print(f"{symbol} kazandı")
                break
            elif matrix[0][0]==symbol and matrix[1][1]==symbol and matrix[2][2]==symbol:
                 print(f"{symbol} kazandı")
                 break
            elif matrix[0][2]== symbol and matrix[1][1]== symbol and matrix[2][0]==symbol:
                print(f"{symbol} kazandı")
                break
            else:
                print("Daha bitmedi")
            for satir in matrix:
                for cell in satir:
                    print(f"[{cell}]", end=" ")
                print()
            dolu=True
            for satir in matrix:
                for cell in satir:
                    if cell == " ":
                        dolu=False
            if dolu==True:
                print("TÜM SATIRLAR DOLDU")
                break
    else:
        print("Yanlış sütun numarası")
        continue
