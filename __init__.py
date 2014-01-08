import urllib2
from bs4 import BeautifulSoup

url = raw_input("Enter a website URL: ")
request = urllib2.Request(url)
response = urllib2.urlopen(request)
soup = BeautifulSoup(response)
for a in soup.findAll('a'):
    if a.has_attr('href') and a.string and not a.string.isspace():
        print "URL: " + a['href'] + ", Title: " + a.string

