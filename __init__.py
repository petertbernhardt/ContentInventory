import urllib2
from bs4 import BeautifulSoup

url = raw_input("Enter a website URL: ")
request = urllib2.Request(url)
response = urllib2.urlopen(request)
soup = BeautifulSoup(response)
# For all <a> tags in the page,
for a in soup.findAll('a'):
	# if this tag has an href property and its contents are a non-null string,
    if a.has_attr('href') and a.string and not a.string.isspace():
		# then print out its URL and its Title
        print "URL: " + a['href'] + ", Title: " + a.string

