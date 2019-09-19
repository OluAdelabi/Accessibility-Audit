### PDF download
import csv, requests, os, urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
top_20 = '/Users/fw7424/Documents/New_sites.csv'

def url_to_filename(url):
    url = url.split('://')
    url = url[1]
    file_name = url.replace('/','~')
    return (file_name)

def write_failed_urls(urls):
    with open('/Users/fw7424/Documents/failed.csv', mode='a') as csv_write:
        failed_urls = csv.writer(csv_write, delimiter=',')
        failed_urls.writerow(urls)

def sort_to_folder(audit_file, url):
    rg = requests.get(url, verify = False, allow_redirects=False)
    location = audit_file.split('~')
    pdf_name = location.pop()
    #print(pdf_name)
    s = '/'
    location = s.join(location)
    top_dir = '/Users/fw7424/Documents/' + location
    try:
        os.makedirs(top_dir)
    except OSError:
        open('{}/{}'.format(top_dir, audit_file), 'wb').write(rg.content)
    else:
        open('{}/{}'.format(top_dir, audit_file), 'wb').write(rg.content)

def get_urls_from_csv(csv_list):
    failed_codes = [404,500,300]
    with open(csv_list, mode ='r') as csv_read:
        read_list = csv.reader(csv_read)
        for row in read_list:
            try:
                r = requests.post(row[0], verify = False, timeout=10)
                print(row[0])
            except Exception as issue:
                write_failed_urls(([row[0], issue]))
            else:
                if r.status_code in failed_codes:
                    write_failed_urls(([row[0], r.status_code]))
                else:
                    sort_to_folder(url_to_filename(row[0]), row[0])
                    
get_urls_from_csv(top_20)