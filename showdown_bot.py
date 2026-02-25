from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()

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

#wait for challenge  to load

#accept challenge

#intiate rng for team and move selection

#randomly select team

#randomly select moves until battle is over

driver.quit()