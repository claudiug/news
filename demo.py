from bs4 import BeautifulSoup
from urllib2 import urlopen
site = urlopen("https://news.ycombinator.com/")
soup = BeautifulSoup(site.read())
print soup.title
link = soup.find_all('a')
nycontent = []
for l in link:
    if not l.string == None:
        nycontent.append(l.contents)

def add_uniq(seq):
    c = []
    for x in seq:
        if x not in c:
            c.append(x)
    return c

print len(add_u(nycontent))
print len(nycontent)