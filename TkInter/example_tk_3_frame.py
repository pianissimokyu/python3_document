__author__ = 'raven'

from PIL import Image, ImageTk
from tkinter import Tk, Label, BOTH, Frame


class Example(Frame):

    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()


    def initUI(self):
        self.parent.title("Absolute positioning")
        self.pack(fill=BOTH, expand=1)

        bard = Image.open("linux_256.jpg")
        bardejov = ImageTk.PhotoImage(bard)
        label1 = Label(self, image=bardejov)
        label1.image = bardejov
        label1.place(x=20, y=20)


def main():

    root = Tk()
    root.geometry("300x280+300+300")
    app = Example(root)
    root.mainloop()


if __name__ == '__main__':
    main()

