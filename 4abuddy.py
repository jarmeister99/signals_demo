import math
from tkinter import *

from util import GRID_WIDTH, GRID_HEIGHT, X_AXIS_TICKS, X_AXIS_UNIT, Y_AXIS_TICKS, X_AXIS_TICK_LABEL_FREQ, \
    Y_AXIS_TICK_LABEL_FREQ, Y_AXIS_UNIT


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

        # Populate x-axis
        x_space_pixels = int((self.canvas.width / 2) / ((X_AXIS_TICKS / 2) + 1))
        x_space_units = (GRID_WIDTH / 2) / (X_AXIS_TICKS / 2)
        print(x_space_units)
        for i in range(1, int(X_AXIS_TICKS / 2) + 1):
            tick_x = (self.canvas.width / 2) + (i * x_space_pixels)
            negative_tick_x = (self.canvas.width / 2) - (i * x_space_pixels)
            x_val = i * x_space_units
            tick_y_center = self.canvas.height / 2
            # axis ticks
            self.canvas.create_line((tick_x, tick_y_center - 7), (tick_x, tick_y_center + 7), fill='black', tag='axes')
            self.canvas.create_line((negative_tick_x, tick_y_center - 7), (negative_tick_x, tick_y_center + 7),
                                    fill='black', tag='axes')
            # grid-spanning ticks
            self.canvas.create_line((tick_x, 0), (tick_x, self.canvas.height), fill='grey67', tag='axes')
            self.canvas.create_line((negative_tick_x, 0), (negative_tick_x, self.canvas.height), fill='grey67',
                                    tag='axes')
            # tick labels
            if i % X_AXIS_TICK_LABEL_FREQ == 0:
                self.canvas.create_text((tick_x, tick_y_center + 15), text=x_val, tag='axes')
                self.canvas.create_text((negative_tick_x, tick_y_center + 15), text=x_val * -1, tag='axes')
        x_axis_unit_x = self.canvas.width - 10
        x_axis_unit_y = (self.canvas.height / 2) - 10
        self.canvas.create_text((x_axis_unit_x, x_axis_unit_y), text=X_AXIS_UNIT, tag='axes')

        # Populate y-axis
        y_space_pixels = int((self.canvas.height / 2) / ((Y_AXIS_TICKS / 2) + 1))
        y_space_units = (GRID_HEIGHT / 2) / (Y_AXIS_TICKS / 2)
        for i in range(1, int(Y_AXIS_TICKS / 2) + 1):
            tick_y = (self.canvas.height / 2) - (i * y_space_pixels)
            negative_tick_y = (self.canvas.height / 2) + (i * y_space_pixels)
            y_val = i * y_space_units
            tick_x_center = self.canvas.width / 2
            # axis ticks
            self.canvas.create_line((tick_x_center - 7, tick_y), (tick_x_center + 7, tick_y), fill='black', tag='axes')
            self.canvas.create_line((tick_x_center - 7, negative_tick_y), (tick_x_center + 7, negative_tick_y),
                                    fill='black', tag='axes')
            # tick labels
            if i % Y_AXIS_TICK_LABEL_FREQ == 0:
                self.canvas.create_text((tick_x_center - 20, tick_y), text=y_val, tag='axes')
                self.canvas.create_text((tick_x_center - 20, negative_tick_y), text=y_val * -1, tag='axes')
        y_axis_unit_x = (self.canvas.width / 2) + 10
        y_axis_unit_y = 10
        self.canvas.create_text((y_axis_unit_x, y_axis_unit_y), text=Y_AXIS_UNIT, tag='axes')

    def grid_scale_ratio(self):
        return self.canvas.width / GRID_WIDTH, self.canvas.height / GRID_HEIGHT


if __name__ == '__main__':
    app = App()
    app.mainloop()
