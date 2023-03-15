import re
from operator import itemgetter
from collections import OrderedDict
lista = []
with open("versek.txt","r",encoding="UTF-8")as f:
    for sor in f:
        adatok = re.findall(r'\w+',sor)
        adatok = str(adatok).lower()
        lista.append(adatok)

with open("versnyers.txt","w",encoding="UTF-8")as f:
    for i in range(len(lista)):
        f.write(f"{lista[i]}\n")

nyrsl = []
with open("versnyers.txt","r",encoding="UTF-8")as f:
    for sor in f:
        adatok = re.sub(r'[\'|\,|\[|\]]',"",sor)
        nyrsl.append(adatok)

szavak = []
for i in range(len(nyrsl)):
    adat = str(nyrsl[i]).split()
    for j in range(len(adat)):
        szavak.append(adat[j])

stat = {}
for szo in szavak:
    if szo not in stat:
        stat[szo] = 1
    else:
        stat[szo] += 1    

sorteddictionary = {}
maximum = max(stat.values())
for i in range(maximum):
    for j in list(stat):
        if stat[j] == i:
            sorteddictionary[j] = i
            del stat[j]
tiltottszavak = ["s","az","hogy","ha","és","egy","a","e"]
with open("vegsomegoldas.txt","w",encoding="UTF-8") as f:
    for i in list(sorteddictionary):
        for j in tiltottszavak:
            if i == j:
                del sorteddictionary[i]
    reversedDict = OrderedDict(reversed(list(sorteddictionary.items())))
    x = 0
    for i in list(reversedDict):
        f.write(f"{i} - {reversedDict[i]}\n")
        x+=1
        if x == 10:
            break
    print(len(reversedDict))