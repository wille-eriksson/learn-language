

with open('../espanol.txt','r', encoding='utf-8') as f:
    lines = f.readlines()
i=0
for line in lines:
    print(line)
    i = i+1
    if i==10: break
