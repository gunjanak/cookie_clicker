#Buy only Click in first minute
#Buy only Grandma in second minute 
#Buy only Farm in third minute to end
#Here we go to the website click cookie and only buy cursor for five minutes

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from bs4 import BeautifulSoup
import time
import math
import random
import numpy as np

Q = np.zeros((120, 3))
rewards = np.zeros(10)
learning_rate = 0.2
discount_factor = 0.99
episodes = 20
Q[100,0] = 10





#driver.find_element_by_name("Value").send_keys(Keys.RETURN)
options = Options()
options.BinaryLocation = "/usr/bin/chromium-browser"
#options.headless  = True

driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",options=options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(10)

link = driver.find_element(By.LINK_TEXT,"Got it!")
link.click()
time.sleep(10)


eng_lang = driver.find_element(By.ID,"langSelect-EN")
eng_lang.click()
time.sleep(10)


bigCookie = driver.find_element(By.ID,"bigCookie")
cookie_count = driver.find_element(By.ID,"cookies")

#cursor_click
productPrice0 = driver.find_element(By.ID,"productPrice0")
print(productPrice0.text)

#Grandma
productPrice1 = driver.find_element(By.ID,"productPrice1")
grandma_price = productPrice1.text
grandma_price = grandma_price.replace(",","")
print(grandma_price)

tic = time.time()
tok = time.time()

for i in range(episodes):
    print("episode: ",i)
    tic = time.time()
    tok = time.time()
    

    while(tok-tic < 10):
        current_time = math.floor(tok-tic)
        print("current time is %d" %current_time)
        bigCookie.click()
        count = int(cookie_count.text.split(" ")[0].replace(",",""))
        reward_prev = float(cookie_count.text.split(" ")[-1])
        print("Reward is ",reward_prev)
        # Generate a random number between 1 and 3
        random_number_n = random.randint(1, 10)
        if(random_number_n == 10):
            random_number = random.randint(0,2)
        else:
            random_number = np.argmax(Q[count])


        print(random_number)
        if(random_number == 1):
            if(count > int(productPrice0.text)):
                print('Buying cursor\n')
                actions2 = ActionChains(driver)
                actions2.move_to_element(productPrice0)
                actions2.click(productPrice0 )
                actions2.perform()
                reward = float(cookie_count.text.split(" ")[-1]) - reward_prev
                if(current_time < 119):
                    Q[count,1] = Q[count,1] + learning_rate*(reward+discount_factor*(np.max(Q[count+1])-Q[count,1]))
                else:
                    Q[count] = reward
            else:
                print("Cannot buy cursor\n")
                reward = float(cookie_count.text.split(" ")[-1])- reward_prev
                if(count < 119):
                    Q[count,2] = Q[count,2] + learning_rate*(reward+discount_factor*(np.max(Q[count+1])-Q[count,2]))
                else:
                    Q[current_time,2] = reward

            

            
        elif(random_number == 0):
            if(count > int(productPrice1.text.replace(",",""))):
                print('Buying grandma\n')
                actions2 = ActionChains(driver)
                actions2.move_to_element(productPrice1)
                actions2.click(productPrice1)
                actions2.perform()
                reward = float(cookie_count.text.split(" ")[-1]) - reward_prev
                if(count < 119):
                    Q[count,0] = Q[count,0] + learning_rate*(reward+discount_factor*(np.max(Q[count+1])-Q[count,0]))
                    print("After buying grandma\n")
                    print(Q[count,0])
                else:
                    Q[current_time] = reward
            else:
                print("Cannot buy Grandma\n")
                reward = float(cookie_count.text.split(" ")[-1])- reward_prev
                if(count < 119):
                    Q[count,2] = Q[count,2] + learning_rate*(reward+discount_factor*(np.max(Q[count+1])-Q[count,2]))
                else:
                    Q[count,2] = reward
        else:
            print("Doing Nothing\n")
            reward = float(cookie_count.text.split(" ")[-1])- reward_prev
            if(count < 119):
                Q[count,2] = Q[count,2] + learning_rate*(reward+discount_factor*(np.max(Q[count+1])-Q[count,2]))
            else:
                Q[count,2] = reward


        tok = time.time()
        print(".................................")


    print("The Q: \n")
    print(Q)
    print(cookie_count.text)
    # Refresh the page using the F5 key
    driver.refresh()
    time.sleep(5)
    bigCookie = driver.find_element(By.ID,"bigCookie")
    cookie_count = driver.find_element(By.ID,"cookies")

    #cursor_click
    productPrice0 = driver.find_element(By.ID,"productPrice0")
    print(productPrice0.text)

    #Grandma
    productPrice1 = driver.find_element(By.ID,"productPrice1")
    grandma_price = productPrice1.text
    grandma_price = grandma_price.replace(",","")
    


time.sleep(2)

driver.quit()

