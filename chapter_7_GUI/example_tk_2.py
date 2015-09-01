__author__ = 'raven'
# 버튼을 클릭하면 라벨의 숫자가 올라감
import tkinter as tk

class App(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.count = 0

        self.pack()

        self.lb = tk.Label(self, text=str(self.count))
        self.lb.pack()

        self.pb = tk.Button(self, text="clicked", command=self.slot_clicked)
        self.pb.pack()


    def slot_clicked(self):
        self.count += 1
        self.lb.config(text=str(self.count))



root = tk.Tk()
# root.resizable(width=True, height=True)
# root.geometry('{}x{}'.format('640', '480'))
app = App(master=root)
app.mainloop()
root.destroy()
