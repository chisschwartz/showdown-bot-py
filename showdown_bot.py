from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.chrome.options import Options
import time

# chrome_options = Options()
# chrome_options.add_argument("--incognito")

# driver = webdriver.Chrome(options=chrome_options)

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

time.sleep(5)

#send challenge

find_user_button = driver.find_element(By.NAME, value="finduser")
find_user_button.click()

find_user_box = driver.find_element(By.NAME, value="data")
find_user_box.send_keys("Meow559")

find_user_submit = driver.find_element(By.CSS_SELECTOR, value="button[type='submit']")
find_user_submit.click()

find_user_challenge = driver.find_element(By.NAME, value="challenge")
find_user_challenge.click()

challenge_user = driver.find_element(By.NAME, value="makeChallenge")
challenge_user.click()

time.sleep(30)

moves = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.NAME, 'chooseMove'))
    )

# for move in moves:
#     print(move.get_attribute("value"))

move_1 = driver.find_element(By.XPATH, '/html/body/div[4]/div[5]/div/div[2]/div[2]/button[1]')
move_1.click()

time.sleep(30)
# try:
#     move_1 = WebDriverWait(driver, 120).until(
#         EC.visibility_of_element_located(By.NAME, "chooseMove")
#     )

#     move_1.click()

#     time.sleep(10)
    
# finally:

#intiate rng for team and move selection

#randomly select team

#randomly select moves until battle is over
 
driver.quit()