shakesP = ''
with open('t8.shakespeare.txt', 'r') as f_var:
    shakesP = shakesP + f_var.read()

#Lowercase the string
shakesP = shakesP.lower()

def replaceSymbol(shakesP):
    shakesP = shakesP.replace('\n', ' ')
    shakesP = shakesP.replace('\r', ' ')
    shakesP = shakesP.replace('\t', ' ')
    shakesP = shakesP.replace(',', ' ')
    shakesP = shakesP.replace(':', ' ')
    shakesP = shakesP.replace(';', ' ')
    shakesP = shakesP.replace('.', ' ')
    shakesP = shakesP.replace('?', ' ')
    shakesP = shakesP.replace('!', ' ')
    return shakesP

def strToList(shakesP):
    new_list = shakesP.split(' ')
    return new_list

shakesP = replaceSymbol(shakesP)
new_list = strToList(shakesP)
new_dictionary = {}

# count the list using dictionary

# loop through the list and set initial count per key to zero
for mem in new_list:
    new_dictionary.setdefault(mem, 0)

# loop through the same list again and increment key count each time string appear
for mem in new_list:
    new_dictionary[mem] = new_dictionary[mem] + 1

# SORT 1: Alphabetically. sort it alphabetically using key
alphabetically_sorted_list = sorted(new_dictionary)

print('--------sort alphabetically--------')
for mem in alphabetically_sorted_list:
    print(f'{mem} : {new_dictionary[mem]}\n')