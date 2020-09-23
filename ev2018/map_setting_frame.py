from tkinter import Frame, IntVar
from tkinter.ttk import Checkbutton

from ev2018.kincs_check_frame import KincsCheckFrame
from ev2018.routes_check_frame import RoutesCheckFrame


class MapSettingFrame(Frame):
    def __init__(self, root, canvas):
        super().__init__(root)
        self.canvas = canvas

        self.field_names_state = IntVar()
        self.field_names_state.set(1)

        # FieldColorFrame

        Checkbutton(self, text="Mező nevek", variable=self.field_names_state, command=self.field_names_cb).pack()
        KincsCheckFrame(self, canvas).pack()
        RoutesCheckFrame(self, canvas).pack()

    def field_names_cb(self):
        if self.field_names_state.get():
            self.canvas.itemconfigure('field_name', state='normal')
        else:
            self.canvas.itemconfigure('field_name', state='hidden')
