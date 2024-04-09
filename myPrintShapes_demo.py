# import myPrintShapes
# myPrintShapes.draw_down_left_triangle()

from myPrintShapes import draw_down_left_triangle
# from myPrintShapes import *

def main():
    h = int(input('Высота'))
    j = str(input('Заливка'))

    draw_down_left_triangle(h,j)
if __name__ == '__main__':
    main()
