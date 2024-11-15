class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        return (
            self.pos_x >= x_1 and
            self.pos_x <= x_2 and
            self.pos_y >= y_1 and
            self.pos_y <= y_2
        )

class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        units_in_blast_range = []
        for unit in units:
            #print(f"x:{x},y:{y}")
            #print(f"unit.pos_x:{unit.pos_x}, unit.pos_y:{unit.pos_y}")
            #print(f"x - pos_x:{x - unit.pos_x}, y - pos_y:{y - unit.pos_y}")
            #print(f"x + pos_x:{x + unit.pos_x}, y + pos_y:{y + unit.pos_y}")
            if unit.in_area(x - self.__fire_range, y - self.__fire_range,
                            x + self.__fire_range, y + self.__fire_range):
                units_in_blast_range.append(unit)
        return units_in_blast_range

def main():
    sheep = Unit('sheep', 3, 2)
    knight = Unit('knight', 5, 5)
    villager = Unit('villager', 7, 7)
    smaug = Dragon('Smaug', 4, 4, 3)

    units = [sheep, knight, villager]

    print(f'Is in area: {sheep.in_area(1,1,4,4)}') # True

    print(f'Total units: {len(units)}\n')
    for unit in units:
        print(f'Unit name: {unit.name}, pos_x: {unit.pos_x}, pos_y: {unit.pos_y}')
    print(f"Units in blast range of Smaug fire breath:\n")

    for unit in smaug.breathe_fire(2,2,units):
        print(f'{unit.name}')

main()
