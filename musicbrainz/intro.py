from misc_data import UserInput


# Unused, was supposed to be possible to choose web browser.
def user_browser():
    print("Choose between:\nFirefox \nChrome")
    user_browser_input = input("Type here: ")
    return user_browser_input


# Takes in websites that is going to be parsed.
# In: website links
# out: string
def user_website():
    print("If you want to stop type \"\" or nothing or just press enter")
    user_website_input = input("Type here: ")
    return user_website_input


def check_credential(user):
    file = open("/Users/Justin/Desktop/Games/Programming/Github/musicbrainz-automatic-filler/musicbrainz/input.txt",
                "r")
    content = file.read()
    lines = content.split("\n")
    username = lines[0].split(":")
    username = username[1]
    username = username[1:len(username)]
    password = lines[1].split(":")
    password = password[1]
    password = password[1:len(password)]

    user.add_username(username)
    user.add_password(password)


def check_link(user):
    file = open("/Users/Justin/Desktop/Games/Programming/Github/musicbrainz-automatic-filler/musicbrainz/input.txt",
                "r")
    content = file.read()

    for lines in content.split("\n"):
        if lines != "" and lines[0] != "#" and "username:" not in lines and "password" not in lines:
            user.add_website(lines)


# The main part of the intro.
# Responsible for getting the user input and putting it into object.
# In: username, password, links to be scraped
# Out: UserInput object
def intro():
    # user_browser_input = user_browser()
    # this_user = UserInput(user_browser_input)
    this_user = UserInput("nothing")

    check_credential(this_user)

    if this_user.user_username == "":
        username = input("Musicbrainz username: ")
        this_user.add_username(username)
    if this_user.user_password == "":
        password = input("Musicbrainz password: ")
        this_user.add_password(password)

    check_link(this_user)

    if not this_user.user_websites:
        print("First input is given highest priority")
        user_website_input = user_website()

        while user_website_input != "":
            this_user.add_website(user_website_input)
            user_website_input = user_website()

    return this_user
