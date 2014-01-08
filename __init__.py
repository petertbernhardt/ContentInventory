import urllib2
from bs4 import BeautifulSoup

request = urllib2.Request("http://www.google.com/")
response = urllib2.urlopen(request)
soup = BeautifulSoup(response)
for a in soup.findAll('a'):
    print a['href']

