import json, os, fnmatch, pathlib, csv

file_list = []

def Write_To_CSV(folder_name, all):
    file_write = ('/Users/fw7424/Accessibility_Audit/{}.csv'.format(folder_name))
    with open(file_write, mode='a') as csv_write:
                violation_csv = csv.writer(csv_write, delimiter= ',')
                violation_csv.writerow(all) 
                
def json_checks(collection, dict_name, pageURL, count, folder_name):
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
                all = (docNUM, pageURL,checkpoint, impact, component, description, element, remediation)
                Write_To_CSV(folder_name, all)


def json_to_dict(json_file, count=0):
    file_object = open(json_file, 'r')
    # Load JSON file data to a python dict object.
    dict_object = json.load(file_object)
    pageURL = (dict_object['url']) 
    folder_name = json_file.rsplit('/',2)[1]
    print(folder_name)
#     try:
#         json_checks(dict_object['incomplete'], 'incomplete', pageURL, count, folder_name)
#     except KeyError:
#         pass
#     try:
#         json_checks(dict_object['passes'], 'passes', pageURL, count, folder_name)
#     except KeyError:
#         pass
#     json_checks(dict_object['violations'], 'violations', pageURL, count,folder_name)
    
json_file_path = '/Users/fw7424/Accessibility_Audit/psychiatry.med/acn.json'

json_to_dict(json_file_path)