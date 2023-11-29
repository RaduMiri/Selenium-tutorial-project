from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://orteil.dashnet.org/cookieclicker/")

# driver.implicitly_wait(5) #This is a much better method to wait for this app, but I should only use explicit wait, otherwise I might add unnecessary delays

#For privacy window
try:
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.CLASS_NAME, "fc-button.fc-cta-manage-options.fc-secondary-button")))
except:
    pass
else:
    driver.find_element(By.CLASS_NAME, "fc-button.fc-cta-manage-options.fc-secondary-button").click()
    driver.find_element(By.CLASS_NAME, "fc-button.fc-confirm-choices.fc-primary-button").click()

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.CLASS_NAME, "langSelectButton.title")))
driver.find_element(By.CLASS_NAME, "langSelectButton.title").click()
#Alternatives with XPATH
# For this I just copied XPATH from chrome console
# driver.find_element(By.XPATH, '//*[@id="langSelect-EN"]').click() 
# This XPATH is a bit more interesting. First we need //*[] the syntax for an XPATH, then in there we use the function contains(), and the type of object is text(), the text is 'English'
# driver.find_element(By.XPATH, "//*[contains(text(), 'English')]").click()

cookie_id = "bigCookie"
cookies_id = "cookies"
product_price_prefix = "productPrice"
product_prefix = "product"

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.ID, cookie_id)))
cookie = driver.find_element(By.ID, cookie_id)

while True:
    cookie.click()
    cookies_count = driver.find_element(By.ID, cookies_id).text.split()[0]
    cookies_count = int(cookies_count.replace(",", ""))
    
    for i in range(4):
        product_price = driver.find_element(By.ID, product_price_prefix + str(i)).text.replace(",","")

        if not product_price.isdigit():
            continue
        
        product_price = int(product_price)
        
        if cookies_count >= product_price:
            product = driver.find_element(By.ID, product_prefix + str(i))
            product.click()
            break

# time.sleep(10)
driver.quit()