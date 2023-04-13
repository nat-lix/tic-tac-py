print("Добро пожаловать в игру!")

def show_matrix(m):
    num = '  0 1 2'
    print(num)
    for row, i in zip(m, num.split()):
        print(f"{i} {' '.join(str(j) for j in row)}")

def player_input(m,player):
    while True:
        place = input(f"Ваш ход {player}:").split()
        if len(place) != 2:
            print("Введите два значения координат через пробел")
            continue
        if not(place[0].isdigit() and place[1].isdigit()):
            print("Координаты должны быть числом")
            continue
        x, y = map(int, place)
        if not (x>=0 and x<3 and y>=0 and y<3):
            print("Введите числа от '0' до '2'")
            continue
        if m[x][y]!='_':
            print("Поле уже занято")
            continue
        break
    return x,y

def victory(m, player):
    v_coord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
               ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
               ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for coord in v_coord:
        symb = []
        for c in coord:
            symb.append(m[c[0]][c[1]])
        if symb == [player, player, player]:
            return True
    return False

def start(matrix):
    count = 0
    while True:
        show_matrix(matrix)
        if count%2 == 0:
            player = 'x'
        else:
            player = 'o'
        if count < 9:
            x, y = player_input(matrix, player)
            matrix[x][y] = player
        if count == 9:
            print("Tie! Победила дружба!")
            break
        if victory(matrix, player):
            print("Ура!", player, "победил!")
            break
        count += 1

matrix = [['_', '_', '_'],
         ['_', '_', '_'],
         ['_', '_', '_']]

start(matrix)

print("Игра завершена!")
