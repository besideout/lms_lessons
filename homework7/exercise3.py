var1 = [int(s) for s in input().split()]
var2 = [int(j) for j in input().split()]
for i in var2:
    var1.append(i)
lst1 = []
count = 0
for i in var1:
    if i not in lst1:
        count = count + 1
        lst1.append(i)
print(count)