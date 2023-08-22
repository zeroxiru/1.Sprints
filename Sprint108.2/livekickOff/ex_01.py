import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
    driver = webdriver.Chrome(
        service=Service(
            ChromeDriverManager().install()
        )
    )
    driver.maximize_window()
    driver.get('https://www.saucedemo.com')

    username_field = driver.find_element(By.ID, 'user-name')
    password_field = driver.find_element(By.ID, 'password')

    username_field.send_keys('standard_user')
    password_field.send_keys('secret_sauce')
    password_field.send_keys(Keys.RETURN)

    # Wait for the page to load completely
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'inventory_item_name')))

    # Locate the fleece jacket by class name and print its price
    items =driver.find_elements(By.CLASS_NAME,'inventory_item_name')
    for i, item in enumerate(items):
        if item.text == 'Sauce Labs Fleece Jacket':
            price_items = driver.find_elements(By.CLASS_NAME, 'pricebar')
            item_price_jacket = price_items[i]
            print(f'Sauce Labs Fleece Jacket -price, {item_price_jacket.text}')

    items = driver.find_elements(By.CLASS_NAME, 'inventory_item_name')
    for i, item in enumerate(items):
        if item.text == 'Sauce Labs Fleece Jacket':
            item_prices = driver.find_elements(By.CLASS_NAME, "pricebar")
            item_price = item_prices[i]
            print(f'Sauce Labs Fleece Jacket -Price, {item_price.text}')


except Exception as e:
    print("An error occurred:", str(e))

finally:
    driver.quit()










