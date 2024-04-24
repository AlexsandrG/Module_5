# Создайте новый класс Buiding с атрибутом total
# Создайте инициализатор для класса Buiding, который будет увеличивать атрибут количества созданных объектов
# класса Building total (по примеру класса Lemming из урока)
# В цикле создайте 40 объектов класса Building и выведите их на экран командой print

class Building:
    total = 0

    def __init__(self):
        Building.total += 1


building = Building()
for i in range(41):
    new_building = Building()
    print(f'Вывод обьекта класса {new_building}')
