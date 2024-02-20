
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
        #прямоугольник с признаком залития
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
        n = 10
        for i in range(n):
            for j in range(n):
                if i == j:  
                    print("*", end="")
                else:
                    print(" ", end="")
            print()
    case 12:
        print("Диагона змейка прот час стр")
        n = 10
        for i in range(n):
            for j in range(n):
                if i + j == n - 1:
                    print("*", end="") 
                else:
                    print(" ", end="")
            print()
    case 13:
        print("Вертикальная змейка")
        n = 10 
        for i in range(n):
            print("*" if i % 2 == 0 else " ")
    case 14:
        print("Горизонтальная змейка -н")
        n = 10
        for i in range(n): 
            print("* " * (i // 2) + " " * (n - i - 1))
    case 15:
        print("Вложенные прямоугольники -н")
        n = 10
        for i in range(n):
            print("*" * (n - i) + " " * i + " " * i + "*" * (n - i))
                
