board = []
rows = 0
cols = 0
node_count = 0
poison_row = -1
poison_col = -1

def init_board(r, c): #initialize the board with all chocolates
    global board, rows, cols, poison_row, poison_col
    rows = r
    cols = c
    board = []
    for i in range(rows): #initialize the board with all chocolates
        board.append([])
        for j in range(cols):
            board[i].append(1) #chocolate

    for i in range(poison_row + 1): #initialize the poison chocolate
        for j in range(poison_col + 1): #initialize the poison chocolate
            board[i][j] = -1 #poison chocolate

def print_board():
    global board, rows, cols
    
    print("     ", end="")
    for j in range(1, cols + 1):
        print(f"{j}    ", end="")
    print("\n")
    for i in range(rows):
        print(f"{i + 1}    ", end="")
        for j in range(cols):
            if i == poison_row and j == poison_col and board[poison_row][poison_col] == -1: #poison chocolate
                print("X    ", end="")
            elif board[i][j] == -1 or board[i][j] == 1: #chocolate
                print("O    ", end="") 
            else: #empty space
                print("     ", end="")
        print("\n")
        
def is_game_over():
    for i in range(poison_row + 1):
        for j in range(poison_col + 1): 
            if board[i][j] == 0:  # if any chocolate in the range is eaten, game is over
                return True
    return False #game is not over

def valid_row_and_column(row ,col):
    if(row < 0 or col < 0  or row >= rows or col >= cols or board[row][col] == 0): #if row or column is out of bounds or chocolate is already eaten
        return False 
    else:
        return True 

def make_move(row, col): #eat the chocolate
    global board
    for x in range(row, rows): #eat all chocolates in the row and column
        for y in range(col, cols): 
            board[x][y] = 0 

def minimax(is_maximizing): #minimax algorithm
    global board, node_count 
    node_count += 1 #increment node count
    
    if is_game_over(): #if game is over
        if(is_maximizing==True):  #if maximizing player wins
            return -1 
        else:
            return 1 #if minimizing player wins

    if is_maximizing==True: #maximizing player
        best_value = -10000
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 1: #if chocolate is not eaten
                    board_copy = [row[:] for row in board] #copy of board
                    make_move(i, j) #eat the chocolate 
                    move_value = minimax(False)
                    best_value = max(best_value, move_value) #maximize the value
                    board = board_copy #restore the board
        return best_value #return the best value
    else:
        best_value = 100000 #minimizing player
        for i in range(rows): 
            for j in range(cols):
                if board[i][j] == 1: #if chocolate is not eaten
                    board_copy = [row[:] for row in board] #copy of board
                    make_move(i, j) #eat the chocolate
                    move_value = minimax(True)
                    best_value = min(best_value, move_value) #minimize the value
                    board = board_copy #restore the board
        return best_value #return the best value

def find_best_move(): #find the best move for the AI
    global board, node_count 
    best_value = -100000
    best_row = 0
    best_col = 0
    node_count = 0
    for i in range(rows): 
        for j in range(cols):
            if board[i][j] == 1: #if chocolate is not eaten
                board_copy = [row[:] for row in board] #copy of board
                make_move(i,j) #eat the chocolate
                move_value = minimax(False) 
                board = board_copy #restore the board
                if (move_value > best_value): #maximize the value
                    best_value = move_value 
                    best_row = i
                    best_col = j
    print(f"Node Count: {node_count}") #print the node count
    return best_row, best_col #return the best row and column

def human_vs_human(): #human vs human game mode
    player = 1
    while not is_game_over(): #while game is not over
        print_board() #print the board
        print(f"Player {player}'s turn")  #print the player's turn
        row = int(input("Enter row: ")) #get the row
        col = int(input("Enter column: ")) #get the column
        row -= 1 
        col -= 1
        if (valid_row_and_column(row, col)): #if row and column are valid
            make_move(row, col) #eat the chocolate
            if(player == 1): #switch players
                player = 2 
            else: 
                player = 1 
        else:
            print("Invalid move, try again.") 
    
    print_board() #print the board
    print(f"Player {player} won!") #print the winner

def human_vs_ai(human_starts): #human vs AI game mode
    player = 1 
    if not human_starts: #if AI starts
        player = 2
    while not is_game_over(): #while game is not over
        print_board() #print the board
        if player == 1: #if player is human
            print("Your turn") #print the player's turn
            row = int(input("Enter row: ")) #get the row
            col = int(input("Enter column: ")) #get the column
            row -= 1
            col -= 1
            if (valid_row_and_column(row, col)): #if row and column are valid
                make_move(row, col) #eat the chocolate
                player = 2 #switch players
            else: 
                print("Invalid move, try again.") 
        else: #if player is AI
            print("AI's turn") #print the player's turn
            row, col = find_best_move() #find the best move         
            make_move(row, col) #eat the chocolate
            player = 1 #switch players

    print_board() #print the board
    if player == 1: #if human wins
        print("You Won!")   
    else: #if AI wins
        print("AI Won!")

rows = int(input("Enter number of rows: ")) #get the number of rows
cols = int(input("Enter number of columns: ")) #get the number of columns
poison_row = int(input("Enter the row of the poison chocolate (initial index = 1): ")) -1 #get the row of the poison chocolate
poison_col = int(input("Enter the column of the posion chocolate (initial index = 1): ")) -1 #get the column of the poison chocolate

init_board(rows, cols) #initialize the board
mode = input("Enter game mode (1 for Human vs Human, 2 for Human vs AI): ") #get the game mode
if mode == "1": #if game mode is human vs human
    human_vs_human() #play human vs human
elif mode == "2": #if game mode is human vs AI
    human_starts = input("Do you want to start first? (yes/no): ") #get if human wants to start first
    if(human_starts == "yes"): #if human starts
        human_starts = True 
    else: #if AI starts
        human_starts = False
    human_vs_ai(human_starts) #play human vs AI
else:
    print("Invalid mode") #invalid mode
