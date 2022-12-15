#Here we go to the website click cookie and only buy farm for five minutes

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
from bs4 import BeautifulSoup
import time

#driver.find_element_by_name("Value").send_keys(Keys.RETURN)
options = Options()
options.BinaryLocation = "/usr/bin/chromium-browser"
#options.headless  = True

driver = webdriver.Chrome(executable_path="/usr/bin/chromedriver",options=options)
driver.get("https://orteil.dashnet.org/cookieclicker/")
time.sleep(10)
#identify the Google search text box and enter the value  
#my_element = driver.find_element("name","q")
#my_element.send_keys('cryptography')
link = driver.find_element(By.LINK_TEXT,"Got it!")
link.click()
time.sleep(10)


eng_lang = driver.find_element(By.ID,"langSelect-EN")
eng_lang.click()
time.sleep(10)


bigCookie = driver.find_element(By.ID,"bigCookie")
cookie_count = driver.find_element(By.ID,"cookies")
#actions = ActionChains(driver)
#actions.click(bigCookie)





def mine():
    print("Inside mine price")
    #buying mine
    productPrice3 = driver.find_element(By.ID,"productPrice3")
    productPrice3 = productPrice3.text
    productPrice3 = productPrice3.replace(",", "")
    print(productPrice3)
    return productPrice3

mine_price = mine()
if(mine_price):
    print("Inside if")

    print(mine_price)


import time
tic = time.time()
tok = time.time()

while(tok-tic < 300):
    bigCookie.click()
    count = int(cookie_count.text.split(" ")[0].replace(",",""))

    mine_price = mine()
    if(mine_price):
        if(count > int(mine_price)):
            print("Buying Mine")
            productPrice3 = driver.find_element(By.ID,"productPrice3")
            actions5 = ActionChains(driver)
            actions5.move_to_element(productPrice3)
            actions5.click(productPrice3)
            actions5.perform()



    

    tok = time.time()







    


print(cookie_count.text)
time.sleep(10)

driver.quit()
