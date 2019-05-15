from Program.intro import intro
from Program.input_parser import input_parser
from Program.compressor import compressor
from Program.printer import printer
from Program.robo_browser import robo_browser
from Object.misc_data import ListAlbum


# This is what runs the program. It calls multiple methods from different files to do so.
user_object = intro()
album_list = ListAlbum()
input_parser(user_object, album_list)
album_object = compressor(album_list)
printer(album_object)
robo_browser(album_object, user_object)
