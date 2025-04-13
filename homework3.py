from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))

url = (
    "https://bonigarcia.dev/selenium-webdriver-java/loading-images.html"
)
driver.get(url)
wait = WebDriverWait(driver, 20)
last_element = wait.until(EC.text_to_be_present_in_element(
    (By.TAG_NAME, "body"), "Done"))

third = driver.find_element(By.CSS_SELECTOR, "#award")
src = third.get_attribute("src")
print("SRC атрибут картинки 3: ", src)
