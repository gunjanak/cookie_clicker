#Giving reward at the end of the episode

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

Q = np.zeros((10, 3))
rewards = np.zeros(10)
learning_rate = 0.2
discount_factor = 0.99
episodes = 300
reward_prev = 0
Q[9] = [-1,-10,-100]






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
        
        #print("Reward is ",reward_prev)
        # Generate a random number between 1 and 3
        random_number_n = random.randint(1, 10)
        if(random_number_n == 3):
            random_number = random.randint(0,2)
        #elif(random_number_n == 4):
         #   random_number = random.randint(1,2)
        else:
            random_number = np.argmax(Q[current_time])


        #print(random_number)
        if(random_number == 1):
            if(count > int(productPrice0.text)):
                print('Buying cursor\n')
                actions2 = ActionChains(driver)
                actions2.move_to_element(productPrice0)
                actions2.click(productPrice0 )
                actions2.perform()
                if(current_time < 9):
                    Q[current_time,1] = Q[current_time,1] + learning_rate*(0+discount_factor*(np.max(Q[current_time+1])-Q[current_time,1]))
                   
                else:
                    Q[current_time,1] = Q[current_time,1] + learning_rate*float(cookie_count.text.split(" ")[-1])
            else:
                if(current_time < 9):
                    Q[current_time,2] = Q[current_time,2] + learning_rate*(0+discount_factor*(np.max(Q[current_time+1])-Q[current_time,2]))
                    
                else:
                    Q[current_time,2] = Q[current_time,2] + learning_rate*float(cookie_count.text.split(" ")[-1])
                

              
            

            
        elif(random_number == 0):
            if(count > int(productPrice1.text.replace(",",""))):
                print('Buying grandma\n')
                actions2 = ActionChains(driver)
                actions2.move_to_element(productPrice1)
                actions2.click(productPrice1)
                actions2.perform()
                if(current_time < 9):
                    Q[current_time,0] = Q[current_time,0] + learning_rate*(0+discount_factor*(np.max(Q[current_time+1])-Q[current_time,0]))
                  
                else:
                    Q[current_time,0] = Q[current_time,0] + learning_rate*float(cookie_count.text.split(" ")[-1])
            else:
                if(current_time < 9):
                    Q[current_time,2] = Q[current_time,2] + learning_rate*(0+discount_factor*(np.max(Q[current_time+1])-Q[current_time,2]))
                else:
                    Q[current_time,2] = Q[current_time,2] + learning_rate*float(cookie_count.text.split(" ")[-1])
                
        else:
            print("Doing Nothing\n")
            if(current_time < 9):
                Q[current_time,2] = Q[current_time,2] + learning_rate*(0+discount_factor*(np.max(Q[current_time+1])-Q[current_time,2]))
                
            else:
                Q[current_time,2] = Q[current_time,2] + learning_rate*float(cookie_count.text.split(" ")[-1])
            
       


        tok = time.time()
        print(".................................")
    
    #current_time = math.floor(tok-tic)
    #reward = float(cookie_count.text.split(" ")[-1])
    #Q[current_time,random_number] = reward
    #reward_prev = reward



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

