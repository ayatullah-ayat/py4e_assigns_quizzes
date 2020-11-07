from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
numList = list()
count = 0
for tag in tags:
    # Look at the parts of a tag
    count = count+1
    numList.append(int(tag.contents[0]))

print('Count', count, '\nSum', sum(numList))