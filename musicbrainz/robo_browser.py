from selenium import webdriver
from selenium.webdriver.support.ui import Select


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


def browser_choice(user):
    choice = user.user_browser
    if choice == "Chrome" or "chrome":
        return None  # need to change
    else:
        return webdriver.Firefox(
            executable_path=
            "/Users/Justin/Desktop/Games/Programming/Github/musicbrainz-automatic-filler"
            "/musicbrainz/Driver/geckodriver")


def input_info(driver, album):
    input_title(driver, album.title)
    input_label(driver, album.label)
    input_cat(driver, album.cat_no)
    input_country(driver, album.country)
    input_date(driver, album.date)


def input_title(driver, title):
    element = driver.find_element_by_id("name")
    element.send_keys(title)


def input_label(driver, label):
    if label is not None:
        element = driver.find_element_by_id("label-0")
        element.send_keys(label)


def input_cat(driver, cat):
    if cat is not None:
        element = driver.find_element_by_id("catno-0")
        element.send_keys(cat)


def input_country(driver, country):
    if country is not None:
        element = driver.find_element_by_id("country-0")
        select = Select(element)
        select.select_by_visible_text(country)


def input_date(driver, date):
    if date is not None:
        input_day(driver, date)
        input_month(driver, date)
        input_year(driver, date)


def input_day(driver, date):
    if len(date) == 3:
        element = driver.find_element_by_xpath(
            "/html/body/div[4]/div[1]/div[1]/div[1]/fieldset[2]/table/tbody/tr[1]/td[2]/span/input[3]")
        element.send_keys(date[0])


def input_month(driver, date):
    element = driver.find_element_by_xpath(
        "/html/body/div[4]/div[1]/div[1]/div[1]/fieldset[2]/table/tbody/tr[1]/td[2]/span/input[2]")
    if len(date) == 2:
        if not isinstance(date[0], int):
            date[0] = translate_month(date[0])
        element.send_keys(date[0])
    elif len(date) == 3:
        if not isinstance(date[1], int):
            date[1] = translate_month(date[1])
        element.send_keys(date[1])


def input_year(driver, date):
    element = driver.find_element_by_id("event-date-0")
    if len(date) == 1:
        element.send_keys(date[0])
    elif len(date) == 2:
        element.send_keys(date[1])
    elif len(date) == 3:
        element.send_keys(date[2])


def translate_month(month):
    month = month.lower()
    if month in "january":
        return "01"
    elif month in "february":
        return "02"
    elif month in "march":
        return "03"
    elif month in "april":
        return "04"
    elif month == "may":
        return "05"
    elif month in "june":
        return "06"
    elif month in "july":
        return "07"
    elif month in "august":
        return "08"
    elif month in "september":
        return "09"
    elif month in "october":
        return "10"
    elif month in "november":
        return "11"
    else:
        return "12"


def robo_browser(album, user):
    driver = webdriver.Firefox(
        executable_path=
        "/Users/Justin/Desktop/Games/Programming/Github/musicbrainz-automatic-filler"
        "/musicbrainz/Driver/geckodriver")
    login(driver, user)
    navigate_home(driver)
    input_info(driver, album)
    input_tracklist(driver, album)
