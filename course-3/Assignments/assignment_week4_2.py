import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
count = int(input('Enter count: '))
position = int(input('Enter Position: '))
nameList = list()


# Retrieve all of the anchor tags
print('Retrieving:', url)


# Helper Functions

def soup_url(url):
	html = urllib.request.urlopen(url, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	return soup('a')
def traverse_link(tags, posCount):
	for tag in tags:
		posCount = posCount+1
		if posCount == position:
			nameList.append(tag.contents[0])
			return tag.get('href', None)



tags = soup_url(url)
t_link = traverse_link(tags, posCount = 0)
print('Retrieving:', t_link)
# Range of looping through anchor tags
while(count > 1):
    count = count - 1
    url = t_link
    tags = soup_url(url)
    t_link = traverse_link(tags, posCount = 0)
    print(t_link)
#	Result
print(nameList[len(nameList) - 1])