import urllib
from BeautifulSoup import *

num = list()

url = "http://python-data.dr-chuck.net/comments_248219.html"

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('span')
count = 0

for tag in tags:
    n = int(tag.contents[0])
    count = count + 1
    num.append(n)

print 'Count',count
print 'Sum',sum(num)
    