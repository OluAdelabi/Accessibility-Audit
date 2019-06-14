#test redirected pdfs
import requests, os, fnmatch, pysftp

# failed_codes = [404, 500,300]
# ideal_path = 'sftp://ws9.cctest.wayne.edu//usr/local/www/sites/'

# url = 'https://wayne.edu/board/orientation/pdf/wsuaa_board_member_responsibilities_2016.pdf'
# r = requests.post(url, verify = True, timeout=10)
# print (r.status_code)

def scan_for_site_inventory(FileLocation, count):
        with os.scandir(FileLocation) as listOfEntries:
            for entry in listOfEntries:
                if fnmatch.fnmatch(entry,'*.pdf'):
                    count += 1
                    print(count, entry.name)
                elif entry.is_dir() == True and "." not in entry.name:
                    #print('{}/{}'.format(os.path.dirname(os.path.abspath(entry)),entry.name))
                    folder = '{}/{}'.format(os.path.dirname(os.path.abspath(entry)),entry.name)
                    scan_for_site_inventory(folder, count)

the_info = {'host':'ws9.cctest.wayne.edu', 'username':'web', 'password':'', 'port':22}
cnopts = pysftp.CnOpts()

private_key='/Users/fw7424/.ssh/id_rsa'
with pysftp.Connection('ws9.cctest.wayne.edu', username='web', password='', cnopts=cnopts) as sftp:
    sftp.cwd('/usr/local/www/sites/')
    FileLocation = '/usr/local/www/sites/caps'
    count = 0
    directory_structure = sftp.listdir_attr()
    # Print data
    for attr in directory_structure:
        print (attr.filename, attr)        
    #scan_for_site_inventory(FileLocation, count)