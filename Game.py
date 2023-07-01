print("Добро пожаловать в игру 'Крестики - Нолики'")

board = list(range(1, 10))
def board_pole(board):
    print('-'* 13)
    for i in range(3):
        print('|', board[0+i * 3], '|',  board[1 + i * 3], '|', board[2 + i * 3], '|')
        print('-' * 13)
def player_choice(player_latter):
    valid = False
    while not valid:
        player_number = input(f'В какую ячейку поставить {player_latter} ?')

        try:
            player_number = int(player_number)
        except:
            print('Неверный ход.Выберите число от 1 до 9.')
            continue
        if player_number >= 1 and player_number <=9:
            if(str(board[player_number -1]) not in "XO"):
                board[player_number - 1] = player_latter
                valid = True
            else:
                print('Здесь уже занято.')
        else:
            print('Неверный ход.Выберите число от 1 до 9.')

def check_winner(board):
    win_list = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    for each in win_list:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def game(board):
    counter = 0
    win = False
    while not win:
        board_pole(board)
        if counter % 2 == 0:
            player_choice("X")
        else:
            player_choice("0")
        counter += 1

        if counter > 4:
            fast_check = check_winner(board)
            if fast_check:
                print(f'{fast_check},Ты Победитель!')
                win = True
                break
        if counter == 9:
            print("Победила дружба!")
            break
    board_pole(board)
game(board)
check_winner(board)