import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


# Get base links
site = 'http://cancerbiologyprogram.med.wayne.edu/'
base = urlparse(site).netloc

to_visit = [site]
outlinks = []
visited = {}
external_visited = {}



while to_visit:
    l = to_visit.pop()
    url = urljoin(site, l)

    try:
        r = requests.get(url)
        visited[l] = r.status_code

    except:
        visited[l] = None

    if r.status_code == 200:
        soup = BeautifulSoup(r.content, 'html5lib')
        links = [l['href'] for l in soup.find_all('a', href=True)]
        for link in links:
            parsed_link = urlparse(link)
            loc = parsed_link.netloc
            path = parsed_link.path
            joined_url = urljoin(site, link)

            if loc == '':
                if joined_url not in to_visit and joined_url not in visited.keys():
                    to_visit.append(joined_url)

            elif loc == base:
                if link not in to_visit and link not in visited.keys():
                    to_visit.append(link)

            else:
                if link not in outlinks and link not in visited.keys():
                    outlinks.append(link)

# check the status of external links
while outlinks:
    l = outlinks.pop()

    try:
        r = requests.get(l)
        external_visited[l] = r.status_code

    except:
        external_visited[l] = None
        

print(external_visited)