import random


def draw_check(current_board, draw: bool = True):
    list = current_board[0] + current_board[1] + current_board[2]
    for element in list:
        if element == " ":
            draw = False
            break
    return draw



def wstaw_znak(current_board: list, koordynaty: str, znak: str):
    index_dict = {"a": 0, "b": 1, "c": 2}
    row_psition = koordynaty[1:]
    column_position = index_dict.get(koordynaty[:1])
    row1 = current_board[0]
    row2 = current_board[1]
    row3 = current_board[2]
    if row_psition == "1":
        if row1[column_position] == " ":
            row1[column_position] = znak
    elif row_psition == "2":
        if row2[column_position] == " ":
            row2[column_position] = znak
    elif row_psition == "3":
        if row3[column_position] == " ":
            row3[column_position] = znak
    else:  # jak poda błędny numer wiersza
        pass

    current_board = [row1, row2, row3]
    # sprawdzić czy dane pole jest dostępne, jak nie to dopytać o prawidłowe
    return current_board


def ai(current_board):
    return current_board


# ma zwracać pozycję którą AI wpisuje/zmodyfikowanego current board

def win_check(current_board, endgame: bool = False):
    # sprawdzanie po wierszach
    werifikator = row1[0] * 3
    werfikowana = row1[0] + row1[1] + row1[2]
    if werfikowana == werifikator and werifikator != "   ":
        endgame = True
    werifikator = row2[0] * 3
    werfikowana = row2[0] + row2[1] + row2[2]
    if werfikowana == werifikator and werifikator != "   ":
        endgame = True
    werifikator = row3[0] * 3
    werfikowana = row3[0] + row3[1] + row3[2]
    if werfikowana == werifikator and werifikator != "   ":
        endgame = True

    # sprawdzanie po kolumnach
    werifikator = row1[0] * 3
    werfikowana = row1[0] + row2[0] + row3[0]
    if werfikowana == werifikator and werifikator != "   ":
        endgame = True
    werifikator = row1[1] * 3
    werfikowana = row1[1] + row2[1] + row3[1]
    if werfikowana == werifikator and werifikator != "   ":
        endgame = True
    werifikator = row1[2] * 3
    werfikowana = row1[2] + row2[2] + row3[2]
    if werfikowana == werifikator and werifikator != "   ":
        endgame = True

    # sprawdzanie po przekątnych
    werifikator = row1[0] * 3
    werfikowana = row1[0] + row2[1] + row3[2]
    if werfikowana == werifikator and werifikator != "   ":
        endgame = True
    werifikator = row1[2] * 3
    werfikowana = row1[2] + row2[1] + row3[0]
    if werfikowana == werifikator and werifikator != "   ":
        endgame = True

    return endgame


def print_board(current_board):
    i_wierszowe = 1
    for row in current_board:
        print(i_wierszowe, end=" ")
        i_wierszowe += 1
        i_elementowe = 1
        for element in row:
            i_elementowe += 1
            print(element, end="")
            if i_elementowe < 4:
                print("|", end="")
        print()
    print("  A B C")


draw = False
endgame = False
krzyzyk = "x"
kolko = "o"
row1 = ["x", " ", "x"]
row2 = ["o", "o", "x"]
row3 = ["x", "x", "o"]
current_board = [row1, row2, row3]
znak = random.choice([krzyzyk, kolko])
zaczyna = random.randint(0, 1)
print_board(current_board)
print(f'Tym razem grasz: {znak}')

if zaczyna < 1:  # sprawdza kto zaczyna, graczy czy komp
    print('Pierwszy ruch robi AI')
    current_board = ai(current_board)
    print_board(current_board)
    endgame = win_check(current_board, endgame)
    draw = draw_check(current_board)
while endgame != True:
    koordynaty = input(f"Podaj koordynaty w których chcesz postawić {znak} np a1: ").lower()
    current_board = wstaw_znak(current_board, koordynaty, znak)
    print_board(current_board)
    endgame = win_check(current_board, endgame)
    draw = draw_check(current_board)

    print(endgame, draw)

    if endgame is True:
        print("Gratulacje Wygrałeś!!!")
        break
    else:
        current_board = ai(current_board)
        print_board(current_board)
        endgame = win_check(current_board)
        if endgame is True:
            print("Trudno, tym razem ci się nie udało")

endgame = win_check(current_board, endgame)
print(endgame)
