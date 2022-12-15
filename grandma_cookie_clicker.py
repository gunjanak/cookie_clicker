#Here we go to the website click cookie and only buy grandma for five minutes

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

link = driver.find_element(By.LINK_TEXT,"Got it!")
link.click()
time.sleep(10)


eng_lang = driver.find_element(By.ID,"langSelect-EN")
eng_lang.click()
time.sleep(10)


bigCookie = driver.find_element(By.ID,"bigCookie")
cookie_count = driver.find_element(By.ID,"cookies")



#grandma
productPrice1 = driver.find_element(By.ID,"productPrice1")
grandma_price = productPrice1.text
grandma_price = grandma_price.replace(",","")
print(grandma_price)


import time
tic = time.time()
tok = time.time()

while(tok-tic < 10):
    bigCookie.click()
    count = int(cookie_count.text.split(" ")[0].replace(",",""))
    if(count > int(productPrice1.text.replace(",",""))):
        #print('Buying grandma')
        actions2 = ActionChains(driver)
        actions2.move_to_element(productPrice1)
        actions2.click(productPrice1)
        actions2.perform()

    tok = time.time()
    #print(tok-tic)


print(cookie_count.text)
time.sleep(10)

driver.quit()
