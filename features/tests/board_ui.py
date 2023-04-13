import time
import imagehash

from io import BytesIO
from selenium import webdriver
from PIL import Image
from selenium.webdriver.common.by import By
from selenium.webdriver.common import action_chains

from features.support.board_support_items import boardSupport
from features.support.locators import locators
from features.configuration.board_creation_conf import boadr_creation
from features.configuration.board_share_conf import share_board


boardSup = boardSupport()
driver = webdriver.Chrome()
driver.implicitly_wait(30)
locate = locators()

class ui_auto:
    ## Global Veriables
    response = ""


    def main_board(self):
        self.user_login(boardSup.main_url, boardSup.userA, boardSup.pass1)
        self.board_creation()
        self.response_validation('<Response [201]>')
        self.get_board()
        self.open_board(boardSup.board_name)
        self.button_click_plus()
        self.button_click_stickers()
        self.place_sticker_in_center()
        self.take_screenShot(boardSup.userA)
        self.share_board(boardSup.userB)
        self.response_validation('<Response [201]>')
        self.user_login(boardSup.main_url, boardSup.userB, boardSup.pass2)
        self.get_board()
        self.open_board(boardSup.board_name)
        self.take_screenShot(boardSup.userB)
        self.image_comparision(boardSup.userA, boardSup.userB)


    def user_login(self, pstr_url, pstr_user, pstr_pass):
        driver.maximize_window()
        driver.get(pstr_url)
        time.sleep(2)
        driver.find_element(By.XPATH, locate.email_xpath).clear()
        driver.find_element(By.XPATH, locate.email_xpath).send_keys(pstr_user)
        driver.find_element(By.XPATH, locate.pass_xpath).clear()
        driver.find_element(By.XPATH, locate.pass_xpath).send_keys(pstr_pass)
        driver.find_element(By.XPATH, locate.login_btn_xpath).click()
        time.sleep(2)



    def board_creation(self):
        self.response = boadr_creation(boardSup.board_name)
        print (self.response)

    def response_validation(self, responseCode):
        try:
            if str(self.response) == responseCode:
                assert True
            else:
                assert False
        except Exception as e:
            print("An Exception occurred:" + str(e))

    def get_board(self):
        time.sleep(60)
        driver.find_element(By.XPATH, locate.switchToDev_btn).click()

    def open_board(self, pstr_brdName):
        time.sleep(5)
        driver.find_element(By.XPATH, locate.open_board_xpath+pstr_brdName+'"])').click()
        time.sleep(30)

    def button_click_plus(self):
        time.sleep(10)
        driver.find_element(By.XPATH, locate.plus_btn_xpath).click()
        driver.find_element(By.XPATH, locate.stickerEmo_btn_xpath).click()

    def button_click_stickers(self):
        time.sleep(5)
        driver.find_element(By.XPATH, locate.sticker_btn_xpath).click()
        time.sleep(5)

    def place_sticker_in_center(self):
        hold_elem = driver.find_element(By.XPATH, locate.select_sticker_xpath)
        time.sleep(5)

        action = webdriver.common.action_chains.ActionChains(driver)


        action.click_and_hold(hold_elem)
        action.move_by_offset(500, 200)
        time.sleep(5)
        action.release().perform()
        time.sleep(30)

    def share_board(self, pstr_user):
        sharable_userId = self.get_user_id()
        self.response = share_board(sharable_userId, pstr_user)
        print (self.response)
        time.sleep(30)

    def get_user_id(self):
        sharable_userId = driver.current_url
        try:
            if sharable_userId.__contains__('https://miro.com/app/board/'):
                sharable_userId = sharable_userId.replace('https://miro.com/app/board/', "")
                sharable_userId = sharable_userId.replace(sharable_userId[len(sharable_userId) - 1], "")
                if sharable_userId[len(sharable_userId) - 1].__contains__('='):
                    sharable_userId = sharable_userId.replace(sharable_userId[len(sharable_userId) - 1],
                                                              "%3D")

            return sharable_userId
        except Exception as e:
           print ("An Exception occurred:" + str(e))


    def take_screenShot(self, pstr_fileName):
        png = driver.get_screenshot_as_png()
        im = Image.open(BytesIO(png))

        left = 600
        right = 1000
        top = 150
        bottom = 600
        im = im.crop((left, top, right, bottom))  # defines crop points
        im.save(boardSup.testdata+pstr_fileName+'.png')  # saves new cropped image

    def image_comparision(self,pstr_fileName1, pstr_fileName2):
        try:
            userA = (boardSup.testdata+pstr_fileName1+'.png')
            userB = (boardSup.testdata+pstr_fileName2+'.png')

            user1 = imagehash.average_hash(Image.open(userA))
            user2 = imagehash.average_hash(Image.open(userB))

            if (user1 == user2):
                print("Images are same")
                assert True
            else:
                print("Images are not same")
                assert False
        except Exception as e:
            print("An Exception occurred:" + str(e))

driver.close()


