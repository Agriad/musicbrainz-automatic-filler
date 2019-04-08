import requests
from bs4 import BeautifulSoup
import lxml


def diverse_title(soup):
    element = soup.find("div", {"class": "xfd_none"})
    title = element.find("h2")
    return title.string


def diverse_label(soup):
    element = soup.find("div", {"class": "cw clearfix"})
    label = element.find("a")
    return label.string


def diverse_cat(soup):
    element = soup.find("dl", {"class": "clearfix"})
    header = element.findAll("dt")
    info = element.findAll("dd")
    counter = 0

    for head in header:
        if "Model Number:" in head.string:
            return info[counter].string
        counter += 1

    return None


def diverse_date(soup):
    element = soup.find("dl", {"class": "clearfix"})
    header = element.findAll("dt")
    info = element.findAll("dd")
    final_date = []
    counter = 0

    for head in header:
        if "Release Date:" in head.string:
            date = info[counter].string
            date = date.split("/")
            final_date.append(date[2])
            final_date.append(date[1])
            final_date.append(date[0])
            return final_date
        counter += 1

    return None


def diverse_tracklist(data, album):
    soup = BeautifulSoup(data, "lxml")  # using lxml as the html is broken and causes issues
    element = soup.find("div", {"class": "left fl"})
    tracklist = element.findAll("tr")

    for songs in tracklist:
        info = songs.findAll("td")
        artist = info[2].string
        title = info[1].string
        title = title[2:len(title) - 2]
        album.add_song(artist, title, None)


def diverse_parser(link, album):
    r = requests.get(link)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")

    print(soup)

    album_title = diverse_title(soup)
    label = diverse_label(soup)
    cat_no = diverse_cat(soup)
    date = diverse_date(soup)

    album.add_title(album_title)
    album.add_label(label)
    album.add_cat(cat_no)
    album.add_date(date)

    diverse_tracklist(data, album)

    return album
