from misc_data import AlbumData
from discogs_parser import discogs_parser
from tanoc_parser import tanoc_parser
from diverse_parser import diverse_parser


# Finds the corresponding code for the links given.
# In: string, AlbumData object
# out: method, bool
def method_finder(link, album):
    if "www.discogs.com" in link:
        return discogs_parser(link, album)
    elif "www.tanocstore.net" in link:
        return tanoc_parser(link, album)
    elif "diverse.direct" in link:
        return diverse_parser(link, album)
    else:
        return False


# Takes the websites to be parsed and put the info into an object.
# In: UserInput object, ListAlbum object
# out:
def input_parser(user_object, album_list):
    for websites in user_object.user_websites:
        album_list.add_album(method_finder(websites, AlbumData()))
