#declare a dictionary of 9 keys and empty values
board ={
        1: ' ', 2: ' ', 3: ' ',
        4: ' ', 5: ' ', 6: ' ',
        7: ' ', 8: ' ', 9: ' '
    }
#define a function for printing a board 
def print_board():
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('---------')
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---------')
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    
#take input of position and character both from user
for i in range(9):
        user=int(input("Enter the position (1-9) to place your mark: "))
        if user<0 or user>9:
            print("Invalid position. Please enter a number between 1 and 9.")
            continue
        if board[user]==' ':
            val=input("Enter the character ")
            board[user]=val
        else:
            print("Position already taken. Try again.")
            continue
        #print the board after each move
        #print(print_board())
        print_board()
