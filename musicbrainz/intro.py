from misc_data import UserInput


def user_browser():
    print("Choose between:\nFirefox \nChrome \nEdge")
    user_browser_input = input("Type here: ")
    return user_browser_input


def user_website():
    print("If you want to stop type \"end\"")
    user_website_input = input("Type here: ")
    return user_website_input


def intro():
    user_browser_input = user_browser()
    this_user = UserInput(user_browser_input)

    print("First input is given highest priority")
    user_website_input = user_website()

    while user_website_input != "end":
        this_user.add_website(user_website_input)
        user_website_input = user_website()

    # print(this_user.user_browser)
    # print(this_user.user_websites)

    return this_user
