import pickle
import time

from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Create a Chrome WebDriver instance
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

try:
    with driver as browser:
        browser.get("https://planetcalc.ru/8678/")
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='dialogv6411ef5258561_quantity']")))

        # Find the element by its XPath and send keys
        input_element = browser.find_element(By.XPATH, "//*[@id='dialogv6411ef5258561_quantity']")
        input_element.send_keys("00")

        time.sleep(0.4)

        # Find and click the element
        button_element = browser.find_element(By.XPATH, "//*[@id='dialogv6411ef5258561_button_text']")
        button_element.click()

        time.sleep(0.4)

        name_element = browser.find_element(By.XPATH, "//*[@id='dialogv6411ef5258561_fio']")
        name_text = name_element.text

        list_name = []
        list_name.append(name_text)
        time.sleep(0.4)

except Exception as ex:
    print("[INFO] Error while interacting with the page:", ex)
finally:
    if driver:
        driver.quit()
        print("[INFO] WebDriver closed")