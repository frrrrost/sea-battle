from random import randint


def make_board():  # формируем игровое поле
    board = []
    rows = 10
    columns = 10
    for row in range(rows):
        row = []
        for col in range(columns):
            row.append('0')
        board.append(row)
    return board


def no_ships(st_row, e_row, st_col, e_col, init_board):  # проверяем есть ли корабль на начальной стадии
    for i in range(st_row, e_row):
        for j in range(st_col, e_col):
            if init_board[i][j] == '1':
                return False
    return True


def display_board(field):  # Вывод графической части
    letters = ' АБВГДЕЖЗИК '
    letters = ' | '.join(letters)
    a = ''
    a += f"{' ' + letters}\n"
    a += f"{'-' * 44}\n"
    for i, row in enumerate(field):
        if i + 1 == 10:
            a += f"{i + 1} {'| ' + ' | '.join(row) + ' |'}\n"
            break
        a += f" {i + 1} {'| ' + ' | '.join(row) + ' |'}\n"
    return a


def place_ships(number_of_ships, size_of_ship, init_board):
    ships_coords = []
    temp_lst = []
    for i in range(number_of_ships):
        while True:
            st_row = randint(0, 9)
            st_col = randint(0, 9)
            direction = randint(0, 3)  # 0- up, 1 - down, 2 - right, 3 - left
            if direction == 0:
                if st_row - size_of_ship < 0:
                    st_row = randint(size_of_ship - 1, 9)
                if no_ships(st_row - size_of_ship if st_row - size_of_ship < 0 else 0, st_row + 2 if st_row < 9 else 10,
                            st_col - 1 if st_col > 0 else 0, st_col + 2 if st_col < 9 else 10,
                            init_board) is True:
                    e_row = st_row - size_of_ship
                    e_col = st_col + 1
                    for r in range(st_row, e_row, -1):
                        for c in range(st_col, e_col):
                            init_board[r][c] = '1'
                            temp_lst += [str(r) + str(c)]
                    ships_coords += [temp_lst]
                    temp_lst = []
                else:
                    continue
            if direction == 1:
                if st_row + size_of_ship > 10:
                    st_row = randint(0, 10 - size_of_ship)
                if no_ships(st_row - 1 if st_row > 0 else 0,
                            st_row + size_of_ship + 1 if st_row + size_of_ship < 10 else 10,
                            st_col - 1 if st_col > 0 else 0, st_col + 2 if st_col < 9 else 10,
                            init_board) is True:
                    e_row = st_row + size_of_ship
                    e_col = st_col + 1
                    for r in range(st_row, e_row):
                        for c in range(st_col, e_col):
                            init_board[r][c] = '1'
                            temp_lst += [str(r) + str(c)]
                    ships_coords += [temp_lst]
                    temp_lst = []
                else:
                    continue
            if direction == 2:
                if st_col + size_of_ship > 10:
                    st_col = randint(0, 10 - size_of_ship)
                if no_ships(st_row - 1 if st_row > 0 else 0, st_row + 2 if st_row < 9 else 10,
                            st_col - 1 if st_col > 0 else 0,
                            st_col + size_of_ship + 1 if st_col + size_of_ship < 10 else 10,
                            init_board) is True:
                    e_row = st_row + 1
                    e_col = st_col + size_of_ship
                    for r in range(st_row, e_row):
                        for c in range(st_col, e_col):
                            init_board[r][c] = '1'
                            temp_lst += [str(r) + str(c)]
                    ships_coords += [temp_lst]
                    temp_lst = []
                else:
                    continue
            if direction == 3:
                if st_col - size_of_ship < -1:
                    st_col = randint(size_of_ship - 1, 9)
                if no_ships(st_row - 1 if st_row > 0 else 0, st_row + 2 if st_row < 9 else 10,
                            st_col - size_of_ship if st_col - size_of_ship > 0 else 0, st_col + 2 if st_col < 9 else 10,
                            init_board) is True:
                    e_row = st_row + 1
                    e_col = st_col - size_of_ship
                    for r in range(st_row, e_row):
                        for c in range(st_col, e_col, -1):
                            init_board[r][c] = '1'
                            temp_lst += [str(r) + str(c)]
                    ships_coords += [temp_lst]
                    temp_lst = []
                else:
                    continue
            break
    return init_board, ships_coords


print('Добро пожаловать в морской бой!')
print('Правила игры в морской бой:\nНа поле 10*10 расставлены корабли: '
      '1 четырёхпалубный, 2 трёхпалубных, 3 двухпалубных и 4 однопалубных '
      'корабля.\nВам нужно найти их все.\nНеизвестное поле обозначается 0. '
      'Если Вы подбили корабль, то поле меняется на +, если Вы промахнулись, '
      'то поле поменяется на X\nЧтобы ввести координату корабля, сначала введите '
      'букву(выбранный столбец), а потом цифру(строку)\nПример: А3(либо а3)\nУдачи!')
initial_field = make_board()  # в этой переменной будут хранится сами кораблики
initial_field, l1 = place_ships(4, 1, initial_field)
initial_field, l2 = place_ships(3, 2, initial_field)
initial_field, l3 = place_ships(2, 3, initial_field)
initial_field, l4 = place_ships(1, 4, initial_field)
coords_of_ships = l1 + l2 + l3 + l4
guess_field = display_board(initial_field)  # В этой переменной будет графическая часть, которая видна пользователю
# print(guess_field[91:188])  # значения столбика А расположены в 97, 142, 187 (шаг 45)
# Тут нужно будет сдлеать графическую часть и рандомно расставить кораблики.
hits = 0  # Определять победителя можно через количество попаданий. Когда их будет 20, то игрок победил
moves_list = []  # Сюда записываются ходы игрока
letters_to_digits = {'А': 0, 'Б': 1, 'В': 2, 'Г': 3, 'Д': 4, 'Е': 5, 'Ж': 6, 'З': 7, 'И': 8, 'К': 9}
while True:  # этот цикл нужен, чтобы игрок делал ходы, пока корабли не закончатся
    print(guess_field)
    print(f'Введите клетку: ')
    p_move = input().upper()  # запрашиваем ход
    try:
        letter = p_move[0]  # берем из этого хода букву, то есть столбик атаки
        digit = int(p_move[1:])  # берем цифру хода, то есть строку атаки
    except ValueError:
        print('Вы ввели некорректные значения, попробуйте ещё раз')
        continue
    if letter not in 'АБВГДЕЖЗИК':
        print('Вы ввели некорректные значения, попробуйте ещё раз')
        continue
    if p_move in moves_list:
        print('Эта клетка уже подбита')
        continue
    moves_list.append(p_move)  # помещаем ход в список ходов
    if initial_field[digit - 1][letters_to_digits[letter]] == '1':
        coord = str(digit - 1) + str(letters_to_digits[letter])
        for i in range(len(coords_of_ships)):
            if coord in coords_of_ships[i]:
                coords_of_ships[i].remove(coord)
                if len(coords_of_ships[i]) == 0:
                    print('Убил')
                else:
                    print("Ранил")
        guess_field = guess_field[:(97 + (45 * (digit - 1)) + ((letters_to_digits[letter]) * 4))] + '+' + \
                      guess_field[(98 + (45 * (digit - 1)) + ((letters_to_digits[letter]) * 4)):]
        # нужно будет ещё заменять подбитые поля на что-нибудь и не давать сбивать эти поля ещё раз
        hits += 1
    else:
        print('Мимо')
        guess_field = guess_field[:(97 + (45 * (digit - 1)) + ((letters_to_digits[letter]) * 4))] + 'x' + \
                      guess_field[(98 + (45 * (digit - 1)) + ((letters_to_digits[letter]) * 4)):]
    if hits == 20:  # если игрок попал уже 20 раз (4 яруса * 1 + 3 яруса * 2...), то он выиграл
        print('Поздравляю! Вы прошли игру!')