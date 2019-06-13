import json, csv
file_path = '/Users/fw7424/Documents/Accessibility Audit/Neurology_med/programstructure.json'

def Write_To_CSV(siteNAME, all):
    file_write = ('/Users/fw7424/Documents/Accessibility Audit/{}.csv'.format(siteNAME))
    with open(file_write, mode='a') as csv_write:
                violation_csv = csv.writer(csv_write, delimiter= ',')
                violation_csv.writerow(all) 
                
def json_checks(collection, dict_name, siteURL, count, siteNAME):
    exclude = ['html','#mainMenu','.wsuheader','.wsufooter']
    for issue in collection:
        print(issue)
        for each in issue['nodes']:
            
            if dict_name == 'incomplete':
                component = each['any'][0]['relatedNodes'][0]['target'][0]
                element = each['target'][0]
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
            description = issue['help']
            remediation = issue['description']
            checkpoint = ','.join(map(str, checkpoint))
            checkpoint = ('=HYPERLINK("{}","{}")'.format(issue['helpUrl'], checkpoint))
            if component in exclude:
                pass
            else:
                docNUM = '3.{}'.format(count) 
                all = (docNUM, siteURL,checkpoint, impact, component, description, element, remediation)
                print(all,'some')
                Write_To_CSV(siteNAME, all)
                
count = 00
def json_to_dict(file_path, count):
#Get a file object with write permission.
    file_object = open(file_path, 'r')
# Load JSON file data to a python dict object.
    dict_object = json.load(file_object)
    siteURL = (dict_object['url']) 
    print(siteURL)
    siteNAME = file_path.rsplit('/',2)[1]
    json_checks(dict_object['incomplete'], 'incomplete', siteURL, count,siteNAME)
    json_checks(dict_object['violations'], 'violations', siteURL, count,siteNAME)
    count += 1

json_to_dict(file_path, count)