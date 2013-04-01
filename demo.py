from bs4 import BeautifulSoup
from urllib2 import urlopen
site = urlopen("https://news.ycombinator.com/")
soup = BeautifulSoup(site.read())
print soup.title
link = soup.find_all('a')
nycontent = []
nylinks = []
dd = []
for l in link:
    if not l.string == None:
        nycontent.append(l.contents)

def add_uniq(seq):
    c = []
    for x in seq:
        if x not in c:
            c.append(x)
    return c


def add_links():
    global l
    for l in link:
        if not l.string == None:
            nylinks.append(l['href'])


add_links()


def just_http(ll, arg="http"):
    global x
    c = []
    for x in ll:
        if  x[0:3] == arg:
            c.append(x)
    return c



print just_http(nylinks, arg="http")



