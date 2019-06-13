from bs4 import BeautifulSoup
import csv, os, fnmatch
FileLocation = '/Users/fw7424/Documents/'

def write_to_CSV(each_item):
    file_save = '{}{}.csv'.format('/Users/fw7424/Documents/', each_item[1].replace('https://','').split('.edu')[0])
    with open(file_save, mode ='a') as csv_write:
        fail_csv = csv.writer(csv_write, delimiter= ',')
        fail_csv.writerow(each_item)

def failed(audit_file, count):
    pdf_url = audit_file.replace('.accreport.html','').rsplit('/',1)
    pdf_url = '{}{}'.format('https://',pdf_url[1].replace('~','/'))
    soup = BeautifulSoup(open(audit_file), 'html.parser')
    for item in soup.table.contents:
        item = BeautifulSoup(str(item), 'html.parser')
        if item.find(string="Failed") == 'Failed':
            rule_name = '=HYPERLINK("{}","{}")'.format(item.a.get('href'), item.a.next_element)
            rule_description = item.a.next_element.next_element.next_sibling.next_element
            each_item = ('{}.{}'.format('3',count),pdf_url, rule_name, 'Critical', rule_description)
            write_to_CSV(each_item)

def scan_for_site_inventory(FileLocation):
    with os.scandir(FileLocation) as listOfEntries:  
        for entry in listOfEntries:
            if entry.is_file():
                    pass
            else:
                fullPath = ('{}{}'.format(FileLocation, entry.name))
                listOfFiles = os.listdir(fullPath) 
                count = 0
                #pattern = "*.accreport.html"
                for audit_item in listOfFiles:  
                    if fnmatch.fnmatch(audit_item, '*.accreport.html'):
                        count += 1
                        failed('{}/{}'.format(fullPath,audit_item), count)
         
#audit_file = '/Users/fw7424/Documents/Cphs_audited/cphs.wayne.edu~giving~nurse_anesthesia_specificgift_form.pdf.accreport.html'                
scan_for_site_inventory(FileLocation)
#failed(audit_file)