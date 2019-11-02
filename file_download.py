import requests, os, urllib3, datetime
from bs4 import BeautifulSoup
from pathlib import Path
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

urllib3.disable_warnings()

class URL_handler():

    def __init__(self,url):
        self.home = str(Path.home())
        self.today = str(datetime.date.today())
        self.url = url
        self.file_location = ('{}/{}-{}'.format(str(Path.home()), self.get_site(),self.today))
        main_content = self.get_content(url)
        self.soup = BeautifulSoup(main_content, 'html.parser')

    def get_site(self):
        self.base_url = 'https://'+ self.url.split('/',3)[2]
        self.site = self.url.split('//')[1]
        return self.site.split('.wayne.edu')[0]

    def get_content(self, url):
        self.r = requests.get(url, verify = False, allow_redirects=False)
        return self.r.content
    
    def get_image_url(self):
        self.A = self.soup.find_all('img')
        for a in self.A:
            src = a.get('src')
            if 'http' not in src:
                self.download_from_links(str(self.base_url + src))
            else:
                self.download_from_links(src)

    def save_it(self,item,*arg):
        string = ''
        for k in arg:
            string += '{}/'
        string = string.rsplit('/',1)[0]
        open((string.format(*arg)),'wb').write(item)

    # def mimic_url_path(self,url):
    #     the_path = url.split('/')
    #     the_path = the_path[3:]
    #     for folder in the_path:
            
    #     print(the_path)

    def download_from_links(self, source):
        item = self.get_content(source)
        # self.mimic_url_path(source)
        source = source.split('/')
        place = self.file_location +'/'+ source[3]
        try:
            os.makedirs(place)
        except OSError:
            self.save_it(item, place, source[4])
        else:
            self.save_it(item, place, source[4])


U = URL_handler('https://physiology.med.wayne.edu/imsd-alumni')

U.get_image_url()

# def change_ext(url):
#     image = url.rsplit('.')
#     if image[1] != 'jpg':
#         return image[0] + '.jpg'
#     else:
#         return url
    
# class URL_handler():
    
#     def __init__(self):
#         pass
    
#     def auto_check(self, url):
#         r = requests.post(url, verify = False, timeout=20)
#         if r.status_code != 404 and r.status_code != 500:
#             return url
#         else:
#             print(url, r.status_code)
    


