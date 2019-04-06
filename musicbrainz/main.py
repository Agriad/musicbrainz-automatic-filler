from intro import intro
from input_parser import input_parser
from printer import printer
from robo_browser import robo_browser


# This is what runs the program. It calls multiple methods from different files to do so.
user_object = intro()
album_object = input_parser(user_object)
printer(album_object)
robo_browser(album_object, user_object)
