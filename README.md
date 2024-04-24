# Past Life Prediction Scraper

This script scrapes past life predictions from a website and stores them in an SQLite database.

## Purpose

The purpose of this script is to collect past life predictions for different dates and store them in a database for analysis or reference.

## How it Works

1. **Scraping Initial Data**: The script initially scrapes the main content of a website that provides past life predictions. It extracts the HTML content of the main element.

2. **Data Collection**: When the user presses the "Know Your Past Life" button on the webpage, the script triggers a Selenium bot to extract past life predictions for different dates. It iterates over all combinations of years, months, and days, submits each combination to the website, and stores the result in the database.

3. **Storage in SQLite Database**: The past life predictions are stored in an SQLite database. Each entry in the database consists of a date and the corresponding past life prediction.

## Usage

1. Install the required dependencies using `pip install -r requirements.txt`.
2. Run the script `main.py`.
3. The script will scrape the initial data and wait for user interaction.
4. Press the "Know Your Past Life" button on the webpage to trigger data collection and storage in the database.

## Dependencies

- Python 3.x
- Selenium
- Chrome WebDriver (for Selenium)

## Note

- Ensure that the Chrome WebDriver is installed and configured properly.
- Adjust the script as needed based on the website structure and requirements.
- Use responsibly and adhere to the website's terms of service.

