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
    output += player_name_board[player['number']]
    for x in Variable.scores:
        output += str(x[player['number']])
        output += "|"
    return output


def set_scoreboard():
    Variable.main_scoreboard=[set_scoreboard2(Variable.player1), set_scoreboard2(Variable.player2)]


def create_name_board(player, length):
    output = "|" + player['name']
    for x in range(length - len(player['name'])):
        output += " "
    output += "|"
    player_name_board[player['number']] = output


def initialise_scoreboard():
    p1_name = Variable.player1['name']
    p2_name = Variable.player1['name']

    if len(p1_name) > len(p2_name):
        length = len(p1_name)
    else:
        length = len(p2_name)

    create_name_board(Variable.player1, length)
    create_name_board(Variable.player2, length)