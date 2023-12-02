import requests
from bs4 import BeautifulSoup


def get_h3_tags(site_url):
    response = requests.get(site_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    h3_tags = soup.find_all('h3')
    return [tag.text for tag in h3_tags]


url = 'http://www.columbia.edu/~fdc/sample.html'
result = get_h3_tags(url)
print(result)
