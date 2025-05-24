from bs4 import BeautifulSoup
import requests
url = 'https://github.com/wzdnzd/aggregator/issues/91'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
class1 = soup.find_all('td', class_='notranslate').get_text()
print(class1)
