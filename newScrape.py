import sqlite3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from datetime import datetime

# Initialize SQLite database connection
conn = sqlite3.connect('past_life_results.db')
c = conn.cursor()

# Create a table to store past life results
c.execute('''CREATE TABLE IF NOT EXISTS past_life_results
             (id INTEGER PRIMARY KEY, date TEXT, prediction TEXT)''')

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

# Iterate over all combinations of years, months, and days
for year in range(1955, 2025):
    for month_num in range(1, 13):
        month_name = datetime.strptime(str(month_num), "%m").strftime("%B")
        for day in range(1, 30):
            try:
                result = test_past_life(str(year), month_name, str(day))
                print("Result:", result)

                # Store the result in the database
                date_str = f"{year}-{month_name}-{day}"
                c.execute("INSERT INTO past_life_results (date, prediction) VALUES (?, ?)",
                          (date_str, result))
                conn.commit()
            except Exception as e:
                print(f"An error occurred for date {year}-{month_name}-{day}: {str(e)}")

# Close the database connection
conn.close()
