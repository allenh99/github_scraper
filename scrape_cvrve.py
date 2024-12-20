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
for row in table.find('tbody').find_all('tr'):
    columns = row.find_all('td')
    #print(columns)
    company = columns[0].text.strip()
    role = columns[1].text.strip()
    location = columns[2].text.strip()
    
    links = columns[3].find_all('a')
    application_links = [{'href': link['href'], 'alt': link.get('alt', 'Link')} for link in links]

    date_posted = columns[4].text.strip()

    data.append({
        'Company': company,
        'Role': role,
        'Location': location,
        'Application/Links': application_links,
        'Date Posted': date_posted
    })

fields = ["Company","Role","Location","Application","Date Posted"]
fields = ["Company","Date Posted","Referal","Applied","Location","Application"]
csv_data = []
for i in data:
    if len(i["Application/Links"]) > 0:
        d = [i["Company"],i["Date Posted"],"","",i["Location"]+" "+i["Role"],i["Application/Links"][0]["href"]]
        csv_data.append(d)
        #print(d)

filename = "job_listings_cvrve.csv"

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(csv_data)
