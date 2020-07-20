from math import inf as infinity
import random
#variables for computer maximization in minimax
human = -1
comp = +1
def create_board():
    '''
    Creates the board for playing tic tac toe as a list of 9 elements,
    each one being an empty string i.e ''.
    :return: A list with 9 '' elements.
    '''
    board = ['','','',
             '', '', '',
             '', '', '',
             ]
    return board

def space_is_free(pos, board):
    '''
    Check if a position on the board is free.
    :param pos: position to be checked, an integer between 0 and 8
    :param board: state of the board to be checked
    :return: True if position is empty i.e. the element in that position is ''
    '''
    if board[pos] == '':
        return True
    else:
        return False
def empty_spaces(board):
    '''
    Return all the empty spaces in a board
    :param board: board to be checked
    :return: a list with the empty indexes of empty spaces in the board
    '''
    indexes = [0,1,2,3,4,5,6,7,8]
    empty = []
    for i in indexes:
        if board[i] == '':
            empty.append(i)

    return empty
def insert_letter(letter, pos, board):
    '''
    Inserts a letter (equivalent to make a move) in a certain position of the board
    :param letter: Letter to be inserted, X or O
    :param pos: Position in the board where the letter is going to be inserted, integer between 0 and 8
    :param board: Board where the letter is going to be inserted
    :return: Board updated with the letter in position pos
    '''
    board[pos] = letter
    return board

def print_board(board):
    '''
    Prints the current board on the console
    :param board: board to be printed on the console
    '''
    print("   "+ board[0]+"   |   " + board[1] + "   |   " +  board[2])
    print("--------------------")
    print("   "+ board[3] +"   |   " + board[4] +"   |   " + board[5])
    print("--------------------")
    print("   "+ board[6] + "   |   " + board[7] + "   |   " + board[8])

def print_example_board():
    '''
    Creates an example board with integers designing the locations
    '''
    print("   " + "0" + "   |   " + "1" + "   |   " + "2" + "   "   )
    print("--------------------")
    print("   " + "3" + "   |   " + "4" + "   |   " + "5" + "   "  )
    print("--------------------")
    print("   " + "6" + "   |   " + "7" + "   |   " + "8" + "   "  )


def isWinner(player,letter, board):
    '''
    Checks whether a player have won the match according to the rules of Tic Tac Toe.
    :param player: player to be evaluated, can be human or comp
    :param board: board to be examined for winning conditions
    :return: bool
    '''
    #first 3 conditions for winning on rows
    if    ( (board[0] == letter and board[1] == letter and board[2] == letter)
        or (board[3] == letter and board[4] == letter and board[5] == letter)
        or (board[6] == letter and board[7] == letter and board[8] == letter)
    #three condition for forming columns
        or (board[0] == letter and board[3] == letter and board[6] == letter)
        or (board[1] == letter and board[4] == letter and board[7] == letter)
        or (board[2] == letter and board[5] == letter and board[8] == letter)
    #two conditions for the diagonals
        or (board[0] == letter and board[4] == letter and board[8] == letter)
        or (board[2] == letter and board[4] == letter and board[6] == letter)
            ):
        return True
    else:
        return False

def is_board_full(board):
    '''
    Checks if the board is full, this means all the elements in the list are different from ''.
    :param board: board to be examined
    :return: boolean
    '''
    if '' in board:
        return False
    else:
        return True

def player_move(board, human_letter):
    '''
    Defines a human player move by asking for an integer between 0 and 8.
    :param board: Board where the move is going to taje place
    :param human_letter: Letter that the human is playing, X or O
    :return: None
    '''
    letter=human_letter
    run=True
    while run:
        move = input('Please select a position to play (0,8):')
        try:
            move = int(move)
        except ValueError:
            print('That was not a valid number, Try again')
            continue
        possible_list = [0,1,2,3,4,5,6,7,8]
        if move in possible_list:
            if space_is_free(move, board):
                insert_letter(letter, move, board)
                run = False
            else:
               print("Space is occupied, enter new move (0,8):")
        else:
            print("Invalid entry")

def evaluate(board, comp_letter, human_letter):
    '''
    Function that evaluates the state of the board
    :param board: A board to be evaluated
    :param comp_letter: Letter that the computer is playing, X or O
    :param human_letter: Letter that the humas is playing, X or O
    :return: 1 if the computer wins, -1 if the human wins, 0 if draw
    '''
    if isWinner('comp', comp_letter, board):
        score = +1
    # human will be O
    elif isWinner('human',human_letter,board):
        score = -1
    else:
        score = 0

    return score
def game_over(board,comp_letter,human_letter):
    """
     This function test if the human or computer wins
     :param state: the state of the current board
     :param comp_letter: Letter that the computer is playing, X or O
     :param human_letter: Letter that the humas is playing, X or O
     :return: True if the human or computer wins
     """
    return isWinner(human,human_letter, board) or isWinner(comp,comp_letter,board)
def comp_move(board,comp_letter,human_letter):
    '''
    Defines the computer move. If the computer is first, it will select a random move
    on the board. Otherwise, it will call the minimax algorithm to define the best possible move.
    :param board: Current state of the board
    :param comp_letter: Letter that the computer is playing, X or O
    :param human_letter: Letter that the humas is playing, X or O
    :return: None
    '''
    depth = len(empty_spaces(board))
    pos_moves = empty_spaces(board)
    if depth == 9:
        pos_moves = empty_spaces(board)
        move = random.choice(pos_moves)
        insert_letter(comp_letter, move, board)
        print_board(board)
    else:
        move = minimax(board,depth, comp,comp_letter,human_letter)
        move = move[0]
        insert_letter(comp_letter, move, board)
        print_board(board)
def minimax(board, depth, player, comp_letter, human_letter):
  '''
  Function that uses the minimax algorithm to provide the best possible move.
  :param board: The current board where the algorithm is going to be applied
  :param depth: node index, in this case is between 0 and 9
  :param player: a human player or a computer
  :param comp_letter: Letter that the computer is playing, X or O
  :param human_letter: Letter that the humas is playing, X or O
  :return: a list with the best position and best score
  '''
  if player == comp:
        let = comp_letter
        best = [-1, -infinity]
  else:
        let = human_letter
        best = [-1, +infinity]

  if depth == 0 or game_over(board,comp_letter,human_letter):
        score = evaluate(board,comp_letter,human_letter)
        return [-1,  score]

  for move in empty_spaces(board):
        pos = move
        board = insert_letter(let,pos,board)
        score = minimax(board, depth - 1, -player, comp_letter, human_letter)
        board = insert_letter('',pos,board)
        score[0] = pos

        if player == comp:
            if score[1] > best[1]:
                best = score
        else:
            if score[1] < best[1]:
                best = score

  return best
def select_letter():
    '''
    Function to prompt to user if it picks X's or O's to play
    '''
    run = True
    while run:
        select_letter = input("Do you want to be Xs or Os? (X/O)")
        if select_letter == 'X':
            human_letter = 'X'
            comp_letter = 'O'
            run = False
        elif select_letter == 'O':
            human_letter = 'O'
            comp_letter = 'X'
            run = False
        else:
            print('Incorrect value, please try again with O or X')

    return human_letter, comp_letter
def main():
    """
    A Main function that calls all functions
    """
    #First lets welcome and give some info
    print("Welcome to Tic Tac Toe by Ivan Flores Linares")
    print("The computers turn is generated with the minimax algorithm")
    print("Select a digit according to the following example to make your move")
    #Print a example board for user to understand how to play
    print_example_board()
    first= input("Do you want to go first? (Y/N)")
    print('-------------------')
    print('--- Game begins ---')
    print('-------------------')
    letters = select_letter()
    human_letter = letters[0]
    comp_letter = letters[1]
    board = create_board()
    print_board(board)
    #Loop through the players while the board is not full, or break if one player wins
    run = True
    while run:
        if first == 'Y':
            first_player = [player_move(board,human_letter), 'human', 'You win', human_letter]
            second_player = [comp_move(board,comp_letter,human_letter), 'comp', 'You lose', comp_letter]
        elif first == 'N':
            first_player = [comp_move(board,comp_letter,human_letter), 'comp', 'You lose', comp_letter]
            second_player =[player_move(board,human_letter), 'human', 'You win', human_letter]

        first_player[0]
        if isWinner(first_player[1], first_player[3], board):
            print(first_player[2])
            break
        second_player[0]
        if isWinner(second_player[1], second_player[3], board):
            print(second_player[2])
            break
        if is_board_full(board):
            run = False
    print('End of the game')
if __name__ == '__main__':
    main()
