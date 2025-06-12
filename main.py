from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

import time

url = "https://www.python.org/"
driver = webdriver.Chrome()

try:
    print("Opening Python page")
    driver.get(url)

    print("Checking Page title")
    assert "Python" in driver.title  # confirm that title has the word “Python” in it:
    print("Title word found")

    print("Finding Search box")
    elem = driver.find_element(By.NAME, "q")

    # Clear ssearch
    elem.clear()  # first clear any pre-populated text in the input field
    print("Typing pycon in search")
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    print("Search submitted")

    # Wait result to load
    time.sleep(3)

    # driver.page_source get the entire html code on the page
    if "No results found." in driver.page_source:
        print("No result found")
        driver.quit()
        exit()

    else:
        print("Result Found")

except Exception as e:
    print(e)

