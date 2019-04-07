from misc_data import AlbumData
from discogs_parser import discogs_parser
from tanoc_parser import tanoc_parser


# def check_website(website, main_website_list):
#     for x in main_website_list:
#         if x in website:  # might need to change
#             return website
#     return False


def method_finder(link, album):
    if "www.discogs.com" in link:
        return discogs_parser(link, album)
    elif "www.tanocstore.net" in link:
        return tanoc_parser(link, album)
    else:
        return False


# def input_parser(user_object):
#     for websites in user_object.user_websites:
#         if check_website(websites, website_list):
#             return method_finder(websites)  # might change


def input_parser(user_object, album_list):
    for websites in user_object.user_websites:
        album_list.add_album(method_finder(websites, AlbumData()))
