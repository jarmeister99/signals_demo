import math
from tkinter import *

from util import X_AXIS_TICKS, X_AXIS_UNIT, Y_AXIS_TICKS, X_AXIS_TICK_LABEL_FREQ, \
    Y_AXIS_TICK_LABEL_FREQ, Y_AXIS_UNIT, DEFAULT_GRID_HEIGHT, DEFAULT_GRID_WIDTH


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
        self.init_logic()
        self.build_widgets()

    def init_logic(self):
        self.amp_max = DEFAULT_GRID_HEIGHT
        self.time_max = DEFAULT_GRID_WIDTH

    def build_widgets(self):
        self.control_panel = Frame(self, borderwidth=1, relief='raised')
        self.control_panel.pack(side=LEFT, fill=Y)
        self.build_control_panel()

        self.canvas = ResizingCanvas(self, bg='grey88', highlightthickness=0)
        self.canvas.pack(side=RIGHT, fill=BOTH, expand=1)
        self.setup_canvas()

    def build_control_panel(self):
        control_panel_label = Label(self.control_panel, text='DEMO CONTROLS')
        control_panel_label.pack(fill=X)

        time_entry = Frame(self.control_panel)
        time_entry.pack(fill=X)

        time_entry_label = Label(time_entry, text='Max Time')
        time_entry_label.pack(side=LEFT)

        time_entry_val = StringVar(time_entry)
        self.time_input = time_entry_val
        time_entry_field = Entry(time_entry, textvariable=time_entry_val)
        time_entry_field.pack(side=LEFT)

        time_entry_button = Button(time_entry, text='Enter', command=self.time_entry_button_handler)
        time_entry_button.pack(side=LEFT)

        amplitude_entry = Frame(self.control_panel)
        amplitude_entry.pack(fill=X)

        amplitude_entry_label = Label(amplitude_entry, text='Max Amp')
        amplitude_entry_label.pack(side=LEFT)

        amplitude_entry_val = StringVar(amplitude_entry)
        self.amplitude_input = amplitude_entry_val
        amplitude_entry_field = Entry(amplitude_entry, textvariable=amplitude_entry_val)
        amplitude_entry_field.pack(side=LEFT)

        amplitude_entry_button = Button(amplitude_entry, text='Enter', command=self.amplitude_entry_button_handler)
        amplitude_entry_button.pack(side=LEFT)

    def time_entry_button_handler(self):
        time_max = self.time_input.get()
        if time_max.isnumeric() and float(time_max) > 0:
            self.time_max = round(float(time_max), 2)
            self.draw_axes()

    def amplitude_entry_button_handler(self):
        amplitude_max = self.amplitude_input.get()
        if amplitude_max.isnumeric() and float(amplitude_max) > 0:
            self.amp_max = round(float(amplitude_max), 2)
            self.draw_axes()

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
        x_space_units = (self.time_max / 2) / (X_AXIS_TICKS / 2)
        for i in range(1, int(X_AXIS_TICKS / 2) + 1):
            tick_x = (self.canvas.width / 2) + (i * x_space_pixels)
            negative_tick_x = (self.canvas.width / 2) - (i * x_space_pixels)
            x_val = round(i * x_space_units, 2)
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
        y_space_units = (self.amp_max / 2) / (Y_AXIS_TICKS / 2)
        for i in range(1, int(Y_AXIS_TICKS / 2) + 1):
            tick_y = (self.canvas.height / 2) - (i * y_space_pixels)
            negative_tick_y = (self.canvas.height / 2) + (i * y_space_pixels)
            y_val = round(i * y_space_units, 2)
            y_val = round(i * y_space_units, 2)
            tick_x_center = self.canvas.width / 2
            # axis ticks
            self.canvas.create_line((tick_x_center - 7, tick_y), (tick_x_center + 7, tick_y), fill='black', tag='axes')
            self.canvas.create_line((tick_x_center - 7, negative_tick_y), (tick_x_center + 7, negative_tick_y),
                                    fill='black', tag='axes')
            # tick labels
            if i % Y_AXIS_TICK_LABEL_FREQ == 0:
                self.canvas.create_text((tick_x_center - 25, tick_y), text=y_val, tag='axes')
                self.canvas.create_text((tick_x_center - 25, negative_tick_y), text=y_val * -1, tag='axes')
        y_axis_unit_x = (self.canvas.width / 2) + 10
        y_axis_unit_y = 10
        self.canvas.create_text((y_axis_unit_x, y_axis_unit_y), text=Y_AXIS_UNIT, tag='axes')

    def grid_scale_ratio(self):
        return self.canvas.width / self.time_max, self.canvas.height / self.amp_max


if __name__ == '__main__':
    app = App()
    app.mainloop()
