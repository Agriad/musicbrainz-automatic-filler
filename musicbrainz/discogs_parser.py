import requests
from bs4 import BeautifulSoup
from misc_data import AlbumData


def music_object_maker(artist, title, length, album):
    array_length = len(title)

    for x in range(0, array_length):
        album.add_song(artist[x], title[x], length[x])

    return album


def discogs_artist_parser(artist):
    final_artist = ""
    new_artist = artist.findAll("a")
    counter = 0

    for text in new_artist:
        counter += 1

        if counter > 1:
            final_artist += " and "

        new_text = text.string
        final_artist += new_text

    return final_artist


def discogs_title_parser(title):
    try:
        new_title = title.find("span", {"class": "tracklist_track_title"}).string
    except AttributeError:
        return None
    return new_title


def discogs_length_parser(length):
    new_length = length.find("span").string
    return new_length


def discogs_album_parser(artist_list, title_list, length_list):
    array_length = len(artist_list)
    modified_artist = []
    modified_title = []
    modified_length = []

    for x in range(0, array_length):
        modified_artist.append(discogs_artist_parser(artist_list[x]))
        modified_title.append(discogs_title_parser(title_list[x]))
        modified_length.append(discogs_length_parser(length_list[x]))

    return [modified_artist, modified_title, modified_length]


def discogs_check_null(artist, title):
    if artist == [] or title == []:
        return False
    else:
        return True


def discogs_single_artist_parser(soup):
    profile = soup.find("h1", {"id": "profile_title"})
    artist = profile.find("a").string
    return artist


def discogs_single_title_parser(soup):
    playlist = soup.find("table", {"class": "playlist"})
    titles = playlist.findAll("a")
    return titles


def discogs_single_album_parser(artist_list, title_list, length_list):
    array_length = len(title_list)
    modified_artist = []
    modified_title = []
    modified_length = []

    for x in range(0, array_length):
        modified_artist.append(artist_list)
        modified_title.append(discogs_title_parser(title_list[x]))
        modified_length.append(discogs_length_parser(length_list[x]))

    return [modified_artist, modified_title, modified_length]


def discogs_title(soup):
    profile = soup.find("h1", {"id": "profile_title"})
    title = profile.findAll("span")
    title = title[2].string.split("\n")
    title = title[1]
    title = title[44:len(title)]
    return title


def discogs_lable(soup):
    profile = soup.find("div", {"class": "profile"})
    lable = profile.findAll("div")

    for x in range(0, len(lable)):
        try:
            if "Label" in lable[x].string:
                out = lable[x + 1].find("a")
                return out.string
        except TypeError:
            continue

    return None


def discogs_cat(soup):
    profile = soup.find("div", {"class": "profile"})
    cat = profile.findAll("div")

    for x in range(0, len(cat)):
        try:
            if "Label" in cat[x].string:
                out = cat[x + 1].find("a").next_sibling.string
                out = out.split("\n")
                out = out[0]
                out = out[4:len(out)]
                return out
        except TypeError:
            continue

    return None


def discogs_country(soup):
    profile = soup.find("div", {"class": "profile"})
    country = profile.findAll("div")

    for x in range(0, len(country)):
        try:
            if "Country" in country[x].string:
                out = country[x + 1].find("a").string
                out = out.split("\n")
                out = out[1]
                out = out[16:len(out)]
                return out
        except TypeError:
            continue

    return None


def discogs_date(soup):
    profile = soup.find("div", {"class": "profile"})
    date = profile.findAll("div")

    for x in range(0, len(date)):
        try:
            if "Released" in date[x].string:
                out = date[x + 1].find("a")
                out = out.string.split("\n")
                out = out[1]
                out = out[16:len(out)]
                return out.split(" ")
            elif "Year" in date[x].string:
                out = date[x + 1].find("a")
                return [out.string]
        except TypeError:
            continue

    return None


def discogs_parser(link):  # change a bit to make it more modular
    r = requests.get(link)
    data = r.text
    soup = BeautifulSoup(data, "html.parser")

    # print(soup)

    album_title = discogs_title(soup)
    label = discogs_lable(soup)
    cat_no = discogs_cat(soup)
    country = discogs_country(soup)
    date = discogs_date(soup)

    album = AlbumData()
    album.add_title(album_title)
    album.add_label(label)
    album.add_cat(cat_no)
    album.add_country(country)
    album.add_date(date)

    artist_list = soup.findAll("td", {"class": "tracklist_track_artists"})
    title_list = soup.findAll("td", {"class": "track tracklist_track_title mini_playlist_track_has_artist"})
    length_list = soup.findAll("td", {"class": "tracklist_track_duration"})

    album_as_text = discogs_album_parser(artist_list, title_list, length_list)

    if discogs_check_null(album_as_text[0], album_as_text[1]):
        album = music_object_maker(album_as_text[0], album_as_text[1], album_as_text[2], album)
        return album
    else:
        artist = discogs_single_artist_parser(soup)
        title_list = discogs_single_title_parser(soup)

        album_as_text = discogs_single_album_parser(artist, title_list, length_list)

        album = music_object_maker(album_as_text[0], album_as_text[1], album_as_text[2], album)
        return album


