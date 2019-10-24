# import file_download
import requests, urllib3, datetime, csv
from bs4 import BeautifulSoup
from pathlib import Path


urllib3.disable_warnings()

url_start ='https://wayne.edu/people/?type=people&q='

def Write_To_CSV(name, accessID):
    all = (name, '-', accessID)
    file_write = ('{}/Accessibility_Audit/{}.csv'.format(str(Path.home()),'CancerBiology'))
    with open(file_write, mode='a') as csv_write:
                violation_csv = csv.writer(csv_write, delimiter= ',')
                violation_csv.writerow(all) 

def soups_up(url):
    html = requests.get(url)
    return BeautifulSoup(html.content, 'html.parser')
    
def find_links(soup, name):
    try:
        ID = soup.find('table').find('a')
    except AttributeError:
        return 'User Not found, try again'
    else:
        return ID.get('href')

names = ['Judith Abrams', 'Asfar Azmi', 'Jennifer Beebe-Dimmer', 'Gerold Bepler', 'Julie Boerner', 'Aliccia Bollig-Fischer', 'George Brush', 'Sreenivasa Chinni', 'Michele Cote', 'Ana deCarvalho', 'Alan Dombkowski', 'Qingping Dou', 'Fei Chen', 'Rodrigo Fernandez-Valdivia', 'Rafael Fridman', 'Yubin Ge', 'Gen Wu', 'Heather Gibson', 'David Gorski', 'Guojun Wu', 'Ahmad Heydari', 'Kenneth Honn', 'Maik Huttemann', 'Jian Wang', 'Michael Joiner', 'Kang Chen', 'David Kessel', 'Benjamin Kidder', 'Seongho Kim', 'Hyeong Kim', 'Jing Li', 'Karin List', 'Haipeng Liu', 'Wanqing Liu', 'Larry Matherly', 'Raymond Mattingly', 'Qing-Sheng Mi', 'Ramzi Mohammad', 'Stephan Patrick', 'Lori Pile', 'Izabela Podgorski', 'Kristen Purrington', 'Manohar Ratnam', 'Ramandeep Rattan', 'Avraham Raz', 'John Reiners', 'Arun Rishi', 'Ann Schwartz', 'Malathy Shekhar', 'Shijie Sheng', 'Anthony Shields', 'Michael Tainsky', 'Jeffrey Taub', 'Nerissa Viola', 'Kay-Uwe Wagner', 'Wei-Zen Wei', 'Wei Chen', 'Youming Xie', 'Zeng-Quan Yang', 'Xiaohong Zhang']

for name in names:
    NAME = name.replace(' ','+')
    url = url_start+NAME
    # print(url)
    soup = soups_up(url)
    accessID = find_links(soup,name)
    accessID = accessID.replace('/people/','').replace('/','')
    Write_To_CSV(name, accessID)
    
    # print(info)
