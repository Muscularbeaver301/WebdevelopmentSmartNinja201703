import re
from urllib2 import urlopen

from Class13.repetition.BeautifulSoup import BeautifulSoup


def get_soup(site_url):
    site_html = urlopen(site_url).read()
    site_soup = BeautifulSoup(site_html)
    return site_soup


def main():
    url = 'https://scrapebook22.appspot.com/'

    soup = get_soup(url)

    print
    print "PRINTING PERSON INFO"
    print

    for link in soup.findAll("a"):

        if 'person' in link['href']:
            person_url = "https://scrapebook22.appspot.com" + link["href"]
            person_soup = get_soup(person_url)

            # Find Name on Profile Site
            name_header = person_soup.findAll("h1")[1]
            name = name_header.string

            # Find Age on Profile Site, using regex, special library to discuss
            age_text = person_soup.html.find("li", text=re.compile('(Age)'))
            found_numbers = re.findall(r"(\d+)", age_text) # \d searches for digits, \d+ searches for any number of consecutive digits
            age = found_numbers[0] # findAll gives us a list of all found numbers. we only have 1 number in this place, so we always take the oth

            # Find Gender on Profile Site
            gender_span = person_soup.find("span", attrs={"data-gender": True})
            gender = gender_span.string

            # Find City on Profile Site
            city_span = person_soup.find("span", attrs={"data-city": True})
            city = city_span.string

            # Find Email on Profile Site
            emailspan = person_soup.find("span", attrs={"class": "email"})
            email = emailspan.string

            print name,age,gender,city,email


if __name__ == '__main__':
    main()
