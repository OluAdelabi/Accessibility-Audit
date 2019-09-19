#import pytest
import requests, json, ssl, time, os
from selenium import webdriver
from axe_selenium_python import Axe
ssl._create_default_https_context = ssl._create_unverified_context
        
Psychiatry_med = ['https://psychiatry.med.wayne.edu/404', 'https://psychiatry.med.wayne.edu/acn', 'https://psychiatry.med.wayne.edu/addiction-psychiatry', 'https://psychiatry.med.wayne.edu/adhd-program', 'https://psychiatry.med.wayne.edu/administration', 'https://psychiatry.med.wayne.edu/adult-alumni', 'https://psychiatry.med.wayne.edu/adult-general-psych', 'https://psychiatry.med.wayne.edu/adult-psych/benefits', 'https://psychiatry.med.wayne.edu/adult-psych/curriculum', 'https://psychiatry.med.wayne.edu/adult-pysch', 'https://psychiatry.med.wayne.edu/adult-residency', 'https://psychiatry.med.wayne.edu/adult/about', 'https://psychiatry.med.wayne.edu/adult/app-process', 'https://psychiatry.med.wayne.edu/adult/city-life', 'https://psychiatry.med.wayne.edu/adult/residents', 'https://psychiatry.med.wayne.edu/anxiety-disorder', 'https://psychiatry.med.wayne.edu/anxiety-obsessive-disorder', 'https://psychiatry.med.wayne.edu/apa-doctoral-program', 'https://psychiatry.med.wayne.edu/behavioral', 'https://psychiatry.med.wayne.edu/brain', 'https://psychiatry.med.wayne.edu/brain-imaging', 'https://psychiatry.med.wayne.edu/brain-metabolomics', 'https://psychiatry.med.wayne.edu/career-development', 'https://psychiatry.med.wayne.edu/child-adolescent-program', 'https://psychiatry.med.wayne.edu/child-adolescent-pysch', 'https://psychiatry.med.wayne.edu/child-adolescent-services', 'https://psychiatry.med.wayne.edu/child-development', 'https://psychiatry.med.wayne.edu/child-psychiatry', 'https://psychiatry.med.wayne.edu/child/alumni', 'https://psychiatry.med.wayne.edu/child/app-process', 'https://psychiatry.med.wayne.edu/child/benefits', 'https://psychiatry.med.wayne.edu/child/detroit', 'https://psychiatry.med.wayne.edu/child/residents', 'https://psychiatry.med.wayne.edu/child/training-program', 'https://psychiatry.med.wayne.edu/clinical', 'https://psychiatry.med.wayne.edu/clinical-affairs', 'https://psychiatry.med.wayne.edu/clinical-electro-lab', 'https://psychiatry.med.wayne.edu/clinical-trials', 'https://psychiatry.med.wayne.edu/cognitive-research', 'https://psychiatry.med.wayne.edu/comps-outcomes', 'https://psychiatry.med.wayne.edu/conference-day', 'https://psychiatry.med.wayne.edu/contact', 'https://psychiatry.med.wayne.edu/depart-review-board', 'https://psychiatry.med.wayne.edu/design-outcomes-services', 'https://psychiatry.med.wayne.edu/edu-training', 'https://psychiatry.med.wayne.edu/education-research', 'https://psychiatry.med.wayne.edu/emergent-tech', 'https://psychiatry.med.wayne.edu/fac-profiles', 'https://psychiatry.med.wayne.edu/faculty', 'https://psychiatry.med.wayne.edu/fellowships', 'https://psychiatry.med.wayne.edu/gambling', 'https://psychiatry.med.wayne.edu/gen-community-program', 'https://psychiatry.med.wayne.edu/goals-objectives', 'https://psychiatry.med.wayne.edu/high-intervention', 'https://psychiatry.med.wayne.edu/hospital-rotation', 'https://psychiatry.med.wayne.edu/index', 'https://psychiatry.med.wayne.edu/integrated-care-track', 'https://psychiatry.med.wayne.edu/master-psychiatry', 'https://psychiatry.med.wayne.edu/mental-health', 'https://psychiatry.med.wayne.edu/metab', 'https://psychiatry.med.wayne.edu/molecular-neurobiology', 'https://psychiatry.med.wayne.edu/molecular-toxicology', 'https://psychiatry.med.wayne.edu/neuro-research-unit', 'https://psychiatry.med.wayne.edu/neuropharm-addiction', 'https://psychiatry.med.wayne.edu/news', 'https://psychiatry.med.wayne.edu/news/archive', 'https://psychiatry.med.wayne.edu/news/category', 'https://psychiatry.med.wayne.edu/news/topic', 'https://psychiatry.med.wayne.edu/news/topics', 'https://psychiatry.med.wayne.edu/newsletters', 'https://psychiatry.med.wayne.edu/obsessive-compulsive', 'https://psychiatry.med.wayne.edu/ocd-research', 'https://psychiatry.med.wayne.edu/office-business', 'https://psychiatry.med.wayne.edu/office-chair', 'https://psychiatry.med.wayne.edu/outpatient-rotation', 'https://psychiatry.med.wayne.edu/patient-care', 'https://psychiatry.med.wayne.edu/philosophy-phd', 'https://psychiatry.med.wayne.edu/profile', 'https://psychiatry.med.wayne.edu/profiles', 'https://psychiatry.med.wayne.edu/psychosis-research', 'https://psychiatry.med.wayne.edu/public-psych-fellowship', 'https://psychiatry.med.wayne.edu/public-service', 'https://psychiatry.med.wayne.edu/research', 'https://psychiatry.med.wayne.edu/research-administration', 'https://psychiatry.med.wayne.edu/research-divisions', 'https://psychiatry.med.wayne.edu/research-services', 'https://psychiatry.med.wayne.edu/sleep-lab-services', 'https://psychiatry.med.wayne.edu/substance-abuse', 'https://psychiatry.med.wayne.edu/supervision', 'https://psychiatry.med.wayne.edu/therapy-training', 'https://psychiatry.med.wayne.edu/thermoregulation', 'https://psychiatry.med.wayne.edu/trauma', 'https://psychiatry.med.wayne.edu/trauma-center', 'https://psychiatry.med.wayne.edu/triage', 'https://psychiatry.med.wayne.edu/undergrad-med-education', 'https://psychiatry.med.wayne.edu/voluntary']
page_list =[]

def test_site(site,folderName):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    driver = webdriver.Chrome(executable_path='/Users/fw7424/Documents/chromedriver', options=options)
    driver.get(site)
    axe = Axe(driver)
    # Inject axe-core javascript into page.
    axe.inject()
    # Run axe accessibility checks.
    results = axe.run()
    # Write results to file
    page_name = (site.split('.edu/',1)[1]).replace('/','_')
    file_location = ('{}{}/{}.json'.format('/Users/fw7424/Accessibility_Audit/', folderName, page_name))
    try:
        os.makedirs('{}{}'.format('/Users/fw7424/Accessibility_Audit/', folderName))
    except OSError:
        page_list.append('{}.json'.format(page_name))
        axe.write_results(results, file_location)
        driver.close()
    else:
        print('investigate')
        page_list.append('{}.json'.format(page_name))
        axe.write_results(results, file_location)
        driver.close()
    # Assert no violations are found
    #assert len(results["violations"]) == 0, axe.report(results["violations"])

def auto_check(sites,folderName):
    count = len(sites)
    for site in sites:
        r = requests.post(site, verify = False, timeout=20)
        print(count)
        if r.status_code != 404 and r.status_code != 500:
            test_site(site, folderName)
        count = count - 1


auto_check(Psychiatry_med,'Psychiatry_med')
print(page_list)

