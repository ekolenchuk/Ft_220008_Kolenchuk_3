import sys


def find_path_bishop(x1, y1, x2, y2):
    x1_new = x1
    y1_new = y1
    while x1 < 8 and y1 < 8:
        x1_new = x1_new + 1
        y1_new = y1_new + 1
        if abs(x1_new - x2) != abs(y1_new - y2):
            continue
        else:
            return x1_new, y1_new

    while x1 < 8 and y1 > 1:
        x1_new = x1_new + 1
        y1_new = y1_new - 1
        if abs(x1_new - x2) != abs(y1_new - y2):
            continue
        else:
            return x1_new, y1_new

    while x1 > 1 and y1 > 1:
        x1_new = x1_new - 1
        y1_new = y1_new - 1
        if abs(x1_new - x2) != abs(y1_new - y2):
            continue
        else:
            return x1_new, y1_new

    while x1 > 1 and y1 < 8:
        x1_new = x1_new - 1
        y1_new = y1_new + 1
        if abs(x1_new - x2) != abs(y1_new - y2):
            continue
        else:
            return x1_new, y1_new


def find_path_knight(x1, y1, x2, y2):
    x1_new = x1
    y1_new = y1
    i = 1
    j = 2
    k = 1
    while 9 > y1 > 0 and 9 > x1 > 0 and 8 > k >= 1:
        x1_new = x1_new + i
        y1_new = y1_new + j
        dx = abs(x1_new - x2)
        dy = abs(y1_new - y2)
        if dx == 1 and dy == 2 or dx == 2 and dy == 1:
            return x1_new, y1_new
        elif k == 1:
            i = 2
            j = 1
            k = k + 1
            continue
        elif k == 2:
            i = -1
            j = -2
            k = k + 1
            continue
        elif k == 3:
            i = -2
            j = -1
            k = k + 1
            continue
        elif k == 4:
            i = 1
            j = -2
            k = k + 1
            continue
        elif k == 5:
            i = 2
            j = -1
            k = k + 1
            continue
        elif k == 6:
            i = -1
            j = 2
            k = k + 1
            continue
        elif k == 7:
            i = -2
            j = 1
            k = k + 1
            continue
    return [0, 0]


print(
    'Введите координаты первой фигуры'
    '\n[первое число — номер вертикали (при счете слева направо)] '
    '\n[второе число — номер горизонтали (при счете снизу вверх)]: '
)
x1 = int(input())
y1 = int(input())

print('Введите координаты второй фигуры:')
x2 = int(input())
y2 = int(input())

if x1 <= 0 or x2 <= 0 or y1 <= 0 or y2 <= 0 or x1 >= 9 or x2 >= 9 or y1 >= 9 or y2 >= 9:
    print('Введено число, выходящее из диапазона от 1 до 8')
    sys.exit(0)

# Одного цвета поля?
if (x1 + x2 + y1 + y2) % 2 == 0:
    print('Фигуры стоят на полях одного цвета')
    sim_colour = True
else:
    print('Фигуры стоят на полях разного цвета')
    sim_colour = False

# Угрожает первая вигура второму полю?
f = ''
while f != 'да':
    print('Ввести название фигуры? Да или Нет')
    f = input().lower()
    if f == 'нет':
        sys.exit(0)

danger = False
figure1 = ''
x1_new = int
y1_new = int
path = False
while f == 'да':
    print('Название первой фигуры (ферзь, ладья, слон или конь):')
    figure1 = input().lower()

    match figure1:
        case 'ферзь':
            if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
                danger = True
            else:
                x1_new = x2
                y1_new = y1
                path = True
            break
        case 'ладья':
            if x1 == x2 or y1 == y2:
                danger = True
            else:
                x1_new = x2
                y1_new = y1
                path = True
            break
        case 'слон':
            if abs(x1 - x2) == abs(y1 - y2):
                danger = True
            elif not sim_colour:
                path = False
            elif sim_colour:
                path = True
                new_cell = find_path_bishop(x1, y1, x2, y2)
                x1_new = new_cell[0]
                y1_new = new_cell[1]
            break
        case 'конь':
            dx = abs(x1 - x2)
            dy = abs(y1 - y2)
            if dx == 1 and dy == 2 or dx == 2 and dy == 1:
                danger = True
            else:
                new_cell = find_path_knight(x1, y1, x2, y2)
                if new_cell[0] == 0:
                    print('За два хода до поля не добраться')
                    break
                x1_new = new_cell[0]
                y1_new = new_cell[1]
                path = True
            break
        case _:
            print('Фигура не понятна. Ввести еще раз? Да или Нет')
            f = input().lower()
            if f == 'нет':
                sys.exit(0)
            else:
                continue

if not danger:
    print(f'{figure1} ({x1},{y1}) не угрожает полю ({x2},{y2})')
    if path:
        print(
            f'Можно попасть на поле за два хода через поле ({x1_new},{y1_new})'
        )
else:
    print(
        f'{figure1} ({x1},{y1}) угрожает полю ({x2},{y2}), '
        'на которое может попасть одним ходом.'
    )
