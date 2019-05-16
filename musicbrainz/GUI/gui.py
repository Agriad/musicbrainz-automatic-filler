from tkinter import Tk, Label, Frame, Entry


class Graphics:
    counter = 1

    def __init__(self, tk, user_input):
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

        self.text_input()

    def text_input(self):
        Label(self.tk, text="Link " + str(self.counter)).pack()
        Entry(self.tk).pack()


def gui(user_input):
    tk = Tk()
    graphics = Graphics(tk, user_input)

    tk.mainloop()


def read_support():
    file = open("/Users/Justin/Desktop/Games/Programming/Github/musicbrainz-automatic-filler/"
                "musicbrainz/Text/supports.txt",
                "r")
    content = file.read()
    return content
