board=[["-","-","-","-"], 
       ["-","-","-","-"],
       ["-","-","-","-"],
       ["-","-","-","-"]]
print(board)
def my_function(team):
    if team == "X":
        symbol = "X"
        opp = "0"
    elif team == "0":
        symbol = "0"
        opp = "X"
    for i in range(16):
        choice = input("enter your move in the form RC")
        r = int(choice[0])
        c = int(choice[1])
        board[r][c] = symbol
        print(board)
        if board[0][0] == symbol and board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][2] == board[0][3]:
            print(symbol, "wins")
            break
        elif board[1][0] == symbol and board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][2] == board[1][3]:
            print(symbol,"wins")
            break
        elif board[2][0] == symbol and board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][2] == board[2][3]:
            print(symbol, "wins")
            break
        elif board[3][0] == symbol and board[3][0] == board[3][1] and board[3][1] == board[3][2] and board[3][2] == board[3][3]:
            print(symbol, "wins")
            break  
        elif board[0][0] == symbol and board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[2][0] == board[3][0]:
            print(symbol, "wins")
            break
        elif board[0][1] == symbol and board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[2][1] == board[3][1]:
            print(symbol, "wins")
            break
        elif board[0][2] == symbol and board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[2][2] == board[3][2]:
            print(symbol, "wins")
            break
        elif board[0][3] == symbol and board[0][3] == board[1][3] and board[1][3] == board[2][3] and board[2][3] == board[3][3]:
            print(symbol, "wins")
            break     
        elif board[0][0] == symbol and board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] == board[3][3]:
            print(symbol, "wins")
            break
        elif board[3][0] == symbol and board[3][0] == board[2][1] and board[2][1] == board[1][2] and board[1][2] == board[0][3]:
            print(symbol, "wins")
            break

        choice2 = input("enter your move in the form RC")
        x = int(choice2[0])
        y = int(choice2[1])
        board[x][y] = opp
        print(board)
        if board[0][0] == opp and board[0][0] == board[0][1] and board[0][1] == board[0][2] and board[0][2] == board[0][3]:
            print(opp, "wins")
            break
        elif board[1][0] == opp and board[1][0] == board[1][1] and board[1][1] == board[1][2] and board[1][2] == board[1][3]:
            print(opp,"wins") 
            break
        elif board[2][0] == opp and board[2][0] == board[2][1] and board[2][1] == board[2][2] and board[2][2] == board[2][3]:
            print(opp,"wins") 
            break
        elif board[3][0] == opp and board[3][0] == board[3][1] and board[3][1] == board[3][2] and board[3][2] == board[3][3]:
            print(opp,"wins")
            break
        elif board[0][0] == opp and board[0][0] == board[1][0] and board[1][0] == board[2][0] and board[2][0] == board[3][0]:
            print(opp,"wins")   
            break
        elif board[0][1] == opp and board[0][1] == board[1][1] and board[1][1] == board[2][1] and board[2][1] == board[3][1]:
            print(opp,"wins")
            break
        elif board[0][2] == opp and board[0][2] == board[1][2] and board[1][2] == board[2][2] and board[2][2] == board[3][2]:
            print(opp,"wins")
            break
        elif board[0][3] == opp and board[0][3] == board[1][3] and board[1][3] == board[2][3] and board[2][3] == board[3][3]:
            print(opp,"wins") 
            break    
        elif board[0][0] == opp and board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[2][2] == board[3][3]:
            print(opp,"wins") 
            break    
        elif board[3][0] == opp and board[3][0] == board[2][1] and board[2][1] == board[1][2] and board[1][2] == board[0][3]:
            print(opp,"wins")
            break

    print(board)
            

my_function("X")
