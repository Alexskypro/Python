from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=ChromeService
                          (ChromeDriverManager().install()))

driver.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

driver.implicitly_wait(10)
driver.find_element(By.NAME, 'first-name').send_keys("Иван")
driver.find_element(By.NAME, 'last-name').send_keys("Петров")
driver.find_element(By.NAME, 'address').send_keys("Ленина, 55-3")
driver.find_element(By.NAME, 'zip-code').send_keys("")
driver.find_element(By.NAME, 'city').send_keys("Москва")
driver.find_element(By.NAME, 'country').send_keys("Россия")
driver.find_element(By.NAME, 'e-mail').send_keys("test@skypro.com")
driver.find_element(By.NAME, 'phone').send_keys("+7985899998787")
driver.find_element(By.NAME, 'job-position').send_keys("QA")
driver.find_element(By.NAME, 'company').send_keys("SkyPro")

driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


zip_color = driver.find_element(By.CSS_SELECTOR, "#zip-code")
assert_color = zip_color.value_of_css_property("background-color")
assert assert_color == "rgba(248, 215, 218, 1)"


def check_green_field():
    green_field = driver.find_elements(By.CSS_SELECTOR, 'div.alert.py-2.alert-success')
    for form in green_field:
        assert form.value_of_css_property("background-color") == "rgba(209, 231, 221, 1)"


check_green_field()

driver.quit()
