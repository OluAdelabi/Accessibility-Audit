#test redirected pdfs
import os, fnmatch, csv, requests

def scan_for_site_inventory(FileLocation, pattern, Ignore=None):
    try:
        with os.scandir(FileLocation) as listOfEntries:
            for entry in listOfEntries:
                if fnmatch.fnmatch(entry, pattern):
                    print(os.path.abspath(entry))
                elif entry.is_dir() == True and entry.name.startswith( '.' ) == False and entry.name not in Ignore:
                    folder = '{}/{}'.format(os.path.dirname(os.path.abspath(entry)),entry.name)
                    scan_for_site_inventory(folder, pattern, Ignore)
    except PermissionError:
        pass
    
def read_urls(csv_item):
    with open(csv_item, mode ='r') as csv_read:
            read_list = csv.reader(csv_read, delimiter=',')
            for row in read_list:
                if row[2] == '1':
                    auto_check(row[1])

def auto_check(site):
    folderName = site.rsplit('.', 2)[0].split('//')[1]
    print(folderName)
 
# Ignore=['Library','wild-wayne','anaconda']
# scan_for_site_inventory('/Users/','*.edu.csv', Ignore=Ignore)

read_urls('/Users/fw7424/Documents/2019-09-19-psychiatry.med.wayne.edu.csv')

        