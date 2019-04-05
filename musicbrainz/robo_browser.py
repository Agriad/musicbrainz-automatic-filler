from selenium import webdriver


def login(driver, user):
    # driver.get("https://musicbrainz.org/login?uri=%2F")
    driver.get("https://test.musicbrainz.org/login?uri=%2F")  # test
    element = driver.find_element_by_name("username")
    element.send_keys(user.user_username)
    element = driver.find_element_by_name("password")
    element.send_keys(user.user_password)
    element = driver.find_element_by_xpath("/html/body/div[4]/form/div[4]/span")
    element.click()


def navigate_home(driver):
    driver.get("https://test.musicbrainz.org/release/add")  # test


# def input_release(driver, album):


def input_tracklist(driver, album):
    element = driver.find_element_by_xpath("/html/body/div[4]/div[1]/ul/li[3]")
    element.click()
    element = driver.find_element_by_xpath("/html/body/div[8]/div[2]/div[1]/textarea")
    counter = 1

    for music in album.songs:
        artist = music.artist
        title = music.title
        length = music.length

        if title is not None:
            if length is None:
                element.send_keys(str(counter) + " " + title + " - " + artist + "\n")
            else:
                element.send_keys(str(counter) + " " + title + " - " + artist + " (" + length + ")" + "\n")

        counter += 1

    # element = driver.find_element_by_id("parse-tracks")
    element = driver.find_element_by_xpath("/html/body/div[8]/div[2]/div[4]/button[2]")
    element.click()
    element = driver.find_element_by_id("format-unknown")
    element.click()


def robo_browser(album, user):
    driver = webdriver.Firefox(
        executable_path=
        "/Users/Justin/Desktop/Games/Programming/Github/musicbrainz-automatic-filler/musicbrainz/Driver/geckodriver")
    login(driver, user)
    navigate_home(driver)
    # input_release(driver)
    input_tracklist(driver, album)
