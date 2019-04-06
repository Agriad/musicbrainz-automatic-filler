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


# The main part of the intro.
# Responsible for getting the user input and putting it into object.
# In: username, password, links to be scraped
# Out: UserInput object
def intro():
    # user_browser_input = user_browser()
    # this_user = UserInput(user_browser_input)
    this_user = UserInput("nothing")

    username = input("Musicbrainz username: ")
    password = input("Musicbrainz password: ")

    this_user.add_credentials(username, password)

    print("First input is given highest priority")
    user_website_input = user_website()

    while user_website_input != "":
        this_user.add_website(user_website_input)
        user_website_input = user_website()

    return this_user
