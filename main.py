#Global variables

game_still_going=True

current_player="X"


winner = None


board = [
    "_","_","_",
    "_","_","_",
    "_","_","_"]

def display_board():
    print(board[0]+" | "+ board[1]+" | "+ board[2])
    print(board[3]+" | "+ board[4]+" | "+ board[5])
    print(board[6]+" | "+ board[7]+" | "+ board[8])

def play_game():
    display_board()

    while game_still_going():
        handle_turn(current_player)
        check_if_game_over()
        flip_player()


    if winner=="X" or winner =="O":
        print(winner + " won.")
    elif winner==None:
        print("Tie")

       #check where error is     

def handle_turn(player):

    print(player + "s Turn.")
    position = input("Choose Position from 1 to 9: ")
    position=int(position)-1
    board[position]=player
    display_board()


def check_if_game_over():
    check_if_winner()
    check_if_tie()


def check_if_winner():

    global winner

    row_winner=check_rows()

    column_winner=check_columns()

    diagonal_winner=check_diagonals()

    if row_winner:
        #row winner
        winner=row_winner
    elif column_winner:
        #col winner
        winner=column_winner
    elif diagonal_winner:
        #dia winner
        winner=diagonal_winner
    else:
        #there was no win
        winner=None
    return


def check_rows():
    global game_still_going

    row_1 = board[0]==board[1]==board[2] !="-"
    row_2 = board[3]==board[4]==board[5] !="-"
    row_3 = board[6]==board[7]==board[8] !="-"

    if row_1 or row_2 or row_3:
        game_still_going=False

    if row_1:
       return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]

    return

def check_columns():
    global game_still_going

    col_1 = board[0]==board[3]==board[6] !="-"
    col_2 = board[1]==board[4]==board[7] !="-"
    col_3 = board[2]==board[5]==board[8] !="-"

    if col_1 or col_2 or col_3:
        game_still_going=False

    if col_1:
       return board[0]
    if col_2:
        return board[1]
    if col_3:
        return board[2]
    return


def check_diagonals():
    global game_still_going

    dia_1 = board[0]==board[4]==board[8] !="-"
    dia_2 = board[6]==board[4]==board[2] !="-"
    

    if dia_1 or dia_2 :
        game_still_going=False

    if dia_1:
       return board[0]
    if dia_2:
        return board[6]
    return

def check_if_tie():
    global game_still_going

    if "-" not in board:
        game_still_going=False

    return

def flip_player():

    global current_player
    if current_player == "X":
        current_player="O"
    elif current_player =="O":
        current_player = "X"
        

    return

play_game()


