import random
import string
pencils = 0
players = ['John', 'Jack']
current_player = -1
possible_values = ['1', '2', '3']
while pencils == 0:
    pencil_input = input('How many pencils would you like to use:')
    if pencil_input[0] == "-":
        print('The number of pencils should be numeric')
    elif pencil_input == '0':
        print('The number of pencils should be positive;')
    else:
        try:
            pencils = int(pencil_input)
        except ValueError:
            print('The number of pencils should be numeric')
while current_player == -1:
    try:
        current_player = players.index(input('Who will be the first (John, Jack):'))
    except ValueError:
        print('Choose between John and Jack')
while pencils != 0:
    print('|' * pencils)
    print(f"{players[current_player]}'s turn:")
    if current_player == 0:
        pencils_taken = input()
        if pencils_taken in possible_values:
            if int(pencils_taken) > pencils:
                print('Too many pencils were taken')
            else:
                pencils -= int(pencils_taken)
                current_player = int(not current_player)
        else:
            print("Possible values: '1', '2' or '3'")
    elif pencils == 1:
        print("1")
        pencils -= 1
        current_player = int(not current_player)
    elif pencils % 4 == 0:
        print("3")
        pencils -= 3
        current_player = int(not current_player)
    elif pencils % 4 == 1:
        pencils_taken = random.randrange(2) + 1
        print(pencils_taken)
        pencils -= pencils_taken
        current_player = int(not current_player)
    elif pencils % 4 == 2:
        print("1")
        pencils -= 1
        current_player = int(not current_player)
    elif pencils % 4 == 3:
        print("2")
        pencils -= 2
        current_player = int(not current_player)

print(f'{players[current_player]} won!')
