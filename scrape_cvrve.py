import requests
from bs4 import BeautifulSoup
import pandas
import csv

URL = "https://github.com/cvrve/Summer2025-Internships"
page = requests.get(URL)
soup = BeautifulSoup(page.text, 'html.parser')
#print(soup.prettify())

data = []
table = soup.find_all('table')[1]
print(table)