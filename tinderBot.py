from selenium import webdriver
from time import sleep
import random

from secrets import username, password


class TinderBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://tinder.com')

        sleep(3)
        accept_cookies_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div/button')
        accept_cookies_btn.click()

        sleep(3)

        try:
            glogin_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/div[1]/div/button')
            glogin_btn.click()
        except Exception:
            glogin_btn = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/div/div/button')
            glogin_btn.click()
            pass

        sleep(2)
        # switch to login popup
        base_window = self.driver.window_handles[0]
        self.driver.switch_to.window(self.driver.window_handles[1])

        sleep(2)
        email_in = self.driver.find_element_by_xpath('//*[@id="identifierId"]')
        email_in.send_keys(username)

        gloginnext_btn = self.driver.find_element_by_xpath('//*[@id="identifierNext"]/span/span')
        gloginnext_btn.click()

        sleep(2)

        pw_in = self.driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input')
        pw_in.send_keys(password)

        passwordNext_btn = self.driver.find_element_by_xpath('//*[@id="passwordNext"]/span/span')
        passwordNext_btn.click()

        sleep(5)
        self.driver.switch_to.window(base_window)

        sleep(2)
        allow_location = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]/span')
        allow_location.click()

        sleep(2)
        block_notifications = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]/span')
        block_notifications.click()

        sleep(2)
        set_location_reject = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button/span')
        set_location_reject.click()

    def like(self):
        like_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[4]/button')
        like_btn.click()

    def dislike(self):
        dislike_btn = self.driver.find_element_by_xpath(
            '//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[2]/button')
        dislike_btn.click()

    def auto_swipe(self):
        while True:
            sleep(1)
            try:
                if random.choice([1, 2, 3, 4, 5]) > 2:
                    self.like()
                else:
                    self.dislike()
            except Exception:
                try:
                    self.close_popup()
                except Exception:
                    self.close_match()
                    continue

    def close_popup(self):
        popup_3 = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        popup_3.click()

    def close_match(self):
        match_popup = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        match_popup.click()

bot = TinderBot()
bot.login()
bot.auto_swipe()