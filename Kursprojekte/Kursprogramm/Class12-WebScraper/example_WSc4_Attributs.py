from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

url = 'https://scrapebook22.appspot.com/'

response = urlopen(url).read()

soup = BeautifulSoup(response)

print
print "PRINTING ALL LINKS"
print

# print all links
for link in soup.findAll("a"):
    #
    # link.attrs gives a list, each entry is a tuple of 2 values, attribute and value.
    #
    # dict(link.attrs) gives us all attributes and their values in a 'dictionary' fashion
    # it turns the 2-value tuples into a key-value entry
    #
    print dict(link.attrs)

print
print "PRINTING PERSON LINKS"
print

# only print links which have 'person' in their reference
for link in soup.findAll("a"):
    # link has information about its attributes just like a dictionary. we look for 'person' in the url of the link
    if 'person' not in link.string:
        print link['href']
