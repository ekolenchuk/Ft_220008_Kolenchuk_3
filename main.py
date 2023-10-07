import sys

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
else:
    print('Фигуры стоят на полях разного цвета')

# Угрожает первая вигура второму полю?
f = ''
while f != 'да':
    print('Ввести название фигуры? Да или Нет')
    f = input().lower()
    if f == 'нет':
        sys.exit(0)

danger = False
figure1 = ''
while f == 'да':
    print('Название первой фигуры (ферзь, ладья, слон или конь):')
    figure1 = input().lower()

    match figure1:
        case 'ферзь':
            if abs(x1 - x2) == abs(y1 - y2) or x1 == x2 or y1 == y2:
                danger = True
            break
        case 'ладья':
            if x1 == x2 or y1 == y2:
                danger = True
            break
        case 'слон':
            if abs(x1 - x2) == abs(y1 - y2):
                danger = True
            break
        case 'конь':
            dx = abs(x1 - x2)
            dy = abs(y1 - y2)
            if dx == 1 and dy == 2 or dx == 2 and dy == 1:
                danger = True
            break
        case _:
            print('Фигура не понятна. Ввести еще раз? Да или Нет')
            f = input().lower()
            if f == 'нет':
                sys.exit(0)
            else:
                continue

if danger:
    print(
        f'{figure1} ({x1},{y1}) угрожает полю ({x2},{y2}), '
        'на которое может попасть одним ходом.'
    )
else:
    print(f'{figure1} ({x1},{y1}) не угрожает полю ({x2},{y2})')
