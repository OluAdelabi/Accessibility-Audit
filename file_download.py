import requests, os, urllib3, datetime
from pathlib import Path
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

urllib3.disable_warnings()
main = 'https://cancerbiologyprogram.med.wayne.edu/faculty/'

items = ['2019_jing_li.jpg', 'boerner_julie_1.jpg', 'brush_george2_.jpg', 'chen_kang.jpg', 'chen_wei.jpg', 'cherm-directory.jpg', 'cote_michele.jpg', 'decarvalho_anna.jpg', 'dombkowski_alan.jpg', 'drbeebe-dimmer_ph_dphoto.jpg', 'dsc_0644_edited.jpg', 'dsc_0644_edited_1.jpg', 'ge_yubin2__1.jpg', 'gibson_heather.jpg', 'gorski_david.jpg', 'hillman.jpg', 'huttemann.jpg', 'huttemann_small.jpg', 'jing_li_11062015_resized.jpg', 'joinermichael.jpg', 'kidder_reduced.jpg', 'kimhrc_small.jpg', 'kim_seongho2_.jpg', 'lijing_2016_resized.jpg', 'listkaren.jpg', 'listkarin.jpg', 'liu.jpg', 'li_chunying.jpg', 'majumdaradhip.jpg', 'mattingly_raymond_1.jpg', 'mittal2.jpg', 'mittal_photo_2015.jpg', 'mi_qing-sheng.jpg', 'mohammad_ramzi.jpg', 'patrick_reduced.jpg', 'photo_-_ken_honn.jpg', 'photo_chen.jpg', 'purrington_kristen.jpg', 'ratnammanohar.jpg', 'ratnam_small.jpg', 'rattan_ramendeep.jpg', 'raz_avraham.jpg', 'rishi_arun_resized.jpg', 'schwartz_ann.jpg', 'schwartz_ann2_.jpg', 'sheng_reduced.jpg', 'sheng_shijie_1.jpg', 'shields_tony.jpg', 'tainsky_michael.jpg', 'updated_photo_pile_2017.jpg', 'viola-villegas_nerissa_1.jpg', 'wagnerkay-uwe.jpg', 'wanqing-liu_reduced.jpg', 'wu_gen_sheng.jpg', 'xie_youming.jpg', 'yang_zeng-quan.jpg', 'zhang_mary_reduced.jpg']

URLS = []
for item in items:
    URLS.append(main+item)

def get_name(url):
    url = url.rsplit('/',1)
    return url[1]

def change_ext(url):
    image = url.rsplit('.')
    if image[1] != 'jpg':
        return image[0] + '.jpg'
    else:
        return url
    
class URL_handler():
    
    def __init__(self):
        pass
    
    def auto_check(self, url):
        r = requests.post(url, verify = False, timeout=20)
        if r.status_code != 404 and r.status_code != 500:
            return url
        else:
            print(url, r.status_code)
    
    def fetch_content(self, url):
        r = requests.get(url, verify = False, allow_redirects=False)
        return r.content



  
URL = URL_handler()

for url in URLS:
    URL.auto_check(url)
    rg = URL.fetch_content(url)
    top_dir = ('{}/{}-File'.format(str(Path.home()), datetime.date.today()))
    url = get_name(url)
    url = change_ext(url)
    try:
        os.makedirs(top_dir)
    except OSError:
        open('{}/{}'.format(top_dir, url), 'wb').write(rg)
    else:
        open('{}/{}'.format(top_dir, url), 'wb').write(rg)
    