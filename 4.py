import urllib
from BeautifulSoup import *

# url = raw_input('Enter URL:')

count = raw_input('Enter count:')
c = int(count)

position = raw_input('Enter position:')
p = int(position)

url = "http://python-data.dr-chuck.net/known_by_Shafira.html"
print 'Retrieving:',url

for i in range(c):
    

    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    tags = soup('a')
    print 'Retrieving:',tags[p - 1].get('href', None)
    url = tags[p - 1].get('href', None)
    
        
