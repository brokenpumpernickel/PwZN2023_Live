import requests
from bs4 import BeautifulSoup
import json

res = requests.get('https://www.fizyka.pw.edu.pl/Pracownicy/Lista-pracownikow/Pracownicy-badawczo-dydaktyczni')
#print(res.status_code)
#print(res.headers)
#print(res.text)

soup = BeautifulSoup(res.text, 'html.parser')

main_div = soup.find('div', class_='content-view-full-folder-pracownikow')

# names = main_div.find_all('h2')
# for name in names:
#     print(name.text.strip())
#     print('------------------')

names = []
contacts = []

raw_data = main_div.select('h2, h2 + div')
for data in raw_data:
    print(data.name)
    print(data.text.strip())
    print('------------------')

    if data.name == 'h2':
        names.append(data.text.strip())
    else:
        contacts.append(data.text.strip())

assert len(names) == len(contacts)

#print(names)
#print(contacts)

employees = list(zip(names, contacts))
print(employees)

with open('scripts/Lab005/employees.json', 'w') as f:
    json.dump(employees, f, indent=4)