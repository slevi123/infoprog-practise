from tkinter import Tk, Label, Frame

from ev2018.map_frame import MapFrame
from ev2018.map_setting_frame import MapSettingFrame


class BaseFrame(Frame):
    def __init__(self, root):
        super().__init__(root)
        Label(self, text='testing..').pack()
        canvas = MapFrame(self)
        canvas.pack(side="left")
        MapSettingFrame(self, canvas).pack(side="right")


def start():
    root = Tk()
    root.title("Infoprog 2018: döntő - SL megoldás")
    BaseFrame(root).pack()
    root.mainloop()


if __name__ == "__main__":
    start()
