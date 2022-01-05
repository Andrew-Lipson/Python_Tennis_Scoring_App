def scoreboard_print(set_scores, game_scores):
    output = "\n"
    output += set_scores[0] + game_scores[0]
    output += "\n"
    output += set_scores[1] + game_scores[1]
    print(output)


def scoreboard_create(player, length):
    output = "|" + player['Name']
    for x in range(length - len(player['Name'])):
        output += " "
    for x in player['score']:
        output += "|"
        output += str(x)
    output += "|"
    return output


def scoreboard_main(player1, player2):
    p1_name = player1['Name']
    p2_name = player2['Name']

    if len(p1_name) > len(p2_name):
        length = len(p1_name)
    else:
        length = len(p2_name)

    output = "\n"
    output += scoreboard_create(player1, length)
    output += "\n"
    output += scoreboard_create(player2, length)
    return [scoreboard_create(player1, length), scoreboard_create(player2, length)]