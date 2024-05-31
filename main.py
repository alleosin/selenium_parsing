import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

price_list = []
dic = dict()

browser = webdriver.Chrome()
browser.get("https://auto.ru/")
CONF_BUT = '//*[@id="confirm-button"]'
conf = browser.find_element(by=By.XPATH, value=CONF_BUT)
conf.click()
print("Открыли сайт")

time.sleep(5)
FILTER_LADA = '//*[@id="LayoutIndex"]/div/div/div[1]/div/div[1]/div[3]/div/div[1]/a[1]/img'
lada = browser.find_element(by=By.XPATH, value=FILTER_LADA)
lada.click()
print("Выбрали лады")

time.sleep(15)
FILTER_CREDIT = '//*[@id="fab6NGE01_OO0BR9NGVYW"]/div[2]/div[1]/div[2]/label'
credit = browser.find_element(by=By.XPATH, value=FILTER_CREDIT)
credit.click()
print("Выбрали в кредит")

time.sleep(5)
BUTTON = '//*[@id="fab6NGE01_OO0BR9NGVYW"]/div[2]/div[3]/div[3]/button/span'
button = browser.find_element(by=By.XPATH, value=BUTTON)
button.click()
print("Показали предложения")

time.sleep(5)
# Найдём все цены
XPATH_PRICE = '//*[@id="fab6NGE01_OO0BR9NGVYW"]/div[7]/div[3]/div/div[2]/div[1]/div[1]/div[2]/div[1]/div/div[1]'
elements = browser.find_elements(by=By.XPATH, value=XPATH_PRICE)
# for element in elements:
#     print(element.text)
className = elements[0].get_attribute("class")
prices = browser.find_elements(by=By.CSS_SELECTOR, value=f"div[class='{className}']")

#print(f"Количество цен {len(prices)}")

for element in prices:
    parent1 = element.find_element(by=By.XPATH, value='..')
    parent2 = parent1.find_element(by=By.XPATH, value='..')
    parent3 = parent2.find_element(by=By.XPATH, value='..')
    try:
        pc = element.text
        pc = pc[:-2]
        pc = pc.replace(" ","")
        pc = int(pc)
        cName = "Link ListingItemTitle__link"
        mark = parent3.find_element(by=By.CSS_SELECTOR, value=f"a[class='{cName}']")
        mk =mark.text
        dic[pc] = mk
    except:
        pass
print(dic)
print(f"{dic[min(dic)]}: {min(dic)} ₽")
