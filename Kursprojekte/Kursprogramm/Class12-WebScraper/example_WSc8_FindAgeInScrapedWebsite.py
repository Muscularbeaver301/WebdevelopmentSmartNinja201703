from BeautifulSoup import BeautifulSoup
from urllib2 import urlopen

with open("csv_file.csv", "w") as scrapetxt:
    url = 'https://scrapebook22.appspot.com/'
    response = urlopen(url).read()
    soup = BeautifulSoup(response)
    for personlink in soup.findAll("a"):
        if personlink.string == "See full profile":
            person_link = "https://scrapebook22.appspot.com" + personlink["href"]
            personhtml = urlopen(person_link).read()
            personsoup = BeautifulSoup(personhtml)
            person_email = personsoup.find("span", attrs={"class": "email"}).string
            person_city =  personsoup.find("span", attrs={"data-city": True}).string
            person_gender = personsoup.find("span", attrs={"data-gender": True}).string
            person_name = personsoup.find("div", attrs={"class": "col-md-8"}).h1.string
            #person_age = personsoup.findAll("li")[1].string
            for agestr in personsoup.findAll("li"):
                if 'Age' in personsoup.findAll("li")[1].text:
                    person_age =  personsoup.findAll("li")[1].text
            scrape = person_name + ", " + person_age + ", " + person_gender + ", " + person_city + ", " + person_email
            scrapetxt.write(scrape + "\n")
print "file saved!"