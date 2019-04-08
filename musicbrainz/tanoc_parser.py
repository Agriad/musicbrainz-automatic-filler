import requests
from bs4 import BeautifulSoup


# Finds the album title.
# In: Beautifulsoup object
# Out: string
def tanoc_title(soup):
    element = soup.find("div", {"class": "detailr"})
    title = element.find("h2")
    return title.string


# Finds the label.
# In: Beautifulsoup object
# Out: string
def tanoc_label(soup):
    element = soup.find("div", {"class": "detailr"})
    label = element.find("span")
    return label.string.split(" / ")


# Finds the dics whick can contain multiple track list.
# In: Beautifulsoup object
# Out: string
def tanoc_disc(soup, album):
    element = soup.find("div", {"class": "detailf"})
    disc = element.findAll("table")

    for tracklist in disc:
        tanoc_tracklist(tracklist, album)


# Finds the track list and songs in it.
# In: Beautifulsoup object, AlbumData object
# Out:
def tanoc_tracklist(soup, album):
    song_list = soup.findAll("tr")

    for song in song_list:
        info = song.findAll("td")
        album.add_song(info[3].string, info[1].string, None)


# Parses the tanocstore link.
# In: string, AlbumData object
# Out: AlbumData object
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
