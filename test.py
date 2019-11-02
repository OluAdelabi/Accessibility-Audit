from bs4 import BeautifulSoup
import requests, datetime
from pathlib import Path

main = 'https://physiology.med.wayne.edu/imsd-alumni/sdfsd/asdfsd/sdf'
# date = str(datetime.date.today())
home = str(Path.home())+'/'+ str(datetime.date.today())

site = 'https://'+ main.split('/',3)[2]
print(site)

def save(*arg):
    string = ''
    for k in arg:
        string += '{}/'
    string = string.rsplit('/',1)[0]
    return (string.format(*arg))
    
    
save('a','b','c','x','y','z')