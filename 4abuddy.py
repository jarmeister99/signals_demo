import math
from tkinter import *

from util import GRID_WIDTH, GRID_HEIGHT, X_AXIS_TICKS


class ResizingCanvas(Canvas):
    def __init__(self, parent, **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        self.parent = parent
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self, event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width) / self.width
        hscale = float(event.height) / self.height
        self.width = self.winfo_width()
        self.height = self.winfo_height()
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all", 0, 0, wscale, hscale)
        self.parent.draw_axes()


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.build_widgets()

    def build_widgets(self):
        self.control_panel = Frame(self, borderwidth=1, relief='raised')
        self.control_panel.pack(side=LEFT, fill=Y)
        self.build_control_panel()

        self.canvas = ResizingCanvas(self, bg='grey88', highlightthickness=0)
        self.canvas.pack(side=RIGHT, fill=BOTH, expand=1)
        self.setup_canvas()

    def build_control_panel(self):
        label = Label(self.control_panel, text='DEMO CONTROLS')
        label.pack(fill=X)

    def setup_canvas(self):
        self.draw_axes()

    def draw_axes(self):
        self.canvas.delete('axes')
        self.canvas.create_line((0, (self.canvas.height / 2) - 1), (self.canvas.width, (self.canvas.height / 2) - 1),
                                fill='black', tag='axes', width=3)
        self.canvas.create_line(((self.canvas.width / 2) - 1, 0), ((self.canvas.width / 2) - 1, self.canvas.height),
                                fill='black', tag='axes', width=3)
        x_space_pixels = int((self.canvas.width / 2) / ((X_AXIS_TICKS / 2) + 1))
        for i in range(1, int(X_AXIS_TICKS / 2) + 1):
            tick_x = (self.canvas.width / 2) + (i * x_space_pixels)
            tick_y_center = self.canvas.height / 2
            self.canvas.create_line((tick_x, tick_y_center - 7), (tick_x, tick_y_center + 7), fill='black', tag='axes')
            tick_x = (self.canvas.width / 2) - (i * x_space_pixels)
            self.canvas.create_line((tick_x, tick_y_center - 7), (tick_x, tick_y_center + 7), fill='black', tag='axes')


    def grid_scale_ratio(self):
        return self.canvas.width, GRID_WIDTH, self.canvas.height / GRID_HEIGHT


if __name__ == '__main__':
    app = App()
    app.mainloop()
