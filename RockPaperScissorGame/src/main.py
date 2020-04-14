# Rock Paper Scissor Game
import random

__author__ = 'codinglukas'

# valid moves
MOVES = 'RPS'

# switch: two players or one player and AI
TWO_PLAYERS = False

# draws and wins for player 1 -> player 2 wins
# in all other cases
rules_dict = {
    # draws
    'SS': 0, 'RR': 0, 'PP': 0,
    # player 1 wins
    'SP': 1, 'RS': 1, 'PR': 1,
}

# the winners for each round go here
results = []


def get_move(player_id):
    """
    Reads the player's input until a valid move is played.

    :param player_id:
    :return: the move S, P or R
    """
    move = 'x'
    while move not in MOVES:
        move = input(f'Player {player_id} enter your move: ')
        move = move.upper()
    return move


def check_win(move_first_player, move_second_player):
    """
    Check who won the current round of the game.

    :param move_first_player:
    :param move_second_player:
    :return: winner id of the current round
    """
    current_game = move_first_player + move_second_player
    if current_game not in rules_dict:
        return 2
    else:
        return rules_dict.get(current_game)


def get_ai_move():
    """
    Get a random move for the AI. This is a very simple
    random strategy.
    The probabilities are: R => 3/6, P => 1/6, S => 2/6
    :return: the AI's move
    """
    weighted_strategy = ['S', 'R', 'R', 'P', 'R', 'S']
    move_idx = random.randint(0, len(weighted_strategy) - 1)
    return weighted_strategy[move_idx]


def print_total_winner():
    """
    After all rounds of the game finished, this function
    evaluates who won in total.
    :return: Winner id of the whole game
    """
    first_player_total = results.count(1)
    second_player_total = results.count(2)
    winner = 0

    if first_player_total == second_player_total:
        print('>>> The game ends with a draw!')
        return
    elif first_player_total > second_player_total:
        winner = 1
    else:
        winner = 2

    print(f'>>> Player {winner} wins it all!!!')


if __name__ == '__main__':
    while True:
        print('Input: R = Rock, P = Paper, S = Scissor')

        move_player_1 = get_move(1)
        if TWO_PLAYERS:
            move_player_2 = get_move(2)
        else:
            move_player_2 = get_ai_move()
            print(f'The AI (player 2) plays {move_player_2}')

        result = check_win(move_player_1, move_player_2)
        results.append(result)

        if result == 0:
            print(">>> It's a draw!")
        else:
            print(f'>>> Player {result} wins this time!')

        option = input('Hit x to stop, any other key to continue: ')
        if option == 'x':
            break
        print('------------------------------------------')

    print('Game ended')
    print('------------------------------------------')
    print_total_winner()

