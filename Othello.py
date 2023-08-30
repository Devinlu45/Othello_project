class Player():
    '''
    A player class to store player information
    '''
    def __init__(self, player_name, player_color):
        self._player_name = player_name
        self._player_color = player_color
    # Get method for the player name
    def get_player_name(self):
        return self._player_name
    # Get method for the player color
    def get_player_color(self):
        return self._player_color
    
class Othello():
    '''
    An Othello class which will be for making the game run.
    '''
    def __init__(self):
        # The following sets up the initial board.
        self._players = []
        self._board = []
        self._done_game = False
        for x in range(0, 10):
            self._board.append(["*"] * 10)
        for i in range(1, 9):
            for j in range(1, 9):
                self._board[i][j] = '.'
        self._board[4][4] = "O"
        self._board[4][5] = "X"
        self._board[5][5] = "O"
        self._board[5][4] = "X" 

    
    def print_board(self):
        # This prints the board when called.
        for row in self._board:
            print (" ".join(row))
        
    def create_player(self, player_name, color):
        # Uses the player class to store the player information.
        A_player = Player(player_name, color)
        self._players.append(A_player)
        return self._players
    
    def return_winner(self):
        # Return the winner by iterating through the board.
        black_pieces = 0
        white_pieces = 0
        for i in range(1,9):
            for j in range(1, 9):
                # While iterating through the board, keep track of player score by counting their pieces.
                if self._board[i][j] == 'O':
                    white_pieces += 1
                if self._board[i][j] == 'X':
                    black_pieces += 1
        for a in self._players:
            print("Game is Ended: ")
            # Following if elif else statements returns winner.
            if self._players[0].get_player_color() == 'black' and black_pieces > white_pieces:
                print("Winner is black player: " + self._players[0].get_player_name())
                return("Winner is black player: " + self._players[0].get_player_name())
            elif self._players[1].get_player_color() == 'black' and black_pieces > white_pieces:
                print("Winner is black player: " + self._players[1].get_player_name())
                return("Winner is black player: " + self._players[1].get_player_name())
            elif black_pieces == white_pieces:
                print("It's a tie")
                return("It's a tie")
            elif self._players[0].get_player_color() == 'white' and white_pieces > black_pieces:
                print("Winner is white player: " + self._players[0].get_player_name())
                return("Winner is white player: " + self._players[0].get_player_name())
            else:
                print("Winner is white player: " + self._players[1].get_player_name())
                return("Winner is white player: " + self._players[1].get_player_name())
            
    def return_available_positions(self, color):
        # Returns the available positions that the player can place their pieces on.
        white_position = []
        black_position = []
        for x in range(1,9):
            for y in range(1, 9):
                if self._board[x][y] == '.':
                    # uses the helper method "pos_to_check" to check all directions for valid moves.
                    if self.pos_to_check('black', (x, y)):
                        black_position.append((x, y))
                    elif self.pos_to_check('white', (x, y)):
                        white_position.append((x, y))
        # Returns available positions depending on color.
        if color == 'white':
            print(white_position)
            return white_position
        elif color == 'black':
            print(black_position)
            return black_position
        if white_position == [] and black_position ==[]:
            self._done_game = True
         
    def pos_to_check(self, color, piece_position):
        # Will check if the position we are checking is valid or not based on Othello rules.
        can_make_move = False
        if color == 'white':
            player_1 = 'O'
            player_2 = 'X'
        if color == 'black':
            player_1 = 'X'
            player_2 = 'O'
        for next_direction in range(8):
            # Iterates through possible direction using another helper method "pos_dir_check"
            hold_val = piece_position
            pos_to_check = self.pos_dir_check(hold_val, next_direction)
            row, column = pos_to_check
            if self._board[row][column] == '.':
                color_to_check = '.'
            elif self._board[row][column] == '*':
                color_to_check = '*'
            elif self._board[row][column] == 'O':
                color_to_check = 'O'
            elif self._board[row][column] == 'X':
                color_to_check = 'X'
            while color_to_check == player_2:
                # This initially checks to see if a move is valid if the position direction is the opposite color of current player piece.
                pos_to_check = self.pos_dir_check(pos_to_check, next_direction)
                row, column = pos_to_check
                if self._board[row][column] == '.':
                    color_to_check = '.'
                elif self._board[row][column] == '*':
                    color_to_check = '*'
                elif self._board[row][column] == 'O':
                    color_to_check = 'O'
                elif self._board[row][column] == 'X':
                    color_to_check = 'X'
                if color_to_check == player_1:
                    # If this if statement activates, then that means that the initial piece to check is the opposite and the piece after that is the same as current player piece.
                    # This means a capture happens, so it would be a valid move.
                    can_make_move = True
                    break
        return can_make_move
            
    def pos_dir_check(self, piece_position, next_direction):
        # Will check the next directions of the current player piece. Left, right, top, down, etc.
        row, column = piece_position
        if next_direction == 0:
            return(row-1, column + 1)
        if next_direction == 1:
            return(row-1, column)
        if next_direction == 2:
            return(row + 1, column)
        if next_direction == 3:
            return (row-1, column -1)
        if next_direction == 4:
            return(row, column + 1)
        if next_direction == 5:
            return(row, column-1)
        if next_direction == 6:
            return(row+1, column-1)
        if next_direction == 7:
            return(row + 1, column + 1)
        
    def play_game(self, player_color, piece_position):
        # Uses the "make_move" helper to actually place pieces and return necessary information.
        list_of_position = self.return_available_positions(player_color)
        # As long as a valid move exist, then the player places that piece.
        if piece_position in list_of_position:
            self.make_move(player_color, piece_position)
        # If it doesn't exist, then we return invalid moves.
        elif piece_position not in list_of_position:
            print("Here are the valid moves:", list_of_position)
            return("Invalid move")
        # Returns winner once no more moves can be placed.
        if self._done_game == True:
            self.return_winner()
            return
        
    def make_move(self, player_color, piece_position):
        # helper method to play game.
        list_of_position = []
        if player_color == 'white':
            player_1 = 'O'
            player_2 = 'X'
        if player_color == 'black':
            player_1 = 'X'
            player_2 = 'O'
        for next_direction in range(8):
            # Iterates through all possible directions and checks to see if the next_color is equal to opponent.
            hold_val = piece_position
            pos_to_check = self.pos_dir_check(hold_val, next_direction)
            row, column = pos_to_check
            if self._board[row][column] == '.':
                next_color = '.'
            elif self._board[row][column] == '*':
                next_color = '*'
            elif self._board[row][column] == 'O':
                next_color = 'O'
            elif self._board[row][column] == 'X':
                next_color = 'X'
            while next_color == player_2:
                # This iterates until we hit the if statement which means capture happens or it doesn't and that means capture doesn't happen.
                list_of_position.append(pos_to_check)
                pos_to_check = self.pos_dir_check(pos_to_check, next_direction)
                row, column = pos_to_check
                if self._board[row][column] == '.':
                    next_color = '.'
                elif self._board[row][column] == '*':
                    next_color = '*'
                elif self._board[row][column] == 'O':
                    next_color = 'O'
                elif self._board[row][column] == 'X':
                    next_color = 'X'
                if player_1 == next_color:
                    # This if statement indicates capture because in the initial while loop it shows that our piece == opponent color and this if statement
                    # shows that the next while loop check == our current player color so Othello rules == capture.
                    row, column = piece_position
                    self._board[row][column] = player_1
                    for piece_position in list_of_position:
                        row, column = piece_position
                        self._board[row][column] = player_1
        return self._board

game = Othello()
game.print_board()
game.create_player("Helen", "white")
game.create_player("Leo", "black")
game.play_game("black", (6,5))
game.print_board()
game.play_game("white", (6,6))
game.print_board()