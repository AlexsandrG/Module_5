class House:
    def __init__(self):
        self.numberOffloors = 0

    def setNewNumberOfFloors(self, floors):
        self.numberOffloors = floors
        print(f'Количество этажей стало - {floors}')


house = House()
print(f'Было количество этажей - {house.numberOffloors}')
house.setNewNumberOfFloors(3)

