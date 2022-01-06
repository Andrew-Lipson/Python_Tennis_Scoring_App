import Scoreboard
import Variable
import Set
import math


def player_names():
    Variable.player1['name'] = input("Player 1's name: ")
    Variable.player2['name'] = input("Player 2's name: ")


def initialise_match():
    player_names()
    while True:
        try:
            val = int(input("\nHow many sets(1,3,5): "))
            if val == 1 or val == 3 or val == 5:
                for x in range(val):
                    Variable.scores.append([0, 0])
                return val
            print("\nPlease enter either '1', '3' or '5'. ")
        except ValueError:
            print("\nPlease enter either '1', '3' or '5'. ")


def start_match():
    number_of_sets = initialise_match()
    Scoreboard.initialise_scoreboard()
    target = math.ceil(number_of_sets / 2)
    sets_won = [0,0]
    for x in range(number_of_sets):
        player_number = Set.a_set(x)
        sets_won[player_number] += 1
        if sets_won[player_number] == target:
            end_match(player_number)
            return


def end_match(player_number):
    Scoreboard.set_scoreboard()
    Scoreboard.scoreboard_print(["", ""])
    output = "Contratulations "
    if "Ryan" in Variable.player1['name'] or "Ryan" in Variable.player2['name']:
        output += "Ryan"
    elif Variable.player1['number'] == player_number:
        output += Variable.player1['name']
    else:
        output += Variable.player2['name']
    output += "!"
    print(output)

start_match()
