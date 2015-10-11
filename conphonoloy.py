import random

c1 = ['m','n','p','t','k','s','f']
c2 = ['p','t','k','s','f']
c3 = ['r','l']
v = ['a','e','i','o','u']

none = [""]

syll1 = [[c1,none],[v],[c1,none]]
syll2 = [[c2],[c3],[v],[c1,none]]

sylllist = [syll1,syll2]

rule1 = {"target":'p', "result":'b', "before":v, "after":v}
rule2 = {"target":'t', "result":'d', "before":v, "after":v}
rule3 = {"target":'k', "result":'g', "before":v, "after":v}
rule4 = {"target":'s', "result":'z', "before":v, "after":v}
rule5 = {"target":'f', "result":'v', "before":v, "after":v}

rules = [rule1, rule2, rule3, rule4, rule5]

def apply_rules(word):
    wordlist = []
    for c in range(len(word)):
        wordlist.append(word[c])
        for r in rules:
            if word[c] == r["target"]:
                if (c-1 >= 0) and (word[c-1] in r["before"]):
                    if (c+1 < len(word)) and (word[c+1] in r["after"]):
                        wordlist[c] = r["result"]
    word = "".join(wordlist)
    return word

def word_make(length):
    word = ""
    for i in range(length):
        for j in random.choice(sylllist):
            word += random.choice(random.choice(j))
    print(word)
    print(apply_rules(word))

word_make(1)
word_make(1)
word_make(2)
word_make(3)