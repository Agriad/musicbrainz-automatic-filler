website_list = ["www.discogs.com"]


# Used to store user information and websites to parse.
class UserInput:
    user_browser = ""
    user_websites = []
    user_username = ""
    user_password = ""

    def __init__(self, user_browser):
        self.user_browser = user_browser

    def change_browser(self, browser):
        self.user_browser = browser

    def add_website(self, website):
        self.user_websites.append(website)

    def add_credentials(self, username, password):
        self.user_username = username
        self.user_password = password


# Used to store music information.
class MusicData:
    artist = ""
    title = ""
    length = ""

    def __init__(self, artist, title, length):
        self.artist = artist
        self.title = title
        self.length = length


# Used to store album information.
class AlbumData:
    artist = ""
    title = ""
    label = ""
    cat_no = ""
    country = ""
    date = []
    songs = []

    def __init__(self):
        self.songs = []

    def add_song(self, artist, title, length):
        self.songs.append(MusicData(artist, title, length))

    def add_artist(self, artist):
        self.artist = artist

    def add_title(self, title):
        self.title = title

    def add_label(self, label):
        self.label = label

    def add_cat(self, cat):
        self.cat_no = cat

    def add_country(self, country):
        self.country = country

    def add_date(self, date):
        self.date = date


# class AlbumDataDone:
#     songs = [MusicData("BOB", "a song", "9.99")]
#
#
# class UserInputDone:
#     user_browser = ""
#     user_websites = ["https://www.discogs.com/Various-The-Best-Of-Hardcore-TanoC/release/1030045"]
#     user_username = ""
#     user_password = ""
#
#     def __init__(self, username, password):
#         self.user_username = username
#         self.user_password = password
