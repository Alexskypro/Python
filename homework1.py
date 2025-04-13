from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))


driver.implicitly_wait(16)
driver.get("http://uitestingplayground.com/ajax")
button = driver.find_element(By.CSS_SELECTOR, "#ajaxButton")
button.click()
panel = driver.find_element(By.CSS_SELECTOR, "#content")
result = panel.find_element(By.CSS_SELECTOR, "p.bg-success").text
print(result)
