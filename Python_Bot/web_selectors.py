# Link : https://selenium-python.readthedocs.io/locating-elements.html

#*  Single Elements
#
# find_element_by_id
#                _class_name  
#                _name
#
#  Multi Elements
#
# find_elements_by_id
#                 _class_name  
#                 _name
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
import time

inputText=input("Github'da aramak istediğiniz başlık nedir?\n=>")

driver=webdriver.Edge()
url="https://github.com"
driver.get(url)
driver.fullscreen_window()
searchInput=driver.find_element(By.NAME,"q")
time.sleep(1)
searchInput.send_keys(inputText)
searchInput.send_keys(Keys.ENTER)
driver.fullscreen_window()
typeText=driver.find_elements(By.CSS_SELECTOR,".v-align-middle")
blank=driver.find_elements(By.CSS_SELECTOR,".blankslate")
bulunamadi=(f"We couldn’t find any repositories matching '{inputText}'\nYou could try an advanced search.")

for blanks in blank:
    blankText=blanks.text
    if blankText in bulunamadi:
        print(f"Aranan {inputText} söz dizini bulunamadı.")
        break

for element in typeText:
    print(element.text)

driver.close()


