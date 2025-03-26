from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("http://the-internet.herokuapp.com/login")

username = driver.find_element(By.ID, "username")
username.send_keys("tomsmith")

password = driver.find_element(By.ID, "password")
password.send_keys("SuperSecretPassword!")

login_but = driver.find_element(By.XPATH, "//button[@type='submit']")
login_but.click()
time.sleep(2)

green_text = driver.find_element(By.ID, "flash")
banner_text = green_text.text
print(banner_text)

driver.quit()
