

class RouteFinder:
    def __init__(self, terkep):
        self.terkep = terkep
        # print(self.find_mountains())
        self.treasure = self.find_treasure()

    def find_mountains(self):
        mountains = []
        for i, sor in enumerate(self.terkep):
            for j, field in enumerate(sor):
                if field.nev == "hegy":
                    mountains.append((i, j))
        return mountains

    def find_treasure(self):
        mountains = self.find_mountains()
        a = mountains[0]
        del mountains[0]
        for _ in range(len(mountains)):
            current = mountains.pop(0)
            if not self.is_paralell(*a, *current, *mountains[0], *mountains[1]):
                return self.find_middlepoint(*a, *current)
            mountains.append(current)
        raise ValueError("Can't find the treasure!")

    @staticmethod
    def is_paralell(xa, ya, xb, yb, xc, yc, xd, yd):
        try:
            return (yb-ya)/(xb-xa) == (yd-yc)/(xd-xc)
        except ZeroDivisionError:
            return True


    @staticmethod
    def find_middlepoint(xa, ya, xb, yb):
        x = round((xa + xb) / 2)
        y = round((ya + yb) / 2)
        return x, y
