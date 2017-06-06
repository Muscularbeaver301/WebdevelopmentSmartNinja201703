from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen


def get_soup(site_url):
    site_html = urlopen(site_url).read()
    site_soup = BeautifulSoup(site_html)
    return site_soup


def main():
    url = 'https://scrapebook22.appspot.com/'

    soup = get_soup(url)

    print
    print "PRINTING PERSON LINKS"
    print

    # only print links which have 'person' in their reference
    for link in soup.findAll("a"):
        # link.attrs gives a list, each entry is a tuple of 2 values, attribute and value.
        # trick to make it more easy to access: turn it into a dictionary
        if 'person' in link['href']:
            person_url = "https://scrapebook22.appspot.com" + link["href"]
            person_soup = get_soup(person_url)
            print person_soup.html.head.title.string


if __name__ == '__main__':
    main()
