import Variable


global player_name_board
player_name_board = ["", ""]


def scoreboard_print(game_scores):
    output = "\n"
    output += Variable.main_scoreboard[0] + game_scores[0]
    output += "\n"
    output += Variable.main_scoreboard[1] + game_scores[1]
    print(output)


def set_scoreboard2(player):
    output = ""
    output += player_name_board[player['number']-1]
    for x in player['score']:
        output += str(x)
        output += "|"
    return output


def set_scoreboard():
    Variable.main_scoreboard=[set_scoreboard2(Variable.player1), set_scoreboard2(Variable.player2)]


def create_name_board(player, length):
    output = "|" + player['Name']
    for x in range(length - len(player['Name'])):
        output += " "
    output += "|"
    player_name_board[player['number'] - 1] = output


def initialise_scoreboard():
    p1_name = Variable.player1['Name']
    p2_name = Variable.player1['Name']

    if len(p1_name) > len(p2_name):
        length = len(p1_name)
    else:
        length = len(p2_name)

    create_name_board(Variable.player1, length)
    create_name_board(Variable.player2, length)