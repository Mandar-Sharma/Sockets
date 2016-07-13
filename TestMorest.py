import json
w = open('RecFinal.json', 'w')
dict = {}
with open('Rec2.txt','r') as f:
    for line in f:
        for splita in line.split(';')[:-1]:
            kv = splita.split(':')
            dict[kv[0]]=kv[1]
        json.dump(dict,w)
w.close()
