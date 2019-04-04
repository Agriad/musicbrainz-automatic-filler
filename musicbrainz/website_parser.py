import requests
from bs4 import BeautifulSoup
from misc_data import AlbumData


def music_object_maker(artist, title, length):
    album = AlbumData
    array_length = len(title)

    for x in range(0, array_length):
        album.add_song(artist[x], title[x], length[x])

    return album


def discogs_parser(link): #change a bit to make it more modular
    r = requests.get(link)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")

    artist_list = soup.findAll("td", {"class": "tracklist_track_artists"})
    title_list = soup.findAll("td", {"class": "track tracklist_track_title mini_playlist_track_has_artist"})
    length_list = soup.findAll("td", {"class": "tracklist_track_duration"})

    album = music_object_maker(artist_list, title_list, length_list)

    return album
