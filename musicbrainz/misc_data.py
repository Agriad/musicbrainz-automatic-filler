website_list = ["www.discogs.com"]


class UserInput:
    user_browser = ""
    user_websites = []
    user_username = ""
    user_password = ""

    def __init__(self, user_browser):
        self.user_browser = user_browser

    def add_website(self, website):
        self.user_websites.append(website)

    def add_credentials(self, username, password):
        self.user_username = username
        self.user_password = password


class MusicData:
    artist = ""
    title = ""
    length = ""

    def __init__(self, artist, title, length):
        self.artist = artist
        self.title = title
        self.length = length


class AlbumData:
    title = ""
    label = ""
    cat_no = ""
    country = ""
    date = ""
    songs = []

    def __init__(self):
        self.songs = []

    def add_song(self, artist, title, length):
        self.songs.append(MusicData(artist, title, length))


class AlbumDataDone:
    songs = [MusicData("BOB", "a song", "9.99")]


class UserInputDone:
    user_browser = ""
    user_websites = ["https://www.discogs.com/Various-The-Best-Of-Hardcore-TanoC/release/1030045"]
    user_username = ""
    user_password = ""

    def __init__(self, username, password):
        self.user_username = username
        self.user_password = password
