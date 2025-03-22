import keyboard
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))

driver.get("http://uitestingplayground.com/classattr")

sleep(2)

greenbutton = driver.find_element(By.CLASS_NAME, "btn-primary")
greenbutton.click()
sleep(2)
keyboard.send("Enter")
sleep(2)
greenbutton = driver.find_element(By.CLASS_NAME, "btn-primary")
greenbutton.click()
sleep(2)
keyboard.send("Enter")
sleep(2)
greenbutton = driver.find_element(By.CLASS_NAME, "btn-primary")
greenbutton.click()
sleep(2)
keyboard.send("Enter")
sleep(2)
