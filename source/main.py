def player_names():
    global p1_name
    global p2_name

    p1_name = input("Player 1's name: ")
    p2_name = input("Player 2's name: ")


def start_match():
    player_names()
    while True:
        try:
            val = int(input("\nHow many sets(1,3,5): "))
            if val == 1 or val == 3 or val == 5:
                return val
            print("\nPlease enter either '1', '3' or '5'. ")
        except ValueError:
            print("\nPlease enter either '1', '3' or '5'. ")


def user_input():
    while True:
        try:
            val = int(input("\nWho won the point:\n1. " + p1_name + "\n2. " + p2_name + "\n"))
            if val == 1 or val == 2:
                return val
            print("\nPlease enter either '1' or '2'. ")
        except ValueError:
            print("\nPlease enter either '1' or '2'. ")








number_of_sets = start_match()
user_input()
print(p1_name, p2_name, number_of_sets)

