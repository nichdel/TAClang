import random
import csv

inv_file = 'inventories.csv'
syll_file = 'syllables.csv'
rule_file = 'rules.csv'

inv_dict = {}
with open(inv_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=['name'], restkey='rest')

    for row in reader:
        name = row['name']
        rest = row['rest']
        inv_dict[name] = []
        for entry in rest:
            if entry[0] == '$':
                inv_dict[name] += inv_dict[entry[1:]]
            elif entry[0] == '-':
                if entry[1] == '$':
                    for rem_item in inv_dict[entry[2:]]:
                        inv_dict[name].remove(rem_item)
                else:
                    inv_dict[name].remove(entry[1:])
            else:
                inv_dict[name].append(entry)

syll_list = []
with open(syll_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=['head'], restkey='rest')

    for row in reader:
        construct = []
        for item in ([row['head']] + row['rest']):
            if item[0] == '$':
                construct.append([inv_dict[item[1:]]])
            elif item[0] == '?':
                if item[1] == '$':
                    construct.append([[''],inv_dict[item[2:]]])
                else:
                    construct.append([[''], item[1:]])
            else:
                construct.append([item])
        syll_list.append(construct)

rule_list = []
with open(rule_file, 'r') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        construct = {}
        for key in row.keys():
            item = row[key]
            if item[0] == '$':
                construct[key] = inv_dict[item[1:]]
            else:
                construct[key] = item
        rule_list.append(construct)

#TODO Use the new lists/dicts to generate words.

print(inv_dict)
for item in syll_list:
    print(item)
print(rule_list)

def apply_rules(word):
    wordlist = []
    for c in range(len(word)):
        wordlist.append(word[c])
        for r in rule_list:
            if word[c] == r["target"]:
                if (c-1 >= 0) and (word[c-1] in r["before"]):
                    if (c+1 < len(word)) and (word[c+1] in r["after"]):
                        wordlist[c] = r["result"]
    word = "".join(wordlist)
    return word

def word_make(length):
    word = ""
    for i in range(length):
        for j in random.choice(syll_list):
            word += random.choice(random.choice(j))
    print(word)
    print(apply_rules(word))

word_make(1)
word_make(1)
word_make(2)
word_make(3)
