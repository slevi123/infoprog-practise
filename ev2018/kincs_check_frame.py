from tkinter import IntVar
from tkinter.ttk import LabelFrame, Checkbutton


class KincsCheckFrame(LabelFrame):
    def __init__(self, root, canvas):
        super().__init__(root, text="Kincs helye")
        self.canvas = canvas
        self.lada = IntVar()
        self.x = IntVar()
        self.lada.set(1)
        self.x.set(1)
        Checkbutton(self, text="Láda", variable=self.lada, command=self.lada_cb).pack()
        Checkbutton(self, text="..X..", variable=self.x, command=self.x_cb).pack()

    def lada_cb(self):
        if self.lada.get():
            self.canvas.itemconfigure('lada', state='normal')
        else:
            self.canvas.itemconfigure('lada', state='hidden')

    def x_cb(self):
        if self.x.get():
            self.canvas.itemconfigure('x', state='normal')
        else:
            self.canvas.itemconfigure('x', state='hidden')
