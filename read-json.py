import json, os, fnmatch, pathlib, csv

main_folder = '/Users/fw7424/Accessibility_Audit/'
file_list = []
# def read_the_entries(main_folder, file_list)
with os.scandir(main_folder) as listOfEntries:
    for entry in listOfEntries:
        if entry.is_file():
            pass
        else:
            count = 00
            sub_folder = ('{}{}/'.format(main_folder,entry.name))
            listOfFiles = os.listdir(sub_folder)  
            pattern = "*.json"
            for audit_item in listOfFiles:
                count += 1
                if fnmatch.fnmatch(audit_item, pattern):
                    file_path = '{}{}'.format(sub_folder, audit_item)
                    pair = [count, file_path]
                    file_list.append(pair)
                    

def Write_To_CSV(siteNAME, all):
    file_write = ('/Users/fw7424/Accessibility_Audit/{}.csv'.format(siteNAME))
    with open(file_write, mode='a') as csv_write:
                violation_csv = csv.writer(csv_write, delimiter= ',')
                violation_csv.writerow(all) 
                
def json_checks(collection, dict_name, siteURL, count, siteNAME):
    exclude = ['html','#mainMenu','.wsuheader','.wsufooter','.icon-twitter > span','.icon-twitter > span','.icon-facebook > span','.icon-instagram > span','.icon-flickr > span','.icon-youtube > span','.wsuwordmark > .spf-nolink[href$="wayne\.edu\/"]']
    for issue in collection:
        for each in issue['nodes']:
            if dict_name == 'incomplete':
                try:
                    component = each['any'][0]['relatedNodes'][0]['target'][0]
                except IndexError:
                    component = each['target'][0]
                element = each['target'][0]
            elif dict_name == 'passes':
                if 'style' in each.get('html'):
                    component = each['target'][0]
                    element = each['html']
                else:
                    break
            else:
                component = each['target'][0]
                element = each['html']
            checkpoint = []
            for tag in issue['tags']:
                if 'wcag' in tag and '2a' not in tag:
                    checkpoint.append(tag.split('wcag')[1])
                elif 'best-practice' in tag:
                    checkpoint.append('best-practice')
            impact = issue['impact']
            if impact == None:
                impact = 'table'
            description = issue['help']
            remediation = issue['description']
            checkpoint = ', '.join(map(str, checkpoint))
            checkpoint = ('=HYPERLINK("{}","{}")'.format(issue['helpUrl'], checkpoint))
            if component in exclude:
                pass
            else:
                docNUM = '3.{}'.format(count) 
                all = (docNUM, siteURL,checkpoint, impact, component, description, element, remediation)
                Write_To_CSV(siteNAME, all)

def json_to_dict(file_path, count):
#Get a file object with write permission.
    file_object = open(file_path, 'r')
# Load JSON file data to a python dict object.
    dict_object = json.load(file_object)
    siteURL = (dict_object['url']) 
    siteNAME = file_path.rsplit('/',2)[1]
    try:
        json_checks(dict_object['incomplete'], 'incomplete', siteURL, count,siteNAME)
    except KeyError:
        pass
    try:
        json_checks(dict_object['passes'], 'passes', siteURL, count, siteNAME)
    except KeyError:
        pass
    json_checks(dict_object['violations'], 'violations', siteURL, count,siteNAME)
    

for site in file_list:
    json_to_dict(site[1], site[0])