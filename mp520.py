"""
Compute the value brought by a given move by placing a new token for player
at (row, column). The value is the number of opponent pieces getting flipped
by the move. 

A move is valid if for the player, the location specified by (row, column) is
(1) empty and (2) will cause some pieces from the other player to flip. The
return value for the function should be the number of pieces hat will be moved.
If the move is not valid, then the value 0 (zero) should be returned. Note
here that row and column both start with index 0. 
"""

from collections import deque
import copy

def get_opponent(player):
    if player == 'B':
        return 'W'
    else:
        return 'B'

def get_move_value(state, player, row, column):
    flipped = 0
    # Your implementation goes here

    row_max = len(state)
    col_max = len(state[0])

    if column + 2 < col_max and state[row][column+2] == player and state[row][column+1] == get_opponent(player):
        flipped += 1

    if column - 2 >= 0 and state[row][column-2] == player and state[row][column-1] == get_opponent(player):
        flipped += 1

    if row + 2 < row_max and state[row+2][column] == player and state[row+1][column] == get_opponent(player):
        flipped += 1

    if row - 2 >= 0 and state[row-2][column] == player and state[row-1][column] == get_opponent(player):
        flipped += 1

    if column + 2 < col_max and row + 2 < row_max and state[row+2][column+2] == player and state[row+1][column+1] == get_opponent(player):
        flipped += 1

    if column - 2 >= 0 and row - 2 >= 0 and state[row-2][column-2] == player and state[row-1][column-1] == get_opponent(player):
        flipped += 1

    if column - 2 >= 0 and row + 2 < row_max and state[row+2][column-2] == player and state[row+1][column-1] == get_opponent(player):
        flipped += 1

    if column + 2 < col_max and row - 2 >= 0 and state[row-2][column+2] == player and state[row-1][column+1] == get_opponent(player):
        flipped += 1

    return flipped


"""
Execute a move that updates the state. A new state should be crated. The move
must be valid. Note that the new state should be a clone of the old state and
in particular, should not share memory with the old state. 
"""


def execute_move(state, player, row, column):
    new_state = None
    # Your implementation goes here

    new_state = copy.deepcopy(state)
    row_max = len(state)
    col_max = len(state[0])

    if column + 2 < col_max and state[row][column+2] == player and state[row][column+1] == get_opponent(player):
        new_state[row][column+1] = player

    if column - 2 >= 0 and state[row][column-2] == player and state[row][column-1] == get_opponent(player):
        new_state[row][column-1] = player

    if row + 2 < row_max and state[row+2][column] == player and state[row+1][column] == get_opponent(player):
        new_state[row+1][column] = player

    if row - 2 >= 0 and state[row-2][column] == player and state[row-1][column] == get_opponent(player):
        new_state[row-1][column] = player

    if column + 2 < col_max and row + 2 < row_max and state[row+2][column+2] == player and state[row+1][column+1] == get_opponent(player):
        new_state[row+1][column+1] = player

    if column - 2 >= 0 and row - 2 >= 0 and state[row-2][column-2] == player and state[row-1][column-1] == get_opponent(player):
        new_state[row-1][column-1] = player

    if column - 2 >= 0 and row + 2 < row_max and state[row+2][column-2] == player and state[row+1][column-1] == get_opponent(player):
        new_state[row+1][column-1] = player

    if column + 2 < col_max and row - 2 >= 0 and state[row-2][column+2] == player and state[row-1][column+1] == get_opponent(player):
        new_state[row-1][column+1] = player

    new_state[row][column] = player

    return new_state


"""
A method for counting the pieces owned by the two players for a given state. The
return value should be two tuple in the format of (blackpeices, white pieces), e.g.,

    return (4, 3)

"""


def count_pieces(state):
    blackpieces = 0
    whitepieces = 0
    # Your implementation goes here
    for i in range (0, len(state)):
        for j in range (0, len(state[0])):
            if(state[i][j] == 'B'):
                blackpieces += 1
            elif(state[i][j] == 'W'):
                whitepieces += 1

    return (blackpieces, whitepieces)


"""
Check whether a state is a terminal state. 
"""


def is_terminal_state(state, state_list=None):
    terminal = False
    # Your implementation goes here

    row_max = len(state)
    col_max = len(state[0])

    for row in range (0, len(state)):
        for column in range (0, len(state[0])):
            if(state[row][column] == ' '):
                if column + 2 < col_max and state[row][column+2] != ' ' and state[row][column+1] == get_opponent(state[row][column+2]):
                    # print('1')
                    return terminal

                if column - 2 >= 0 and state[row][column-2] != ' ' and state[row][column-1] == get_opponent(state[row][column-2]):
                    # print('2')
                    return terminal

                if row + 2 < row_max and state[row+2][column] != ' ' and state[row+1][column] == get_opponent(state[row+2][column]):
                    # print('3')
                    return terminal

                if row - 2 >= 0 and state[row-2][column] != ' ' and state[row-1][column] == get_opponent(state[row-2][column]):
                    # print('4')
                    return terminal

                if column + 2 < col_max and row + 2 < row_max and state[row+2][column+2] != ' ' and state[row+1][column+1] == get_opponent(state[row+2][column+2]):
                    # print('5')
                    return terminal

                if column - 2 >= 0 and row - 2 >= 0 and state[row-2][column-2] != ' ' and state[row-1][column-1] == get_opponent(state[row-2][column-2]):
                    # print('6')
                    return terminal

                if column - 2 >= 0 and row + 2 < row_max and state[row+2][column-2] != ' ' and state[row+1][column-1] == get_opponent(state[row+2][column-2]):
                    # print('7')
                    return terminal

                if column + 2 < col_max and row - 2 >= 0 and state[row-2][column+2] != ' ' and state[row-1][column+1] == get_opponent(state[row-2][column+2]):
                    # print('8')
                    return terminal

    return not terminal


"""
The minimax algorithm. Your implementation should return the best value for the
given state and player, as well as the next immediate move to take for the player. 
"""

def find_all_moves(state, player):
    row_max = len(state)
    col_max = len(state[0])
    moves = []

    for row in range (0, len(state)):
        for column in range (0, len(state[0])):
            if(state[row][column] == ' '):
                if ((column + 2 < col_max and state[row][column+2] == player and state[row][column+1] == get_opponent(player)) or
                (column - 2 >= 0 and state[row][column-2] == player and state[row][column-1] == get_opponent(player)) or
                (row + 2 < row_max and state[row+2][column] == player and state[row+1][column] == get_opponent(player)) or
                (row - 2 >= 0 and state[row-2][column] == player and state[row-1][column] == get_opponent(player)) or
                (column + 2 < col_max and row + 2 < row_max and state[row+2][column+2] == player and state[row+1][column+1] == get_opponent(player)) or
                (column - 2 >= 0 and row - 2 >= 0 and state[row-2][column-2] == player and state[row-1][column-1] == get_opponent(player)) or
                (column - 2 >= 0 and row + 2 < row_max and state[row+2][column-2] == player and state[row+1][column-1] == get_opponent(player)) or
                (column + 2 < col_max and row - 2 >= 0 and state[row-2][column+2] == player and state[row-1][column+1] == get_opponent(player))):

                    moves.append((row,column))

    return moves

def minimax(state, player):
    value = 0
    row = -1
    column = -1
    # Your implementation goes here

    (blackpieces, whitepieces) = count_pieces(state)
    value = blackpieces - whitepieces

    if is_terminal_state(state):
        return (value, row, column)
    
    best_move = (value, -1, -1)

    moves = find_all_moves(state, player)
    if not moves: # no available moves yet not terminal state
        moves.append((-1,-1))

    for move in moves:
        if move[0] != -1: # not a do-nothing move
            move_state = execute_move(state, player, move[0], move[1])
        else: # do-nothing move
            move_state = state

        move_value = minimax(move_state, get_opponent(player))
        if player == 'B' and move_value > best_move[0]:
            best_move = (move_value, move[0], move[1])
        elif player == 'W' and move_value < best_move[0]:
            best_move = (move_value, move[0], move[1])

    return best_move
    # return (value, row, column)



"""
This method should call the minimax algorithm to compute an optimal move sequence
that leads to an end game. 
"""


def full_minimax(state, player):
    value = 0
    move_sequence = []
    # Your implementation goes here

    (value, move_deque) = full_minimax_helper(state, player)
    move_sequence = list(move_deque)

    return (value, move_sequence)

def full_minimax_helper(state, player):

    (blackpieces, whitepieces) = count_pieces(state)
    board_value = blackpieces - whitepieces

    if is_terminal_state(state):
        move_deque = deque()
        move_deque.append((player, -1, -1))
        return (board_value, move_deque)
    
    if player == 'W':
        best_move = (999, -1, -1) # Using -999 for -infinity and 999 for +infinity
    else:
        best_move = (-999, -1, -1)

    moves = find_all_moves(state, player)
    if not moves: # no available moves for the player, yet not a terminal state
        moves.append((-1,-1))

    for move in moves:
        if move[0] != -1: # not a do-nothing move
            move_state = execute_move(state, player, move[0], move[1])
        else: # do-nothing move
            move_state = copy.deepcopy(state)

        (move_value, move_deque) = full_minimax_helper(move_state, get_opponent(player))
        if player == 'B' and move_value > best_move[0]:
            best_move = (move_value, move[0], move[1])
        elif player == 'W' and move_value < best_move[0]:
            best_move = (move_value, move[0], move[1])

    if(move[0] != -1): # add the move if it wasn't a do-nothing move
        move_deque.appendleft((player, move[0], move[1]))

    return (move_value, move_deque)

"""
The minimax algorithm with alpha-beta pruning. Your implementation should return the
best value for the given state and player, as well as the next immediate move to take
for the player. 
"""


def minimax_ab(state, player, alpha=-10000000, beta=10000000):
    value = 0
    row = -1
    column = -1
    # Your implementation goes here
    return (value, row, column)


"""
This method should call the minimax_ab algorithm to compute an optimal move sequence
that leads to an end game, using alpha-beta pruning.
"""


def full_minimax_ab(state, player):
    value = 0
    move_sequence = []
    # Your implementation goes here
    return (value, move_sequence)
