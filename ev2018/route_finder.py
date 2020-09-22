from heapq import heappush, heappop, heapify


class RouteFinder:
    def __init__(self, terkep):
        self.terkep = terkep
        # print(self.find_mountains())
        self.treasure = self.find_treasure()
        self.terkep_meret = len(self.terkep)

    def init_cell_costs(self):
        for sor in self.terkep:
            for cell in sor:
                cell.neighbours = cell.get_neighbours()
                cell.init_costs()
        self.terkep[0][0].g_cost = 0

    def print_utvonal(self):
        current = self.treasure
        while True:
            # print(current.parent)
            print(f"{current.field.nev}: ({current.x}, {current.y})<--", end="")
            if current.parent is None:
                break
            else:
                current = current.parent

    def legrovidebb_utovonal(self):
        terkep_meret = len(self.terkep)
        self.init_cell_costs()
        open_list = [self.terkep[0][0]]
        closed_list = []
        while open_list:
            current = heappop(open_list)
            # print("current: ", current)
            if current is self.treasure:
                return True
            closed_list.append(current)
            # print(open_list, closed_list)
            heapify_needed = False
            # print('n', current.neighbours)
            for neighbour in current.neighbours:
                if neighbour not in closed_list:
                    if neighbour not in open_list:
                        neighbour.parent = current
                        neighbour.g_cost = current.g_cost + 1  # TODO 's
                        heappush(open_list, neighbour)
                    elif neighbour.g_cost < current.g_cost + 1:
                        heapify_needed = True
                        neighbour.g_cost = current.g_cost + 1
                        neighbour.parent = current
            if heapify_needed:
                heapify(open_list)
        return False

    def find_mountains(self):
        mountains = []
        for i, sor in enumerate(self.terkep):
            for j, cell in enumerate(sor):
                # print( cell.field.nev)
                if cell.field.nev == "hegy":
                    mountains.append(cell)
        # print(mountains)
        return mountains

    def find_treasure(self):
        mountains = self.find_mountains()
        a = mountains[0]
        del mountains[0]
        for _ in range(len(mountains)):
            current = mountains.pop(0)
            if not self.is_paralell(a, current, mountains[0], mountains[1]):
                return self.find_middlepoint(a, current)
            mountains.append(current)
        raise ValueError("Can't find the treasure!")

    @staticmethod
    def is_paralell(a, b, c, d):
        try:
            return (b.y-a.y)/(b.x-a.x) == (d.y-c.y)/(d.x-c.x)
        except ZeroDivisionError:
            return True

    def find_middlepoint(self, a, b):
        x = round((a.x + b.x) / 2)
        y = round((a.y + b.y) / 2)
        return self.terkep[x][y]
