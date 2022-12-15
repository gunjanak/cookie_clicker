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





def farm():
    print("Inside farm price")
    #buying farm
    productPrice2 = driver.find_element(By.ID,"productPrice2")
    productPrice2 = productPrice2.text
    productPrice2 = productPrice2.replace(",", "")
    #print(productPrice2)
    return productPrice2



tic = time.time()
tok = time.time()

while(tok-tic < 60):
    bigCookie.click()
    count = int(cookie_count.text.split(" ")[0].replace(",",""))

    farm_price = farm()
    if(farm_price):
        if(count > int(farm_price)):
            #print("Buying Farm")
            productPrice2 = driver.find_element(By.ID,"productPrice2")
            actions4 = ActionChains(driver)
            actions4.move_to_element(productPrice2)
            actions4.click(productPrice2)
            actions4.perform()



    

    tok = time.time()
    







    


print(cookie_count.text)
time.sleep(10)

driver.quit()
