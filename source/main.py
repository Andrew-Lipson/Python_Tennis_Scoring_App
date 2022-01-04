def user_input():
    while True:
        try:
            val = int(input("Who won the point: "))
            if val == 1 or val == 2:
                return val
            print("Please enter either '1' or '2'. ")
        except ValueError:
            print("Please enter either '1' or '2'. ")

print(user_input())
