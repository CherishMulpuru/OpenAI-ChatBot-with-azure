import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# Function to fetch HTML content
def fetch_html(url):
    response = requests.get(url)
    response.raise_for_status()  # Check for request errors
    return response.text

# Function to clean and extract text from elements
def clean_text(element):
    return re.sub(r'\s+', ' ', element.get_text(strip=True))

# Function to parse HTML and extract data
def parse_html(html):
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find all tables on the page
    tables = soup.find_all('table')
    
    if not tables:
        # If no tables, find all paragraphs
        data = {'Content': [clean_text(p) for p in soup.find_all('p')]}
    else:
        # Extract data from the first table (for simplicity)
        table = tables[0]
        headers = [clean_text(th) for th in table.find_all('th')]
        rows = []
        for row in table.find_all('tr'):
            cells = row.find_all(['td', 'th'])
            rows.append([clean_text(cell) for cell in cells])
        
        # Organize data into a dictionary
        data = {headers[i]: [row[i] for row in rows[1:]] for i in range(len(headers))}
    
    return data

# Function to save data to CSV
def save_to_csv(data, filename):
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False, encoding='utf-8')

# Main function
def main():
    url = 'https://example.com'  # Replace with the target URL
    html = fetch_html(url)
    data = parse_html(html)
    save_to_csv(data, 'output.csv')

if __name__ == '__main__':
    main()

# to test
def main():
    url = 'https://example.com'  # Replace with the target URL
    html = fetch_html(url)
    data = parse_html(html)
    save_to_csv(data, 'output.csv')
#to run the script
python web_scraper.py


# To run Script online
#Open Google Colab: Go to Google Colab.

#reate a New Notebook: Click on "New Notebook".

#Install Required Libraries: In a new code cell, run:

!pip install requests beautifulsoup4 pandas

# to download the output in csv files
from google.colab import files
files.download('output.csv')
