from math import inf

from ev2018.decoder import Decoder
from ev2018.field import Field
from ev2018.route_finder import RouteFinder


class Cell:
    fields = Field.filder()
    terkep = []  # get_map(cls)
    terkep_meret = 0
    treasure_place = None

    def __init__(self, field, x, y):
        self.field = field
        self.x, self.y = x, y

        self.g_cost = inf
        self.h_cost = inf
        self.parent = None

    @property
    def f_cost(self):
        return self.g_cost + self.h_cost

    def __repr__(self):
        return f"Cell: {self.field.nev} x.y:({self.x}, {self.y})"

    @classmethod
    def get_map(cls):
        sima_terkep = Decoder().decode()
        terkep = [[] for _ in range(len(sima_terkep))]
        for i, sor in enumerate(sima_terkep):
            for j, field_name in enumerate(sor):
                terkep[i].append(
                    Cell(cls.fields[field_name], i, j)
                )

        cls.terkep = terkep
        cls.terkep_meret = len(terkep)
        # print('tm', cls.terkep_meret)
        return terkep

    def __lt__(self, other):
        return self.f_cost < other.f_cost

    def init_costs(self):
        self.g_cost = inf
        self.h_cost = abs(self.__class__.treasure_place.x - self.x) + abs(self.__class__.treasure_place.y - self.y)
        # print(self.h_cost)

    def get_neighbours(self):
        coords = ((self.x-1, self.y), (self.x+1, self.y), (self.x, self.y-1), (self.x, self.y+1))
        # print(coords)
        # print(self.terkep_meret)
        x = [self.terkep[coord[0]][coord[1]] for coord in coords if
                coord[0] in range(self.terkep_meret) and
                coord[1] in range(self.terkep_meret)]
        # print('return... ', x)
        return x
