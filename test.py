def RemoveIthWord(list, word, N): 
    word = word[2]
    count = 0
    for i in range(0, len(list)): 
        if (list[i][2] == word): 
            count = count + 1
              
            if(count == N): 
                del(list[i]) 
                return True
                  
    return False
  
# Driver code 
list = [['geeks', 'fo0r', 'geeks'],['geekss', 'foor', 'geek'],['geeksss', 'for', 'geek']]

N = 2
for word in list:
    RemoveIthWord(list, word, N) 
print(list)
  
# if (flag == True): 
#     print("Updated list is: ", list) 
# else: 
#     print("Item not Updated")  