from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))

# Открываем стартовую страницу

driver.get("http://the-internet.herokuapp.com/add_remove_elements/")
sleep(1)

# Пять раз нажимаем на кнопку Add Element

for i in range(5):
    element = driver.find_element(By.XPATH, "//button[text()='Add Element']")
    element.click()
sleep(2)

# Ищем количество кнопок Delete
elements = driver.find_elements(By.XPATH, "//button[text()='Delete']")
print("Количество кнопок на странице", len(elements))
