from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
import os, time


USERNAME = "nft.phantasy"
PASSWORD = "chermondeco1"
SIMILAR_ACCOUNT = "nft.community"
HASHTAG = "dofaddicts"
HASHTAG_LIST = ["nftart", "nftcollection", "nftlovers"]
COMMENT = "Great post! Keep it up!"
MESSAGE = "Hey there! Nice profile :)"


class InstagramFollowersBot:
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path='/Users/joan//Downloads/chromedriver')
        self.driver.maximize_window()

    def Login(self):
        self.driver.get("https://www.instagram.com/accounts/login")
        self.driver.find_element(By.XPATH, "/html/body/div[4]/div/div/button[1]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input").send_keys(f"{USERNAME}")
        self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input").send_keys(f"{PASSWORD}")
        time.sleep(2.5)
        self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]/button").click()
        time.sleep(5)

    def find_Account(self):
        self.driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/div/div/div/button").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[3]/button[2]").click()
        time.sleep(3)

        self.driver.get(f"https://instagram.com/{SIMILAR_ACCOUNT}")
        self.driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a/div").click()


    def follow(self):
        div = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//div[@class='isgrP']")))
        start_index = 0
        def repeat(start_index):
            time.sleep(3)
            followers = self.driver.find_elements(By.CSS_SELECTOR, "li button")[start_index:start_index+7]
            for follower in followers:
                if follower.text =="Seguir":
                    follower.click()
                    time.sleep(2)
                    print("I Just followed")
                    if follower == followers[-1]:
                        self.driver.execute_script(f"arguments[0].scrollBy(0, {46 * 6})", div)
                        time.sleep(2)
                        print("Scrolled")
            start_index += 7
            print(start_index)
            if start_index > 48:
                print("ended loop")
                return "end"
            repeat(start_index)
        repeat(start_index)

    def like_posts(self):
        j=0
        for j in range(2):
            self.driver.get(f"https://www.instagram.com/explore/tags/{HASHTAG_LIST[j]}")
            time.sleep(2)
            #click most recent post
            self.driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div[1]/div[2]").click()
            time.sleep(2)
            #like
            i=0
            for i in range(3):
                self.driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[2]/section[1]/span[1]/button").click()
                time.sleep(2)
                self.driver.find_element(By.XPATH, "/html/body/div[6]/div[2]/div/div[2]/button").click()
                time.sleep(5)
                i+=1
            j+=1

    def send_pm(self):
        i=0
        for i in range(len(HASHTAG_LIST)):
            self.driver.get(f"https://www.instagram.com/explore/tags/{HASHTAG_LIST[i]}")
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/article/div[2]/div/div[1]/div[1]/a/div[1]/div[2]").click()
            time.sleep(2)
            #click profile
            self.driver.find_element(By.XPATH, "/html/body/div[6]/div[3]/div/article/div/div[2]/div/div/div[1]/div/header/div[2]/div[1]/div[1]/div").click()
            time.sleep(3)
            #click send message
            
            if self.driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/div/div[1]/button"):
                print("button found")
                self.driver.find_element(By.XPATH, "//*[@id='react-root']/section/main/div/header/section/div[1]/div[1]/div/div[1]/button").click()
                time.sleep(3)
                #notifications
                if i==0:
                    self.driver.find_element(By.XPATH, "/html/body/div[6]/div/div/div/div[3]/button[2]").click()
                #write and send message
                TEXTAREA = self.driver.find_element(By.XPATH, "//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")
                TEXTAREA.click()
                TEXTAREA.send_keys(f"{MESSAGE}")
                self.driver.find_element(By.XPATH, "//*[@id='react-root']/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
                i+=1
                print(i)
            else:
                send_pm(self)


bot = InstagramFollowersBot()
bot.Login()
bot.find_Account()
bot.follow()
#bot.like_posts()
#bot.send_pm()