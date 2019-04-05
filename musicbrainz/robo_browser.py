from selenium import webdriver


def start():
    driver = webdriver.firefox
    login(driver)


def login(driver):
    # driver.get("https://musicbrainz.org/login?uri=%2F") # real one
    driver.get("https://test.musicbrainz.org/login?uri=%2F")
    element = driver.find_element_by_name("username")
    element.send_keys(input("Please type your username: "))
    element = driver.find_element_by_name("password")
    element.send_keys(input("Please type your password: "))
    element = driver.find_element_by_xpath("/html/body/div[2]/form/div[4]/span/button")
    element.click()

# def navigate_pg1():


def robo_browser(album):
    start()
