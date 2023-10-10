symbol = "X"
#create board
board=[["-","-","-"],
       ["-","-","-"],
       ["-","-","-"]]
print(board)
for i in range(9):
    choice = input("enter your move in the form RC")
    r = int(choice[0])
    c = int(choice[1])
    board[r][c] = symbol
    print(board)
    if symbol == "X":
        symbol = "0"
    else: 
        symbol = "X"
    if board[0][0] == board[0][1] and board[0][1] == board[0][2]:
        print(symbol,"wins")
    if board[1][0] == board[1][1] and board[1][1] == board[1][2]:
        print(symbol,"wins")
    if board[2][0] == board[2][1] and board[2][1] == board[2][2]:
        print(symbol,"wins")
    if board[0][0] == board[1][0] and board[1][0] == board[2][0]:
        print(symbol,"wins")
    if board[0][1] == board[1][1] and board[1][1] == board[2][1]:
        print(symbol,"wins")
    if board[0][2] == board[1][2] and board[1][2] == board[2][2]:
        print(symbol,"wins")
    if board[0][0] == board[1][1] and board[1][1] == board[2][2]:
        print(symbol,"wins")
    if board[0][2] == board[1][1] and board[1][1] == board[2][0]:
        print(symbol,"wins")