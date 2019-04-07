import requests
from bs4 import BeautifulSoup
from misc_data import AlbumData


def tanoc_title(soup):
    element = soup.find("div", {"class": "detailr"})
    title = element.find("h2")
    return title.string


def tanoc_label(soup):
    element = soup.find("div", {"class": "detailr"})
    label = element.find("span")
    return label.string.split(" / ")


def tanoc_disc(soup, album):
    element = soup.find("div", {"class": "detailf"})
    disc = element.findAll("table")

    for tracklist in disc:
        tanoc_tracklist(tracklist, album)


def tanoc_tracklist(soup, album):
    song_list = soup.findAll("tr")

    for song in song_list:
        info = song.findAll("td")
        album.add_song(info[3].string, info[1].string, None)


def tanoc_parser(link, album):
    r = requests.get(link)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")

    print(soup)

    album_title = tanoc_title(soup)
    label_list = tanoc_label(soup)

    album.add_title(album_title)
    album.add_label(label_list[0])
    album.add_cat(label_list[1])

    tanoc_disc(soup, album)

    return album
