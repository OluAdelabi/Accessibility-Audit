import requests, json, ssl, time, os, csv, fnmatch, readJSON
from selenium import webdriver
from pathlib import Path
from axe_selenium_python import Axe
ssl._create_default_https_context = ssl._create_unverified_context

# page_list =[]

def read_urls(csv_item):
    with open(csv_item, mode ='r') as csv_read:
            read_list = csv.reader(csv_read, delimiter=',')
            for i, row in enumerate(read_list):
                if row[2] == '1':
                    auto_check(row[1])
                if i == 0:
                    print(csv_item)

def scan_for_files(pattern, FilePath, Ignore=None):
    try:
        with os.scandir(FilePath) as listOfEntries:
            for entry in listOfEntries:
                if fnmatch.fnmatch(entry, pattern):
                    read_urls(os.path.abspath(entry))
                elif entry.is_dir() == True and entry.name.startswith( '.' ) == False and entry.name not in Ignore:
                    folder = '{}/{}'.format(os.path.dirname(os.path.abspath(entry)),entry.name)
                    scan_for_files(pattern, folder, Ignore)
    except PermissionError:
        pass

def test_site(site,folderName):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(executable_path='/Users/fw7424/Documents/chromedriver', options=options)
    driver.get(site)
    axe = Axe(driver)
    axe_options = {"resultTypes": ["violations"]} #'reporter':'no-passes'
    # Inject axe-core javascript into page.
    axe.inject()
    results = axe.run(options=axe_options)
    # Write results to file
    page_name = (site.split('.edu/',1)[1]).replace('/','_')
    file_location = ('{}/Accessibility_Audit/{}/{}.json'.format(str(Path.home()), folderName, page_name))
    try:
        os.makedirs('{}/Accessibility_Audit/{}'.format(str(Path.home()), folderName))
    except OSError:
        pass
    # page_list.append('{}.json'.format(page_name))
    axe.write_results(results, file_location)
    driver.close()

def auto_check(site):
    r = requests.post(site, verify = False, timeout=20)
    if r.status_code != 404 and r.status_code != 500:
        folderName = site.rsplit('.', 2)[0].split('//')[1]
        test_site(site, folderName)

scan_for_files('*.edu.csv', str(Path.home()), Ignore=['Library','wild-wayne','anaconda'])
readJSON.program_run()
