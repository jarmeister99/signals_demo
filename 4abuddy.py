from tkinter import *


class ResizingCanvas(Canvas):
    def __init__(self, parent, **kwargs):
        Canvas.__init__(self, parent, **kwargs)
        self.bind("<Configure>", self.on_resize)
        self.height = self.winfo_reqheight()
        self.width = self.winfo_reqwidth()

    def on_resize(self, event):
        # determine the ratio of old width/height to new width/height
        wscale = float(event.width) / self.width
        hscale = float(event.height) / self.height
        # resize the canvas
        self.config(width=self.width, height=self.height)
        # rescale all the objects tagged with the "all" tag
        self.scale("all", 0, 0, wscale, hscale)


class App(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.build_widgets()

    def build_widgets(self):
        self.control_panel = Frame(self, bg='grey')
        self.control_panel.pack(side=LEFT, fill=Y)
        self.build_control_panel()

        self.canvas = ResizingCanvas(self, highlightthickness=0)
        self.canvas.pack(side=RIGHT, fill=BOTH, expand=1)

    def build_control_panel(self):
        label = Label(self.control_panel, text='Demo Controls')
        label.pack(fill=X)



if __name__ == '__main__':
    app = App()
    app.mainloop()
