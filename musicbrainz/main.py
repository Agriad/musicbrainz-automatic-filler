from intro import intro
from input_parser import input_parser
from printer import printer
from robo_browser import robo_browser

from misc_data import AlbumDataDone
from misc_data import UserInputDone

# user_object = intro()
# album_object = input_parser(user_object)

album_object = input_parser(UserInputDone)
printer(album_object)
# robo_browser(album_object, user_object)

# robo_browser(AlbumDataDone, UserInputDone(input("username "), input("password ")))
