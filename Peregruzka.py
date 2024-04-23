# Создайте новый класс Buiding
# Создайте инициализатор для класса Buiding, который будет задавать целочисленный атрибут этажности self.numberOfFloors
# и строковый атрибут self.buildingType
# Создайте(перегрузите) __eq__, используйте атрибут numberOfFloors и buildingType для сравнения

class Building:
    def __init__(self, numberOfFloors, buildingType):
        self.numberOfFloors = numberOfFloors
        self.buildingType = buildingType

    def __eq__(self, other):
        return self.numberOfFloors == other.numberOfFloors and self.buildingType == other.buildingType

# Пример использования класса:
building1 = Building(5, "office")
building2 = Building(5, "office")
building3 = Building(10, "residential")

# Проверка равенства
print(building1 == building2)  # Ожидаем получить True
print(building1 == building3)  # Ожидаем получить False
