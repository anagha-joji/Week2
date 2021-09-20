import random
import numpy as np

def screen(choice):
    print("| {} | {} | {} |".format(choice[0][0], choice[0][1], choice[0][2]))
    print("| {} | {} | {} |".format(choice[1][0], choice[1][1], choice[1][2]))
    print("| {} | {} | {} | \n".format(choice[2][0], choice[2][1], choice[2][2]))

def compare(val, symbol):
    out_comes_row = [[0, 0, 0], [1, 1, 1], [2, 2, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 1, 2]]
    out_comes_col = [[0, 1, 2], [0, 1, 2], [0, 1, 2], [0, 0, 0], [1, 1, 1], [2, 2, 2], [0, 1, 2], [2, 1, 0]]
    for row, col in zip(out_comes_row, out_comes_col):
        if val[row[0]][col[0]] == val[row[1]][col[1]] == val[row[2]][col[2]] == symbol:
            return True
    return False

def play_game():
    his = [None] * 10
    flag = 0
    options = ["X", "O"]
    values = np.array([[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]])
    sample = ["00", "01", "02", "10", "11", "12", "20", "21", "22"]
    for i in range(0, 9):
        if i % 2 == 0:
            while True:
                try:
                    user = str(input("Now your turn, select a position :"))
                    if user in sample:
                        sample.remove(user)
                        values[int(user[0])][int(user[1])] = options[0]
                        screen(values)
                        his[i] = values.copy()
                        if compare(values, options[0]):
                            result = "User Won the Game"
                            print(result, "\n")
                            his[9] = result
                            flag = 1
                        break
                    else:
                        print("selected position is already occupied, select another position..")
                        continue
                except:
                    print("please Enter correct input :")
            if flag == 1:
                break
        else:
            print("Computer turn")
            computer = random.choice(sample)
            sample.remove(computer)
            values[int(computer[0])][int(computer[1])] = options[1]
            screen(values)
            his[i] = values.copy()
            if compare(values, options[1]):
                result = "Computer Won the Game"
                print(result, "\n")
                his[9] = result
                break
    if flag == 0:
        result = "Tie in Game"
        print(result)
        his[9] = result

    return his


# main part
game_rounds = 1
history = {}
while game_rounds <= 2:
    print("Game {}:".format(game_rounds))
    screen([["00", "01", "02"], ["10", "12", "13"], ["20", "21", "22"]])
    history[game_rounds] = play_game()
    game_rounds += 1

details = int(input("Are you want to see any round :"))
for key, value in history.items():
    if key == details:
        for element in range(len(value) - 1):
            if value[element] is not None:
                print("Move {} ({})".format(element + 1, "user" if element % 2 == 0 else "computer"))
                screen(value[element])
        print(value[-1])


