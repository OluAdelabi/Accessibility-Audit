#import pytest
import requests, json, ssl, time, os
from selenium import webdriver
from axe_selenium_python import Axe
ssl._create_default_https_context = ssl._create_unverified_context
        
Cardiology_med = ['https://cardiology.med.wayne.edu/schedules-calls']
page_list =[]

def test_site(site,folderName):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(executable_path='/Users/fw7424/Documents/chromedriver', options=options)
    driver.get(site)
    axe = Axe(driver)
    axe_options = {} #'reporter':'no-passes'
    # Inject axe-core javascript into page.
    axe.inject()
    results = axe.run(options=axe_options)
    # Write results to file
    page_name = (site.split('.edu/',1)[1]).replace('/','_')
    file_location = ('{}{}/{}.json'.format('/Users/fw7424/Accessibility_Audit/', folderName, page_name))
    try:
        os.makedirs('{}{}'.format('/Users/fw7424/Accessibility_Audit/', folderName))
    except OSError:
        pass
    else:
        pass   
    page_list.append('{}.json'.format(page_name))
    axe.write_results(results, file_location)
    driver.close()

def auto_check(sites,folderName):
    count = len(sites)
    for site in sites:
        r = requests.post(site, verify = False, timeout=20)
        print(count)
        if r.status_code != 404 and r.status_code != 500:
            test_site(site, folderName)
        count = count - 1

auto_check(Cardiology_med,'Cardiology_med')