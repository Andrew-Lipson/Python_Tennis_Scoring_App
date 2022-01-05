import Scoreboard


global player1_name
global player2_name


def who_won_the_point():
    while True:
        try:
            val = int(input("\nWho won the point:\n1. " + player1_name + "\n2. " + player2_name + "\n"))
            if val == 1 or val == 2:
                return val-1
            print("\nPlease enter either '1' or '2'. ")
        except ValueError:
            print("\nPlease enter either '1' or '2'. ")


def a_game(set_scoreboard):
    Scoreboard.scoreboard_print(set_scoreboard, ["", ""])
    points_won = [0, 0]
    while True:
        points_won[who_won_the_point()] += 1
        game_over, player = won_the_game(points_won)
        if game_over:
            return player
        else:
            game_score = game_score_calculated(points_won)
            Scoreboard.scoreboard_print(set_scoreboard, game_score)


def won_the_game(points_won):
    for x in range(2):
        y = (x+1) % 2
        if points_won[x] > 3:
            if (points_won[x]-points_won[y]) > 1:
                return True, x
    return False, 0


def game_score_calculated(points_won):
    game_score = ["0", "0"]
    if points_won[0]+points_won[1] < 6:
        for x in range(2):
            if points_won[x] == 0:
                game_score[x] = "0"
            elif points_won[x] == 1:
                game_score[x] = "15"
            elif points_won[x] == 2:
                game_score[x] = "30"
            elif points_won[x] == 3:
                game_score[x] = "40"
    else:
        if points_won[0] > points_won[1]:
            game_score = ["Ad", ""]
        elif points_won[0] < points_won[1]:
            game_score = ["", "Ad"]
        elif points_won[0] == points_won[1]:
            game_score = ["40", "40"]

    return game_score
