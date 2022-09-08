#*
# Selenium Nedir? (Web Otomasyon Kütüphanesi)
#   Selenium ile bir web sitesinin ziyaret edip etkileşimde bulunmamızı sağlar.
# 
# Selenium Kütüphanesi Nasıl Kurulur?
#   py -m pip install selenium    (py --version : 3.10.6)
# *#


from selenium import webdriver

options=webdriver.EdgeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver=webdriver.Edge(options=options)
url="https://www.google.com.tr/"

driver.get(url)