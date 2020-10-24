import random                                               #importing the random class

class TicTacToe(object):                                    #declaring a class for wining combinations
    winning_combos = (
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    )

    winners = ('X-win', 'Draw', 'O-win')

    def __init__(self, board=[]):
        '''
        Initialize the tic tac toe board

        :param board: 1-D list of board positions
        '''
        if len(board) == 0:
            self.board = [0 for i in range(9)]
        else:
            self.board = board

    def print_board(self):                                  #definition for printing the tic tac toe board
        for i in range(3):
            print(
                "| " + str(self.board[i * 3]) +
                " | " + str(self.board[i * 3 + 1]) +
                " | " + str(self.board[i * 3 + 2]) + " |"
            )

    def check_game_over(self):
                                                            #definition for checking wether the game is over or there is a winner on the board
        if 0 not in [element for element in self.board]:    # the game is over when there are no empty moves or no 0 in the grid
            return True
        if self.winner() != 0:                              # The game is over if someone has already won it
            return True
        return False

    def available_moves(self):

                                                                #To check what all possible moves are remaining for a player

        return [index for index, element in enumerate(self.board) if element is 0]

    def available_combos(self, player):

                                                                #To check what are the possible places to play for winning the game

        return self.available_moves() + self.get_acquired_places(player)

    def X_won(self):                                            #member function for minimax
        return self.winner() == 'X'

    def O_won(self):                                            #member function for minimax
        return self.winner() == 'O'

    def is_tie(self):                                           #member function for minimax
        return self.winner() == 0 and self.check_game_over()

    def winner(self):
        '''
        Checks for the winner of the game

        :return player: return 'X' or 'O' whoever has won the game
                        else returns 0
        '''
        for player in ('X', 'O'):
            positions = self.get_acquired_places(player)  #storing all the acquired position in a positions variable
            for combo in self.winning_combos:             #checking all the winning combinations
                win = True                                #Initializing a variable win as initially true
                for pos in combo:
                    if pos not in positions:              #checking all the positions and  it does not founds it then initilizes the value of win as false
                        win = False
                if win:
                    return player                         #if a player has won then return the player code(x or o) else return 0
        return 0

    def get_acquired_places(self, player):
        '''
        To get the positions already acquired by a particular player

        :param player: 'X' or 'O'
        '''
        return [index for index, element in enumerate(self.board) if element == player]         #returning all the acquired places

    def make_move(self, position, player):                          #accepting the position and player from the main function
        self.board[position] = player                               #replacing the specified position by the move of that player i.e x for 0

    def minimax(self, node, player):                                # Minimax algorithm for choosing the best possible move towards
                                                                    # winning the game

        if node.check_game_over():                                  #checking if the game is over or not
            if node.X_won():                                        #checking for the winning member
                return -1
            elif node.is_tie():
                return 0
            elif node.O_won():
                return 1
        best = 0                                                    #varible used for determing the best move
        for move in node.available_moves():                         #checking all the available moves
            node.make_move(move, player)                            #making the move by marking it in the board
            val = self.minimax(node, get_enemy(player))             #calling the function recursively for determing the best possible move
            node.make_move(move, 0)                                 #making the best possible move
            if player == 'O':                                       #evaluation for the best move
                if val > best:                                      #evaluation for the best move
                    best = val                                      #evaluation for the best move
            else:
                if val < best:                                      #evaluation for the best move
                    best = val                                      #evaluation for the best move
        return best                                                 #returning the best value after every iteration


def determine(board, player):
    '''
    Driver function to apply minimax algorithm
    '''
    a = 0                                                           #Initializing the variable a
    choices = []                                                    #to keep a record of all the choices
    if len(board.available_moves()) == 9:                           #if all the moves are available
        return 4
    for move in board.available_moves():                            #iterating all the avalible moves
        board.make_move(move, player)                               #marking the move
        val = board.minimax(board, get_enemy(player))               #calling the minimac function
        board.make_move(move, 0)                                    #making a move
        if val > a:
            a = val
            choices = [move]
        elif val == a:
            choices.append(move)                                    #keeping a track of all the moves
    try:
        return random.choice(choices)                               #returning random choies
    except IndexError:
        return random.choice(board.available_moves())


def get_enemy(player):                                              #changing the value of the opponent player from (X to O) or vice versa
    if player == 'X':
        return 'O'
    return 'X'


if __name__ == "__main__":                                              #initializing the driver code
    board = TicTacToe()                                                 #Making an object of the TicTacToe class to use all its member functions
    print('Board positions are like this: ')                            #Printing message for informing the board positions
    for i in range(3):
        print(                                                          #printing the grid of tictactoe with its postitions
            "| " + str(i * 3 + 1) +
            " | " + str(i * 3 + 2) +                                    #printing the grid of tictactoe with its postitions
            " | " + str(i * 3 + 3) + " |"                               #printing the grid of tictactoe with its postitions
        )
    print('Type in the position number you to make a move on..')        #Taking the input position of the user so that he can play his move in the game
    while not board.check_game_over():                                  #checking that wether the game is over or not by calling the chech_game_over() member function
        player = 'X'
        player_move = int(input("Your Move: ")) - 1                     #taking the move from the user
        if player_move not in board.available_moves():                  #checking if the move is already present or not i.e.if the position entered is valid i.e from 1 to 9
            print('Please check the input!')                            #displaying the error message if the move is not present
            continue
        board.make_move(player_move, player)                            #passing the player and its move to the make_move() so that it can mark the move of that player in the grid
        board.print_board()                                             #printing the grid
        print()
        if board.check_game_over():                                     #checking if the game is over
            break                                                       #breaking the loop if the game is over
        print('Computer is playing.. ')                                 #printing the message when the computer starts playing or minimax algorithm is being applied
        player = get_enemy(player)                                      #defining the player as opposite to the one that played before
        computer_move = determine(board, player)                        #initiating the minimax algorithm to evaluate the computers next move
        board.make_move(computer_move, player)                          #marking the move of the computer on the board
        board.print_board()                                             #printing the resultant board
    if board.winner() != 0:                                             #Checking if there is a winner
        if board.winner() == 'X':                                       #if the winner is the user
            print ("Congratulations you win!")                          #Displaying the message
        else:
            print('Computer Wins!')                                     #Displaying the message
    else:
        print("Game tied!")                                             #If there is no winner then the game is tied