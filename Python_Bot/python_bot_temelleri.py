from selenium import webdriver
from time import sleep



options=webdriver.EdgeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver=webdriver.Edge(options=options)
url="http://github.com/dsomuncuoglu"

driver.get(url)


pageTitle=driver.title
splitTitle=pageTitle.split()
sleep(2)
if "dsomuncuoglu" in pageTitle:
    driver.maximize_window()
    driver.save_screenshot(f"{splitTitle[0]}.png")
    print(pageTitle)

sleep(2)
driver.close()