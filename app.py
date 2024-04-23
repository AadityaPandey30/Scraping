from flask import Flask, render_template, request
from bs4 import BeautifulSoup
import subprocess
import requests

app = Flask(__name__)

def scrape_website():
    url = "https://www.prokerala.com/astrology/past-life/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    main_content = soup.find('main', class_='body container')
    return str(main_content)

@app.route('/')
def display_scraped_content():
    scraped_content = scrape_website()
    return render_template('index.html', scraped_content=scraped_content)

@app.route('/get_past_life', methods=['POST'])
def get_past_life():
    # Get the selected birth date from the form submission
    birth_year = request.form['birth_year']
    birth_month = request.form['birth_month']
    birth_day = request.form['birth_day']
    
    # Call the Selenium bot script with the birth date as an argument
    process = subprocess.Popen(['python', 'newScrape.py', birth_year, birth_month, birth_day], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()

    # Extract the output from the subprocess and pass it to the template
    output = stdout.decode('utf-8')

    return output


if __name__ == '__main__':
    app.run(debug=True)
