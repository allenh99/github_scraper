import requests
from bs4 import BeautifulSoup

URL = "https://github.com/SimplifyJobs/Summer2025-Internships"
page = requests.get(URL)
soup = BeautifulSoup(page.text, 'html')