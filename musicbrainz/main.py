from intro import intro
from input_parser import input_parser
from compressor import compressor
from printer import printer
from robo_browser import robo_browser
from misc_data import ListAlbum


# This is what runs the program. It calls multiple methods from different files to do so.
user_object = intro()
album_list = ListAlbum()
input_parser(user_object, album_list)
album_object = compressor(album_list)
printer(album_object)
robo_browser(album_object, user_object)
