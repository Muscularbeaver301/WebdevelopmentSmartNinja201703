"""
If you have no suitable json file "prices.json", make one and
paste an empty json content into it, i.e write {} into the file.
"""
import urllib2 # rewrite some of this with import urllib, if using Python 3
import re
import json
import time

FILENAME = "prices.json"
HEADER = {'User-Agent': 'Mozilla/5.0'}  # go in as a browser
URL = "https://www.worldcoinindex.com/"

def main():
    pairs = sorted(get_prices().iteritems())
    for currency, price in pairs:
        print(currency.ljust(6) + price)

def get_text(url):
    print('reading {} ...\n'.format(url))
    request = urllib2.Request(url, headers=HEADER)
    page = urllib2.urlopen(request)
    return page.read()

def find(string, left, right):
    pattern = '{0}(.*){1}'.format(left, right)
    findings = re.search(pattern, string)
    try:
        return findings.group(1)
    except AttributeError:
        return False

def get_prices():
    text = get_text(URL)
    prices = {}
    for string in text.split('</tr>'):
        currency = find(string, '<h2>', '</h2>')
        price = find(string, '<span class="span">', '</span>')
        if currency and price:
            prices.update({currency: price})
    return prices

if __name__ == '__main__':
    main()
