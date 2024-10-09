class Unit:
    def __init__(self, name, pos_x, pos_y):
        self.name = name
        self.pos_x = pos_x
        self.pos_y = pos_y

    def in_area(self, x_1, y_1, x_2, y_2):
        if self.pos_x >= x_1 and self.pos_x <= x_2 and self.pos_y >= y_1 and self.pos_y <= y_2:
            return True
        return False


class Dragon(Unit):
    def __init__(self, name, pos_x, pos_y, fire_range):
        super().__init__(name, pos_x, pos_y)
        self.__fire_range = fire_range

    def breathe_fire(self, x, y, units):
        self.fire_blasted = []
        for unit in units:
            #print(self.__fire_range)
            if unit.in_area(x - self.__fire_range, y - self.__fire_range, x + self.__fire_range, y + self.__fire_range):
                print("#debug: I did this part!")
                self.fire_blasted.append(unit)
        return self.fire_blasted
            
