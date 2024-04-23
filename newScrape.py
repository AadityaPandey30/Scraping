from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def test_past_life(year, month, day):
    # Initialize Selenium WebDriver
    driver = webdriver.Chrome()  # You need to download the appropriate driver for your browser

    try:
        # Open the main site
        driver.get("https://www.prokerala.com/astrology/past-life/")

        # Find and set the values of the three select tags
        year_select = driver.find_element(By.ID, "fin_year")
        month_select = driver.find_element(By.ID, "fin_month")
        day_select = driver.find_element(By.ID, "fin_day")

        year_select.send_keys(year)
        month_select.send_keys(month)
        day_select.send_keys(day)

        # Click the "Know Your Past Life" button
        # Wait until the button is clickable
        know_btn = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "btn-past-life")))
        know_btn.click()

        # Wait for the page to load
        time.sleep(3)  # Adjust the time according to your page load time

        # Get the result
        result = driver.find_element(By.ID, "resultDiv").text

        return result

    finally:
        # Close the browser window
        driver.quit()

# Example usage
year = "1990"
month = "May"
day = "15"

result = test_past_life(year, month, day)
print("Result:", result)
