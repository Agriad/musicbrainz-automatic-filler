from tkinter import Tk, Label, Frame, Entry, StringVar


class Graphics:
    text1 = ""

    def __init__(self, tk):
        self.tk = tk
        self.frame = Frame(self.tk)
        self.frame.pack()
        self.initialize_interface()

    def initialize_interface(self):
        self.tk.title("MusicBrainz Automatic Filler")
        self.tk.geometry("800x600")

        Label(self.tk, text="Currently supports taking data from: ").pack()
        supports = read_support()
        Label(self.tk, text=supports, justify="left").pack()

        Label(self.tk, textvariable=self.text1)
        self.text_input()

    def text_input(self):
        self.text1 = StringVar()
        self.text1.set("")
        Label(self.tk, text="Link " + str(self.counter)).pack()
        self.text1.trace("w", lambda name, index, mode, text1=self.text1: self.callback(text1))
        entry = Entry(self.tk, textvariable=self.text1)

        entry.pack()

    def callback(self, something):
        s = something.get()
        print(s)
        if s:
            self.text_input()
        else:
            self.selfdestroy()


def gui():
    tk = Tk()
    graphics = Graphics(tk)

    tk.mainloop()


def read_support():
    file = open("/Users/Justin/Desktop/Games/Programming/Github/musicbrainz-automatic-filler/"
                "musicbrainz/Text/supports.txt",
                "r")
    content = file.read()
    return content
