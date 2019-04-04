from misc_data import website_list
from website_parser import *


def check_website(website, main_website_list):
    for x in main_website_list:
        if website == x:  # might need to change
            return website
        else:
            return False


def method_finder(website, link):
    if website == "discog":
        discogs_parser(link)
    else:
        return False


def input_parser(user_object):
    for x in user_object.user_website:
        if check_website(x, website_list):
            method_finder()  # might change
