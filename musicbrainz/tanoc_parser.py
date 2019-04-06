import requests
from bs4 import BeautifulSoup
from misc_data import AlbumData


def tanoc_title(soup):



def tanoc_parser(link):
    r = requests.get(link)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")

    print(soup)

    album_title = tanoc_title(soup)
    label = discogs_lable(soup)
    cat_no = discogs_cat(soup)
    country = discogs_country(soup)
    date = discogs_date(soup)
