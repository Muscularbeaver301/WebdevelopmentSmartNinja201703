from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

url = 'https://scrapebook22.appspot.com/'

response = urlopen(url).read()

soup = BeautifulSoup(response)

print
print "PRINTING PERSON LINKS"
print

# only print links which have 'person' in their reference
for link in soup.findAll("a"):
    # link.attrs gives a list, each entry is a tuple of 2 values, attribute and value.
    # trick to make it more easy to access: turn it into a dictionary

    if 'person' in link['href']:
        person_url = "https://scrapebook22.appspot.com" + link["href"]
        person_html = urlopen(person_url).read()
        person_soup = BeautifulSoup(person_html)
        print person_soup.html.head.title.string
