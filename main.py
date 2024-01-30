import time

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By


ACCOUNT = "name of the profile eg. michael_jordann_"
EMAIL = "instagram account email"
PASSWORD = "account password"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])


class InstaLikeClicker:
    def __init__(self):
        self.driver = webdriver.Chrome(options=chrome_options)

    def login(self):
        self.driver.get("https://instagram.com")

        time.sleep(3)
        cookies = self.driver.find_element(by=By.XPATH,
                                           value="/html/body/div[4]/div[1]/div/div[2]/div/div/div/div/div["
                                                 "2]/div/button[2]")
        cookies.click()

        time.sleep(2)
        email_input = self.driver.find_element(by=By.NAME, value="username")
        password_input = self.driver.find_element(by=By.NAME, value="password")
        login_button = self.driver.find_element(by=By.TAG_NAME, value="button")

        email_input.send_keys(EMAIL)
        password_input.send_keys(PASSWORD)
        login_button.click()
        time.sleep(5)
        save_prompt = self.driver.find_element(By.XPATH,
                                               value="//div[contains(text(), 'Not now')]")
        if save_prompt:
            save_prompt.click()

        time.sleep(2)
        notifications = self.driver.find_element(By.XPATH,
                                                 value="//button[contains(text(), 'Not now')]")
        if notifications:
            notifications.click()

    def like_posts(self):
        self.driver.get(f"https://instagram.com/{ACCOUNT}")
        time.sleep(5)
        posts = self.driver.find_elements(By.CLASS_NAME, value="_aagw")
        for post in posts:
            post.click()
            time.sleep(2)
            like = self.driver.find_element(By.CSS_SELECTOR, value="._aamw span")
            like.click()
            try:
                escape = self.driver.find_element(By.XPATH,
                                                  value='/html/body/div[7]/div[1]/div/div[2]/div/div')
            except selenium.common.exceptions.NoSuchElementException:
                escape = self.driver.find_element(By.XPATH,
                                                  value='/html/body/div[8]/div[1]/div/div[2]/div/div')
            escape.click()
            time.sleep(1)


like_clicker = InstaLikeClicker()
like_clicker.login()
like_clicker.like_posts()
