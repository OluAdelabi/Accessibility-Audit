#test redirected pdfs
import requests, os, fnmatch, pysftp

def scan_for_site_inventory(FileLocation, count):
    #listOfEntries = sftp.listdir()
        with os.scandir(FileLocation) as listOfEntries:
            for entry in listOfEntries:
                if fnmatch.fnmatch(entry,'*.accreport.html'):
                    count += 1
                    print(count, entry.name)
                    #sftp.isdir()
                elif entry.is_dir() == True and entry.name.startswith( '.' ) == False:
                    #print('{}/{}'.format(os.path.dirname(os.path.abspath(entry)),entry.name))
                    folder = '{}/{}'.format(os.path.dirname(os.path.abspath(entry)),entry.name)
                    scan_for_site_inventory(folder, count)


count = 0
scan_for_site_inventory('/Users/fw7424', count)