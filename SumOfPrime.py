from math import sqrt

l = [619, 514, 857, 518, 825, 940, 585]
ll = []

for i in range(len(l)):
    flag = 0
    if l[i] != 1: 
        for j in range(2, int(sqrt(l[i]))+1):
            if l[i]%j==0:
                flag = 1
                break
    if flag == 0:
        ll.append(l[i])
# print(ll)
print(sum(ll))
