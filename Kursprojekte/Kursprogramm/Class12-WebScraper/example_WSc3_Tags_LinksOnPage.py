from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

url = 'https://scrapebook22.appspot.com/'

response = urlopen(url).read()

soup = BeautifulSoup(response)

for link in soup.findAll("a"):
    print link

