from selenium import webdriver
from selenium.webdriver.chrome.service import Service #We need to install a web driver the same vesion as the chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
#These are so that we wait for the page to load so we don't have issues with pages not yet loading when we try the code
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#To use selenium you need to use a webdriver, an automation tool for the browser
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://google.com")

#Chrom privacy policy does not allow me to use the text area, so first I will close it
driver.find_element(By.ID, "W0wltc").click() #Eyy, it works

#Maybe I should make one for the first thing, like the policy, but that is not really necessary here, though it would be the safe and right call
WebDriverWait(driver, 5).until( #just wait up to 5 seconds
    EC.presence_of_element_located((By.CLASS_NAME, "gLFyf"))) 

input_element = driver.find_element(By.CLASS_NAME, "gLFyf") #method to get elements
input_element.clear() #If it already has sth, because the send keys just writes that in, not overwrite
input_element.send_keys("tech with tim" + Keys.ENTER) #also presses enter from the keys

#! find_element reutrns the first element, whereas find_elements returns a list of elements

WebDriverWait(driver, 5).until(
    EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Tech With Tim")))
link = driver.find_element(By.PARTIAL_LINK_TEXT, "Tech With Tim")
#If the text is in any anchor tag, link tag, I will remember it within this object
#If I want the exact text, I can delete the PARTIAL_
link.click()

time.sleep(10)
driver.quit()