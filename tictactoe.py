board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
playing = False

def draw_board(board):
    print(board[0] + " |" + board[1] + "| " + board[2])
    print("-+-+-+-")
    print(board[3] + " |" + board[4] + "| " + board[5])
    print("-+-+-+-")
    print(board[6] + " |" + board[7] + "| " + board[8])

def main():
    while not playing:
        move = int(input("Enter range (1-9): "))
        if move == 0:
            board[0]="X"    
        elif move == 1:
            board[1] = "X"
        elif move == 2:
            board[2] = "X"
        elif move == 3:
            board[3] = "X"
        elif move == 4:
            board[4] = "X"
        elif move == 5:
            board[5] = "X"
        draw_board(board)
       

draw_board(board)

if __name__ == "__main__":
    main()