from bs4 import BeautifulSoup
from urllib2 import urlopen
site = urlopen("https://news.ycombinator.com/")
soup = BeautifulSoup(site.read())
print soup.title
link = soup.find_all('a')
nycontent = []
nylinks = []
for l in link:
    if not l.string == None:
        nycontent.append(l.contents)

def add_uniq(seq):
    c = []
    for x in seq:
        if x not in c:
            c.append(x)
    return c



for l in link:
    if not l.string == None:
        nylinks.append(l['href'])


def remove_not_href(seq):
    for x in seq:
        if x.find("http://") == -1:
            seq.remove(x)

remove_not_href(nylinks)

for x in nylinks:
    print x