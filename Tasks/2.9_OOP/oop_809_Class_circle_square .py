# 809
# Напишіть клас з назвою Circle для обчислення площі круга за введеним радіусом.
# Клас Circle має містити метод, який обчислює площу круга.
class Circle:
    '''Area of a circle'''
    def __init__(self, radius):
        self.r = radius

    def area_circle (self):
        return 3.14 * (self.r ** 2)

circle1 = Circle (3)
print(circle1.area_circle())
