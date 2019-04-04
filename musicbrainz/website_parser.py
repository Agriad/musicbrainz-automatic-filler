import requests
from bs4 import BeautifulSoup
from misc_data import AlbumData


def music_object_maker(artist, title, length):
    album = AlbumData
    array_length = len(title)

    # print(album.songs)

    for x in range(0, array_length):
        # print("artist")
        # print(artist[x])
        #
        # print("title")
        # print(title[x])
        #
        # print("length")
        # print(length[x])
        # print("\n")

       album.add_song(artist[x], title[x], length[x])

    return album

#def discog_artist_parser(artist):


def discog_title_parser(title):
    new_title = title.find("span", {"class": "tracklist_track_title"})
    return new_title


#def discog_length_parser(length):

def discog_album_parser(artist_list, title_list, length_list):
    array_length = len(artist_list)
    modified_artist = []
    modified_title = []
    modified_length = []

    for x in range(0, array_length):

        modified_title.append(discog_title_parser(title_list[x]))


    return [modified_artist, modified_title, modified_length]


def discogs_parser(link): # change a bit to make it more modular
    r = requests.get(link)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")

    artist_list = soup.findAll("td", {"class": "tracklist_track_artists"})
    title_list = soup.findAll("td", {"class": "track tracklist_track_title mini_playlist_track_has_artist"})
    length_list = soup.findAll("td", {"class": "tracklist_track_duration"})

    album_as_text = discog_album_parser(artist_list, title_list, length_list)

    album = music_object_maker(album_as_text[0], album_as_text[1], album_as_text[2])

    return album
