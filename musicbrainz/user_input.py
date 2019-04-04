from array import array


class UserInput:
    user_browser = ""
    user_websites = []

    def __init__(self, user_browser):
        self.user_browser = user_browser

    def add_website(self, website):
        self.user_websites.append(website)