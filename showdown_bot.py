from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

#grab website
driver.get("https://play.pokemonshowdown.com/")

driver.implicitly_wait(0.5)

# time.sleep(6)

#log in with user and pass

user_box_button = driver.find_element(By.NAME, value="login")
user_box_button.click()

text_box = driver.find_element(By.NAME, value="username")
text_box.send_keys("testing559")

text_box_submit = driver.find_element(By.CSS_SELECTOR, value="button[type='submit']")
text_box_submit.click()

time.sleep(3)

#send challenge

find_user_button = driver.find_element(By.NAME, value="finduser")
find_user_button.click()

find_user_box = driver.find_element(By.NAME, value="data")
find_user_box.send_keys("ChisBitz")

find_user_submit = driver.find_element(By.CSS_SELECTOR, value="button[type='submit']")
find_user_submit.click()

find_user_challenge = driver.find_element(By.NAME, value="challenge")
find_user_challenge.click()

challenge_user = driver.find_element(By.NAME, value="makeChallenge")
challenge_user.click()

time.sleep(10)

#intiate rng for team and move selection

#randomly select team

#randomly select moves until battle is over

driver.quit()