from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))
driver.get("https://dzen.ru")
driver.get("https://vk.com")
sleep(5)
driver.back()
driver.forward
sleep(10)
driver.refresh
