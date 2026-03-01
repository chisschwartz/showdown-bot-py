from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.options import Options
import time

# chrome_options = Options()
# chrome_options.add_argument("--incognito")

# driver = webdriver.Chrome(options=chrome_options)

play = True

driver = webdriver.Firefox()

#grab website
driver.get("https://play.pokemonshowdown.com/")
# driver.get("https://china.psim.us/")

driver.implicitly_wait(5)

time.sleep(30)

#log in with user and pass

user_box_button = driver.find_element(By.NAME, value="login")
user_box_button.click()

text_box = driver.find_element(By.NAME, value="username")
text_box.send_keys("testing559")

text_box_submit = driver.find_element(By.CSS_SELECTOR, value="button[type='submit']")
text_box_submit.click()

# check_1 = input("Team ready?")

# if check_1 == "yes":
#     print("continuing")
# else:
#     driver.quit()

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

find_user_box = driver.find_element(By.NAME, value="message")
find_user_box.send_keys("/challenge gen9nationaldexdoublesubers @@@ pickedteamsize = 4")

# start_format_change = driver.find_element(By.NAME, value="format")
# start_format_change.click()

# change_format = driver.find_element(By.XPATH, '/html/body/div[4]/span/ul[1]/details[2]/li[1]/button')
# change_format.click()

# if check_2 == "yes":
#     print("continuing")


find_user_box.send_keys(Keys.ENTER)

challenge_user = driver.find_element(By.NAME, value="makeChallenge")
challenge_user.click()

time.sleep(15)

move_wait = WebDriverWait(driver, 300)
target_wait = WebDriverWait(driver, 30)

# timer = move_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[name='openTimer']")))
# timer.click()

while play == True:
    ran_num = random.randrange(1, 4)
    ran_target= random.randrange(1 , 2)
    ran_wait = random.randrange(5, 15)

    print(ran_num)
    print("target is", ran_target)

    # move_1 = driver.find_element(By.XPATH, f'/html/body/div[4]/div[5]/div/div[2]/div[2]/button[{ran_num}]')
    move_1 = move_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, f"button[name='chooseMove'][value='{ran_num}']")))
    # move_1 = driver.find_element(By.CSS_SELECTOR, value="button[name='chooseMove'][value='1']")
    move_1.click()

    # print (ran_wait)
    # time.sleep(ran_wait)

    # target_1 = driver.find_element(By.XPATH, f'/html/body/div[4]/div[5]/div/div[2]/button[{ran_target}]')
    
    # if ran_num >= 3:
    #     target_1 = target_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[name='chooseMoveTarget'][value='1']")))
    #     target_1.click()
    # else:
    #     target_1 = target_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[name='chooseMoveTarget'][value='2']")))
    # target_1 = driver.find_element(By.CSS_SELECTOR, value="button[name='chooseMoveTarget'][value='1']")
    # target_1.click()

    target_1 = target_wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "button[name='chooseMoveTarget'][value='1']")))
    target_1.click()

    # time.sleep(ran_wait)
    

    # if ran_num >= 3:
        
    #     WebDriverWait(driver, 20).until(
    #     EC.presence_of_all_elements_located((By.NAME, 'chooseMoveTarget')))

    #     target_1 = driver.find_element(By.XPATH, '/html/body/div[4]/div[5]/div/div[2]/button[1]')
    #     target_1.click()
        
    #     print(ran_wait)
    #     time.sleep(ran_wait)

    # if ran_num <= 2:
        # WebDriverWait(driver, 20).until(
        # EC.presence_of_all_elements_located((By.NAME, 'chooseMoveTarget')))

        # target_2 = driver.find_element(By.XPATH, '/html/body/div[4]/div[5]/div/div[2]/button[2]')
        # target_2.click()
        
        # print(ran_wait)
        # time.sleep(ran_wait)


#intiate rng for team and move selection

#randomly select moves until battle is over
 
# driver.quit()