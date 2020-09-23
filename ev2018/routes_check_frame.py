from tkinter import IntVar
from tkinter.ttk import LabelFrame, Checkbutton


class RoutesCheckFrame(LabelFrame):
    def __init__(self, root, canvas):
        super().__init__(root, text="Utak:")
        self.legrovidebb_state = IntVar()
        self.legrovidebb_state.set(1)
        self.canvas = canvas
        Checkbutton(self, text="Legrövidebb", variable=self.legrovidebb_state, command=self.legrovidebb_cb).pack()

    def legrovidebb_cb(self):
        if self.legrovidebb_state.get():
            self.canvas.itemconfigure("legrovidebb", state='normal')
        else:
            self.canvas.itemconfigure("legrovidebb", state='hidden')
