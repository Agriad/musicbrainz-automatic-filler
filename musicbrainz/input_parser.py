from misc_data import website_list
from website_parser import *


def check_website(website, main_website_list):
    for x in main_website_list:
        if x in website:  # might need to change
            return website
    return False


def method_finder(link):
    if "www.discogs.com" in link:
        return discogs_parser(link)
    else:
        return False


def input_parser(user_object):
    for websites in user_object.user_websites:
        if check_website(websites, website_list):
            return method_finder(websites)  # might change
