import csv, os, fnmatch
FileLocation = '/Users/fw7424/Documents/'
csv_list = []
def scan_for_site_inventory(FileLocation, csv_list):
    pattern = '*.edu.csv'
    with os.scandir(FileLocation) as ListOfEntries:
        for item in ListOfEntries:
            if fnmatch.fnmatch(item,'*.DS_Store'):
                pass
            elif fnmatch.fnmatch(item, pattern):
                path = '{}{}'.format(FileLocation, item.name)
                csv_list.append(path)

def Write_To_CSV(content):
    file_write = ('/Users/fw7424/Documents/{}.csv'.format('Top_20'))
    with open(file_write, mode='a') as csv_write:
        pdfs_csv = csv.writer(csv_write, delimiter=",")
        pdfs_csv.writerow([content])
        
## Add which site the pdf came from in the case of subsites with different subdomain from main cms site.
def get_pdfs_only(csv_list):
    pdf_array = []
    print(pdf_array)
    count = 0
    for csv_item in csv_list:
        with open(csv_item, mode ='r') as csv_read:
            read_list = csv.reader(csv_read, delimiter=',')
            for row in read_list:
                if row[0] in (None,'') and '.pdf' in row[1]:
                    if row[1] in pdf_array:
                        count += 1
                        print(count)
                    else:
                        pdf_array.append(row[1])
    for pdf in pdf_array:
        Write_To_CSV(pdf)

scan_for_site_inventory(FileLocation, csv_list)
get_pdfs_only(csv_list)