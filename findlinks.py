# import file_download
import requests, urllib3, datetime, csv, os
from bs4 import BeautifulSoup
from pathlib import Path


urllib3.disable_warnings()

url_start ='http://cancerbiologyprogram.med.wayne.edu/faculty/'

def print_out(content):
    top_dir = ('{}/{}-File'.format(str(Path.home()), datetime.date.today()))
    try:
        os.makedirs(top_dir)
    except OSError:
        open('{}/{}'.format(top_dir, 'filee'), 'a').write(content)
    else:
        open('{}/{}'.format(top_dir, 'filee'), 'a').write(content)


def print_csv(name):
    # all = (name, '-', accessID)
    file_write = ('{}/Accessibility_Audit/{}.csv'.format(str(Path.home()),'CancerBiology'))
    with open(file_write, mode='a') as csv_write:
                violation_csv = csv.writer(csv_write, delimiter= ',')
                violation_csv.writerow(name) 

def soups_up(url):
    html = requests.get(url)
    return BeautifulSoup(html.content, 'html.parser')
    
def find_links(soup):
    Body = soup.find('div', 'content')
    return Body.find_all('a')


links = find_links(soups_up(url_start))
for link in links:
    link = ('{}{}'.format(link.get('href'),'\n'))
    print_out(link)
# print(links)


