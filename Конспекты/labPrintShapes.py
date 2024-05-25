
def print_rectangle(width: int, heights:int,symbol:bool):
    """нарисовать прямоугольник в консоли
    параметры: width: int, heights:int,symbol:bool
    """
x = 20
h = 5
s = 'a'
voit = int(input("Enter a number: "))
match voit:
    case 1:
        print('Прямоугольник')
        for r in range(h):

            print(s * x)
    case 2:
        print('Пустой прямоугольник')
        for r in range(h):
            if r == 0 or r == h - 1:
                print(f'{s * x}') 
            else:
                print(f'{s}{" " * (x - 2)}{s}')
    case 3:
        print('Равнобедренный прямоугольный треугольник по правому')
        kat = int(input("Длина катета: "))
        for i in range(kat, 0, -1):
            print(f'{"*" * i:>{kat}}')
    case 4:             
        print('Равнобедренный прямоугольный треугольник по левому краю')
        kat = int(input("Длина катета: "))
        for i in range(kat, 0, -1):
            print(f'{"*" * i:<{kat}}')
    case 5:
        print('Левый нижний угол треугольник')
        kat = int(input("Длина катета: "))
        for i in range(kat):
            print(f'{" " * i}{"*" * (kat - i)}')
    case 6:
        print("Правый нижний угол")
        kat = int(input("Длина катета: "))
        for i in range(kat):
            print(f'{" " * (kat - i)}{"*" * (i+1)}')
    case 7:
        print("Заполненный ромб")
        symbol = input("Введите символ: ")
        size = int(input("Размер ромба: "))
        for i in range(size):
            print(f'{" " * (size - i - 1)}{symbol * (i * 2 + 1)}')
        for i in range(size-2, -1, -1):
            print(f'{" " * (size - i - 1)}{symbol * (i * 2 + 1)}')
    case 8:
        print("Пустой ромб ")
        symbol = input("Введите символ: ")
        size = int(input("Размер ромба: "))
        for i in range(size):
            print(symbol * (size - i - 1)," " * (i * 2 + 1),symbol * (size - i - 1))
        for i in range(size-2, -1, -1):
            print(symbol * (size - i - 1)," " * (i * 2 + 1), symbol * (size - i - 1))      
    case 9:
        print("Песочные часы")
        rows = int(input("Введите число: "))
        k=0
        l=rows//2
        t=rows-3
        p=1
        y=1
        for i in range(rows, 0, -2):
            print(" "* k, str(t-k) * i) 
            k+=1 
        for i in range(1, rows+1,2): 
            print(" "*l , str(y) * i)
            y+=1
            l-=1

    case 10:
        print("Песочные часы из символов")
        rows = int(input("Введите число: "))
        k=0
        l=rows//2
        t=rows-3
        p=1
        y=1
        for i in range(rows, 0, -2):
            print(" "* k, '\\',' '*(i-1),'/') 
            k+=1 
        for i in range(1, rows+1,2): 
            print(" "*l , '/', ' '* (i-1),'\\')
            y+=1
            l-=1           
    case 11:
        print("Диаг змейка по час стр")
        size_of_snake = int(input('size_of_snake'))
        l=size_of_snake
        for i in range((size_of_snake//11)*2+1):
            if i%2 == 0:
                if size_of_snake < 10:
                    print(size_of_snake * '□')
                    break
                print(10 * '□')
                size_of_snake -=10
            if (i % 4 == 1):
                print(' ' * ((l - 2) % 10), '□')
                size_of_snake -= 1
            if (i%4==3):
                print('□')
                size_of_snake -=1
    case 12:
        print("Диаг змейка против час стр")
        size_of_snake = int(input('size_of_snake: '))
        l = size_of_snake

        for i in range((size_of_snake // 11) * 2 + 1):
            if i % 2 == 0:
                if size_of_snake <= 10:
                    print(' ' * (10 - size_of_snake) + size_of_snake * '□')
                    break
                print(' ' * (10 - 10) + 10 * '□')
                size_of_snake -= 10
            if i % 4 == 1:
                print('□')
                size_of_snake -= 1
            if i % 4 == 3:
                print(' ' * ((l - 2) % 10), '□')
                size_of_snake -= 1   
    case 13:
        print('вертикальная змейка')
        n, m = map(int, input().split())
        k=0
        for i in range(n*m):
            k+=1
            d = [['*' if (c % 2 != 0 and r == n - 1) or (c % 2 == 0 and (r != n - 1 or r % 2 == 0)) else ' ' for c in range(m)] for r in range(n)]
        for row in d:
            print(*row)
    case 14:
        print("Вложенные прямоугольники")
        w, h = map(int, input("Введите ширину и высоту внешнего прямоугольника: ").split())
        n = int(input("Введите количество вложенных прямоугольников: "))
        fill = input("Введите символ заполнения: ")
        print(fill * w)
        for i in range(h - 2):
            line = fill
            for j in range(w - 2):
                line += ' '
                for k in range(n):
                    if i >= k and i < h - 2 - k and j >= k and j < w - 2 - k:
                        line += ' '
                    else:
                        line += fill
            line += fill
            print(line)
        print(fill * w)


                
