from gui import gui
from intro import intro
from input_parser import input_parser
from printer import printer
from robo_browser import robo_browser
from misc_data import UserInput

# gui = gui(UserInput("Firefox"))
user_object = intro()
album_object = input_parser(user_object)
printer(album_object)
robo_browser(album_object, user_object)
