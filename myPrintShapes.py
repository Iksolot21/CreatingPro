# модуль для функций рисования в консоли

def draw_down_left_triangle(h, fill='*'):
    for i in range(1, h + 1):
        spaces = ' ' * (h - i)
        print(fill * i + spaces)
draw_down_left_triangle(5, fill='*')

print("Модуль draw_down_left_triangle - Загружен")

if __name__ == '__main__':
    print("Модуль draw_down_left_triangle - Главный")


