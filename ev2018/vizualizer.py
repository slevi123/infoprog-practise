from pathlib import Path
from tkinter import Tk, Label, Frame, Canvas

from PIL import Image
from PIL.ImageTk import PhotoImage

from ev2018.cell import Cell
from ev2018.field import Field
from ev2018.route_finder import RouteFinder


class Vizualizer(Canvas):
    BASE = Path("./given").resolve()

    def __init__(self, root):
        super().__init__(root, height=800, width=800, borderwidth=8, relief="solid")

        # getting the map
        Field.filder()
        self.terkep = Cell.get_map()
        # self.routes = # TODO: find the routes
        route_finder = RouteFinder(self.terkep)
        Cell.treasure_place = route_finder.treasure  # TODO: find the perfect place
        route_finder.legrovidebb_utovonal()
        route_finder.print_utvonal()

        self.treasure_place = Cell.treasure_place

        self.field_colors = {"ocean": "#050bb5",
                             "tenger": "#2436bd",
                             "part": "#e8d499",
                             "oserdo": "#0a4d00",
                             "sivatag": "#f5f4bc",
                             "hegy": "#adaaa3",
                             "to": "#8fc0f2",
                             "folyo": "#0574b5",
                             "mocsar": "#052e0b",
                             }
        self.field_font_colors = {"ocean": "#f5fcf6",
                             "tenger": "#f5fcf6",
                             "part": "#000000",
                             "oserdo": "#f5fcf6",
                             "sivatag": "#000000",
                             "hegy": "#000000",
                             "to": "#000000",
                             "folyo": "#f5fcf6",
                             "mocsar": "#f5fcf6",
                             }
        self.field_size = self.winfo_reqheight() // len(self.terkep)
        img = Image.open('./res/pic/treasure.png').resize((round(self.field_size*0.75), round(self.field_size*0.75)),
                                                          Image.ANTIALIAS)
        self.treasure_picture = PhotoImage(img)

        self.draw_field_colors()
        self.write_fields()
        self.draw_treasure()
        self.draw_grids()

    def draw_treasure(self):
        # X-version
        self.create_line(x := self.treasure_place.x*self.field_size, y := self.treasure_place.x*self.field_size,
                         x+self.field_size, y+self.field_size, fill='red', width=self.field_size//36)
        self.create_line(x := self.treasure_place.x*self.field_size,
                         self.treasure_place.x*self.field_size+self.field_size,
                         x+self.field_size, self.treasure_place.x*self.field_size, fill='red', width=self.field_size//36)

        # pic-version
        half = self.field_size // 2
        self.create_image(self.treasure_place.x*self.field_size+half, self.treasure_place.y*self.field_size+half,
                           image=self.treasure_picture)

    def draw_grids(self, color='black'):
        width = self.winfo_reqheight()
        height = self.winfo_reqwidth()
        for i in range(1, len(self.terkep)):
            self.create_line(0, i * self.field_size, width, i * self.field_size, fill=color)
            self.create_line(i * self.field_size, 0, i * self.field_size, height, fill=color)

    def draw_field_colors(self):
        for i, sor in enumerate(self.terkep):
            for j, cell in enumerate(sor):
                self.create_rectangle(i*self.field_size, j*self.field_size,
                                      (i+1)*self.field_size, (j+1)*self.field_size, fill=self.field_colors[cell.field.nev])

    def write_fields(self):
        half = self.field_size // 2
        betumeret = self.field_size // 6
        for i, sor in enumerate(self.terkep):
            for j, cell in enumerate(sor):
                self.create_text(i * self.field_size + half, j * self.field_size + half, text=cell.field.nev,
                                 fill=self.field_font_colors[cell.field.nev], font=("sans-sheriff", betumeret))


class BaseFrame(Frame):
    def __init__(self, root):
        super().__init__(root)
        Label(self, text='testing..').pack()
        Vizualizer(self).pack()


def start():
    root = Tk()
    BaseFrame(root).pack()
    root.mainloop()


if __name__ == "__main__":
    start()
