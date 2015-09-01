__author__ = 'raven'

import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master, width=640, bg='blue')
        self.master = master
        self.count = 0
        self.pack()

        self.lb = tk.Label(self, text=str(self.count))
        self.lb.pack()

        self.pb = tk.Button(self, text="clicked", command=self.slot_clicked)
        self.pb.config()
        self.pb.pack()

    def init_ui(self):
        self.master.title('Hello')

    def slot_clicked(self):
        self.count += 1
        self.lb.config(text=str(self.count))



root = tk.Tk()

app = App(master=root)
app.mainloop()
root.destroy()
