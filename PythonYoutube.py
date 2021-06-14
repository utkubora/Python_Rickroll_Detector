from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as expect
from selenium.webdriver.common.keys import Keys
import time
from random import randint

class YoutubeCommentFounder():
    def __init__(self,link):
        self.link = link

    def delay(self,n):
        time.sleep(randint(2, n))

    def CommentGetter(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument("--headless")

        driver = webdriver.Chrome()
        driver.get(self.link)
        wait_a_minute = WebDriverWait(driver, 600)
        driver.maximize_window()
        print("enter " + driver.title)
        self.delay(5)

        SCROLL_PAUSE_TIME = 2
        CYCLES = 12
        html = driver.find_element_by_tag_name('html')
        html.send_keys(Keys.PAGE_DOWN)
        html.send_keys(Keys.PAGE_DOWN)
        time.sleep(SCROLL_PAUSE_TIME * 3)
        for i in range(CYCLES):
            html.send_keys(Keys.END)
            time.sleep(SCROLL_PAUSE_TIME)
        comment_elems = driver.find_elements_by_xpath('//*[@id="content-text"]')


        all_comments = [elem.text for elem in comment_elems]

        final = False
        for i in all_comments:
            b = str(i).lower()
            if "rickroll" in b or "rick" in b or "astley" in b or "rolled" in b or "rikrolling" in b:
                final = True
        return final








