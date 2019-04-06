from tkinter import *


def browser(tk, user_input):
    button_firefox = Button(tk, text="Firefox", command=user_input.change_browser("Firefox"))
    button_chrome = Button(tk, text="Chrome", command=user_input.change_browser("Chrome"))
    button_firefox.pack()
    button_chrome.pack()


def done_button(tk, user_input):
    button_enter = Button(tk, text="Enter", command=done(user_input))
    button_enter.pack()


def done(user_input):
    return user_input


def gui(user_input):
    top = Tk()
    top.geometry("800x600")
    browser(top, user_input)
    done = done_button(top, user_input)

    top.mainloop()

