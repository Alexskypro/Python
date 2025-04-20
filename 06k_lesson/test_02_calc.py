import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.mark.usefixtures("driver")
def test_screen(driver):
    driver.get(
        ("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
        )
    waiter = WebDriverWait(driver, 50)

    delay = driver.find_element(By.CSS_SELECTOR, '#delay')

    delay.clear()
    delay.send_keys('45')
    sev = driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[1]')
    sev.click()
    pl = driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[4]')
    pl.click()
    ei = driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[2]')
    ei.click()
    sm = driver.find_element(By.XPATH, '//*[@id="calculator"]/div[2]/span[15]')
    sm.click()
    screen = driver.find_element(By.CSS_SELECTOR, 'div.screen')
    waiter.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "div.screen"), "15")
    )
    assert screen.text == "15"
    driver.quit()
