name=input("Enter fine name: ")
fh=open(name)
counts=dict()
hours=list()

for line in fh:
    line.rstrip()
    lst=line.split()
    if len(lst) == 0:
        continue
    if lst[0] != 'From' or lst[0]=='From:':
        continue
    word=lst[5].split(':')
    hours.append(word[0])
#print(hours)

for i in hours:
    counts[i]=counts.get(i,0)+1
print(counts)

tmp=list()
for k,v in counts.items():
    tmp.append((k,v))

tmp=sorted(tmp)
print(tmp)
for k,v in tmp:
    print(k, v)
