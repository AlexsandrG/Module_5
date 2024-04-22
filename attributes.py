# Создайте новый класс House
# Задайте ему новый атрибут numberOfFloors = 10
# В цикле пройдитесь по атрибуту numberOfFloors
# и распечайте значение "Текущий этаж равен"
# Полученный код напишите в ответ к домашему заданию

class House:

    def __init__(self):
        self.numberOfFloors = 10

    def floors_(self):
        for floor in range(1, self.numberOfFloors+1):
            print('Текущий этаж равен', floor)


house = House()
house.floors_()