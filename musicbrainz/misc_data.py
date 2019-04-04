website_list = ["discogs"]


class UserInput:
    user_browser = ""
    user_websites = []

    def __init__(self, user_browser):
        self.user_browser = user_browser

    def add_website(self, website):
        self.user_websites.append(website)


class MusicData:
    artist = ""
    title = ""
    length = ""

    def __init__(self, artist, title, length):
        self.artist = artist
        self.title = title
        self.length = length


class AlbumData:
    songs = []

    # def __init__(self, artist, title, length):
    #     self.songs.append(MusicData(artist, title, length))

    def add_song(self, artist, title, length):
        self.songs.append(MusicData(artist, title, length))
