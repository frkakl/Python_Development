#Mean
list = [12, 41, 34, 61, 80, 69, 62]
mean= sum(list)/len(list)
print(mean)

#Mode
a = {}
for i in list:
    a.setdefault(i, 0)
    a[i]+=1

frequent = max(a.values())
for i, j in a.items():
    if j == frequent:
        mode = i
print(mode)

# Median
list.sort()

if len(list) % 2 == 0:
    m1 = list[len(list)//2]
    m2 = list[len(list)//2 - 1]
    median = (m1 + m2)/2
else:
    median = list[len(list)//2]
print(median)