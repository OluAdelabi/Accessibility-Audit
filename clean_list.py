from pathlib import Path
import os, fnmatch, csv

def RemoveIthWord(list, word):
    N = 2
    word = word[6]
    count = 0
    for i in range(0, len(list)): 
        if (list[i][6] == word): 
            count = count + 1
              
            if(count == N): 
                del(list[i]) 
                return True
                  
    return False

def program_run():
    main_folder = ('{}/Accessibility_Audit/'.format(str(Path.home())))

    with os.scandir(main_folder) as listOfEntries:
        for entry in listOfEntries:
            pattern = "*.csv"
            if fnmatch.fnmatch(entry.name, pattern):
                print('yes')
                file_name = '{}/{}'.format(os.path.dirname(os.path.abspath(entry)),entry.name)
                read_items(file_name)
                
                # read_items(file-name)
    
        #     if entry.is_file():
        #         pass
        #     else:
        #         count = 00
        #         sub_folder = ('{}{}/'.format(main_folder,entry.name))
        #         listOfFiles = os.listdir(sub_folder)  
                
        #         for audit_item in listOfFiles:
        #             count += 1
        #             if fnmatch.fnmatch(audit_item, pattern):
        #                 file_path = '{}{}'.format(sub_folder, audit_item)
        #                 pair = [count, file_path]
        #                 file_list.append(pair)
        # print(file_list)

def read_items(csv_item):
    with open(csv_item, mode ='r') as csv_read:
            read_list = csv.reader(csv_read, delimiter=',')
            group = []
            for row in enumerate(read_list):
                group.append(row)
            print(group[0]) 
# group.append(all)
# for code in group:
#     RemoveIthWord(group, code)
program_run()
    
        