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
        if 'person' in link['href']:
            person_url = "https://scrapebook22.appspot.com" + link["href"]
            person_soup = get_soup(person_url)
            # we know the Email is in a span, however there might be many spans on the website.
            # fortunately, we can add additonal information about the span we try to find, e.g. the attributes:
            # we know, our span has the attribute: class = "email", so we can insert that in our find() function
            email = person_soup.find("span", attrs={"class": "email"}).string
            print email


if __name__ == '__main__':
    main()
