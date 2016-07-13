w = open('Rec2Ed.txt', 'w')
lines_seen = set()
with open('Data.txt','r') as f:
    for line in f:
        if line not in lines_seen:
            w.write(line)
            lines_seen.add(line)
w.close()